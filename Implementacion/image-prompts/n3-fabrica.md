# Prompts de imagen — N3 · La Fábrica Retrofuturista

Fase 7 del plan de guión unificado (`~/.claude/plans/effervescent-scribbling-goblet.md`).
Vocabulario visual del espacio (Fase 0 / skill `prealgebra-narrative-style`): máquinas
industriales, engranajes, bloques, balanza de laboratorio, palancas, bancos de prueba. Es el
espacio más "futurista" del catálogo — tecnológico por defecto, no un toque puntual. Cero
vocabulario de ágora/mercado (nada de columnas de plaza pública ni puestos con toldos).

**Línea gráfica obligatoria (`frontend/public/prealgebra/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `step-racionales.png`, `step-reales.png`,
`escalera-conjuntos.png`, `katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`.
Antes de generar, abrir/adjuntar esas imágenes como referencias visuales si la herramienta lo
permite; si no, copiar completa esta línea gráfica dentro del prompt final.

**Método aprobado para KatIA en N3:** no regenerar a KatIA desde prompt libre. Para una escena
con KatIA, generar primero un fondo SIN KatIA, sin gatos/personajes principales y con espacio
libre para componerla; después montar encima `frontend/public/prealgebra/katia-canon-sprite-hard.png`.
El bloque canónico de abajo se usa para validar identidad, no para pedirle al modelo que invente
una nueva versión del personaje.

**Bloque canónico de KatIA (obligatorio para cualquier imagen donde aparezca):** usar
`katia-primer-plano-enteros.png` como referencia de identidad, no solo de estilo. KatIA es una
gata cyborg adulta, serena y socrática, no una mascota infantil. Conservar proporciones del
personaje original: rostro blanco con hocico adulto redondeado, expresión tranquila y
observadora, orejas grandes pero no caricaturescas, ojo verde almendrado visible, mancha
naranja/negra asimétrica en la frente y oreja, ocular mecánico teal sobre el otro ojo con
placas metálicas grises, pata/brazo mecánico segmentado, túnica griega morada con ornamentos
dorados y silueta de tutora/maestra. Si el encuadre es pequeño, simplificar el entorno antes que
simplificar a KatIA. Debe seguir reconociéndose como la misma KatIA del primer plano.

**Estilo base:** `pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad,
con clusters de píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering
sutil, silueta con escalones de píxel visibles y poca mezcla suave; NO pintura digital
hiperrealista ni ilustración lisa. Mantener el lenguaje visual de los assets existentes:
KatIA legible en primer/medio plano, escena contenida tipo aula/taller, pocos ayudantes o
personajes secundarios, objetos pedagógicos claros sobre banco de trabajo, sombras azul noche,
luz dorada de lámpara y acentos teal pequeños. KatIA debe conservar identidad: gata blanca
con mancha naranja/negra en la cabeza, ojo verde visible, ocular mecánico teal, pata/brazo
mecánico, túnica morada y ornamentos dorados; en N3 puede sumar un delantal/arnés de trabajo
discreto sin tapar su silueta ni reemplazar la túnica. La fábrica es maquinaria griega
imaginada con bronce, engranajes de latón, palancas y tubos de vapor, no ciencia ficción
genérica.`

**Personajes secundarios:** cualquier rol humano mencionado en los prompts (ayudante,
técnico, operario, etc.) debe representarse como animal antropomórfico. Preferencia: otros
gatos bípedos con delantales o arneses de taller griego, pelajes variados (atigrado, negro,
gris, calicó, siamés, naranja, blanco moteado) y texturas de pelaje diferenciadas. No humanos
realistas.

**Escaleras y peldaños:** si aparece una escalera, escalinata o peldaño en cualquier imagen,
debe estar completamente limpio: sin símbolos, letras, números, runas, marcas, medallones,
flechas, etiquetas ni relieves matemáticos.

**Negativos de estilo:** no sci-fi duro, no laboratorio cyberpunk, no pintura digital lisa,
no render suavizado, no piel/pelaje con aerógrafo, no bordes antialias suaves, no neón
saturado, no máquinas gigantes que tapen a KatIA, no multitudes, no anime/chibi, no kawaii, no
gatita bebé, no cabeza sobredimensionada, no ojos brillantes infantiles, no mascota simplificada
tipo sticker, no humanos realistas, no cambiar a KatIA por una gata totalmente metálica ni
vestirla con overol completo.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ningún prompt muestra
el resultado numérico de un ejercicio ni un valor final en un display/báscula de la máquina.

---

## M00 — Hub: El Laboratorio de las Propiedades Misteriosas

**Header de nivel** (`.level-presentation-header` + `.level-presentation-media`, ancho
completo, 16:9) — de `welcome_text`/`scene_text`: "El laboratorio tiene cinco máquinas
industriales... una demostración, una serie guiada y una formalización."

> Interior de un laboratorio-taller griego retrofuturista, contenido como los assets de
> `frontend/public/prealgebra`, con cinco máquinas distintas
> dispuestas en el espacio (una prensa, un horno de fundición, una cinta transportadora, un
> calibre de banco y una prensa de contrapesos — siluetas reconocibles pero sin detalle de
> primer plano de ninguna), tuberías de bronce recorriendo el techo, luz teal proveniente de
> paneles de control simples. KatIA aparece en primer/medio plano con su túnica morada y un
> delantal/arnés de trabajo discreto, mirando hacia las cinco máquinas con una libreta en la
> pata.
> Estilo base + aspect ratio 16:9.

**Icebreaker ICE1** (numeric, cuadrado ~1:1) — de `icebreaker.items.ICE1.prompt`: "Una
máquina del laboratorio pesa 3 bloques de 4 kg cada uno en el platillo izquierdo."

> Una balanza de laboratorio de bronce con brazos articulados, con tres bloques metálicos
> idénticos apilados en el platillo izquierdo y el platillo derecho vacío, aguja del fiel
> inclinada hacia la izquierda. Sin marcador numérico visible en la escala.
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE2** (single_select, cuadrado ~1:1) — de `icebreaker.items.ICE2.story` +
`support_objects`: "2 balanzas de laboratorio idénticas" con "un engranaje de 5 kg y uno de 3
kg por balanza", colocados en orden distinto.

> Dos balanzas de laboratorio idénticas lado a lado. En la primera, un ayudante mecánico
> coloca un engranaje grande en el platillo y luego uno pequeño encima; en la segunda, otro
> ayudante coloca primero el pequeño y luego el grande encima. Ambas balanzas deben verse
> con el fiel en la misma posición inclinada, sin marcar el peso total.
> Estilo base + aspect ratio 1:1.

**Icebreaker ICE3** (numeric, cuadrado ~1:1) — de `icebreaker.items.ICE3.prompt`: "La
balanza marca 9 kg con una pieza de prueba puesta. Al retirar esa pieza..."

> Una balanza de laboratorio con una única pieza de prueba metálica sobre el platillo y una
> mano mecánica (brazo articulado de la propia máquina) a punto de retirarla, congelada a
> medio camino. El fiel de la balanza debe verse en una posición ambigua/intermedia, sin
> indicar aún el resultado final tras retirar la pieza.
> Estilo base + aspect ratio 1:1.

---

## M01 — Máquina Conmutativa: la Prensa de Intercambio

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "banco de ensamblaje...
colocar primero 3 engranajes y luego 6 tornillos, o al revés."

> Un banco de ensamblaje mecánico con dos bandejas de piezas: una con engranajes de bronce y
> otra con tornillos plateados, y un brazo robótico articulado suspendido sobre ambas
> bandejas como decidiendo por cuál empezar. KatIA observa desde un panel de control lateral
> con indicadores analógicos (agujas, no dígitos).
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Enteros — "La suma conmuta con negativos"** (cuadrado ~1:1) — de `statement`:
"En el banco de ensamblaje, aun con una pieza de peso negativo en la báscula, el orden de la
suma no cambia el total."

> Una báscula de banco mecánica con dos ranuras de carga, una recibiendo una pieza de
> contrapeso marcada con un símbolo de "menos" grabado (sin número) y la otra vacía, con dos
> brazos robóticos gemelos listos para insertar las piezas en cualquier orden. Fiel de la
> báscula en posición neutra, sin marcar el resultado.
> Estilo base + aspect ratio 1:1.

---

## M02 — Máquina Asociativa: el Horno de Fundición

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "Tres lingotes distintos
entran al horno de fundición... fundir primero el par de la izquierda... o agrupar al
revés."

> Un horno de fundición retrofuturista con tres lingotes metálicos de distinto tamaño
> dispuestos sobre una cinta de alimentación antes de la boca del horno, con un brazo
> mecánico de agarre suspendido entre el primer par y el tercer lingote, como decidiendo qué
> par fundir primero. Resplandor teal/violeta saliendo de la boca del horno.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Enteros — "La suma asocia con negativos"** (cuadrado ~1:1) — de `statement`:
"En el horno, con un lingote de peso negativo en el trío, reagrupar la fundición no cambia el
total."

> Tres lingotes sobre la cinta de alimentación del horno, uno de ellos marcado con un
> símbolo de "menos" grabado en su superficie (sin número), con líneas de agrupación
> proyectadas por el panel de control mostrando dos formas distintas de agrupar el trío
> (un par distinto marcado cada vez) sin indicar el resultado final de la fundición.
> Estilo base + aspect ratio 1:1.

---

## M03 — Máquina Distributiva: la Cinta Repartidora

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "La cinta repartidora
envía 3 cajas a cada bahía... 6 bahías con piezas pequeñas y 4 con piezas grandes."

> Una cinta transportadora industrial larga con múltiples bahías de descarga numeradas por
> símbolos genéricos (sin cifras), repartiendo cajas idénticas hacia varias bahías a la vez
> mediante compuertas mecánicas. Algunas bahías con piezas pequeñas amontonadas, otras con
> piezas grandes, sin totalizar ninguna cantidad.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Enteros — "Distribuye con un factor negativo"** (cuadrado ~1:1) — de
`statement`: "En la cinta repartidora, un factor negativo se reparte a cada bahía
conservando los signos."

> La cinta repartidora con una compuerta central marcada con un símbolo de "menos" grabado,
> repartiendo simultáneamente hacia dos bahías laterales, cada una recibiendo una pieza
> también marcada con el mismo símbolo de "menos" al caer, mostrando el reparto en pleno
> movimiento, sin marcar el total final en ninguna bahía.
> Estilo base + aspect ratio 1:1.

---

## M04 — Máquina del Elemento Neutro: el Calibre Cero

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "En el calibre de la
fábrica, sumar 0 gramos de ajuste no cambia el peso... multiplicar por 1 vuelta no altera
cuántas unidades produce."

> Un calibre de banco mecánico con una aguja indicadora apuntando al centro exacto de su
> escala (posición "sin ajuste"), junto a una perilla marcada con una sola muesca en el
> punto neutro, y una pieza de metal ya calibrada esperando a un lado sin alteración visible.
> KatIA gira la perilla suavemente sin moverla del centro.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Enteros — "El 0 deja igual a un negativo"** (cuadrado ~1:1) — de `statement`:
"En el calibre, sumar 0 gramos de ajuste a una pieza con peso negativo no la cambia, por
ningún lado."

> Una pieza de metal marcada con un símbolo de "menos" grabado sobre la bandeja del calibre,
> con la aguja del calibre en la posición neutra central (marca de "0" grabada en la propia
> escala, sin más cifras) y una segunda pieza fantasma idéntica superpuesta en transparencia
> sugiriendo que "no cambió", sin mostrar ningún valor numérico de peso.
> Estilo base + aspect ratio 1:1.

---

## M05 — Máquina de Inversos: la Prensa de Contrapesos

**KatiaStorySlot** (columna imagen | copy, ~4:3) — de `katia.body`: "cada ajuste tiene su
contrapeso. Si la prensa añade... presión, la báscula vuelve a cero... dividir una plancha en
raciones iguales, volver a juntarlas reconstruye la plancha entera."

> Una prensa hidráulica retrofuturista con un manómetro de aguja en el centro, un brazo
> aplicando presión desde arriba sobre una plancha metálica dividida en secciones iguales
> marcadas con líneas de corte, y un juego de contrapesos de bronce colgando a un lado listos
> para "deshacer" la presión. La aguja del manómetro en una posición intermedia, no en cero.
> Estilo base + aspect ratio 4:3.

**Ejemplo 1 · Enteros — "Opuesto: descargar la prensa"** (cuadrado ~1:1) — de `statement`:
"En la prensa, el opuesto de 6 kg de presión es −6 kg porque juntos devuelven la báscula al
neutro 0."

> Primer plano del manómetro de la prensa con la aguja inclinada hacia un lado por la
> presión aplicada, y junto a él un contrapeso de bronce marcado con un símbolo de "menos"
> grabado, a punto de colocarse en el brazo opuesto de la prensa. La aguja no debe mostrarse
> ya en la posición neutra — el contrapeso está a punto de aplicarse, no aplicado.
> Estilo base + aspect ratio 1:1.

**Ejemplo 2 · Racionales — "Recíproco: recomponer la plancha"** (cuadrado ~1:1) — de
`statement`: "El recíproco de 4 vueltas de la máquina es 1/4 porque su producto es el neutro
1."

> Una plancha metálica circular dividida en cuatro secciones iguales por líneas de corte
> grabadas, con una sola sección ya separada y levantada por un brazo mecánico, mostrando
> el hueco que deja — sugiriendo la idea de "una parte de cuatro" sin mostrar la plancha ya
> completamente recompuesta ni marcar la fracción con números.
> Estilo base + aspect ratio 1:1.
