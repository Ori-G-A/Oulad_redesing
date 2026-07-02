# PROMPT — Replicar el formato unificado + escalera de cierre a las 5 operaciones N2 restantes

## Objetivo
El nodo **División (E04)** ya es la referencia del patrón "operación extendida a los conjuntos numéricos". Replicar ese patrón a **Suma (E01), Resta (E02), Multiplicación (E03), Potenciación (E05) y Radicación (E06)**, con su propia escalera de cierre y ejemplos que recorren los conjuntos.

## Qué YA está construido — NO rehacer (reutilizar tal cual)
- **Renderer**: `LevelTwoOperation` en `frontend/src/pages/Student/lessons/LevelTwoLesson.tsx`. Detecta `content.story_contract.type === "unified_set_extension"` y pinta automáticamente: `KatiaStorySlot` → `[descubrimiento | definición formal]` → ejemplos resueltos en 2 columnas → trampa en columna ancha → escalera de cierre → práctica → footer. Marca la trampa con `trap: true` (el renderer la baja a la columna ancha).
- **CSS**: `LevelTwoLesson.css` (`.n2-closure`, `.n2-closure-ladder/-row/-badge`, `.n2-examples-2col`, `.n2-example-wide`, `.n2-image-slot`, `.n2-example-latex`).
- **Tipos**: `frontend/src/api/student.ts` (`katia`, `discovery`, `closure`, `worked_examples` con `latex/eyebrow/title/image_slot/trap`, `situations.set_label`).
- **Componente** `KatiaStorySlot` (props `question`, `formulas`).

⇒ El trabajo es SOLO de **contenido**: editar el dict de cada operación en `_N2_OPERATION_CONTENT[<NODE_ID>]` dentro de `src/domain/learning/prealgebra.py`, copiando la forma EXACTA de `N2_DIVISION_NODE_ID` como plantilla.

## Estructura a poner en cada dict (igual que División)
```
story_contract = {"type": "unified_set_extension", "practice_position": "after_definition_plus_examples", "is_integrated": True}
katia          = {eyebrow, title, body, question}          # apertura griega + pregunta detonadora
discovery      = {eyebrow, title, body}                    # descubrimiento guiado
definition, definition_title, definition_katex             # definición formal (LaTeX explícito)
worked_examples = [ ...ejemplos por conjunto..., {trap: True, ...} ]  # N normales (2 col) + 1 trampa (ancha)
closure        = {title, intro, rows: [6 filas: ℕ ℤ ℚ 𝕀 ℝ ℂ]}       # SIEMPRE los 6 conjuntos
situations     = [ ...por conjunto, set_label, answer tecleable... ]
validation_status = "F2_<EXX>_unified_set_extension"
```
Cada `worked_example`: `eyebrow="Ejemplo N · <Conjunto>"`, `title`, `statement`, `latex` (KaTeX explícito), `steps` (pasos completos), `image_slot: True` donde haya imagen.
Cada `closure.row`: `{symbol, name, closed: "yes"|"no", latex, note}`.

## Reglas NO negociables
1. **KatIA es una gata cyborg GRIEGA.** Contextos del ágora: ánforas, aceitunas, higos, dracmas, hogazas, columnas, discípulos, mercado griego. **Prohibido** pizza u otros contextos no griegos. La apertura **no** debe repetir el ejercicio exacto de la práctica.
2. **Diferenciación mínima en cada ejercicio (planteado o resuelto).** Ningún caso concreto se repite: la apertura, el descubrimiento, cada ejemplo resuelto y cada ítem de práctica usan números y/o contexto **distintos** entre sí. Nada de mostrar `12÷4` como ejemplo y volver a pedir `12÷4` en la práctica. Variar objeto griego (aceitunas/higos/ánforas/dracmas/hogazas) y cantidades.
3. **LaTeX explícito que COMPILE en KaTeX** (verificar 0 elementos `.katex-error` en el render real). Usar `\dfrac`, `\tfrac`, `\sqrt`, `\cdot`, `\div`, `\neq`, `\notin`, `\in`, `\mathbb{}`. **Coma decimal es-CO** con la llave: `2{,}5`. No usar el `mathFromText` (el renderer unificado ya pasa el LaTeX directo).
3. **Pasos completos, sin omitir.** Cada ejemplo y cada fila de cierre con su justificación.
4. **La escalera SIEMPRE lleva los 6 conjuntos** (ℕ, ℤ, ℚ, 𝕀, ℝ, ℂ), con ℂ como "desvío opcional avanzado".
5. **Tema recurrente — 𝕀 (irracionales) NO es cerrado bajo NINGUNA operación aritmética**: el resultado siempre puede "caerse" a ℚ. Es la trampa profunda que se repite en suma, resta, multiplicación, potenciación y división (refuerza por qué necesitamos ℝ = ℚ ∪ 𝕀). En radicación el eje es el inverso (la radicación *produce* irracionales y motiva ℂ).
6. **Práctica con respuestas numéricas tecleables**: el backend valida con regex `-?\d{1,6}(,\d{1,4})?`. Solo enteros o decimales de ≤4 cifras (`2,5`, `1,75`, `-3`). **Prohibido** `0,333…` o respuestas no finitas. Si un cálculo da periódico/irracional, elige números que den resultado finito (p. ej. `√8÷√2=2`, `9^{1/2}=3`).
7. Ejemplos resueltos en **2 columnas**; la **trampa** en **columna ancha abajo** (automático con `trap: True`).

## Análisis de cierre por operación — USAR ESTO (ya verificado)

### E01 Suma (cerrada salvo en 𝕀)
| Conj. | closed | latex sugerido |
|---|---|---|
| ℕ | yes | `3+5=8` |
| ℤ | yes | `-3+5=2` |
| ℚ | yes | `\dfrac{1}{2}+\dfrac{1}{3}=\dfrac{5}{6}` |
| 𝕀 | **no** | `\sqrt{2}+(-\sqrt{2})=0` (∈ ℚ) |
| ℝ | yes | `\sqrt{2}+\pi\in\mathbb{R}` |
| ℂ | yes | `(2+i)+(3+2i)=5+3i` |
Trampa = 𝕀. Pregunta: "¿Juntar dos cantidades siempre da una cantidad del mismo tipo?"

### E02 Resta (rompe en ℕ → motiva ℤ; y 𝕀 no cierra)
| Conj. | closed | latex |
|---|---|---|
| ℕ | **no** | `3-5=-2\notin\mathbb{N}` |
| ℤ | yes | `3-5=-2` |
| ℚ | yes | `\dfrac{1}{2}-\dfrac{1}{3}=\dfrac{1}{6}` |
| 𝕀 | **no** | `\sqrt{2}-\sqrt{2}=0` (∈ ℚ) |
| ℝ | yes | `\pi-\sqrt{2}\in\mathbb{R}` |
| ℂ | yes | `(3+2i)-(1+i)=2+i` |
Ejemplo estrella: `3-5=-2` entra a ℤ (motiva B05). Trampa = 𝕀. Pregunta: "¿Restar dos naturales siempre da un natural?"

### E03 Multiplicación (cerrada salvo en 𝕀)
| Conj. | closed | latex |
|---|---|---|
| ℕ | yes | `3\times 4=12` |
| ℤ | yes | `(-3)\times 4=-12` |
| ℚ | yes | `\dfrac{2}{3}\times\dfrac{3}{4}=\dfrac{1}{2}` |
| 𝕀 | **no** | `\sqrt{2}\times\sqrt{2}=2` (∈ ℚ) |
| ℝ | yes | `\sqrt{2}\cdot\pi\in\mathbb{R}` |
| ℂ | yes | `(1+i)(1-i)=2` |
Trampa = 𝕀. Pregunta: "¿Multiplicar dos irracionales da siempre un irracional?"

### E05 Potenciación (eje = ampliar el EXPONENTE; `closed` = "¿el resultado se queda en el conjunto de la base?")
| Caso | closed | latex | nota |
|---|---|---|---|
| exp. natural (ℕ) | yes | `2^{3}=8` | base y exp naturales → natural |
| exp. entero negativo (ℤ) | **no** | `2^{-2}=\dfrac{1}{4}` | el exponente negativo lleva a ℚ |
| exp. fraccionario (ℚ) | **no** | `2^{1/2}=\sqrt{2}` | exponente fraccionario = raíz → ℝ (irracional) |
| potencia de un irracional (𝕀) | **no** | `(\sqrt{2})^{2}=2` | vuelve a ℚ |
| base real (ℝ) | yes | `2^{\pi}\in\mathbb{R}` | |
| base negativa, exp fraccionario (ℂ) | yes | `(-1)^{1/2}=i` | desvío opcional |
Trampas frecuentes a desmentir en pasos: `2^{3}\neq 2\times 3`; `2^{0}=1`; `2^{-1}=\dfrac{1}{2}` (no `-2`). Pregunta: "Si subimos el exponente por debajo de cero o entre enteros, ¿el resultado sigue siendo natural?"

### E06 Radicación (eje inverso: PRODUCE irracionales → motiva ℝ y ℂ)
| Conj. | closed | latex | nota |
|---|---|---|---|
| ℕ | **no** | `\sqrt{16}=4` pero `\sqrt{2}\notin\mathbb{N}` | solo cuadrados perfectos |
| ℤ | **no** | `\sqrt{2}\notin\mathbb{Z}` | |
| ℚ | **no** | `\sqrt{2}\notin\mathbb{Q}` | raíz de no-cuadrado = irracional → motiva 𝕀 (B07) |
| 𝕀 | (produce) | `\sqrt{2}\in\mathbb{R}\setminus\mathbb{Q}` | la radicación CREA irracionales |
| ℝ | yes | `\sqrt{20}\approx 4{,}4721` (radicando ≥ 0) | |
| ℂ | yes | `\sqrt{-1}=i` | radicando negativo → motiva ℂ (B09) |
Trampa = ℂ (`\sqrt{-1}=i`) o el salto ℚ→𝕀. Pregunta: "¿Toda raíz de un número entero es otro entero?"

## Ejemplos resueltos y práctica — guía
- Worked examples: 1 por conjunto donde la operación es interesante (mín. 4: cubrir ℕ, ℤ, ℚ, y la trampa). Incluir el caso **fracción⊕fracción** explícito en ℚ (como en División Ej5).
- Práctica (`situations`): recorrer ℕ → ℤ → ℚ → 𝕀, con `set_label` y respuestas finitas tecleables. Ejemplos de respuestas válidas: suma `\frac{1}{4}+\frac{1}{4}` → `0,5`; potenciación `2^{-2}` → `0,25`; radicación `\sqrt{16}` → `4`, `\sqrt{8}\div\sqrt{2}` no aplica aquí pero `9^{1/2}` → `3`.
- Marcar `image_slot: True` en 2 ejemplos concretos por nodo (los de contexto físico, p. ej. aceitunas/ánforas/higos/dracmas).

## Verificación (obligatoria por nodo)
1. `python -c "import src.domain.learning.prealgebra"` carga sin error (cuidado con UTF-8; el archivo admite acentos).
2. `cd frontend && ./node_modules/.bin/tsc --noEmit` (sin errores; valida tipos).
3. **Reiniciar el backend** (corre sin `--reload`) para cargar el contenido nuevo.
4. Render en vivo de cada nodo y comprobar por DOM: `0` elementos `.katex-error`; escalera con 6 filas; ejemplos en 2 columnas; trampa en columna ancha debajo; práctica con `set_label` cruzando conjuntos. (Los screenshots del preview suelen agotar tiempo en estas páginas KaTeX-pesadas: verificar por DOM, no por imagen.)

## Orden sugerido
Resta (E02) → Multiplicación (E03) → Suma (E01) → Potenciación (E05) → Radicación (E06).
Razón: resta y multiplicación son las más cercanas a División; suma consolida el patrón "cerrada salvo 𝕀"; potenciación y radicación son las de eje especial (exponente / produce irracionales) y conviene hacerlas al final con el patrón ya afinado.
