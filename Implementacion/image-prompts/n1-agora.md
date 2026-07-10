# Prompts de imagen — N1 · El Ágora

Fase 7 del plan de guión unificado (`~/.claude/plans/effervescent-scribbling-goblet.md`).
Vocabulario visual del espacio (Fase 0 / skill `prealgebra-narrative-style`): columnas,
mármol, tablillas, plaza pública, ciudadanos, escalinatas. Ningún toque mecánico forzado —
KatIA (gata cyborg) es la única nota tecnológica del nivel.

**Línea gráfica obligatoria (`frontend/public/prealgebra/`):** usar como referencia directa
`escalera-conjuntos.png`, `step-naturales.png`, `step-enteros.png`, `step-racionales.png`,
`step-reales.png`, `katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`.
Antes de generar, abrir/adjuntar esas imágenes como referencias visuales si la herramienta lo
permite; si no, copiar completa esta línea gráfica dentro del prompt final.

**Estilo base (los 4 archivos comparten esta cola):**
`pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad, con clusters de
píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering sutil; NO
pintura digital hiperrealista. Composición contenida como los assets existentes: KatIA
legible en primer/medio plano, escalinatas o mesa de mármol como ancla, columnas/arcos
griegos en segundo plano, pocos personajes secundarios desenfocados, sombras azul noche,
mármol beige cálido, luz dorada de lámpara/antorcha y acentos teal pequeños. KatIA debe
conservar la identidad visual de frontend/public/prealgebra: gata blanca con mancha
naranja/negra en la cabeza, ojo verde visible, ocular mecánico teal en el otro ojo,
pata/brazo mecánico, túnica morada y ornamentos dorados.`

**Personajes secundarios:** cualquier rol humano mencionado en los prompts (ciudadano,
escriba, mercader, aprendiz, albañil, joven, niño, mozo, vendedor, mensajero, etc.) debe
representarse como animal antropomórfico. Preferencia: otros gatos bípedos con túnicas
griegas, pelajes variados (atigrado, negro, gris, calicó, siamés, naranja, blanco moteado) y
texturas de pelaje diferenciadas. No humanos realistas.

**Escaleras y peldaños:** si aparece una escalera, escalinata o peldaño en cualquier imagen,
debe estar completamente limpio: sin símbolos, letras, números, runas, marcas, medallones,
flechas, etiquetas ni relieves matemáticos.

**Negativos de estilo:** no panorámicas turísticas de Atenas, no Acrópolis heroica al fondo,
no multitudes, no composición cinematográfica hiperrealista, no pintura digital lisa, no
neón saturado, no anime/chibi, no humanos realistas, no cambiar la identidad de KatIA por
una mascota metálica completa.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ningún prompt incluye
el resultado numérico de un ejercicio ni una cantidad de objetos que permita contarlo y
resolver el ejercicio mirando la imagen.

N1 no usa el campo `image_slot` (es contenido i18n en `es.ts`/`en.ts`, no dicts de Python) —
las entradas de abajo cubren el header del nivel (B01, equivalente a hub) y el beat de
apertura de cada nodo (`KatiaStorySlot` o su equivalente bespoke en cada componente TSX).

---

## B01 — Bienvenida ("Todo número tiene un lugar")

**Header de nivel** (`.level-presentation-header` + `.level-presentation-media`, ancho
completo, 16:9) — tomado de `body`: "El recorrido comienza en el ágora, la plaza donde los
ciudadanos cuentan, miden y reparten."

> Encuadre de presentación contenido, alineado con `escalera-conjuntos.png`: KatIA en
> primer/medio plano a la derecha, junto a una mesa de mármol con pergaminos, tablillas de
> cera y una cesta pequeña. Detrás se sugiere el ágora como una galería abierta con columnas,
> arcos y escalinatas de piedra; pocos gatos antropomórficos con túnicas conversan suavemente al fondo,
> sin competir con KatIA. KatIA mira hacia el espectador como dando la bienvenida al
> recorrido. Luz dorada de lámparas sobre mármol cálido, sombras azul noche. Sin texto ni
> números visibles.
> Estilo base + aspect ratio 16:9.

---

## B02 — Pregunta detonadora ("¿Contar alcanza para todo?")

**Escena de apertura** (ancho completo, 16:9) — B02 no tiene beat de KatIA; el ancla visual
son las 3 situaciones que presenta (`situations.temperature/pizza/debt`), ahora relocalizadas
implícitamente al ágora del recorrido.

> Tres viñetas dentro de una misma plaza de mármol al atardecer, sin separarlas con bordes
> duros: (1) un termómetro de mercurio antiguo apoyado en una columna con la aguja bajando
> por debajo de una marca central; (2) un pan de trigo entero o apenas preparado sobre una
> mesa de piedra con gatos antropomórficos alrededor esperando su parte; (3) una tablilla de
> cera con marcas abstractas de deuda y un gato antropomórfico revisando una bolsa de monedas
> sin llegar a completar el monto. KatIA observa
> las tres escenas desde una esquina, pensativa. No mostrar el resultado de ninguna
> operación ni completar visualmente ningún reparto.
> Estilo base + aspect ratio 16:9.

---

## B03 — Escalera de la necesidad ("Cada peldaño nace de una necesidad")

**Escena de apertura** (ancho completo, 16:9) — ancla en `staircaseAria`: "Escalera de cinco
peldaños: naturales, enteros, racionales, irracionales y reales; con un desvío opcional
hacia los complejos".

> Una escalinata de mármol de cinco peldaños tallada en el ágora, completamente limpia, sin
> símbolos, letras, números, runas, marcas, medallones ni relieves matemáticos. Un sexto
> peldaño lateral y más pequeño, algo separado del camino principal, insinúa un desvío
> opcional sin ninguna etiqueta. KatIA sube el primer peldaño con una pata alzada hacia el
> segundo, mirando hacia arriba de la escalera. Luz cálida de antorchas marcando cada
> peldaño ya recorrido.
> Estilo base + aspect ratio 16:9.

---

## B04 — Naturales ("Contar cantidades completas")

**KatiaStorySlot** (equivalente bespoke, columna imagen | copy, ~4:3) — de `story.katiaBody`:
"KatIA... puede contar 1 tablilla, 2 cestas, 3 ciudadanos o 0 monedas en un cofre vacío" y del
`scenario`: "una cesta con tablillas... para completar el censo de la ciudad".

> KatIA sentada junto a una mesa de mármol en la plaza, contando tablillas de arcilla que
> saca una por una de una cesta de mimbre. A un lado, un cofre de ofrendas vacío y abierto.
> Detrás, ciudadanos conversando junto a una columna. Ninguna tablilla debe verse apilada en
> un total ya sumado — solo el gesto de contar una por una, cesta y cofre por separado.
> Estilo base + aspect ratio 4:3.

---

## B05 — Enteros ("Cruzar el cero")

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `story.katiaBody`: "consejo de la
ciudad... mármol y cinceles fiados... para tallar un monumento en la plaza... colecta
pública" y del ejemplo: "taller del cantero".

> El taller de un cantero en el ágora: bloques de mármol sin tallar apilados junto a
> cinceles colgados de un panel de madera. Un escriba del consejo de la ciudad sostiene una
> tablilla de cuentas con una balanza de fiel dibujada (sin números), mostrando el gesto de
> "aún se debe" — el platillo de la izquierda más bajo que el de la derecha, sin marcar el
> monto exacto. KatIA observa la balanza con una pata sobre el mentón. Ambiente de plaza
> pública al fondo, columnas y escalinatas.
> Estilo base + aspect ratio 4:3.

---

## B06 — Racionales ("Repartir una unidad")

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `scenario`: "Tres panes entre cuatro
ciudadanos, en el ágora" y `story.katiaBody`: "fruits/juice" (paralelo en-solo, ver nota).

> Una mesa de piedra en el ágora con panes de trigo enteros, sin cortar todavía, y cuatro
> ciudadanos de pie alrededor esperando su parte con las manos abiertas. KatIA está junto a
> la mesa con un cuchillo de piedra en una pata, a punto de partir uno de los panes, mirando
> a los cuatro ciudadanos como calculando cómo repartir en partes iguales. No mostrar los
> panes ya cortados ni las porciones repartidas.
> Estilo base + aspect ratio 4:3.

---

## B07 — Irracionales ("Decimales que no vienen de una fracción")

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `story.katiaBody`: "KatIA mide la
diagonal de una plaza empedrada cuyo lado mide exactamente 1" y del ejemplo trampa: "traza un
círculo en la plaza y divide su circunferencia entre su diámetro".

> KatIA arrodillada sobre un patio de baldosas cuadradas del ágora, con una cuerda de medir
> tensada en diagonal de una esquina a la otra de una sola baldosa cuadrada, mirando la
> cuerda con curiosidad como si la medida no encajara en ninguna marca exacta de la cuerda.
> Al fondo, un círculo trazado en el suelo con tiza y un ciudadano midiendo su borde con la
> misma cuerda. Ninguna cifra ni fracción visible sobre la cuerda o el suelo.
> Estilo base + aspect ratio 4:3.

---

## B08 — Reales ("Todo junto en la recta")

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `story.katiaBody`: "un camino de
baldosas atraviesa la plaza de extremo a extremo... cada baldosa es un número real" y
`discoveryBody`: "de la entrada de la plaza a la escalinata del templo".

> Vista elevada de un largo camino de baldosas de mármol que atraviesa toda la plaza del
> ágora, desde el arco de entrada hasta la escalinata de un templo al fondo. Las baldosas
> tienen texturas ligeramente distintas (algunas lisas, algunas con vetas onduladas) para
> sugerir dos familias de números conviviendo en el mismo camino, sin marcar ninguna con
> números o símbolos. KatIA camina por el centro del camino mirando hacia el templo lejano.
> Estilo base + aspect ratio 4:3.

---

## B09 — Complejos (desvío opcional, "Números en el plano")

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `story.katiaBody`: "el camino de
baldosas del ágora... algunas situaciones necesitan una ampliación más... un plano" (no un
plano cartesiano formal, sino la idea de "salir de la línea").

> KatIA de pie al borde del camino de baldosas del ágora, con una pata levantada como
> probando pisar fuera del camino, hacia un espacio nuevo sugerido apenas por un tenue
> resplandor teal cuadriculado que se extiende perpendicular al camino — una insinuación de
> plano, no un plano cartesiano dibujado con ejes ni números. Expresión de curiosidad, no de
> confusión. El ágora clásica sigue siendo el fondo dominante.
> Estilo base + aspect ratio 4:3.

---

## B10 — El Clasificador I ("Conjunto más específico")

**KatiaStorySlot** — de `katiaAlt` (texto ya escrito, literal): "KatIA junto a una zona de
clasificación con tarjetas de números".

> KatIA de pie junto a un tablero de mármol dividido en casillas etiquetadas únicamente con
> símbolos de conjunto (ℕ, ℤ, ℚ, 𝕀, ℂ — sin ejemplos numéricos escritos), sosteniendo una
> tablilla en blanco con una pata como si fuera a colocarla en una casilla. Ambiente de
> plaza pública de fondo. Ninguna tarjeta debe mostrarse ya colocada en su casilla correcta.
> Estilo base + aspect ratio 4:3.

---

## B11 — El Clasificador II ("Todos los conjuntos")

**KatiaStorySlot** — de `katiaAlt`: "KatIA junto a una matriz de pertenencia".

> KatIA junto a una gran tabla de mármol grabada con una cuadrícula vacía (columnas
> marcadas solo con los símbolos ℕ ℤ ℚ 𝕀 ℝ ℂ, filas en blanco sin números), señalando la
> cuadrícula con una pata como explicando que una fila puede marcarse en varias columnas a
> la vez. Sin ninguna casilla marcada todavía.
> Estilo base + aspect ratio 4:3.

---

## B12 — El Detective de Falsedades ("Caza la falsedad")

**KatiaStorySlot** — de `katiaAlt`: "KatIA con lupa de detective".

> KatIA con una lupa de bronce y cristal en una pata, examinando de cerca una tablilla de
> mármol con una frase grabada (la tablilla debe verse con líneas de texto ilegibles/
> abstractas, nunca una afirmación matemática real ni verdadera/falsa marcada), expresión
> entrecerrando los ojos con sospecha. Ambientación nocturna del ágora, antorchas proyectando
> sombras largas.
> Estilo base + aspect ratio 4:3.

---

## B13 — Diagnóstico del nivel ("Tu recorrido del nivel")

**Header de cierre** (ancho completo, 16:9) — de `title`: "Tu recorrido del nivel", tono de
cierre/resumen sin revelar el resultado del diagnóstico del estudiante.

> Encuadre de cierre contenido dentro de la misma galería de mármol de los assets existentes:
> la escalinata de cinco peldaños aparece al fondo medio, el camino de baldosas entra desde
> el primer plano y se pierde hacia una puerta luminosa. KatIA está de pie cerca de la
> escalinata, mirando hacia atrás en pose de cierre/celebración discreta (no eufórica). Luz
> dorada de amanecer entrando por los arcos, con sombras suaves y pocos detalles secundarios.
> Ningún marcador de puntaje, porcentaje ni insignia visible en la escena.
> Estilo base + aspect ratio 16:9.
