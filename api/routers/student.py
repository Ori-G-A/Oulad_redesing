"""
api/routers/student.py
======================
Endpoints del flujo de práctica del estudiante:
  POST /student/next-question  → siguiente pregunta adaptativa
  POST /student/answer         → procesar respuesta + actualizar ELO
  GET  /student/stats          → ELO global, por tópico, racha
  GET  /student/achievements   → logros/badges desbloqueados
  GET  /student/courses        → catálogo de cursos disponibles
  POST /student/enroll         → matricularse en un curso
  POST /student/enroll-by-code → acceso especial por código de invitación
  DELETE /student/enroll/{course_id} → darse de baja
  GET  /student/history        → historial de intentos
  POST /student/exam/start     → inicia sesión de examen cronometrado
  POST /student/exam/submit    → envía respuestas del examen y obtiene resultados
"""

import hashlib
import random

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from api.dependencies import CurrentUser, RepoDep, build_vector_rating
from api.schemas.student import (
    AnswerRequest,
    AnswerResponse,
    CourseMapResponse,
    CourseResponse,
    DiagnosticQuestion,
    DiagnosticResultResponse,
    DiagnosticStatusResponse,
    DiagnosticSubmitRequest,
    EnrollByCodeRequest,
    MapNode,
    EnrollRequest,
    ExamStartRequest,
    ExamStartResponse,
    ExamSubmitRequest,
    ExamSubmitResponse,
    ExamTemplateSummary,
    ItemResponse,
    LessonDetailResponse,
    LessonEventRequest,
    LessonInteractionRequest,
    LessonInteractionResponse,
    NextQuestionRequest,
    NextQuestionResponse,
    PendingExam,
    ProcedureSubmitResponse,
    StudentStatsResponse,
    TopicELO,
)
from src.application.services.student_service import StudentService
from src.domain.elo.vector_elo import aggregate_global_elo
from src.domain.learning.prealgebra import (
    CLASSIFIER_BASIC_NODE_ID,
    CLASSIFIER_RIGOROUS_NODE_ID,
    CLOSING_NODE_ID,
    COMPLEX_NODE_ID,
    DETECTIVE_NODE_ID,
    DIAGNOSTIC_NODE_IDS,
    INTEGERS_NODE_ID,
    IRRATIONALS_NODE_ID,
    N2_DIVISION_NODE_ID,
    N2_EXPONENTIATION_NODE_ID,
    N2_HUB_NODE_ID,
    N2_MULTIPLICATION_NODE_ID,
    N2_OPERATION_NODE_IDS,
    N2_RADICATION_NODE_ID,
    N2_SUBTRACTION_NODE_ID,
    N2_SUM_NODE_ID,
    N3_ASSOCIATIVE_NODE_ID,
    N3_COMMUTATIVE_NODE_ID,
    N3_DISTRIBUTIVE_NODE_ID,
    N3_HUB_NODE_ID,
    N3_IDENTITY_NODE_ID,
    N3_INVERSES_NODE_ID,
    N3_MACHINE_NODE_IDS,
    N4_CONCEPT_NODE_IDS,
    N4_DIVISIBILITY_NODE_ID,
    N4_FACTORIZATION_NODE_ID,
    N4_GCD_NODE_ID,
    N4_HUB_NODE_ID,
    N4_LCM_NODE_ID,
    N4_MULTIPLES_NODE_ID,
    N4_PRIMES_NODE_ID,
    NATURALS_NODE_ID,
    PREALGEBRA_COURSE_ID,
    RATIONALS_NODE_ID,
    REALS_NODE_ID,
    STAIRCASE_NODE_ID,
    TRIGGER_NODE_ID,
    WELCOME_NODE_ID,
    evaluate_interaction,
    get_lesson,
    presentation_band,
    recommended_node_for_misconception,
)

router = APIRouter(prefix="/student", tags=["student"])


def _make_service(repo) -> StudentService:
    return StudentService(repository=repo)


# ── Preguntas ──────────────────────────────────────────────────────────────────


@router.post("/next-question", response_model=NextQuestionResponse)
def next_question(body: NextQuestionRequest, user: CurrentUser, repo: RepoDep):
    """Selecciona la siguiente pregunta adaptativa (ZDP) para el estudiante."""
    service = _make_service(repo)
    vector = build_vector_rating(user["user_id"], repo)

    topic = body.topic or body.course_id  # fallback: usar curso como tópico ELO

    item, status_str = service.get_next_question(
        student_id=user["user_id"],
        topic=topic,
        vector_rating=vector,
        session_correct_ids=set(body.session_correct_ids),
        session_wrong_timestamps=body.session_wrong_timestamps,
        session_questions_count=body.session_questions_count,
        course_id=body.course_id,
        block=body.block,
        topic_filter=body.topic,  # práctica desde el mapa filtra por este tópico
    )

    if item is None:
        return NextQuestionResponse(item=None, status=status_str)

    return NextQuestionResponse(
        item=ItemResponse(
            id=item["id"],
            content=item["content"],
            difficulty=item["difficulty"],
            topic=item["topic"],
            options=item["options"],
            image_url=item.get("image_url"),
            tags=item.get("tags") or [],
        ),
        status=status_str,
    )


# ── Respuestas ─────────────────────────────────────────────────────────────────


@router.post("/answer", response_model=AnswerResponse)
def answer(body: AnswerRequest, user: CurrentUser, repo: RepoDep):
    """Procesa una respuesta: actualiza ELO y persiste el intento de forma atómica."""
    service = _make_service(repo)
    vector = build_vector_rating(user["user_id"], repo)

    # Recuperar correct_option desde DB — el cliente no la envía (seguridad)
    item_db = repo.get_item_by_id(body.item_id)
    if not item_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ítem '{body.item_id}' no encontrado.",
        )
    # Fusionar datos del cliente con datos canónicos de la DB
    item_data = {**body.item_data, "correct_option": item_db["correct_option"]}

    elo_topic = body.elo_topic or item_data.get("topic", body.item_id)
    elo_before = vector.get(elo_topic)

    is_correct, cog_data = service.process_answer(
        user_id=user["user_id"],
        item_data=item_data,
        selected_option=body.selected_option,
        reasoning=body.reasoning or "",
        time_taken=body.time_taken,
        vector_rating=vector,
        elo_topic=elo_topic,
    )

    elo_after = vector.get(elo_topic)
    rd_after = vector.get_rd(elo_topic)

    return AnswerResponse(
        is_correct=is_correct,
        elo_before=round(elo_before, 2),
        elo_after=round(elo_after, 2),
        rd_after=round(rd_after, 2),
        delta_elo=round(elo_after - elo_before, 2),
        cog_data=cog_data,
    )


# ── Stats ──────────────────────────────────────────────────────────────────────


@router.get("/stats", response_model=StudentStatsResponse)
def stats(user: CurrentUser, repo: RepoDep):
    """Retorna el ELO global, ELO por tópico, racha de estudio y total de intentos."""
    vector = build_vector_rating(user["user_id"], repo)
    global_elo = aggregate_global_elo(vector)

    # Consolidar tópicos duplicados.
    #
    # Algunos estudiantes tienen intentos con `attempts.topic = item.topic` (flujo
    # viejo) y otros con `attempts.topic = course_id` (flujo actual con elo_topic).
    # Ambos persisten en student_topic_elo y aparecen como tópicos distintos en
    # vector.ratings, confundiendo al estudiante (ver bug #7 del QA de mayo 2026).
    #
    # Fix: usar el catálogo de cursos para mapear slugs (course_id) a nombre
    # legible. Si el mismo curso aparece como slug Y como nombre, conservar la
    # entrada del slug (refleja el flujo actual) y descartar el twin viejo.
    courses_catalog = repo.get_courses() if hasattr(repo, "get_courses") else []
    course_id_to_name = {c["id"]: c["name"] for c in courses_catalog}
    # Nombre humano → slug, para detectar twins (case-insensitive)
    name_lower_to_id = {c["name"].lower(): c["id"] for c in courses_catalog}

    consolidated: dict[str, tuple[float, float]] = {}
    for topic, (r, rd) in vector.ratings.items():
        if topic in course_id_to_name:
            # Es un slug — el display es el nombre del curso.
            display = course_id_to_name[topic]
            consolidated[display] = (r, rd)
        else:
            # Posible nombre humano. Si su slug equivalente ya está en
            # vector.ratings, omitir esta entrada (la del slug gana).
            twin_slug = name_lower_to_id.get(topic.lower())
            if twin_slug and twin_slug in vector.ratings:
                continue
            consolidated[topic] = (r, rd)

    topic_elos = [
        TopicELO(topic=t, rating=round(r, 2), rd=round(rd, 2))
        for t, (r, rd) in sorted(consolidated.items())
    ]

    total = repo.get_total_attempts_count(user["user_id"])
    streak = repo.get_study_streak(user["user_id"])

    # Rank label (16 niveles)
    rank_label = _elo_to_rank(global_elo)

    return StudentStatsResponse(
        user_id=user["user_id"],
        global_elo=round(global_elo, 2),
        topic_elos=topic_elos,
        total_attempts=total,
        study_streak=streak,
        rank_label=rank_label,
    )


# ── Cursos y matrículas ────────────────────────────────────────────────────────


@router.get("/courses", response_model=list[CourseResponse])
def courses(user: CurrentUser, repo: RepoDep):
    """Catálogo de cursos disponibles para el nivel educativo del estudiante."""
    service = _make_service(repo)
    available = service.get_available_courses(user["user_id"])
    enrolled_ids = {e["id"] for e in repo.get_user_enrollments(user["user_id"])}
    diag_done = set(repo.get_completed_diagnostic_course_ids(user["user_id"]))

    return [
        CourseResponse(
            id=c["id"],
            name=c["name"],
            block=c.get("block", ""),
            enrolled=c["id"] in enrolled_ids,
            group_id=c.get("group_id"),
            diagnostic_done=c["id"] in diag_done,
        )
        for c in available
    ]


@router.get("/blocks/{course_id}")
def course_blocks(course_id: str, user: CurrentUser, repo: RepoDep):
    """Bloques temáticos de un curso (concursos) con conteo de ítems."""
    return repo.get_course_blocks(course_id)


@router.get("/pvp/history")
def pvp_history(user: CurrentUser, repo: RepoDep):
    """Historial de partidas PvP del estudiante autenticado."""
    return repo.get_pvp_history(user["user_id"])


@router.post("/enroll", status_code=status.HTTP_201_CREATED)
def enroll(body: EnrollRequest, user: CurrentUser, repo: RepoDep):
    """Matricula al estudiante en un curso."""
    # Validar que el curso existe
    courses = repo.get_courses()
    valid_ids = {c["id"] if isinstance(c, dict) else c[0] for c in courses}
    if body.course_id not in valid_ids:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"El curso '{body.course_id}' no existe.",
        )
    service = _make_service(repo)
    service.enroll_in_course(user["user_id"], body.course_id, body.group_id)
    return {"message": f"Matriculado en {body.course_id} correctamente."}


@router.post("/enroll-by-code", status_code=status.HTTP_201_CREATED)
def enroll_by_code(body: EnrollByCodeRequest, user: CurrentUser, repo: RepoDep):
    """Acceso especial inter-nivel mediante código de invitación del docente."""
    group = repo.get_group_by_invite_code(body.invite_code)
    if not group:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Código de invitación inválido o expirado.",
        )
    group_id = group["id"] if isinstance(group, dict) else group[0]
    course_id = group["course_id"] if isinstance(group, dict) else group[2]
    if not course_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El grupo no tiene un curso asignado.",
        )
    repo.enroll_user(user["user_id"], course_id, group_id)
    return {"message": "Acceso especial activado correctamente.", "course_id": course_id}


@router.delete("/enroll/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
def unenroll(course_id: str, user: CurrentUser, repo: RepoDep):
    """Cancela la matrícula en un curso."""
    repo.unenroll_user(user["user_id"], course_id)


# ── Historial ──────────────────────────────────────────────────────────────────


@router.get("/history")
def history(user: CurrentUser, repo: RepoDep):
    """Últimos 20 intentos del estudiante (para el gráfico de ELO en el frontend)."""
    attempts = repo.get_latest_attempts(user["user_id"], limit=20)
    return {"attempts": attempts}


@router.get("/activity")
def activity(user: CurrentUser, repo: RepoDep, days: int = 70):
    """Heatmap de actividad diaria: {date: count} de intentos por día (últimos N días)."""
    data = repo.get_activity_heatmap(user["user_id"], days=days)
    return {"activity": data}


@router.get("/streak/{course_id}")
def streak_by_course(course_id: str, user: CurrentUser, repo: RepoDep):
    """Racha de estudio para un curso específico."""
    streak = repo.get_study_streak(user["user_id"], course_id=course_id)
    return {"course_id": course_id, "streak": streak}


@router.get("/group-ranking")
def group_ranking(user: CurrentUser, repo: RepoDep, course_id: str | None = None):
    """Ranking ELO de los compañeros del grupo del estudiante."""
    user_data = repo.get_user_by_id(user["user_id"])
    if not user_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado.")
    group_id = user_data.get("group_id") if isinstance(user_data, dict) else None
    if not group_id:
        return {"ranking": [], "my_rank": None}
    ranking = repo.get_group_ranking(group_id, course_id=course_id)
    # Encontrar la posición del usuario actual
    my_rank = next((r["rank_pos"] for r in ranking if r["user_id"] == user["user_id"]), None)
    return {"ranking": ranking, "my_rank": my_rank}


# ── Logros / Achievements ─────────────────────────────────────────────────────


@router.get("/achievements")
def achievements(user: CurrentUser, repo: RepoDep):
    """Retorna los logros/badges desbloqueados por el estudiante."""
    earned = repo.get_achievements(user["user_id"])
    # Enriquecer con metadatos del catálogo
    svc = _make_service(repo)
    catalog_map = {b["badge_id"]: b for b in svc._BADGE_CATALOG}
    result = []
    for a in earned:
        info = catalog_map.get(a["badge_id"], {})
        result.append(
            {
                "badge_id": a["badge_id"],
                "label": info.get("label", a["badge_id"]),
                "icon": info.get("icon", "🏅"),
                "desc": info.get("desc", ""),
                "earned_at": a["earned_at"],
            }
        )
    return {"achievements": result, "catalog": svc._BADGE_CATALOG}


# ── Procedimientos manuscritos ────────────────────────────────────────────────


@router.post("/procedure", response_model=ProcedureSubmitResponse)
async def submit_procedure(
    user: CurrentUser,
    repo: RepoDep,
    item_id: str = Form(...),
    item_content: str = Form(default=""),
    file: UploadFile = File(...),
    ai_proposed_score: float | None = Form(default=None),
    ai_feedback: str | None = Form(default=None),
):
    """Recibe y persiste un procedimiento manuscrito del estudiante.

    Si vienen ai_proposed_score/ai_feedback (del endpoint /procedure/analyze),
    se guardan en la submission para que el docente los vea como sugerencia.
    El score de IA (ai_proposed_score) NO afecta el ELO — solo teacher_score lo hace.
    """
    allowed = {"image/jpeg", "image/png", "image/webp", "application/pdf"}
    mime = file.content_type or "image/jpeg"
    if mime not in allowed:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Tipo de archivo no soportado: {mime}. Usa JPEG, PNG, WebP o PDF.",
        )

    image_data = await file.read()
    if len(image_data) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="El archivo excede el límite de 10 MB.",
        )

    file_hash = hashlib.sha256(image_data).hexdigest()

    repo.save_procedure_submission(
        student_id=user["user_id"],
        item_id=item_id,
        item_content=item_content,
        image_data=image_data,
        mime_type=mime,
        file_hash=file_hash,
    )

    if ai_proposed_score is not None:
        try:
            repo.save_ai_proposed_score(
                user["user_id"],
                item_id,
                float(ai_proposed_score),
                ai_feedback=ai_feedback or "",
            )
        except Exception:
            pass

    return ProcedureSubmitResponse(
        submission_id=0,
        ai_score=ai_proposed_score,
        ai_feedback=ai_feedback,
        status="pending" if ai_proposed_score is None else "PENDING_TEACHER_VALIDATION",
    )


@router.get("/ai-status")
def ai_status():
    """Indica al frontend si el servidor tiene IA configurada (sin revelar keys)."""
    from api.config import settings
    from src.infrastructure.external_api.ai_client import detect_provider_from_key

    procedure_key = settings.get_ai_key("procedure")
    if not procedure_key:
        return {"available": False, "provider": None}
    provider = settings.system_ai_provider or detect_provider_from_key(procedure_key) or "unknown"
    return {"available": True, "provider": provider}


@router.post("/procedure/analyze")
async def analyze_procedure(
    user: CurrentUser,
    item_id: str = Form(...),
    item_content: str = Form(default=""),
    api_key: str = Form(default=""),
    file: UploadFile = File(...),
):
    """Analiza un procedimiento con IA SIN PERSISTIR.

    Prioridad de API key: la del estudiante (si la envía) > la del sistema
    (env SYSTEM_AI_API_KEY). Soporta Groq (revisión rigurosa con Llama 4 Scout)
    y otros proveedores (revisión genérica con visión).
    """
    from api.config import settings
    from src.infrastructure.external_api.ai_client import detect_provider_from_key

    effective_key = settings.get_ai_key("procedure", api_key)
    if not effective_key:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="No hay API key de IA configurada. Pide al administrador que configure SYSTEM_AI_API_KEY.",
        )

    provider = detect_provider_from_key(effective_key)
    if settings.system_ai_provider and not api_key.strip():
        provider = settings.system_ai_provider

    allowed = {"image/jpeg", "image/png", "image/webp", "application/pdf"}
    mime = file.content_type or "image/jpeg"
    if mime not in allowed:
        raise HTTPException(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            detail=f"Tipo de archivo no soportado: {mime}.",
        )

    image_data = await file.read()
    if len(image_data) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="El archivo excede el límite de 10 MB.",
        )

    if mime == "application/pdf":
        try:
            import fitz  # PyMuPDF

            pdf_doc = fitz.open(stream=image_data, filetype="pdf")
            page = pdf_doc[0]
            pix = page.get_pixmap(dpi=200)
            image_data = pix.tobytes("png")
            mime = "image/png"
            pdf_doc.close()
        except Exception as pdf_err:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=f"No se pudo procesar el PDF: {pdf_err}",
            )

    if provider == "groq":
        from src.infrastructure.external_api.math_procedure_review import (
            review_math_procedure,
        )

        try:
            review = review_math_procedure(
                image_data,
                mime,
                api_key=effective_key,
                question_content=item_content or "",
            )
        except ValueError as exc:
            raise HTTPException(status_code=502, detail=f"Respuesta inválida de la IA: {exc}")
        except ConnectionError as exc:
            raise HTTPException(status_code=503, detail=f"Error de red con Groq: {exc}")
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Error al revisar procedimiento: {exc}")

        return {"item_id": item_id, "provider": "groq", "review": review}

    else:
        from src.infrastructure.external_api.ai_client import analyze_procedure_image

        try:
            result = analyze_procedure_image(
                image_data,
                mime,
                question_content=item_content or "",
                model_name="",
                api_key=effective_key,
                provider=provider,
            )
        except Exception as exc:
            raise HTTPException(status_code=500, detail=f"Error al analizar procedimiento: {exc}")

        if result == "VISION_NOT_SUPPORTED":
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="El modelo configurado no soporta visión. Usa Groq o un modelo con visión.",
            )

        return {
            "item_id": item_id,
            "provider": provider or "unknown",
            "review": {
                "score_procedimiento": None,
                "evaluacion_global": result,
                "transcripcion": None,
                "pasos": [],
                "errores_detectados": [],
                "saltos_logicos": [],
                "resultado_correcto": None,
                "corresponde_a_pregunta": None,
            },
        }


@router.get("/procedures")
def list_my_procedures(user: CurrentUser, repo: RepoDep, limit: int = 50):
    """Lista los procedimientos enviados por el estudiante actual con su
    estado y, si están validados, score docente, comentario y delta ELO.
    Nunca incluye contenido sensible (R9/V2-R9: solo aplica a items, no a procedimientos)."""
    rows = repo.get_student_procedure_submissions(user["user_id"], limit=limit)
    return {"submissions": rows}


# ── Reportes técnicos ─────────────────────────────────────────────────────────


@router.post("/problems", status_code=status.HTTP_201_CREATED)
def submit_problem_report(body: dict, user: CurrentUser, repo: RepoDep):
    """Crea un reporte de problema técnico (mínimo 10 caracteres en la descripción)."""
    description = (body.get("description") or "").strip()
    if len(description) < 10:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La descripción debe tener al menos 10 caracteres.",
        )
    if len(description) > 2000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La descripción no puede exceder 2000 caracteres.",
        )
    repo.save_problem_report(user_id=user["user_id"], description=description)
    return {"message": "Reporte enviado. Gracias por avisarnos."}


# ── Perfil ───────────────────────────────────────────────────────────────────


@router.patch("/profile")
def update_profile(body: dict, user: CurrentUser, repo: RepoDep):
    """Actualiza el correo electrónico del estudiante."""
    email = (body.get("email") or "").strip()
    if not email:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="El correo electrónico es obligatorio.",
        )
    try:
        repo.update_user_email(user["user_id"], email)
    except ValueError as e:
        code = (
            status.HTTP_409_CONFLICT
            if "registrado" in str(e)
            else status.HTTP_422_UNPROCESSABLE_ENTITY
        )
        raise HTTPException(status_code=code, detail=str(e))
    return {"message": "Correo actualizado correctamente."}


# ── Modo Examen ───────────────────────────────────────────────────────────────


def _build_standard_exam(repo, course_id: str, n: int) -> list[dict]:
    """
    Construye un examen estándar de N preguntas con curva de dificultad fija.

    Distribución por bandas:
      - 30% fácil (cuartil bajo de difficulty)
      - 40% media
      - 30% difícil
    Mezcla aleatoria dentro de cada banda, orden global ascendente.
    Sin selector adaptativo y sin tocar el ELO del estudiante.
    """
    all_items = repo.get_items_from_db(course_id=course_id)
    if not all_items:
        return []

    sorted_items = sorted(all_items, key=lambda it: it["difficulty"])
    total = len(sorted_items)
    third = max(1, total // 3)
    band_easy = sorted_items[:third]
    band_mid = sorted_items[third : 2 * third]
    band_hard = sorted_items[2 * third :]

    n_easy = max(1, round(n * 0.30))
    n_hard = max(1, round(n * 0.30))
    n_mid = max(0, n - n_easy - n_hard)

    pool: list[dict] = []
    pool += random.sample(band_easy, min(n_easy, len(band_easy)))
    pool += random.sample(band_mid, min(n_mid, len(band_mid)))
    pool += random.sample(band_hard, min(n_hard, len(band_hard)))

    # Si alguna banda quedó corta, rellenar con items no usados de cualquier banda
    used_ids = {it["id"] for it in pool}
    remaining = [it for it in sorted_items if it["id"] not in used_ids]
    random.shuffle(remaining)
    while len(pool) < n and remaining:
        pool.append(remaining.pop())

    pool.sort(key=lambda it: it["difficulty"])
    return pool[:n]


def _items_from_template(repo, template: dict) -> list[dict]:
    """Carga los items de una plantilla preservando el orden definido por el docente."""
    by_id = {it["id"]: it for it in repo.get_items_from_db(course_id=template["course_id"])}
    return [by_id[i] for i in template["item_ids"] if i in by_id]


@router.get("/exam/templates", response_model=list[ExamTemplateSummary])
def list_exam_templates_for_student(
    repo: RepoDep,
    user: CurrentUser,
    course_id: str,
):
    """Plantillas de examen visibles a este estudiante en el curso.

    Filtrado por:
    - Plantilla NO archivada del curso indicado
    - Y: no tiene asignaciones (legacy/abierta) → visible a todos los inscritos
    -    O: hay una asignación al grupo del estudiante con ventana activa
    """
    templates = repo.list_active_templates_for_student(user_id=user["user_id"], course_id=course_id)
    return [
        ExamTemplateSummary(
            id=t["id"],
            title=t["title"],
            course_id=t["course_id"],
            n_questions=len(t["item_ids"]),
            time_limit_min=t["time_limit_min"],
            created_at=t["created_at"],
            window_ends_at=t.get("window_ends_at"),
        )
        for t in templates
    ]


@router.get("/exam/pending", response_model=list[PendingExam])
def list_pending_exams(repo: RepoDep, user: CurrentUser):
    """Plantillas pendientes para el estudiante en TODOS sus cursos inscritos.

    Se usa para el badge de notificación en el sidebar.
    """
    rows = repo.list_pending_exams_for_student(user_id=user["user_id"])
    return [PendingExam(**r) for r in rows]


@router.post("/exam/start", response_model=ExamStartResponse)
def exam_start(body: ExamStartRequest, user: CurrentUser, repo: RepoDep):
    """
    Inicia una sesión de examen.

    Modos:
      - Con `template_id`: usa exactamente los items de la plantilla del docente
        en el orden definido. Ignora n_questions y time_limit_minutes (toma los
        del template).
      - Sin `template_id`: examen estándar con curva de dificultad 30/40/30.

    En ambos casos, NO afecta el ELO del estudiante.
    """
    if body.template_id is not None:
        template = repo.get_exam_template(body.template_id)
        if not template or template.get("archived"):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Plantilla no encontrada o archivada.",
            )
        if template["course_id"] != body.course_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La plantilla no corresponde al curso indicado.",
            )
        selected = _items_from_template(repo, template)
        time_limit_seconds = template["time_limit_min"] * 60
    else:
        n = min(body.n_questions, 30)
        selected = _build_standard_exam(repo, body.course_id, n)
        time_limit_seconds = body.time_limit_minutes * 60

    if not selected:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No hay preguntas disponibles para este examen.",
        )

    items = [
        ItemResponse(
            id=it["id"],
            content=it["content"],
            difficulty=it["difficulty"],
            topic=it["topic"],
            options=it["options"],
            image_url=it.get("image_url"),
            tags=it.get("tags") or [],
        )
        for it in selected
    ]

    return ExamStartResponse(
        items=items,
        n_questions=len(items),
        time_limit_seconds=time_limit_seconds,
        course_id=body.course_id,
    )


@router.post("/exam/submit", response_model=ExamSubmitResponse)
def exam_submit(body: ExamSubmitRequest, user: CurrentUser, repo: RepoDep):
    """
    Recibe las respuestas del examen y devuelve la calificación.

    El examen es EVALUATIVO, no formativo: NO actualiza el ELO del estudiante
    ni la dificultad del ítem. Solo cuenta correctas/incorrectas y persiste
    la sesión en `exam_sessions` para el historial.

    El ELO solo cambia en la sala de práctica.
    """
    results = []
    correct_count = 0
    responses = []  # por pregunta, para análisis del docente

    for ans in body.answers:
        item_db = repo.get_item_by_id(ans.item_id)
        if not item_db:
            continue

        is_correct = ans.selected_option == item_db["correct_option"]
        if is_correct:
            correct_count += 1

        results.append(
            {
                "item_id": ans.item_id,
                "is_correct": is_correct,
                "selected_option": ans.selected_option,
                "elo_delta": 0.0,  # examen no afecta ELO
            }
        )
        responses.append(
            {
                "item_id": ans.item_id,
                "topic": item_db.get("topic"),
                "is_correct": is_correct,
            }
        )

    # ELO global actual (sin modificación, solo para mostrar en results)
    vector = build_vector_rating(user["user_id"], repo)
    score_pct = round(correct_count / len(body.answers) * 100, 1) if body.answers else 0.0
    global_elo = round(aggregate_global_elo(vector), 2)

    try:
        repo.save_exam_session(
            user_id=user["user_id"],
            course_id=body.course_id,
            course_name=body.course_name,
            n_questions=len(body.answers),
            correct_count=correct_count,
            score_pct=score_pct,
            global_elo_after=global_elo,
            template_id=body.template_id,
            responses=responses,
        )
    except Exception:
        pass

    return ExamSubmitResponse(
        results=results,
        correct_count=correct_count,
        total_questions=len(body.answers),
        score_pct=score_pct,
        global_elo_after=global_elo,
    )


@router.get("/exam/history")
def exam_history(user: CurrentUser, repo: RepoDep):
    """Historial de intentos de examen del estudiante (últimos 20)."""
    return repo.get_exam_history(user["user_id"], limit=20)


# ── Examen diagnóstico (inicio de materia) ────────────────────────────────────

_DIAG_N = 10  # longitud estándar del diagnóstico


def _diff_tier(difficulty: float) -> dict:
    """Mapea la dificultad del ítem a pesos ELO (win/loss) del diagnóstico."""
    if difficulty < 1100:
        return {"win": 14, "loss": -20}
    if difficulty >= 1450:
        return {"win": 34, "loss": -6}
    return {"win": 22, "loss": -12}


_DIAG_LEAGUES = [
    {"name": "Diamante", "min": 1320, "color": "#7dd3fc", "rank": "Avanzado"},
    {"name": "Oro", "min": 1180, "color": "#ffd700", "rank": "Intermedio-alto"},
    {"name": "Plata", "min": 1040, "color": "#cbd5e1", "rank": "Intermedio"},
    {"name": "Bronce", "min": 0, "color": "#d8975a", "rank": "Inicial"},
]


def _diag_league(elo: float) -> dict:
    for lg in _DIAG_LEAGUES:
        if elo >= lg["min"]:
            return lg
    return _DIAG_LEAGUES[-1]


@router.get("/diagnostic/{course_id}", response_model=DiagnosticStatusResponse)
def diagnostic_status(course_id: str, user: CurrentUser, repo: RepoDep, redo: bool = False):
    """Estado del diagnóstico de una materia.

    Si ya está hecho → devuelve el resultado guardado. Si no (o `redo=true`) →
    devuelve ~10 preguntas (sin la opción correcta) para presentarlo."""
    existing = repo.get_diagnostic(user["user_id"], course_id)
    if existing and not redo:
        return DiagnosticStatusResponse(
            completed=True,
            course_id=course_id,
            result={**existing["result"], "initial_elo": existing["initial_elo"],
                    "score_pct": existing["score_pct"]},
        )

    items = _build_standard_exam(repo, course_id, _DIAG_N)
    questions = [
        DiagnosticQuestion(
            id=it["id"],
            content=it["content"],
            topic=it.get("topic"),
            difficulty=int(it.get("difficulty", 1000)),
            options=it.get("options", []),
        )
        for it in items
    ]
    return DiagnosticStatusResponse(completed=False, course_id=course_id, questions=questions)


@router.post("/diagnostic/{course_id}/submit", response_model=DiagnosticResultResponse)
def diagnostic_submit(
    course_id: str, body: DiagnosticSubmitRequest, user: CurrentUser, repo: RepoDep
):
    """Califica el diagnóstico, fija el ELO inicial por tópico y lo marca hecho.

    Evaluativo: no genera intentos. 'No lo sé'/saltar = opción vacía → no
    cambia ELO pero cuenta como vacío del tema."""
    BASE = 1000.0
    by_topic: dict[str, dict] = {}
    correct_total = 0
    answered = 0

    for ans in body.answers:
        item_db = repo.get_item_by_id(ans.item_id)
        if not item_db:
            continue
        topic = item_db.get("topic") or course_id
        tier = _diff_tier(float(item_db.get("difficulty", 1000)))
        t = by_topic.setdefault(topic, {"elo": BASE, "correct": 0, "total": 0})
        t["total"] += 1
        if not ans.selected_option:  # no contestada / no lo sé
            continue
        answered += 1
        if ans.selected_option == item_db["correct_option"]:
            t["elo"] += tier["win"]
            t["correct"] += 1
            correct_total += 1
        else:
            t["elo"] += tier["loss"]

    # fijar ELO inicial por tópico (clamp) y construir desglose
    themes = []
    elos = []
    for topic, t in by_topic.items():
        elo = max(760.0, round(t["elo"], 2))
        elos.append(elo)
        repo.set_topic_elo_baseline(user["user_id"], topic, elo)
        ratio = t["correct"] / t["total"] if t["total"] else 0.0
        status = "strong" if ratio >= 0.67 else "mid" if ratio >= 0.34 else "gap"
        themes.append(
            {
                "topic": topic,
                "correct": t["correct"],
                "total": t["total"],
                "ratio": round(ratio, 2),
                "status": status,
                "elo": elo,
            }
        )

    total_q = sum(t["total"] for t in by_topic.values())
    initial_elo = round(sum(elos) / len(elos), 2) if elos else BASE
    score_pct = round(correct_total / total_q * 100, 1) if total_q else 0.0
    league = _diag_league(initial_elo)

    import json as _json

    result_payload = {
        "themes": themes,
        "league": league,
        "correct_total": correct_total,
        "answered": answered,
    }
    repo.save_diagnostic(
        user["user_id"], course_id, initial_elo, score_pct, _json.dumps(result_payload)
    )

    return DiagnosticResultResponse(
        initial_elo=initial_elo,
        score_pct=score_pct,
        league=league,
        themes=themes,
        correct_total=correct_total,
        answered=answered,
    )


# ── Mapa de contenido ─────────────────────────────────────────────────────────

_MASTERY_ELO = 1250.0  # umbral para considerar un tópico "dominado"
_LESSON_EVENTS = {
    "node_viewed",
    "objectives_viewed",
    "math_convention_viewed",
    "node_completed",
}


def _ensure_n2_hub_completed_if_cards_opened(repo, user_id: int, course_id: str) -> None:
    """Repara estados previos: 6 carteles abiertos => hub N2 completado."""
    progress = repo.get_lesson_progress(user_id, course_id, N2_HUB_NODE_ID)
    if progress["state"] == "completed":
        return

    hub = get_lesson(N2_HUB_NODE_ID)
    if not hub:
        return
    required = {interaction["interaction_id"] for interaction in hub.get("interactions", [])}
    responses = repo.get_lesson_interactions(user_id, course_id, N2_HUB_NODE_ID)
    if required and required.issubset(responses):
        repo.record_lesson_event(user_id, course_id, N2_HUB_NODE_ID, "node_completed")


def _ensure_n3_hub_completed_if_machines_introduced(repo, user_id: int, course_id: str) -> None:
    """Repara estados previos: 5 máquinas introducidas => hub N3 completado."""
    progress = repo.get_lesson_progress(user_id, course_id, N3_HUB_NODE_ID)
    if progress["state"] == "completed":
        return

    hub = get_lesson(N3_HUB_NODE_ID)
    if not hub:
        return
    required = {interaction["interaction_id"] for interaction in hub.get("interactions", [])}
    responses = repo.get_lesson_interactions(user_id, course_id, N3_HUB_NODE_ID)
    if required and required.issubset(responses):
        repo.record_lesson_event(user_id, course_id, N3_HUB_NODE_ID, "node_completed")


def _all_nodes_completed(repo, user_id: int, course_id: str, node_ids: list[str]) -> bool:
    return all(
        repo.get_lesson_progress(user_id, course_id, node_id)["state"] == "completed"
        for node_id in node_ids
    )


def _lesson_with_progress(repo, user_id: int, course_id: str, lesson: dict) -> dict:
    """Combina el catálogo con progreso, respetando el desbloqueo secuencial."""
    if lesson["node_id"] == N2_HUB_NODE_ID or lesson.get("unlock_after") == N2_HUB_NODE_ID:
        _ensure_n2_hub_completed_if_cards_opened(repo, user_id, course_id)
    if lesson["node_id"] == N3_HUB_NODE_ID or lesson.get("unlock_after") == N3_HUB_NODE_ID:
        _ensure_n3_hub_completed_if_machines_introduced(repo, user_id, course_id)
    if lesson["node_id"] in {N3_HUB_NODE_ID, *N3_MACHINE_NODE_IDS}:
        if not _all_nodes_completed(repo, user_id, course_id, N2_OPERATION_NODE_IDS):
            raise HTTPException(status_code=403, detail="Completa el Nivel 2 primero")

    unlock_after = lesson.get("unlock_after")
    if unlock_after:
        prerequisite = repo.get_lesson_progress(user_id, course_id, unlock_after)
        if prerequisite["state"] != "completed":
            raise HTTPException(status_code=403, detail="Completa el nodo anterior primero")

    progress = repo.get_lesson_progress(user_id, course_id, lesson["node_id"])
    progress["responses"] = repo.get_lesson_interactions(
        user_id, course_id, lesson["node_id"]
    )
    diagnostic = repo.get_diagnostic(user_id, course_id)
    presentation = presentation_band(diagnostic.get("score_pct") if diagnostic else None)

    # Complejos (B09) es callejón opcional: solo banda intermedia/avanzada.
    if lesson["node_id"] == COMPLEX_NODE_ID and presentation == "basico":
        raise HTTPException(
            status_code=403,
            detail="Nodo opcional disponible solo para banda intermedia o avanzada",
        )

    # explored_complex_branch (derivado): el estudiante abrió/completó B09.
    # Gobierna el contenido complejo en cascada (B10–B13).
    complex_state = repo.get_lesson_progress(user_id, course_id, COMPLEX_NODE_ID)["state"]
    explored_complex_branch = complex_state in ("viewed", "completed")

    lesson_payload = {**lesson}
    if lesson["node_id"] == N3_HUB_NODE_ID and lesson.get("content"):
        content = {**lesson["content"]}
        machines = []
        previous_completed = True
        for machine in content.get("machines", []):
            machine_progress = repo.get_lesson_progress(user_id, course_id, machine["node_id"])
            state = (
                "completed"
                if machine_progress["state"] == "completed"
                else "current"
                if previous_completed
                else "blocked"
            )
            machines.append({**machine, "state": state})
            previous_completed = machine_progress["state"] == "completed"
        content["machines"] = machines
        lesson_payload["content"] = content

    return {
        **lesson_payload,
        "course_id": course_id,
        "state": progress["state"],
        "presentation": presentation,
        "explored_complex_branch": explored_complex_branch,
        "progress": progress,
    }


@router.get(
    "/lessons/{course_id}/{node_id}",
    response_model=LessonDetailResponse,
)
def lesson_detail(course_id: str, node_id: str, user: CurrentUser, repo: RepoDep):
    """Entrega metadatos curriculares sin exponer respuestas ni tocar ELO."""
    lesson = get_lesson(node_id)
    if course_id != PREALGEBRA_COURSE_ID or lesson is None:
        raise HTTPException(status_code=404, detail="Lección no encontrada")

    return LessonDetailResponse(
        **_lesson_with_progress(repo, user["user_id"], course_id, lesson)
    )


@router.post(
    "/lessons/{course_id}/{node_id}/events",
    response_model=LessonDetailResponse,
)
def lesson_event(
    course_id: str,
    node_id: str,
    body: LessonEventRequest,
    user: CurrentUser,
    repo: RepoDep,
):
    """Registra progreso idempotente de contenido; nunca actualiza ELO."""
    lesson = get_lesson(node_id)
    if course_id != PREALGEBRA_COURSE_ID or lesson is None:
        raise HTTPException(status_code=404, detail="Lección no encontrada")
    if body.event not in _LESSON_EVENTS:
        raise HTTPException(status_code=422, detail="Evento de lección inválido")

    _lesson_with_progress(repo, user["user_id"], course_id, lesson)
    required_by_node = {
        TRIGGER_NODE_ID: {"PREALG-N1-B02-Q01", "PREALG-N1-B02-Q02"},
        STAIRCASE_NODE_ID: {"PREALG-N1-B03-Q01"},
        NATURALS_NODE_ID: {
            "PREALG-N1-B04-Q01",
            "PREALG-N1-B04-Q02",
            "PREALG-N1-B04-Q03",
            "PREALG-N1-B04-Q04",
        },
        INTEGERS_NODE_ID: {
            "PREALG-N1-B05-Q01",
            "PREALG-N1-B05-Q02",
            "PREALG-N1-B05-Q03",
            "PREALG-N1-B05-Q04",
            "PREALG-N1-B05-Q05",
        },
        RATIONALS_NODE_ID: {
            "PREALG-N1-B06-Q01",
            "PREALG-N1-B06-Q02",
            "PREALG-N1-B06-Q03",
            "PREALG-N1-B06-Q04",
        },
    }
    if body.event == "node_completed" and node_id in required_by_node:
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        required = required_by_node[node_id]
        if not required.issubset(responses):
            raise HTTPException(status_code=409, detail="Responde las dos preguntas primero")
    if body.event == "node_completed" and (
        node_id == N2_HUB_NODE_ID or node_id in N2_OPERATION_NODE_IDS
    ):
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        required = {interaction["interaction_id"] for interaction in lesson.get("interactions", [])}
        if not required.issubset(responses):
            raise HTTPException(status_code=409, detail="Completa las interacciones del nodo")
    if body.event == "node_completed" and (
        node_id == N3_HUB_NODE_ID or node_id in N3_MACHINE_NODE_IDS
    ):
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        required = {interaction["interaction_id"] for interaction in lesson.get("interactions", [])}
        if not required.issubset(responses):
            raise HTTPException(status_code=409, detail="Completa las interacciones del nodo")
    repo.record_lesson_event(user["user_id"], course_id, node_id, body.event)
    return LessonDetailResponse(
        **_lesson_with_progress(repo, user["user_id"], course_id, lesson)
    )


@router.post(
    "/lessons/{course_id}/{node_id}/interactions",
    response_model=LessonInteractionResponse,
)
def lesson_interaction(
    course_id: str,
    node_id: str,
    body: LessonInteractionRequest,
    user: CurrentUser,
    repo: RepoDep,
):
    """Evalúa y guarda solo una selección cerrada; no acepta texto libre."""
    lesson = get_lesson(node_id)
    if course_id != PREALGEBRA_COURSE_ID or lesson is None:
        raise HTTPException(status_code=404, detail="Lección no encontrada")
    _lesson_with_progress(repo, user["user_id"], course_id, lesson)
    result = evaluate_interaction(node_id, body.interaction_id, body.selected_option)
    if result is None:
        raise HTTPException(status_code=422, detail="Interacción u opción inválida")

    repo.save_lesson_interaction(
        user["user_id"],
        course_id,
        node_id,
        result["interaction_id"],
        result["selected_option"],
        result["is_expected"],
        result["misconception_tag"],
    )
    if node_id == N2_HUB_NODE_ID:
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        required = {interaction["interaction_id"] for interaction in lesson.get("interactions", [])}
        if required and required.issubset(responses):
            repo.record_lesson_event(user["user_id"], course_id, node_id, "node_completed")
    if node_id == N3_HUB_NODE_ID:
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        required = {interaction["interaction_id"] for interaction in lesson.get("interactions", [])}
        if required and required.issubset(responses):
            repo.record_lesson_event(user["user_id"], course_id, node_id, "node_completed")
    return LessonInteractionResponse(**result)


_NODE_MAP_TITLE = {
    NATURALS_NODE_ID: "prealgebra.n1.b04.mapTitle",
    INTEGERS_NODE_ID: "prealgebra.n1.b05.mapTitle",
    RATIONALS_NODE_ID: "prealgebra.n1.b06.mapTitle",
    IRRATIONALS_NODE_ID: "prealgebra.n1.b07.mapTitle",
    REALS_NODE_ID: "prealgebra.n1.b08.mapTitle",
    COMPLEX_NODE_ID: "prealgebra.n1.b09.mapTitle",
    CLASSIFIER_BASIC_NODE_ID: "prealgebra.n1.b10.mapTitle",
    CLASSIFIER_RIGOROUS_NODE_ID: "prealgebra.n1.b11.mapTitle",
    DETECTIVE_NODE_ID: "prealgebra.n1.b12.mapTitle",
}


@router.get("/prealgebra-summary/{course_id}")
def prealgebra_summary(course_id: str, user: CurrentUser, repo: RepoDep):
    """Cierre diagnóstico (B13): agrega progreso y misconceptions del nivel.

    No afecta ELO. MVP: persiste/lee misconceptions de las interacciones y
    propone hasta 4 nodos de repaso. Sin panel docente todavía.
    """
    explored = repo.get_lesson_progress(
        user["user_id"], course_id, COMPLEX_NODE_ID
    )["state"] in ("viewed", "completed")

    applicable = [n for n in DIAGNOSTIC_NODE_IDS if n != COMPLEX_NODE_ID or explored]
    completed_nodes = 0
    misconceptions: list[str] = []
    for node_id in applicable:
        progress = repo.get_lesson_progress(user["user_id"], course_id, node_id)
        if progress["state"] == "completed":
            completed_nodes += 1
        responses = repo.get_lesson_interactions(user["user_id"], course_id, node_id)
        for resp in responses.values():
            tag = resp.get("misconception_tag")
            if tag and tag not in misconceptions:
                misconceptions.append(tag)

    # Ruta de repaso: nodos recomendados (máx 4), únicos, en orden de ruta.
    review_nodes: list[str] = []
    for tag in misconceptions:
        node = recommended_node_for_misconception(tag)
        if node and node in _NODE_MAP_TITLE and node not in review_nodes:
            review_nodes.append(node)
    review_nodes.sort(key=lambda n: DIAGNOSTIC_NODE_IDS.index(n))
    review = [
        {"node_id": n, "label_key": _NODE_MAP_TITLE[n]}
        for n in review_nodes[:4]
    ]

    if not misconceptions and completed_nodes == len(applicable):
        overall_status = "strong"
    elif len(review) >= 3:
        overall_status = "attention"
    else:
        overall_status = "review"

    return {
        "course_id": course_id,
        "completed_nodes": completed_nodes,
        "total_nodes": len(applicable),
        "overall_status": overall_status,
        "review": review,
    }


@router.get("/map/{course_id}", response_model=CourseMapResponse)
def course_map(course_id: str, user: CurrentUser, repo: RepoDep):
    """Mapa de contenido de una materia: un nodo por tópico, ordenados por
    dificultad, con el ELO/estado del estudiante (leído de student_topic_elo,
    incluye el ELO inicial del diagnóstico)."""
    items = repo.get_items_from_db(course_id=course_id)
    elo_map = repo.get_topic_elo_map(user["user_id"])
    diagnostic_done = repo.get_diagnostic(user["user_id"], course_id) is not None

    # agrupar ítems por tópico con sus dificultades
    by_topic: dict[str, list[float]] = {}
    for it in items:
        topic = it.get("topic") or course_id
        by_topic.setdefault(topic, []).append(float(it.get("difficulty", 1000)))

    topics_sorted = sorted(by_topic.items(), key=lambda kv: sum(kv[1]) / max(1, len(kv[1])))

    # Si hay pocos tópicos, subdividir cada uno en niveles por dificultad para
    # que el mapa tenga varios nodos visibles. Si hay muchos, usar tópicos.
    _LEVELS = ["Fundamentos", "Intermedio", "Avanzado"]
    raw: list[dict] = []
    subdivide = len(topics_sorted) < 5

    def _elo_for(topic: str) -> tuple[float, float]:
        te = elo_map.get(topic)
        return (float(te["elo"]) if te else 1000.0, float(te["rd"]) if te else 350.0)

    for topic, diffs in topics_sorted:
        elo, rd = _elo_for(topic)
        if subdivide and len(diffs) >= 3:
            diffs_sorted = sorted(diffs)
            third = max(1, len(diffs_sorted) // 3)
            bands = [diffs_sorted[:third], diffs_sorted[third : 2 * third], diffs_sorted[2 * third :]]
            for bi, band in enumerate(bands):
                if not band:
                    continue
                raw.append({
                    "topic": topic,
                    "label": f"{topic} · {_LEVELS[bi]}",
                    "elo": elo, "rd": rd, "item_count": len(band),
                })
        else:
            raw.append({"topic": topic, "label": topic, "elo": elo, "rd": rd, "item_count": len(diffs)})

    raw = raw[:30]  # tope de nodos para no saturar el mapa

    welcome_progress = None
    trigger_progress = None
    staircase_progress = None
    naturals_progress = None
    integers_progress = None
    rationals_progress = None
    irrationals_progress = None
    reals_progress = None
    curriculum_completed = True
    if course_id == PREALGEBRA_COURSE_ID:
        welcome_progress = repo.get_lesson_progress(
            user["user_id"], course_id, WELCOME_NODE_ID
        )
        trigger_progress = repo.get_lesson_progress(
            user["user_id"], course_id, TRIGGER_NODE_ID
        )
        staircase_progress = repo.get_lesson_progress(
            user["user_id"], course_id, STAIRCASE_NODE_ID
        )
        naturals_progress = repo.get_lesson_progress(
            user["user_id"], course_id, NATURALS_NODE_ID
        )
        integers_progress = repo.get_lesson_progress(
            user["user_id"], course_id, INTEGERS_NODE_ID
        )
        rationals_progress = repo.get_lesson_progress(
            user["user_id"], course_id, RATIONALS_NODE_ID
        )
        irrationals_progress = repo.get_lesson_progress(
            user["user_id"], course_id, IRRATIONALS_NODE_ID
        )
        reals_progress = repo.get_lesson_progress(
            user["user_id"], course_id, REALS_NODE_ID
        )
        complex_progress = repo.get_lesson_progress(
            user["user_id"], course_id, COMPLEX_NODE_ID
        )
        classifier_basic_progress = repo.get_lesson_progress(
            user["user_id"], course_id, CLASSIFIER_BASIC_NODE_ID
        )
        classifier_rigorous_progress = repo.get_lesson_progress(
            user["user_id"], course_id, CLASSIFIER_RIGOROUS_NODE_ID
        )
        detective_progress = repo.get_lesson_progress(
            user["user_id"], course_id, DETECTIVE_NODE_ID
        )
        closing_progress = repo.get_lesson_progress(
            user["user_id"], course_id, CLOSING_NODE_ID
        )
        n2_hub_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_HUB_NODE_ID
        )
        n2_sum_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_SUM_NODE_ID
        )
        n2_subtraction_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_SUBTRACTION_NODE_ID
        )
        n2_multiplication_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_MULTIPLICATION_NODE_ID
        )
        n2_division_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_DIVISION_NODE_ID
        )
        n2_exponentiation_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_EXPONENTIATION_NODE_ID
        )
        n2_radication_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N2_RADICATION_NODE_ID
        )
        n3_hub_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_HUB_NODE_ID
        )
        n3_commutative_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_COMMUTATIVE_NODE_ID
        )
        n3_associative_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_ASSOCIATIVE_NODE_ID
        )
        n3_distributive_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_DISTRIBUTIVE_NODE_ID
        )
        n3_identity_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_IDENTITY_NODE_ID
        )
        n3_inverses_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N3_INVERSES_NODE_ID
        )
        n4_hub_progress = repo.get_lesson_progress(
            user["user_id"], course_id, N4_HUB_NODE_ID
        )
        n4_progress_by_node = {
            node_id: repo.get_lesson_progress(user["user_id"], course_id, node_id)
            for node_id in N4_CONCEPT_NODE_IDS
        }
        # B09 (complejos) solo visible para banda intermedia/avanzada (callejón opcional).
        _diag = repo.get_diagnostic(user["user_id"], course_id)
        complex_visible = presentation_band(
            _diag.get("score_pct") if _diag else None
        ) in ("intermedio", "avanzado")
        curriculum_completed = reals_progress["state"] == "completed"

    # estado: dominado (>=umbral) = completed; el PRIMER nodo no dominado =
    # current (dónde reforzar); el resto = available (no se bloquea: es refuerzo).
    current_idx = (
        next((i for i, n in enumerate(raw) if n["elo"] < _MASTERY_ELO), None)
        if curriculum_completed
        else None
    )
    nodes = [
        MapNode(
            topic=n["topic"],
            label=n["label"],
            elo=round(n["elo"], 1),
            rd=round(n["rd"], 1),
            item_count=n["item_count"],
            state=(
                "blocked"
                if not curriculum_completed
                else "completed"
                if n["elo"] >= _MASTERY_ELO
                else "current"
                if i == current_idx
                else "available"
            ),
        )
        for i, n in enumerate(raw)
    ]

    if welcome_progress is not None:
        nodes.insert(
            0,
            MapNode(
                topic="reales",
                label="Reales",
                label_key="prealgebra.n1.b08.mapTitle",
                node_id=REALS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=2,
                state=(
                    "blocked"
                    if not irrationals_progress or irrationals_progress["state"] != "completed"
                    else "completed"
                    if reals_progress and reals_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="irracionales",
                label="Irracionales",
                label_key="prealgebra.n1.b07.mapTitle",
                node_id=IRRATIONALS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=3,
                state=(
                    "blocked"
                    if not rationals_progress or rationals_progress["state"] != "completed"
                    else "completed"
                    if irrationals_progress and irrationals_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="racionales",
                label="Racionales",
                label_key="prealgebra.n1.b06.mapTitle",
                node_id=RATIONALS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=3,
                state=(
                    "blocked"
                    if not integers_progress or integers_progress["state"] != "completed"
                    else "completed"
                    if rationals_progress and rationals_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="enteros",
                label="Enteros",
                label_key="prealgebra.n1.b05.mapTitle",
                node_id=INTEGERS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=4,
                state=(
                    "blocked"
                    if not naturals_progress or naturals_progress["state"] != "completed"
                    else "completed"
                    if integers_progress and integers_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="naturales",
                label="Naturales",
                label_key="prealgebra.n1.b04.mapTitle",
                node_id=NATURALS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=4,
                state=(
                    "blocked"
                    if not staircase_progress or staircase_progress["state"] != "completed"
                    else "completed"
                    if naturals_progress and naturals_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="organizador_previo",
                label="Escalera de la necesidad",
                label_key="prealgebra.n1.b03.mapTitle",
                node_id=STAIRCASE_NODE_ID,
                node_type="concept_organizer",
                elo=0,
                rd=0,
                item_count=1,
                state=(
                    "blocked"
                    if not trigger_progress or trigger_progress["state"] != "completed"
                    else "completed"
                    if staircase_progress and staircase_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="conflicto_cognitivo_intro",
                label="Pregunta detonadora",
                label_key="prealgebra.n1.b02.mapTitle",
                node_id=TRIGGER_NODE_ID,
                node_type="safe_interaction",
                elo=0,
                rd=0,
                item_count=2,
                state=(
                    "blocked"
                    if welcome_progress["state"] != "completed"
                    else "completed"
                    if trigger_progress and trigger_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        nodes.insert(
            0,
            MapNode(
                topic="orientacion_intro",
                label="Bienvenida",
                label_key="prealgebra.n1.b01.mapTitle",
                node_id=WELCOME_NODE_ID,
                node_type="content_intro",
                elo=0,
                rd=0,
                item_count=0,
                state=(
                    "completed" if welcome_progress["state"] == "completed" else "current"
                ),
            ),
        )
        # B09 complejos: desvío opcional tras los reales, solo para banda
        # intermedia/avanzada. Banda Básico salta de B08 (Reales) a B10.
        if complex_visible:
            nodes.insert(
                8,
                MapNode(
                    topic="complejos",
                    label="Complejos",
                    label_key="prealgebra.n1.b09.mapTitle",
                    node_id=COMPLEX_NODE_ID,
                    node_type="optional_extension",
                    elo=0,
                    rd=0,
                    item_count=3,
                    state=(
                        "blocked"
                        if not reals_progress or reals_progress["state"] != "completed"
                        else "completed"
                        if complex_progress and complex_progress["state"] == "completed"
                        else "available"
                    ),
                ),
            )
        # B10 clasificador básico: consolidación tras la ruta núcleo. Se desbloquea
        # al completar los reales (la rama compleja B09 es opcional). Va justo
        # después del prefijo (índice 9 si B09 está visible, 8 si no).
        nodes.insert(
            9 if complex_visible else 8,
            MapNode(
                topic="clasificacion_especifica",
                label="El Clasificador I",
                label_key="prealgebra.n1.b10.mapTitle",
                node_id=CLASSIFIER_BASIC_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=8,
                state=(
                    "blocked"
                    if not reals_progress or reals_progress["state"] != "completed"
                    else "completed"
                    if classifier_basic_progress and classifier_basic_progress["state"] == "completed"
                    else "current"
                ),
            ),
        )
        # B11 clasificador riguroso: pertenencia múltiple. Va tras B10.
        nodes.insert(
            10 if complex_visible else 9,
            MapNode(
                topic="clasificacion_multiple",
                label="El Clasificador II",
                label_key="prealgebra.n1.b11.mapTitle",
                node_id=CLASSIFIER_RIGOROUS_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=8,
                state=(
                    "blocked"
                    if not classifier_basic_progress or classifier_basic_progress["state"] != "completed"
                    else "completed"
                    if classifier_rigorous_progress and classifier_rigorous_progress["state"] == "completed"
                    else "available"
                ),
            ),
        )
        # B12 detective de falsedades: 14 afirmaciones V/F. Va tras B11.
        nodes.insert(
            11 if complex_visible else 10,
            MapNode(
                topic="evaluacion_conceptual",
                label="El Detective de Falsedades",
                label_key="prealgebra.n1.b12.mapTitle",
                node_id=DETECTIVE_NODE_ID,
                node_type="guided_practice",
                elo=0,
                rd=0,
                item_count=14,
                state=(
                    "blocked"
                    if not classifier_rigorous_progress or classifier_rigorous_progress["state"] != "completed"
                    else "completed"
                    if detective_progress and detective_progress["state"] == "completed"
                    else "available"
                ),
            ),
        )
        # B13 cierre diagnóstico: resumen final del nivel. Va tras B12.
        nodes.insert(
            12 if complex_visible else 11,
            MapNode(
                topic="cierre_diagnostico",
                label="Diagnóstico del nivel",
                label_key="prealgebra.n1.b13.mapTitle",
                node_id=CLOSING_NODE_ID,
                node_type="diagnostic_summary",
                elo=0,
                rd=0,
                item_count=0,
                state=(
                    "blocked"
                    if not detective_progress or detective_progress["state"] != "completed"
                    else "completed"
                    if closing_progress and closing_progress["state"] == "completed"
                    else "available"
                ),
            ),
        )
        n2_level_unlocked = closing_progress["state"] == "completed"
        n2_hub_completed = n2_hub_progress["state"] == "completed"
        n2_progress_by_node = {
            N2_SUM_NODE_ID: n2_sum_progress,
            N2_SUBTRACTION_NODE_ID: n2_subtraction_progress,
            N2_MULTIPLICATION_NODE_ID: n2_multiplication_progress,
            N2_DIVISION_NODE_ID: n2_division_progress,
            N2_EXPONENTIATION_NODE_ID: n2_exponentiation_progress,
            N2_RADICATION_NODE_ID: n2_radication_progress,
        }
        n2_specs = [
            ("ciudad_operaciones", "Ciudad de operaciones", N2_HUB_NODE_ID, "level_hub_3d"),
            ("suma", "Suma", N2_SUM_NODE_ID, "operation_building_manipulative"),
            ("resta", "Resta", N2_SUBTRACTION_NODE_ID, "operation_building_situations"),
            ("multiplicacion", "Multiplicacion", N2_MULTIPLICATION_NODE_ID, "operation_building_progressive"),
            ("division", "Division", N2_DIVISION_NODE_ID, "operation_building_manipulative"),
            ("potenciacion", "Potenciacion", N2_EXPONENTIATION_NODE_ID, "operation_building_growth_table"),
            ("radicacion", "Radicacion", N2_RADICATION_NODE_ID, "operation_building_geometric_last"),
        ]
        first_open_operation = next(
            (
                node_id
                for _, _, node_id, _ in n2_specs[1:]
                if n2_progress_by_node[node_id]["state"] != "completed"
            ),
            None,
        )
        for index, (topic, label, node_id, node_type) in enumerate(n2_specs):
            if index == 0:
                state = (
                    "blocked"
                    if not n2_level_unlocked
                    else "completed"
                    if n2_hub_completed
                    else "current"
                )
            else:
                progress = n2_progress_by_node[node_id]
                state = (
                    "blocked"
                    if not n2_level_unlocked or not n2_hub_completed
                    else "completed"
                    if progress["state"] == "completed"
                    else "current"
                    if node_id == first_open_operation
                    else "available"
                )
            nodes.append(
                MapNode(
                    topic=topic,
                    label=f"Nivel 2 · {label}",
                    node_id=node_id,
                    node_type=node_type,
                    elo=0,
                    rd=0,
                    item_count=6 if index == 0 else 1,
                    state=state,
                )
            )
        n3_level_unlocked = all(
            n2_progress_by_node[node_id]["state"] == "completed"
            for node_id in N2_OPERATION_NODE_IDS
        )
        n3_hub_completed = n3_hub_progress["state"] == "completed"
        n3_progress_by_node = {
            N3_COMMUTATIVE_NODE_ID: n3_commutative_progress,
            N3_ASSOCIATIVE_NODE_ID: n3_associative_progress,
            N3_DISTRIBUTIVE_NODE_ID: n3_distributive_progress,
            N3_IDENTITY_NODE_ID: n3_identity_progress,
            N3_INVERSES_NODE_ID: n3_inverses_progress,
        }
        n3_specs = [
            ("laboratorio_propiedades", "Laboratorio de propiedades", N3_HUB_NODE_ID, "level_hub_laboratory"),
            ("conmutativa", "Conmutativa", N3_COMMUTATIVE_NODE_ID, "property_machine_guided_discovery"),
            ("asociativa", "Asociativa", N3_ASSOCIATIVE_NODE_ID, "property_machine_guided_discovery"),
            ("distributiva", "Distributiva", N3_DISTRIBUTIVE_NODE_ID, "property_machine_guided_discovery"),
            ("elemento_neutro", "Elemento neutro", N3_IDENTITY_NODE_ID, "property_machine_guided_discovery"),
            ("inversos", "Inversos", N3_INVERSES_NODE_ID, "property_machine_cancellation_last"),
        ]
        previous_completed = n3_hub_completed
        for index, (topic, label, node_id, node_type) in enumerate(n3_specs):
            if index == 0:
                state = (
                    "blocked"
                    if not n3_level_unlocked
                    else "completed"
                    if n3_hub_completed
                    else "current"
                )
            else:
                progress = n3_progress_by_node[node_id]
                state = (
                    "blocked"
                    if not n3_level_unlocked or not previous_completed
                    else "completed"
                    if progress["state"] == "completed"
                    else "current"
                )
                previous_completed = progress["state"] == "completed"
            nodes.append(
                MapNode(
                    topic=topic,
                    label=f"Nivel 3 · {label}",
                    node_id=node_id,
                    node_type=node_type,
                    elo=0,
                    rd=0,
                    item_count=5 if index == 0 else 1,
                    state=state,
                )
            )

        n4_level_unlocked = n3_inverses_progress["state"] == "completed"
        n4_hub_completed = n4_hub_progress["state"] == "completed"
        n4_specs = [
            ("puerto_de_la_polis", "El Puerto de la Polis", N4_HUB_NODE_ID, "level_hub_port"),
            ("divisibilidad", "Divisibilidad", N4_DIVISIBILITY_NODE_ID, "divisibility_concept_guided_discovery"),
            ("multiplos", "Múltiplos", N4_MULTIPLES_NODE_ID, "divisibility_concept_guided_discovery"),
            ("primos", "Números primos", N4_PRIMES_NODE_ID, "divisibility_concept_guided_discovery"),
            ("factorizacion_prima", "Factorización prima", N4_FACTORIZATION_NODE_ID, "divisibility_concept_guided_discovery"),
            ("mcd", "Máximo común divisor", N4_GCD_NODE_ID, "divisibility_concept_guided_discovery"),
            ("mcm", "Mínimo común múltiplo", N4_LCM_NODE_ID, "divisibility_concept_guided_discovery"),
        ]
        previous_completed = n4_hub_completed
        for index, (topic, label, node_id, node_type) in enumerate(n4_specs):
            if index == 0:
                state = (
                    "blocked"
                    if not n4_level_unlocked
                    else "completed"
                    if n4_hub_completed
                    else "current"
                )
            else:
                progress = n4_progress_by_node[node_id]
                state = (
                    "blocked"
                    if not n4_level_unlocked or not previous_completed
                    else "completed"
                    if progress["state"] == "completed"
                    else "current"
                )
                previous_completed = progress["state"] == "completed"
            nodes.append(
                MapNode(
                    topic=topic,
                    label=f"Nivel 4 · {label}",
                    node_id=node_id,
                    node_type=node_type,
                    elo=0,
                    rd=0,
                    item_count=9 if index == 0 else 1,
                    state=state,
                )
            )

    course_name = next((c["name"] for c in repo.get_courses() if c["id"] == course_id), course_id)
    return CourseMapResponse(
        course_id=course_id,
        course_name=course_name,
        diagnostic_done=diagnostic_done,
        nodes=nodes,
    )


# ── Helpers ───────────────────────────────────────────────────────────────────


_RANK_THRESHOLDS = [
    (2500, "Leyenda Suprema"),
    (2200, "Leyenda"),
    (2000, "Gran Maestro"),
    (1800, "Maestro"),
    (1600, "Diamante I"),
    (1500, "Diamante II"),
    (1400, "Platino I"),
    (1300, "Platino II"),
    (1200, "Oro I"),
    (1100, "Oro II"),
    (1000, "Plata I"),
    (900, "Plata II"),
    (800, "Bronce I"),
    (700, "Bronce II"),
    (600, "Hierro"),
    (0, "Aspirante"),
]


def _elo_to_rank(elo: float) -> str:
    for threshold, label in _RANK_THRESHOLDS:
        if elo >= threshold:
            return label
    return "Aspirante"
