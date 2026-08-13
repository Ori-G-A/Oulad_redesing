# Prompts de imagen — ALG-N2 y ALG-N3 · Bagdad, la Casa de la Sabiduría

Cierra el hueco de arte de los dos niveles nuevos de Álgebra. **No existe ni un PNG de
Bagdad en `frontend/public/`:** las nueve salas renderizan hoy el marcador «Imagen de KatIA
aquí».

**9 imágenes obligatorias** (una apertura de KatIA por sala) y **9 opcionales** (la tarjeta
de trampa de cada nodo). **No hay imagen de hub:** ni N2 ni N3 tienen nodo hub — P01
encadena directamente tras `ALG-N1-R04-VARIACION` y G01 tras `ALG-N2-P04-TERMINO-COMUN`.

Destino: `frontend/public/algebra/generated/n2-troqueles/` y `…/n3-caravana/`.

---

## Continuidad con Kemet

Mismo mundo, misma KatIA, tercer sitio. Grecia (ágora, ciudad, fábrica, puerto) → Kemet
(las cuatro casas) → **Bagdad, siglo IX**. KatIA ha seguido la ruta de la caravana. La línea
gráfica NO cambia: cambian la arquitectura, la luz y los materiales.

**Línea gráfica obligatoria (`Implementacion/image-prompts/referencias/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `escalera-conjuntos.png`,
`katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`. Antes de generar, adjuntarlas
como referencias visuales si la herramienta lo permite; si no, copiar completa la línea
gráfica dentro del prompt final.

**Estilo base (copiar tal cual en cada prompt):**

`pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad, con clusters de
píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering sutil; NO
pintura digital hiperrealista ni ilustración lisa. Mantener el lenguaje visual de los assets
existentes: KatIA legible en primer/medio plano, escena contenida, pocos personajes
secundarios, objetos pedagógicos claros sobre mesa/banco/mostrador, sombras azul noche, luz
cálida de lámpara de aceite, acentos teal pequeños en el ocular de KatIA y en instrumentos
mecánicos. KatIA conserva identidad: gata blanca con mancha naranja/negra en la cabeza, ojo
verde visible, ocular mecánico teal, pata/brazo mecánico, túnica morada y ornamentos
dorados. El espacio debe leerse como el INTERIOR de un edificio abasí del siglo IX —ladrillo
cocido y estuco tallado, arcos apuntados, nichos hornacinados, celosías de madera torneada,
alfombras de lana, alacenas de papel y pergamino, lámparas de bronce colgadas—, con la
arquitectura de fondo siempre secundaria.`

**Bloque canónico de KatIA (obligatorio siempre que aparezca):** usar
`katia-primer-plano-enteros.png` como referencia de IDENTIDAD, no solo de estilo. Gata cyborg
adulta, serena y socrática, no mascota infantil: rostro blanco de hocico adulto redondeado,
expresión tranquila y observadora, ojo verde almendrado visible, mancha naranja/negra
asimétrica en frente y oreja, ocular mecánico teal con placas grises sobre el otro ojo,
pata/brazo mecánico segmentado, túnica griega morada con ornamentos dorados. Si el encuadre
aprieta, simplificar el entorno antes que a KatIA.

**KatIA sigue siendo forastera.** Mantiene la túnica griega morada: no se la viste de abasí,
no lleva turbante. Es la única figura del cuadro que no pertenece al sitio, y eso debe
notarse un poco — igual que en Kemet.

**Personajes secundarios:** todo rol mencionado (aprendiz, mozo, tonelero, arriero) es
**animal antropomórfico**, preferentemente gatos bípedos con túnica corta de lino, delantal
de cuero o chaleco acolchado; pelajes variados (atigrado, negro, gris, calicó, siamés,
naranja, blanco moteado). Los dos guías tienen aspecto estable entre sus salas:

| Guía | Nivel | Aspecto |
|---|---|---|
| **Rayhana** | La sala de los troqueles (N2) | gata siamesa de porte recto, mandil de cuero con quemaduras de fragua, manguitos de lino, punzón tras la oreja |
| **Salim** | El almacén de la caravana (N3) | gato naranja robusto y mayor, chaleco acolchado de viaje, manojo de llaves al cinto, cálamo y tablilla de albaranes bajo el brazo |

**Escritura árabe:** permitida como textura ambiental en frisos, lomos y estuco, **nunca
legible ni protagonista**, y nunca sobre la superficie donde ocurre la acción pedagógica (la
lámina, el albarán de trabajo, la mesa de despiece). Nada de cartuchos con el nombre del
nodo. Ningún texto legible en ningún idioma, en ninguna imagen.

**Negativos de estilo:** no postal orientalista (nada de alfombras voladoras, lámparas
mágicas, genios, harenes, bazar de cuento), no panorámica turística de cúpulas al atardecer,
no minarete como protagonista, no caligrafía religiosa ni escena de culto, no camellos al
atardecer, no realeza ni califa, no multitudes, no pintura digital lisa, no render suavizado,
no neón saturado, no sci-fi duro, no anime/chibi, no humanos realistas, no convertir a KatIA
en gata totalmente metálica.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ninguna imagen muestra
el resultado del ejercicio ni una cantidad de objetos dispuesta de forma que se pueda
resolver contando en la imagen. Cuando el relato trata de un error ya cometido se muestra
**la consecuencia** (la lámina con el borde sin estampar, el cuño atascado, el bloque hueco,
el precinto roto), nunca la cuenta correcta.

**Paleta por nivel** (dominante + acento; el morado de KatIA se mantiene en los dos):

| Nivel | Dominante | Acento |
|---|---|---|
| N2 · La sala de los troqueles | cobre y ladrillo cocido | verde cardenillo |
| N3 · El almacén de la caravana | índigo y lana cruda | ámbar de lámpara |

---

# ALG-N2 · La sala de los troqueles — Rayhana · cobre y ladrillo

Un taller de estampación dentro de la Casa de la Sabiduría. Las cuatro salas comparten
espacio y luz de fragua, pero **no comparten vocabulario**: matriz/lámina/orla (P01) ·
cuño/cenefa/greca (P02) · molde/capa/arcilla (P03) · bandeja/casilla/pareja (P04). No mezclar
los carriles entre imágenes.

## P01 · La matriz cuadrada
`p01-cuadrado-katia.png` · **4:3**

> Interior de un taller de estampación en penumbra cálida. Sobre un banco de madera gruesa
> descansan varias planchas de cobre cuadradas de distinto tamaño, apiladas con separadores
> de fieltro. Una gata siamesa de porte recto con mandil de cuero quemado (Rayhana) sostiene
> en alto una lámina de cobre recién estampada y la inclina hacia la luz: el relieve llega
> nítido en el centro pero **una franja del borde quedó lisa, sin estampar**, con la marca
> del troquel cortada a media orla. KatIA, de pie al otro lado del banco, mira la franja sin
> tocarla. Al fondo, una prensa de husillo de hierro y la boca de una fragua con brasas
> bajas. Luz naranja de brasa desde la derecha, sombra azul fría en el resto. Ningún número
> ni letra visible en ninguna parte; las láminas no llevan cuadrícula ni marcas contables.

## P02 · El cuño de la cenefa
`p02-conjugados-katia.png` · **4:3**

> Mesa larga de estampación de cenefas: tiras de cobre estrechas y largas extendidas a lo
> ancho del plano, sujetas por listones. Rayhana está inclinada sobre un cuño alargado que
> **se ha quedado atascado a medio recorrido**, torcido en su guía, con un pegote de tinta
> negra desbordado por un lado de la tira y la greca interrumpida por el otro. Un trapo
> manchado y un pote de tinta volcado junto al codo. KatIA se agacha a la altura de la mesa
> para mirar el cuño de lado, con el ocular teal encendido. Al fondo, un panel de celosía de
> madera torneada filtra la luz de la calle en franjas. La greca del cobre es ornamental y
> geométrica, sin signos ni cifras.

## P03 · El molde de tres capas
`p03-cubo-katia.png` · **4:3**

> Rincón de moldeo al fondo del taller, más oscuro y más húmedo. Sobre una losa hay moldes
> altos de barro cocido, abiertos en dos valvas, y un montón de arcilla cubierto con un paño
> mojado. Un aprendiz gato atigrado sostiene con las dos manos un bloque cúbico recién
> desmoldado que **se ha partido y deja ver que está hueco por dentro**, con las paredes
> finas y el interior vacío. Rayhana señala el hueco sin regañar. KatIA, en primer plano
> lateral, observa el corte del bloque. Suelo de ladrillo, salpicaduras de barro, una lámpara
> de bronce colgada arriba a la izquierda. Nada escrito, ningún molde numerado.

## P04 · La bandeja de parejas
`p04-termino-comun-katia.png` · **4:3**

> Última mesa de la sala, más ordenada que las anteriores. Sobre ella, bandejas de madera
> compartimentadas en casillas rectangulares, del tipo de las cajas de tipos móviles. Un
> juego de fichas de cobre idénticas espera en un cuenco. Rayhana sostiene un registro de
> tapas de cuero abierto y mira la bandeja con el ceño de quien acaba de descubrir un
> descuadre; **una franja entera de casillas quedó vacía** mientras el resto está llena.
> KatIA está enfrente, apoyando una mano en el borde de la bandeja. Al fondo, estanterías con
> más bandejas apiladas y, muy secundaria, la prensa del principio de la sala. Las fichas del
> cuenco están amontonadas sin orden, imposibles de contar; las casillas vacías no forman una
> figura que se pueda leer como cantidad.

---

# ALG-N3 · El almacén de la caravana — Salim · índigo y lana

El otro extremo del edificio: donde en los troqueles se estampaba, aquí se abre. Almacén de
caravana con báscula en la puerta, catálogo de calcos, banco de despiece, bodega abajo y sala
de expedición a la salida. Carriles de vocabulario: fardo/báscula/albarán (G01) ·
huella/calco/catálogo (G02) · despiece/listón/muesca (G03) · tonel/duela/aro (G04) ·
guía de carga/precinto/remesa (G05).

## G01 · El pesaje de entrada
`g01-factor-comun-katia.png` · **4:3**

> Puerta interior de un almacén de caravana, vista desde dentro. Una romana de brazo cuelga
> del dintel y un mostrador de madera desgastada cruza el plano. Sobre el mostrador, **un
> fardo de arpillera ya abierto y a medio desatar**, con la cuerda todavía enredada y los
> bultos de dentro asomando sin separar del todo. Un gato naranja robusto y mayor, con
> chaleco acolchado de viaje y llaves al cinto (Salim), sostiene una tablilla de albaranes
> con una anotación tachada, visiblemente ilegible. KatIA está junto al fardo, con una mano
> sobre la arpillera abierta. Al fondo, más fardos apilados contra un muro de ladrillo y el
> hueco luminoso del patio. Ninguna cifra legible en la tablilla ni en las etiquetas de los
> fardos; los bultos del interior están medio ocultos y no se pueden contar.

## G02 · El cotejo de huellas
`g02-cuadrados-katia.png` · **4:3**

> Sala estrecha de cotejo, con luz de lámpara sobre una única mesa. En la pared, un panel con
> calcos colgados de cordeles: hojas de papel con impresiones en relieve de troqueles, todas
> distintas y ninguna legible. Sobre la mesa, un catálogo grueso abierto por la mitad y, al
> lado, **un fardo llegado cerrado que alguien abrió a la fuerza**: la arpillera rasgada, el
> lacre roto en dos mitades. Salim tiene un dedo apoyado en una hoja del catálogo y la mirada
> en el fardo roto. KatIA sostiene un calco a contraluz, comparándolo con el panel. **Un
> hueco vacío entre dos hojas colgadas del cordel**, con el cordel a la vista y sin hoja.
> Índigo dominante, ámbar de lámpara sobre la mesa. Ninguna huella del panel es un símbolo,
> letra ni número: son texturas de relieve geométrico.

## G03 · La mesa de despiece
`g03-trinomio-katia.png` · **4:3**

> Banco de trabajo largo al fondo del almacén, con una hilera de muescas talladas en el canto
> para comprobar medidas. Sobre el banco, **dos listones de madera ya cortados que no entran
> en la muesca**: uno queda corto y el otro sobresale, apoyados en falso sobre el borde. Junto
> a ellos, una sierra de arco y un montón de virutas. Un mozo gato calicó se ha quedado
> mirando el listón que sobresale, con las orejas hacia atrás. Salim, detrás, no interviene.
> KatIA se ha agachado a la altura del canto del banco para mirar la muesca de perfil. Luz
> lateral fría desde un ventanuco alto, ámbar de lámpara sobre el banco. Ninguna medida
> escrita, ninguna regla graduada legible, ningún listón marcado con cifras.

## G04 · La bodega de los toneles
`g04-cubos-katia.png` · **4:3**

> Bodega abovedada bajo el almacén, ladrillo desnudo y aire frío. Toneles de madera con aros
> de hierro descansan en durmientes a media altura. Salim baja los últimos peldaños con una
> lámpara de aceite en alto, y el círculo de luz cae sobre **un tonel al que le sobra líquido:
> un reguero oscuro corre por la duela y encharca el suelo bajo la boca mal ajustada**. En la
> pared, una anotación a tiza tachada y emborronada, ilegible. KatIA está junto al tonel que
> gotea, mirando hacia arriba a la boca. Al fondo, la bóveda se pierde en azul oscuro. Los
> toneles del fondo están en penumbra y no forman una fila contable; ninguna marca de la
> pared es un número legible.

## G05 · La sala de expedición
`g05-expedicion-katia.png` · **4:3**

> Sala de salida del almacén, con el portón entreabierto al patio de carga y luz de tarde
> entrando en diagonal. Sobre un mostrador alto, una guía de carga de papel con un sello de
> lacre, y al lado **un precinto ya roto**: el lacre partido y la cuerda cortada sobre la
> mesa. Detrás, una remesa de bultos preparada para salir, con **un bulto suelto a un lado
> que quedó fuera del atado**. Salim mira el precinto roto con las manos apoyadas en el
> mostrador. KatIA está de espaldas al portón, con la vista en el bulto suelto. Al fondo del
> patio, muy secundarias y sin detalle, dos rutas distintas saliendo del recinto. La guía de
> carga está escrita con trazos ilegibles; los bultos están apilados de forma irregular y no
> se pueden contar.

---

# Opcionales · las nueve trampas

Mismo estilo, formato **1:1**, para la tarjeta de trampa (`worked_examples` con `trap: True`).
Todas muestran a un aprendiz o mozo **en el momento anterior a darse cuenta**, nunca la
corrección. Ninguna lleva números ni fórmulas visibles.

| Archivo | Escena |
|---|---|
| `p01-trampa-orla.png` | Un aprendiz gato deja dos piezas de cobre pequeñas sobre el banco y se retira, satisfecho, dejando el resto del banco vacío. |
| `p02-trampa-suma.png` | Un aprendiz aprieta el cuño con las dos manos sobre una tira que ya está torcida en la guía. |
| `p03-trampa-capas.png` | Un aprendiz cierra las dos valvas de un molde alto habiendo echado arcilla solo en el fondo y en la tapa. |
| `p04-trampa-fila.png` | Un aprendiz sella una bandeja con una franja de casillas todavía vacía, sin mirarla. |
| `g01-trampa-albaran.png` | Un mozo firma un albarán con el fardo aún medio atado detrás de él. |
| `g02-trampa-catalogo.png` | Un mozo saja la arpillera de un fardo con el catálogo cerrado bajo el codo. |
| `g03-trampa-corte.png` | Un mozo apoya la sierra tras cortar, con los dos listones sobre el banco y la muesca a la vista, sin haberlos probado. |
| `g04-trampa-arqueo.png` | Un mozo tapa un tonel dando por bueno el arqueo, con la vara de medir todavía apoyada en la pared. |
| `g05-trampa-precinto.png` | Un mozo estampa el lacre en la guía con un bulto suelto visible al fondo de la sala. |

---

## Checklist antes de aceptar una imagen

1. ¿KatIA se reconoce como la misma de `katia-primer-plano-enteros.png` y sigue con túnica morada griega?
2. ¿El espacio se lee como interior abasí y **no** como postal orientalista?
3. ¿Hay algún texto, cifra o símbolo legible? Si sí, se rechaza.
4. ¿Se puede resolver el ejercicio contando objetos de la imagen? Si sí, se rechaza.
5. ¿La escena muestra la **consecuencia** del error y no la cuenta correcta?
6. ¿El vocabulario visual pisa el carril de otra sala (una cenefa en P01, un tonel en G03)? Si sí, se rechaza.
