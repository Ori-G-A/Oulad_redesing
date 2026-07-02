# PROMPT — Enriquecer los 5 nodos restantes de N4 Divisibilidad (C02–C06)

## Objetivo

**C01 Divisibilidad** ya es el nodo de referencia (piloto), completo y verificado de punta a
punta: contenido rico + `LevelFourLesson.tsx`/`.css` + ruteo + wiring de mapa + tests. Los otros
5 conceptos (**C02 Múltiplos, C03 Primos, C04 Factorización prima, C05 MCD, C06 MCM**) hoy tienen
contenido mínimo viable (`"validation_status": "F4_TODO_stub"` en `prealgebra.py`) — currícularmente
correcto pero sin la riqueza de C01 (menos ejemplos, menos práctica, sin variedad de contextos).
Este documento es la plantilla para llevarlos al mismo nivel, replicando C01 nodo por nodo.

## Qué YA está construido — NO rehacer (reutilizar tal cual)

- **Motor de evaluación backend**: `evaluate_interaction()` en `src/domain/learning/prealgebra.py`
  ya soporta los 3 tipos que necesita N4 (`numeric`, `single_select`, `multi_select`) — **no tocar
  esa función**.
- **Registrador de interacciones mixtas**: `_register_mixed_interactions(node_id, concept_slug,
  items)` (definido justo antes de `_N4_CARDS` en `prealgebra.py`). Recorre una lista de items
  `{"id", "kind", ...}` y genera tanto `_LESSONS[node_id]["interactions"]` como
  `_INTERACTION_RULES[...]`. Ya se usa para el icebreaker del hub y para `practice` de cada
  concepto — reutilizar, no reescribir.
- **Renderer frontend**: `frontend/src/pages/Student/lessons/LevelFourLesson.tsx` +
  `LevelFourLesson.css`. Detecta `content.kind === "level_hub_port"` (hub) vs cualquier otro valor
  (concepto) y pinta automáticamente: `KatiaStorySlot` → `[descubrimiento | definición formal]`
  (`.set-story`/`.set-formal`) → ejemplos resueltos 2 columnas + trampa ancha
  (`.n2-examples-2col`/`.n2-example-wide`, reutilizados de N2) → caja de formalización
  (`.n4-formalization`) → práctica mixta (`PracticeItem`, switch por `item.kind`) → cierre → footer.
  **El trabajo de C02–C06 es SOLO de contenido**: editar
  `_N4_CONCEPT_CONTENT[<NODE_ID>]` en `prealgebra.py`, copiando la forma EXACTA de
  `N4_DIVISIBILITY_NODE_ID` (C01) como plantilla.
- **Ruteo y mapa**: `N4_IDS` en `Lesson.tsx`, inserción secuencial en `course_map`
  (`api/routers/student.py`) — ya cablean los 7 nodos. No hace falta tocarlos al enriquecer
  contenido (solo si se agrega un nodo nuevo, lo cual no aplica aquí).

## Estructura a poner en cada dict (igual que C01)

```python
N4_XXX_NODE_ID: {
    "kind": "divisibility_concept",
    "concept_id": "C0N",
    "concept_slug": "...",                      # usado en default_misconception: error_<slug>
    "title": "...",
    "story_contract": {"type": "guided_discovery_formalization",
                        "practice_position": "after_definition_plus_examples", "is_integrated": True},
    "katia": {"eyebrow", "title", "body", "question"},       # apertura + pregunta problematizadora
    "discovery": {"eyebrow", "title", "body"},                # descubrimiento guiado
    "definition": "...", "definition_title": "...", "definition_katex": r"...",
    "worked_examples": [ ...N normales..., {"trap": True, ...} ],  # 2-3 normales + 1 trampa
    "formalization": {"title", "intro", "items": [{"label", "rule", "latex"?}, ...]},
    "practice": [                                              # 6-9 items, tipos MIXTOS
        {"id": "Q1", "kind": "numeric", "prompt": "...", "expr": r"...", "answer": "..."},
        {"id": "Q2", "kind": "single_select", "prompt": "...",
         "options": [{"id": "a", "text": "..."}, ...], "expected": "a",
         "feedback_by_option": {"a": "correct", "b": "fb_xxx_q2_b", ...},
         "misconception_by_option": {"b": "..."}},
        {"id": "Q3", "kind": "multi_select", "prompt": "...",
         "valid_options": ["...", ...], "expected": ["...", ...], "trap_options": ["...", ...],
         "feedback_correct": "correct", "feedback_trap": "fb_xxx_q3_trap",
         "misconception_trap": "...", "feedback_missing": "fb_xxx_q3_missing",
         "misconception_missing": "...", "feedback_incorrect": "default",
         "misconception_incorrect": "error_<slug>"},
    ],
    "feedback": {"correct": "...", "default": "...", "fb_xxx_qN_x": "...", ...},  # TODAS las keys usadas arriba
    "closing": "...",
    "validation_status": "F4_C0N_pilot",   # cambiar de F4_TODO_stub al terminar
}
```

**IMPORTANTE — bug ya corregido, no reintroducir**: `valid_options`/`expected`/`trap_options` de
`multi_select` deben ser **listas** (`[...]`), NUNCA sets (`{...}`) — viven dentro de `content`,
que viaja al frontend como JSON, y un `set` de Python no es serializable de forma determinista.
`_register_mixed_interactions` ya convierte la lista a `set()` internamente para las reglas del
backend; el frontend solo necesita la lista.

## Reglas NO negociables

1. **Escenario = Puerto de la Polis, pero solo de telón de fondo.** KatIA es la
   funcionaria/heraldo del puerto (muelles, barcos, ánforas, rutas a Atenas/Corinto/Delos/
   Mileto/Rodas/Esparta) — úsalo en la apertura (`katia`) de cada nodo, pero **NO fuerces cada
   ejemplo y cada ítem de práctica a ser "barcos y ánforas"**. Esa fue la corrección explícita
   del usuario sobre N3 ("como que no existiera más cosas en la antigua Grecia").
2. **Banco de contextos variado — ningún objeto se repite más de 2 veces en TODO el nivel** (7
   nodos, contando también C01). Contextos ya usados en C01: caramelos, canicas, entradas de
   feria, sacos de trigo, remos, ánforas de aceite. Para C02–C06 usar variedad nueva: huertos/
   filas de árboles, animales de granja, instrumentos musicales, monedas/entradas de feria (si no
   se repite de C01), útiles escolares, distancias/corredores, torres/bloques. Antes de escribir
   un ejemplo, revisa qué objetos ya aparecieron en los nodos anteriores.
3. **Feedback específico y accionable, nunca "correcto/incorrecto" a secas.** Cada opción
   incorrecta de `single_select`/`multi_select` necesita su propia entrada en `feedback_by_option`
   / `feedback_trap`/`feedback_missing` explicando **por qué** está mal (ver los `fb_c01_qN_x` de
   C01 como ejemplo).
4. **La trampa (`trap: True`) es un error conceptual real**, no un despiste — en C01 fue "par ⇏
   divisible por 4"; sigue el mismo criterio (un contraejemplo que desmiente una generalización
   apresurada).
5. **LaTeX explícito que compile en KaTeX**: `\dfrac`, `\sqrt`, `\times`, `\div`, `\mathbb{}`,
   coma decimal es-CO con llave (`2{,}5`) si aplica. Revisar 0 `.katex-error` en el render real.
6. **Práctica con respuestas numéricas tecleables**: el backend valida `numeric` con regex
   `-?\d{1,6}(,\d{1,4})?` — solo enteros o decimales de ≤4 cifras, nunca periódicos.

## Mapeo del documento fuente a cada nodo

| Nodo | Página del `.md` original | Contenido a expandir |
|---|---|---|
| **C02 Múltiplos** | Página 3 · CONCEPTO 2 | Ya tiene 1 ejemplo (torre de bloques) + 1 trampa + 1 práctica multi_select. Agregar: el ejemplo del "corredor" completo (2,3,4,6,9 horas) como situaciones numéricas adicionales, más práctica (mín. 6-8 items), formalización ya tiene las 4 propiedades del doc — verificar que estén completas. |
| **C03 Primos** | Página 4 · CONCEPTO 3 | Ya tiene 1 ejemplo + trampa (el 1) + 1 multi_select. Agregar: la actividad de "contar divisores" de varios números (7, 12, 1, 11 del doc) como práctica numérica, más ejemplos con números primos/compuestos variados (no solo los del doc), formalización con teorema fundamental ya presente. |
| **C04 Factorización prima** | Página 5 · CONCEPTO 5 (doc) | Ya tiene 1 ejemplo (84) + 1 trampa (36). Agregar: modelar la "división sucesiva" del doc (64, 81, 125, 630, 72, 1200) como **una interacción numérica por paso** (ver nota abajo), más práctica de "formas de descomposición" como multi_select (36, 90, 128 del doc ya tienen opciones correctas/incorrectas listas). |
| **C05 MCD** | Página 6 · CONCEPTO 5 (doc, mal numerado como 5 otra vez) | Ya tiene 1 ejemplo (225,180) + trampa. Agregar: la tabla de pares del doc (24-36, 45-60, 28-42, 54-72, 120-180, 144-216) como práctica `single_select` (elegir el MCD correcto de opciones) o `numeric`, más el algoritmo de Euclides como método explícito en formalización (ya listado). |
| **C06 MCM** | Página 7 · CONCEPTO 6 | Ya tiene 1 ejemplo (20,30) + trampa. Agregar: la tabla de pares del doc (16-24, 21-35, 28-40, 36-54, 132-180, 154-231) como práctica, más la relación MCD×MCM=a×b como pregunta de aplicación. |

**Descomposición sucesiva (C04/C05/C06) — cómo modelarla sin widget nuevo**: cada paso de
división (p. ej. `630÷2=315`, `315÷3=105`, ...) es **una interacción `numeric` independiente**
dentro de `practice`, con su propio `id` (Q1, Q2, Q3...) y `prompt` indicando qué paso es. Se
muestran como una lista vertical normal (reutiliza `.n4-practice-item`, sin componente de árbol).
No es necesario mostrar todos los pasos en una sola tarjeta interactiva — el ejemplo resuelto
(`worked_examples`) ya muestra la secuencia completa con `steps`; la práctica puede pedir 1-2
pasos sueltos o el resultado final.

## Verificación (obligatoria por nodo, igual que se hizo con C01)

1. `python -c "import src.domain.learning.prealgebra"` — carga sin error.
2. `python -c "import json; from src.domain.learning.prealgebra import get_lesson, N4_XXX_NODE_ID; json.dumps(get_lesson(N4_XXX_NODE_ID)['content'])"` — confirma que no se colaron `set()` en `content`.
3. `python -m pytest tests/unit/domain/test_prealgebra_lessons.py -q` — no debe romper nada existente (agregar un caso análogo a `test_n4_divisibility_mixed_interactions` por nodo si se agregan tipos nuevos de interacción).
4. `cd frontend && ./node_modules/.bin/tsc --noEmit` — sin errores (no debería cambiar nada de tipos, solo contenido).
5. Reiniciar el backend **sin** `--reload` para cargar el contenido nuevo.
6. Walk manual vía API (como se hizo con C01): login → `GET /api/student/lessons/algebra_basica/<NODE_ID>` → `POST .../interactions` por cada item de `practice` → `POST .../events {"event":"node_completed"}` → confirmar que el siguiente nodo pasa a `"available"` en `GET /api/student/map/algebra_basica`. Limpiar después las filas de prueba en `lesson_progress`/`lesson_interactions` si se usa una cuenta demo compartida.
7. Cambiar `"validation_status"` de `"F4_TODO_stub"` a `"F4_C0N_pilot"` (o similar) al terminar cada nodo.

## Orden sugerido

C02 Múltiplos → C03 Primos → C04 Factorización prima → C05 MCD → C06 MCM.

Razón: Múltiplos y Primos son las más cercanas en forma a C01 (criterios/definición simple);
Factorización, MCD y MCM comparten el patrón de "descomposición sucesiva" y conviene hacerlas
juntas al final, una vez afinado el patrón de pasos numéricos secuenciales.
