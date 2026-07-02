# Prompt para Claude Code — Implementación del Nivel 2 "Operaciones básicas" (LevelUpElo)

> Pega este prompt en Claude Code con los 7 archivos `F2_nodo_*.md` en `docs/specs/nivel-2/` del repo.
>
> **Valores por defecto (confirmar y ajustar si tu stack difiere):**
> - **Ruta de specs:** `docs/specs/nivel-2/`
> - **Stack asumido:** React + TypeScript (componentes `.tsx`, KaTeX para fórmulas, Framer Motion para animaciones).
> - **Comandos:** `npm run lint` · `npm run typecheck` (o `npx tsc --noEmit`) · `npm test`. Si usas pnpm/yarn, reemplaza `npm run`/`npm` por `pnpm`/`yarn`.

---

## Rol y objetivo

Implementa en este repositorio el **Nivel 2 — Operaciones básicas** (módulo Preálgebra) de LevelUpElo: una **ciudad 3D (hub)** con **6 edificios**, uno por operación. Trabajas a partir de 7 especificaciones de nodo. Como el nivel puede no existir aún o existir parcialmente, **primero audita** lo que haya y reconcilia; no dupliques ni sobreescribas a ciegas.

## Aviso importante sobre el origen del contenido

A diferencia del Nivel 1 (cuyo material venía maduro), el Nivel 2 se desarrolló a partir de un **borrador temprano**. En cada spec, el contenido está etiquetado:
- **verbatim** = texto que venía en el borrador (diálogos de Katia, situaciones, formalizaciones). Respétalo tal cual.
- **[NUEVO]** = autoría añadida para alcanzar el calibre formativo (retroalimentaciones diferenciadas, definición + ejemplos base, storyboards, diferenciación por banda, accesibilidad, JSON). **Implementa el [NUEVO] tal como está, pero deja un marcador/anotación** (p. ej. un comentario o flag de contenido) para que el equipo pedagógico pueda validarlo antes de publicar. No lo trates como contenido aprobado en firme.

## Contexto del producto

- Plataforma gamificada de matemáticas, 8.º grado, Colombia. Formato **es-CO** (coma decimal, punto de miles). Mascota guía: **Katia**. Personajes de situación por edificio: Felipe, Manuel, Andrea, Pablo, Juan.
- Tres bandas de proficiencia: **Básico, Intermedio, Avanzado** (campo `level_presentation` en cada spec).
- Cada spec tiene **PARTE A** (guión legible; A2 es la fuente de verdad del texto visible) y **PARTE B** (JSON: fuente de verdad del modelo de datos, interacciones, eventos, alertas, presentación por banda y handoff).

## Mapa archivo → node_id (orden de ruta)

| Orden | Archivo spec | node_id | Tipo |
|---|---|---|---|
| E00 | `F2_nodo_ciudad_hub.md` | `PREALG-N2-E00-CIUDAD` | Hub 3D (gating: abrir 6 carteles) |
| E01 | `F2_nodo_suma.md` | `PREALG-N2-E01-SUMA-JUNTAR` | Edificio — manipulativo (canasta) |
| E02 | `F2_nodo_resta.md` | `PREALG-N2-E02-RESTA-QUITAR` | Edificio — situaciones |
| E03 | `F2_nodo_multiplicacion.md` | `PREALG-N2-E03-MULTIPLICACION-AGRUPAR` | Edificio — construcción progresiva |
| E04 | `F2_nodo_division.md` | `PREALG-N2-E04-DIVISION-REPARTIR` | Edificio — manipulativo (pizza) |
| E05 | `F2_nodo_potenciacion.md` | `PREALG-N2-E05-POTENCIACION-CRECER` | Edificio — tabla de crecimiento |
| E06 | `F2_nodo_radicacion.md` | `PREALG-N2-E06-RADICACION-RAIZ` | Edificio — geométrico (cierra el nivel) |

## FASE 1 — Auditoría y reconciliación (NO escribir código todavía)

1. Lee los 7 specs completos.
2. Escanea el repo: ¿existe ya estructura del Nivel 2, el hub, algún edificio, rutas, eventos o i18n `prealgebra.n2.*`?
3. Clasifica cada nodo: **EXISTE-COINCIDE / EXISTE-REQUIERE-CAMBIOS / FALTA**. (Probablemente la mayoría sea FALTA, pero verifica scaffolding y componentes compartidos reutilizables del Nivel 1.)
4. Entrega una **tabla de reconciliación** + un **plan por nodo** y **detente para confirmación** antes de codificar.
5. Ante conflicto estructural (un `node_id`, una `unlock_rule`, una ruta, un evento ya consumido por analítica), **márcalo y pregunta**; no lo cambies en silencio.

## FASE 2 — Implementación (tras aprobación, en orden de ruta E00 → E06)

Para cada nodo:

- **Hub E00:** ciudad 3D con 6 edificios; cada edificio despliega un cartel (problema real). **Gating:** abrir los 6 carteles habilita la entrada a los edificios (sin penalización). Reutiliza una escena 3D existente o provee alternativa 2D accesible.
- **Datos:** materializa la PARTE B (interacciones, `expected`/`answer`, `feedback` por caso, `misconception_tags`, `level_presentation`). Conserva `node_id` y wiring; actualiza in situ.
- **Definición + ejemplos base (patrón obligatorio):** cada edificio muestra, **antes** de la práctica, una pantalla con la **definición de la operación** y **1–2 ejemplos resueltos** (bloque `definition_and_worked_examples` en el JSON; evento `definition_and_examples_viewed`). Va antes de las situaciones/manipulación; la **formalización con propiedades** va al final como consolidación.
- **UI / texto:** usa el guión A2 **verbatim** para el texto visible; respeta el marcado [NUEVO]. Reutiliza componentes compartidos (diálogo de Katia, modal de retroalimentación, campo numérico, drag-and-drop, recta numérica, etc.).
- **Mecánicas por edificio:** Suma = arrastrar frutas a canasta con contador; Resta = situaciones con campo numérico + recta (incluye deuda/negativos); Multiplicación = situaciones con intervenciones de Katia (suma repetida → conmutatividad → puente a división); División = arrastrar trozos de pizza a platos, con residuo e inversas; Potenciación = completar tabla de crecimiento por horas + curva; Radicación = situaciones geométricas (área/volumen) con raíz exacta y no exacta.
- **Eventos y persistencia:** registra `events_to_register`; respeta `persistence_required`/`persistence_excluded`. **Nunca persistas `elo_score`** (estos nodos no afectan ELO).
- **Diferenciación:** implementa `level_presentation` (Básico/Intermedio/Avanzado).
- **Accesibilidad:** KaTeX con MathML/`aria-label`; drag-and-drop con alternativa tocar-para-colocar y teclado; estados no dependientes solo de color (íconos ✓/⚠); contraste ≥ 4.5:1 en claro y oscuro.
- **i18n:** strings en recursos es-CO con el `i18n_prefix` del spec (`prealgebra.n2.e00` … `e06`).
- **Pruebas:** lógica de evaluación, ruteo de feedback por error, gating del hub, diferenciación por banda, y el residuo/inversa en división.

## Correcciones YA aplicadas en los specs (no reintroducir desde el PDF original)

Si comparas con el borrador/PDF original, **estas correcciones ya están en los specs y deben conservarse**:
- **Hub:** el título interno "Nivel 1" del borrador → **Nivel 2**.
- **Resta:** el Texto 1 decía "edificio de la suma" → **resta**.
- **Potenciación:** "crecimiento lineal/lineal exponencial" → **exponencial**; el personaje "pablo/repartición" → **Juan/crecimiento**; modelado explícito **población(hora n) = base^(n+1)** (se parte de "base" individuos que se multiplican por "base" cada hora). *(Si prefieres potencias puras población = baseⁿ, habría que reformular el enunciado a "empieza con 1"; decisión pedagógica pendiente — respeta lo que diga el spec salvo indicación contraria.)*
- **Radicación:** área 16 m² → lado **4 m** (no 4 cm); **es-CO** "√20 ≈ 4,4721" (coma); Texto 1 completado a "último edificio".
- **es-CO** en todo el nivel (coma decimal).

## Invariantes que NO se rompen

- **Notación es-CO** (coma decimal, punto de miles).
- **Todos los nodos son formativos:** `safe_zone = true`, `affects_elo = false`, `skip_penalty = false`. No los conectes al ELO.
- **Definición + ejemplos base antes de la práctica** (patrón obligatorio, ver arriba).
- **Alertas en tres niveles:** `observation → reinforcement_suggested → teacher_intervention` (la última requiere persistencia / ≥3 ocurrencias). Hipótesis de diseño parametrizables, no umbrales calibrados.
- **Render de KaTeX obligatorio:** respeta cada `render_blocker`. **Riesgo alto en E05 (superíndices/exponentes) y E06 (índices/radicandos del radical)** — verifícalos explícitamente; no dejes exponentes ni radicales vacíos.
- **Lenguaje de crecimiento** en la retroalimentación; nada punitivo.
- **Datos de menores (Ley 1581 / minimización):** no persistas texto libre crudo del estudiante como dato condicionante.
- **Sin gating de complejos** (no aplica en este nivel). La radicación enlaza con Irracionales/Reales del Nivel 1 (raíces no exactas), pero no introduce ramas opcionales.

## Salida esperada de esta sesión

1. Tabla de reconciliación (existe-coincide / requiere-cambios / falta) + diffs.
2. Plan por nodo en orden E00 → E06.
3. Tras aprobación: implementación nodo por nodo, con resumen de qué se creó vs. actualizó, y marcadores de contenido **[NUEVO]** pendiente de validación pedagógica.
4. Lint/typecheck/tests en verde: `npm run lint`, `npm run typecheck` (o `npx tsc --noEmit`) y `npm test` (ajusta al gestor de paquetes del repo si no es npm).
5. Lista de conflictos o decisiones pendientes (incluida la del modelado de potenciación, si aplica).

**No asumas que todo es nuevo sin auditar, no reintroduzcas los errores ya corregidos, y respeta el patrón definición→práctica→consolidación en cada edificio.**
