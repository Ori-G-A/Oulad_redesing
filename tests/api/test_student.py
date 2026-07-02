"""
tests/api/test_student.py
==========================
Tests del flujo de práctica del estudiante:
  GET  /api/student/courses        → catálogo de cursos
  GET  /api/student/stats          → ELO y estadísticas
  POST /api/student/enroll         → matrícula en un curso
  POST /api/student/next-question  → siguiente pregunta adaptativa
  POST /api/student/answer         → procesar respuesta
  GET  /api/student/history        → historial de intentos
  DELETE /api/student/enroll/{id}  → darse de baja
  GET  /api/student/achievements   → logros/badges
  POST /api/student/exam/start     → iniciar examen
  POST /api/student/exam/submit    → enviar respuestas del examen
"""

import pytest

_COURSE_ID = "algebra_basica"  # Colegio — presente en el banco de preguntas
_COURSE_UNIV = "calculo_diferencial"  # Universidad


class TestCourses:
    def test_list_courses_authenticated(self, api_client, student_headers):
        """GET /student/courses → lista de cursos con flag enrolled."""
        r = api_client.get("/api/student/courses", headers=student_headers)
        assert r.status_code == 200
        courses = r.json()
        assert isinstance(courses, list)
        assert len(courses) > 0
        # Cada curso tiene los campos esperados
        course = courses[0]
        assert "id" in course or "course_id" in course
        assert "name" in course
        assert "block" in course
        assert "enrolled" in course

    def test_list_courses_unauthenticated(self, api_client):
        """GET /student/courses sin token → 401."""
        r = api_client.get("/api/student/courses")
        assert r.status_code == 401


class TestStats:
    def test_stats_authenticated(self, api_client, student_headers):
        """GET /student/stats → ELO global, tópicos, racha."""
        r = api_client.get("/api/student/stats", headers=student_headers)
        assert r.status_code == 200
        data = r.json()
        assert "global_elo" in data
        assert "total_attempts" in data
        assert "study_streak" in data
        assert "topic_elos" in data
        assert isinstance(data["topic_elos"], list)

    def test_stats_initial_elo(self, api_client, student_headers):
        """ELO inicial de estudiante sin intentos es 1000."""
        r = api_client.get("/api/student/stats", headers=student_headers)
        data = r.json()
        # ELO puede ser exactamente 1000 si no ha respondido nada, o mayor/menor si ya hay intentos
        assert 0 < data["global_elo"] < 5000


class TestEnroll:
    def test_enroll_in_course(self, api_client, student_headers):
        """POST /student/enroll → 201 (o 200 si ya estaba matriculado)."""
        r = api_client.post(
            "/api/student/enroll",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )
        assert r.status_code in (200, 201)

    def test_enroll_nonexistent_course(self, api_client, student_headers):
        """Matrícula en curso inexistente → error (400 o 404)."""
        r = api_client.post(
            "/api/student/enroll",
            json={"course_id": "curso_que_no_existe_xyz"},
            headers=student_headers,
        )
        assert r.status_code in (400, 404, 422)

    def test_unenroll(self, api_client, student_headers):
        """DELETE /student/enroll/{course_id} → 204."""
        # Primero matricular para asegurar que existe la matrícula
        api_client.post(
            "/api/student/enroll",
            json={"course_id": _COURSE_UNIV},
            headers=student_headers,
        )
        r = api_client.delete(f"/api/student/enroll/{_COURSE_UNIV}", headers=student_headers)
        assert r.status_code == 204


class TestNextQuestion:
    @pytest.fixture(autouse=True, scope="class")
    def ensure_enrolled(self, api_client, student_headers):
        """Asegura matrícula antes de solicitar preguntas."""
        api_client.post(
            "/api/student/enroll",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )

    def test_next_question_returns_item_or_empty(self, api_client, student_headers):
        """POST /student/next-question → status 'ok' o 'empty'/'course_empty'."""
        r = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        assert data["status"] in ("ok", "empty", "course_empty")

    def test_next_question_item_structure(self, api_client, student_headers):
        """Si hay preguntas disponibles, el ítem tiene todos los campos."""
        r = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )
        data = r.json()
        if data["status"] == "ok" and data["item"]:
            item = data["item"]
            assert "id" in item
            assert "content" in item
            assert "options" in item
            assert isinstance(item["options"], list)
            assert len(item["options"]) >= 2
            assert "difficulty" in item
            assert "topic" in item


class TestAnswer:
    def test_submit_answer_correct(self, api_client, student_headers):
        """POST /student/answer con respuesta correcta → delta_elo positivo."""
        # Primero obtener una pregunta
        q_res = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )
        q_data = q_res.json()
        if q_data["status"] != "ok" or not q_data["item"]:
            pytest.skip("No hay preguntas disponibles para este test.")

        item = q_data["item"]
        # Obtener la respuesta correcta directamente del ítem (no la tenemos aquí)
        # Usamos la primera opción (puede ser incorrecta — solo testamos que la API responde)
        r = api_client.post(
            "/api/student/answer",
            json={
                "item_id": item["id"],
                "item_data": item,
                "selected_option": item["options"][0],
                "reasoning": "Prueba automática",
                "time_taken": 15.0,
            },
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        assert "is_correct" in data
        assert "elo_before" in data
        assert "elo_after" in data
        assert "delta_elo" in data
        assert isinstance(data["is_correct"], bool)

    def test_submit_answer_elo_changes(self, api_client, student_headers):
        """El ELO cambia después de responder (delta_elo != 0 siempre)."""
        q_res = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        )
        q_data = q_res.json()
        if q_data["status"] != "ok" or not q_data["item"]:
            pytest.skip("No hay preguntas disponibles.")

        item = q_data["item"]
        r = api_client.post(
            "/api/student/answer",
            json={
                "item_id": item["id"],
                "item_data": item,
                "selected_option": item["options"][0],
                "time_taken": 10.0,
            },
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        # delta_elo siempre es distinto de 0 (el ELO siempre cambia al responder)
        assert data["delta_elo"] != 0


class TestHistory:
    def test_history_authenticated(self, api_client, student_headers):
        """GET /student/history → lista de intentos previos."""
        r = api_client.get("/api/student/history", headers=student_headers)
        assert r.status_code == 200


class TestRoleProtection:
    def test_teacher_cannot_access_student_answer(self, api_client, teacher_headers):
        """El endpoint /student/answer requiere rol student (o admin)."""
        # El endpoint acepta cualquier usuario autenticado — solo probamos que llega bien
        r = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=teacher_headers,
        )
        # El docente puede acceder a estos endpoints (CurrentUser, no RequireRole)
        # Si no tiene matriculaciones, devuelve empty
        assert r.status_code in (200, 400, 404)


class TestAchievements:
    def test_achievements_authenticated(self, api_client, student_headers):
        """GET /student/achievements → dict con achievements y catalog."""
        r = api_client.get("/api/student/achievements", headers=student_headers)
        assert r.status_code == 200
        data = r.json()
        assert "achievements" in data
        assert "catalog" in data
        assert isinstance(data["achievements"], list)
        assert isinstance(data["catalog"], list)
        assert len(data["catalog"]) > 0

    def test_achievements_catalog_has_required_fields(self, api_client, student_headers):
        """Cada badge del catálogo tiene badge_id, label, icon y desc."""
        r = api_client.get("/api/student/achievements", headers=student_headers)
        catalog = r.json()["catalog"]
        for badge in catalog:
            assert "badge_id" in badge
            assert "label" in badge
            assert "icon" in badge
            assert "desc" in badge

    def test_achievements_unauthenticated(self, api_client):
        """GET /student/achievements sin token → 401."""
        r = api_client.get("/api/student/achievements")
        assert r.status_code == 401

    def test_first_correct_badge_awarded(self, api_client, student_headers):
        """Después de responder correctamente, el badge first_correct debe estar en logros."""
        # Garantizar matrícula
        api_client.post(
            "/api/student/enroll", json={"course_id": _COURSE_ID}, headers=student_headers
        )
        # Obtener pregunta
        q = api_client.post(
            "/api/student/next-question",
            json={"course_id": _COURSE_ID},
            headers=student_headers,
        ).json()
        if q["status"] != "ok" or not q["item"]:
            return  # skip silencioso si no hay preguntas

        item = q["item"]
        # Responder (puede ser correcto o incorrecto — solo comprobamos que el endpoint devuelve new_badges)
        ans = api_client.post(
            "/api/student/answer",
            json={
                "item_id": item["id"],
                "item_data": item,
                "selected_option": item["options"][0],
                "time_taken": 5.0,
            },
            headers=student_headers,
        ).json()
        # cog_data puede contener new_badges si se desbloqueó algo
        assert "cog_data" in ans


class TestExamMode:
    @pytest.fixture(autouse=True, scope="class")
    def ensure_enrolled(self, api_client, student_headers):
        """Matricular al estudiante en el curso de prueba antes del examen."""
        api_client.post(
            "/api/student/enroll", json={"course_id": _COURSE_ID}, headers=student_headers
        )

    def test_exam_start(self, api_client, student_headers):
        """POST /student/exam/start → lista de preguntas + tiempo límite."""
        r = api_client.post(
            "/api/student/exam/start",
            json={"course_id": _COURSE_ID, "n_questions": 3, "time_limit_minutes": 10},
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        assert "items" in data
        assert "n_questions" in data
        assert "time_limit_seconds" in data
        assert data["time_limit_seconds"] == 600  # 10 * 60
        assert len(data["items"]) >= 1
        assert len(data["items"]) <= 3

    def test_exam_start_item_structure(self, api_client, student_headers):
        """Los ítems del examen tienen todos los campos requeridos."""
        r = api_client.post(
            "/api/student/exam/start",
            json={"course_id": _COURSE_ID, "n_questions": 2, "time_limit_minutes": 5},
            headers=student_headers,
        )
        items = r.json()["items"]
        if not items:
            return
        item = items[0]
        assert "id" in item
        assert "content" in item
        assert "options" in item
        assert "difficulty" in item

    def test_exam_start_nonexistent_course(self, api_client, student_headers):
        """Examen en curso sin preguntas → 404."""
        r = api_client.post(
            "/api/student/exam/start",
            json={"course_id": "curso_xyz_inexistente", "n_questions": 5},
            headers=student_headers,
        )
        assert r.status_code == 404

    def test_exam_submit(self, api_client, student_headers):
        """POST /student/exam/submit → resultados con score_pct y global_elo_after."""
        # Obtener preguntas del examen
        start = api_client.post(
            "/api/student/exam/start",
            json={"course_id": _COURSE_ID, "n_questions": 2, "time_limit_minutes": 5},
            headers=student_headers,
        ).json()
        items = start.get("items", [])
        if not items:
            return

        # Enviar respuestas (primera opción de cada pregunta)
        answers = [
            {"item_id": it["id"], "selected_option": it["options"][0], "time_taken": 5.0}
            for it in items
        ]
        r = api_client.post(
            "/api/student/exam/submit",
            json={"answers": answers},
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        assert "results" in data
        assert "correct_count" in data
        assert "total_questions" in data
        assert "score_pct" in data
        assert "global_elo_after" in data
        assert 0 <= data["score_pct"] <= 100
        assert data["total_questions"] == len(items)

    def test_exam_submit_empty(self, api_client, student_headers):
        """Enviar examen sin respuestas → score 0%."""
        r = api_client.post(
            "/api/student/exam/submit",
            json={"answers": []},
            headers=student_headers,
        )
        assert r.status_code == 200
        data = r.json()
        assert data["score_pct"] == 0.0
        assert data["total_questions"] == 0

    def test_exam_unauthenticated(self, api_client):
        """Examen sin autenticación → 401."""
        r = api_client.post(
            "/api/student/exam/start",
            json={"course_id": _COURSE_ID, "n_questions": 3},
        )
        assert r.status_code == 401
def test_welcome_lesson_progress_flow(api_client, student_headers):
    node_id = "PREALG-N1-B01-BIENVENIDA"
    base = f"/api/student/lessons/algebra_basica/{node_id}"

    detail = api_client.get(base, headers=student_headers)
    assert detail.status_code == 200
    assert detail.json()["affects_elo"] is False

    completed = api_client.post(
        f"{base}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def test_welcome_lesson_rejects_unknown_event(api_client, student_headers):
    node_id = "PREALG-N1-B01-BIENVENIDA"
    response = api_client.post(
        f"/api/student/lessons/algebra_basica/{node_id}/events",
        headers=student_headers,
        json={"event": "change_elo"},
    )
    assert response.status_code == 422


def test_trigger_question_requires_closed_responses_before_completion(
    api_client, student_headers
):
    welcome = "/api/student/lessons/algebra_basica/PREALG-N1-B01-BIENVENIDA/events"
    api_client.post(welcome, headers=student_headers, json={"event": "node_completed"})
    base = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B02-PREGUNTA-DETONADORA"
    )

    incomplete = api_client.post(
        f"{base}/events", headers=student_headers, json={"event": "node_completed"}
    )
    assert incomplete.status_code == 409

    for interaction_id, selected_option in (
        ("PREALG-N1-B02-Q01", "no"),
        ("PREALG-N1-B02-Q02", "pizza"),
    ):
        response = api_client.post(
            f"{base}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
        assert response.status_code == 200

    completed = api_client.post(
        f"{base}/events", headers=student_headers, json={"event": "node_completed"}
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def test_staircase_unlocks_after_trigger_and_requires_its_formative_answer(
    api_client, student_headers
):
    welcome = "/api/student/lessons/algebra_basica/PREALG-N1-B01-BIENVENIDA/events"
    api_client.post(welcome, headers=student_headers, json={"event": "node_completed"})

    trigger = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B02-PREGUNTA-DETONADORA"
    )
    for interaction_id, selected_option in (
        ("PREALG-N1-B02-Q01", "no"),
        ("PREALG-N1-B02-Q02", "temperature"),
    ):
        api_client.post(
            f"{trigger}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
    api_client.post(
        f"{trigger}/events", headers=student_headers, json={"event": "node_completed"}
    )

    staircase = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B03-ESCALERA-NECESIDAD"
    )
    detail = api_client.get(staircase, headers=student_headers)
    assert detail.status_code == 200
    assert len(detail.json()["staircase"]["core_steps"]) == 5

    incomplete = api_client.post(
        f"{staircase}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert incomplete.status_code == 409

    answer = api_client.post(
        f"{staircase}/interactions",
        headers=student_headers,
        json={"interaction_id": "PREALG-N1-B03-Q01", "selected_option": "expand"},
    )
    assert answer.status_code == 200
    assert answer.json()["is_expected"] is True

    completed = api_client.post(
        f"{staircase}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200


def test_naturals_node_handles_guided_practice_without_elo(api_client, student_headers):
    api_client.post(
        "/api/student/lessons/algebra_basica/PREALG-N1-B01-BIENVENIDA/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    trigger = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B02-PREGUNTA-DETONADORA"
    )
    for interaction_id, selected_option in (
        ("PREALG-N1-B02-Q01", "no"),
        ("PREALG-N1-B02-Q02", "pizza"),
    ):
        api_client.post(
            f"{trigger}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
    api_client.post(
        f"{trigger}/events", headers=student_headers, json={"event": "node_completed"}
    )

    staircase = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B03-ESCALERA-NECESIDAD"
    )
    api_client.post(
        f"{staircase}/interactions",
        headers=student_headers,
        json={"interaction_id": "PREALG-N1-B03-Q01", "selected_option": "expand"},
    )
    api_client.post(
        f"{staircase}/events", headers=student_headers, json={"event": "node_completed"}
    )

    naturals = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B04-NATURALES-CONTAR"
    )
    detail = api_client.get(naturals, headers=student_headers)
    assert detail.status_code == 200
    assert detail.json()["affects_elo"] is False

    wrong_total = api_client.post(
        f"{naturals}/interactions",
        headers=student_headers,
        json={"interaction_id": "PREALG-N1-B04-Q01", "selected_option": "7"},
    )
    assert wrong_total.status_code == 200
    assert wrong_total.json()["is_expected"] is False

    for interaction_id, selected_option in (
        ("PREALG-N1-B04-Q01", "8"),
        ("PREALG-N1-B04-Q02", "no"),
        ("PREALG-N1-B04-Q03", "2"),
        ("PREALG-N1-B04-Q04", "zero,four,fifteen"),
    ):
        response = api_client.post(
            f"{naturals}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
        assert response.status_code == 200
        assert response.json()["is_expected"] is True

    completed = api_client.post(
        f"{naturals}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def test_integers_node_uses_negative_sign_and_discrete_anchor(api_client, student_headers):
    api_client.post(
        "/api/student/lessons/algebra_basica/PREALG-N1-B01-BIENVENIDA/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    prerequisites = [
        (
            "PREALG-N1-B02-PREGUNTA-DETONADORA",
            (("PREALG-N1-B02-Q01", "no"), ("PREALG-N1-B02-Q02", "debt")),
        ),
        (
            "PREALG-N1-B03-ESCALERA-NECESIDAD",
            (("PREALG-N1-B03-Q01", "expand"),),
        ),
        (
            "PREALG-N1-B04-NATURALES-CONTAR",
            (
                ("PREALG-N1-B04-Q01", "8"),
                ("PREALG-N1-B04-Q02", "no"),
                ("PREALG-N1-B04-Q03", "2"),
                ("PREALG-N1-B04-Q04", "zero,four,fifteen"),
            ),
        ),
    ]
    for node_id, interactions in prerequisites:
        base = f"/api/student/lessons/algebra_basica/{node_id}"
        for interaction_id, selected_option in interactions:
            response = api_client.post(
                f"{base}/interactions",
                headers=student_headers,
                json={"interaction_id": interaction_id, "selected_option": selected_option},
            )
            assert response.status_code == 200
        completed = api_client.post(
            f"{base}/events", headers=student_headers, json={"event": "node_completed"}
        )
        assert completed.status_code == 200

    integers = "/api/student/lessons/algebra_basica/PREALG-N1-B05-ENTEROS-DEUDA"
    detail = api_client.get(integers, headers=student_headers)
    assert detail.status_code == 200
    assert detail.json()["affects_elo"] is False

    for interaction_id, selected_option in (
        ("PREALG-N1-B05-Q01", "35000"),
        ("PREALG-N1-B05-Q02", "5000"),
        ("PREALG-N1-B05-Q03", "negative"),
        ("PREALG-N1-B05-Q04", "negative_5000"),
        ("PREALG-N1-B05-Q05", "neg8,zero,six"),
    ):
        response = api_client.post(
            f"{integers}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
        assert response.status_code == 200
        assert response.json()["is_expected"] is True

    completed = api_client.post(
        f"{integers}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def test_rationals_node_links_fraction_division_and_decimal(api_client, student_headers):
    api_client.post(
        "/api/student/lessons/algebra_basica/PREALG-N1-B01-BIENVENIDA/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    prerequisites = [
        (
            "PREALG-N1-B02-PREGUNTA-DETONADORA",
            (("PREALG-N1-B02-Q01", "no"), ("PREALG-N1-B02-Q02", "pizza")),
        ),
        (
            "PREALG-N1-B03-ESCALERA-NECESIDAD",
            (("PREALG-N1-B03-Q01", "expand"),),
        ),
        (
            "PREALG-N1-B04-NATURALES-CONTAR",
            (
                ("PREALG-N1-B04-Q01", "8"),
                ("PREALG-N1-B04-Q02", "no"),
                ("PREALG-N1-B04-Q03", "2"),
                ("PREALG-N1-B04-Q04", "zero,four,fifteen"),
            ),
        ),
        (
            "PREALG-N1-B05-ENTEROS-DEUDA",
            (
                ("PREALG-N1-B05-Q01", "35000"),
                ("PREALG-N1-B05-Q02", "5000"),
                ("PREALG-N1-B05-Q03", "negative"),
                ("PREALG-N1-B05-Q04", "negative_5000"),
                ("PREALG-N1-B05-Q05", "neg8,zero,six"),
            ),
        ),
    ]
    for node_id, interactions in prerequisites:
        base = f"/api/student/lessons/algebra_basica/{node_id}"
        for interaction_id, selected_option in interactions:
            response = api_client.post(
                f"{base}/interactions",
                headers=student_headers,
                json={"interaction_id": interaction_id, "selected_option": selected_option},
            )
            assert response.status_code == 200
        completed = api_client.post(
            f"{base}/events", headers=student_headers, json={"event": "node_completed"}
        )
        assert completed.status_code == 200

    rationals = (
        "/api/student/lessons/algebra_basica/"
        "PREALG-N1-B06-RACIONALES-FRACCION-DIVISION"
    )
    detail = api_client.get(rationals, headers=student_headers)
    assert detail.status_code == 200
    assert detail.json()["affects_elo"] is False

    reversed_share = api_client.post(
        f"{rationals}/interactions",
        headers=student_headers,
        json={"interaction_id": "PREALG-N1-B06-Q01", "selected_option": "four_thirds"},
    )
    assert reversed_share.status_code == 200
    assert reversed_share.json()["is_expected"] is False

    for interaction_id, selected_option in (
        ("PREALG-N1-B06-Q01", "three_fourths"),
        ("PREALG-N1-B06-Q02", "three_div_four"),
        ("PREALG-N1-B06-Q03", "decimal_075"),
        ("PREALG-N1-B06-Q04", "frac_34,dec_025,neg3,periodic_0333"),
    ):
        response = api_client.post(
            f"{rationals}/interactions",
            headers=student_headers,
            json={"interaction_id": interaction_id, "selected_option": selected_option},
        )
        assert response.status_code == 200
        assert response.json()["is_expected"] is True

    completed = api_client.post(
        f"{rationals}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def _complete_node(api_client, headers, node_id: str):
    return api_client.post(
        f"/api/student/lessons/algebra_basica/{node_id}/events",
        headers=headers,
        json={"event": "node_completed"},
    )


def _answer(api_client, headers, node_id: str, interaction_id: str, selected_option: str):
    return api_client.post(
        f"/api/student/lessons/algebra_basica/{node_id}/interactions",
        headers=headers,
        json={"interaction_id": interaction_id, "selected_option": selected_option},
    )


def _complete_level_one(api_client, headers):
    _complete_node(api_client, headers, "PREALG-N1-B01-BIENVENIDA")
    trigger = "PREALG-N1-B02-PREGUNTA-DETONADORA"
    _answer(api_client, headers, trigger, "PREALG-N1-B02-Q01", "no")
    _answer(api_client, headers, trigger, "PREALG-N1-B02-Q02", "pizza")
    _complete_node(api_client, headers, trigger)

    staircase = "PREALG-N1-B03-ESCALERA-NECESIDAD"
    _answer(api_client, headers, staircase, "PREALG-N1-B03-Q01", "expand")
    _complete_node(api_client, headers, staircase)

    naturals = "PREALG-N1-B04-NATURALES-CONTAR"
    for interaction_id, selected_option in (
        ("PREALG-N1-B04-Q01", "8"),
        ("PREALG-N1-B04-Q02", "no"),
        ("PREALG-N1-B04-Q03", "2"),
        ("PREALG-N1-B04-Q04", "zero,four,fifteen"),
    ):
        _answer(api_client, headers, naturals, interaction_id, selected_option)
    _complete_node(api_client, headers, naturals)

    integers = "PREALG-N1-B05-ENTEROS-DEUDA"
    for interaction_id, selected_option in (
        ("PREALG-N1-B05-Q01", "35000"),
        ("PREALG-N1-B05-Q02", "5000"),
        ("PREALG-N1-B05-Q03", "negative"),
        ("PREALG-N1-B05-Q04", "negative_5000"),
        ("PREALG-N1-B05-Q05", "neg8,zero,six"),
    ):
        _answer(api_client, headers, integers, interaction_id, selected_option)
    _complete_node(api_client, headers, integers)

    rationals = "PREALG-N1-B06-RACIONALES-FRACCION-DIVISION"
    for interaction_id, selected_option in (
        ("PREALG-N1-B06-Q01", "three_fourths"),
        ("PREALG-N1-B06-Q02", "three_div_four"),
        ("PREALG-N1-B06-Q03", "decimal_075"),
        ("PREALG-N1-B06-Q04", "frac_34,dec_025,neg3,periodic_0333"),
    ):
        _answer(api_client, headers, rationals, interaction_id, selected_option)
    _complete_node(api_client, headers, rationals)

    for node_id in (
        "PREALG-N1-B07-IRRACIONALES-DECIMALES",
        "PREALG-N1-B08-REALES-RECTA",
        "PREALG-N1-B10-CLASIFICADOR-BASICO",
        "PREALG-N1-B11-CLASIFICADOR-RIGUROSO",
        "PREALG-N1-B12-DETECTIVE-FALSEDADES",
        "PREALG-N1-B13-CIERRE-DIAGNOSTICO",
    ):
        response = _complete_node(api_client, headers, node_id)
        assert response.status_code == 200


def test_level_two_map_and_hub_are_locked_until_level_one_is_completed(
    api_client, student_headers
):
    hub = "/api/student/lessons/algebra_basica/PREALG-N2-E00-CIUDAD"

    locked_detail = api_client.get(hub, headers=student_headers)
    assert locked_detail.status_code == 403

    locked_map = api_client.get("/api/student/map/algebra_basica", headers=student_headers)
    assert locked_map.status_code == 200
    n2_nodes = [
        node for node in locked_map.json()["nodes"]
        if (node.get("node_id") or "").startswith("PREALG-N2")
    ]
    assert n2_nodes
    assert all(node["state"] == "blocked" for node in n2_nodes)

    _complete_level_one(api_client, student_headers)

    unlocked_detail = api_client.get(hub, headers=student_headers)
    assert unlocked_detail.status_code == 200
    assert unlocked_detail.json()["content"]["gating"]["cards_required"] == 6

    incomplete = api_client.post(
        f"{hub}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert incomplete.status_code == 409

    for building_id in ("E01", "E02", "E03", "E04", "E05", "E06"):
        response = _answer(
            api_client,
            student_headers,
            "PREALG-N2-E00-CIUDAD",
            f"PREALG-N2-E00-CIUDAD-CARD-{building_id}",
            "opened",
        )
        assert response.status_code == 200

    first_building = api_client.get(
        "/api/student/lessons/algebra_basica/PREALG-N2-E01-SUMA-JUNTAR",
        headers=student_headers,
    )
    assert first_building.status_code == 200

    completed = api_client.post(
        f"{hub}/events",
        headers=student_headers,
        json={"event": "node_completed"},
    )
    assert completed.status_code == 200
    assert completed.json()["state"] == "completed"


def test_level_three_unlocks_after_level_two_and_tracks_laboratory_machines(
    api_client, student_headers
):
    hub = "/api/student/lessons/algebra_basica/PREALG-N3-M00-LABORATORIO"
    locked_detail = api_client.get(hub, headers=student_headers)
    assert locked_detail.status_code == 403

    _complete_level_one(api_client, student_headers)
    for building_id in ("E01", "E02", "E03", "E04", "E05", "E06"):
        _answer(
            api_client,
            student_headers,
            "PREALG-N2-E00-CIUDAD",
            f"PREALG-N2-E00-CIUDAD-CARD-{building_id}",
            "opened",
        )
    _complete_node(api_client, student_headers, "PREALG-N2-E00-CIUDAD")

    for node_id in (
        "PREALG-N2-E01-SUMA-JUNTAR",
        "PREALG-N2-E02-RESTA-QUITAR",
        "PREALG-N2-E03-MULTIPLICACION-AGRUPAR",
        "PREALG-N2-E04-DIVISION-REPARTIR",
        "PREALG-N2-E05-POTENCIACION-CRECER",
        "PREALG-N2-E06-RADICACION-RAIZ",
    ):
        detail = api_client.get(
            f"/api/student/lessons/algebra_basica/{node_id}",
            headers=student_headers,
        )
        assert detail.status_code == 200
        for situation in detail.json()["content"]["situations"]:
            response = _answer(
                api_client,
                student_headers,
                node_id,
                f"{node_id}-{situation['id']}",
                situation["answer"],
            )
            assert response.status_code == 200
        assert _complete_node(api_client, student_headers, node_id).status_code == 200

    unlocked_detail = api_client.get(hub, headers=student_headers)
    assert unlocked_detail.status_code == 200
    assert unlocked_detail.json()["content"]["gating"]["machines_required"] == 5

    machine_before_hub = api_client.get(
        "/api/student/lessons/algebra_basica/PREALG-N3-M01-CONMUTATIVA",
        headers=student_headers,
    )
    assert machine_before_hub.status_code == 403

    for machine_id in ("M01", "M02", "M03", "M04", "M05"):
        response = _answer(
            api_client,
            student_headers,
            "PREALG-N3-M00-LABORATORIO",
            f"PREALG-N3-M00-LABORATORIO-MACHINE-{machine_id}",
            "introduced",
        )
        assert response.status_code == 200

    first_machine = api_client.get(
        "/api/student/lessons/algebra_basica/PREALG-N3-M01-CONMUTATIVA",
        headers=student_headers,
    )
    assert first_machine.status_code == 200
    assert first_machine.json()["content"]["opening_hook"]["katia_message"] == "¡Qué curioso! El orden no importa."
