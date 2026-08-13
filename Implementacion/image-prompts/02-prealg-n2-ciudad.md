# Prompts de imagen — N2 · La Ciudad de las Operaciones

**Reemplaza a `n2-mercado.md`.** El nivel dejó de ser un mercado de puestos: son SEIS
EDIFICIOS con nombre propio, y se entra a uno por nodo. El arte actual
(`frontend/public/leccion/02-prealg-n2-mercado/*-v4.png`) muestra puestos de tela y
mostradores — hay que regenerarlo. Los nombres de archivo se conservan para no romper las
rutas del contenido.

| Nodo | Edificio | Oficio · qué se ve dentro |
|---|---|---|
| E01 Suma | **El Granero Público** | dos pisos de sacos, balanza de suelo, tablilla de entradas y salidas junto a la puerta |
| E02 Resta | **La Casa de Cuentas** | salón con arcas, muro de tablillas atravesado por una línea grabada (el cero) |
| E03 Multiplicación | **El Taller de Mosaicos** | mesas largas, cajones de teselas por color, bodega al fondo |
| E04 División | **El Comedor Comunal** | mesas corridas, caldero grande, cucharón, hogazas cortadas |
| E05 Potenciación | **El Invernadero** | techo de vidrio, bandejas de germinación en filas, registro colgado en la puerta |
| E06 Radicación | **La Cantera** | tajo de piedra a cielo abierto, poleas, cinceles, plomada colgando |

**Vocabulario visual del nivel:** arquitectura civil griega de uso diario — muros de
sillería, dinteles de madera, puertas de doble hoja, patios interiores, escaleras de
servicio, poleas, herramienta de oficio. **Cero vocabulario de mercado**: nada de puestos,
toldos de tela, mercaderes tras un mostrador ni cestas de fruta expuestas. Cada edificio se
debe reconocer por su OFICIO, no por un cartel con el símbolo de la operación.

**Línea gráfica obligatoria (`Implementacion/image-prompts/referencias/`):** usar como referencia directa
`step-naturales.png`, `step-enteros.png`, `step-racionales.png`, `step-reales.png`,
`escalera-conjuntos.png`, `katia-primer-plano-enteros.png` y `caso-enteros-recta.jpg`.
Antes de generar, abrir/adjuntar esas imágenes como referencias visuales si la herramienta lo
permite; si no, copiar completa esta línea gráfica dentro del prompt final.

**Estilo base:** `pixel-art educativo refinado, estilo 16/32-bit narrativo de alta calidad,
con clusters de píxeles visibles, bordes pixelados limpios, sombreado por bloques y dithering
sutil; NO pintura digital hiperrealista. Mantener el lenguaje visual de los assets existentes:
KatIA legible en primer/medio plano, escena contenida, pocos personajes secundarios, objetos
pedagógicos claros sobre mesa/suelo/banco de trabajo, sombras azul noche, luz dorada de
lámpara, piedra cálida, acentos teal pequeños en el ocular de KatIA y en instrumentos
mecánicos. KatIA debe conservar identidad: gata blanca con mancha naranja/negra en la cabeza,
ojo verde visible, ocular mecánico teal, pata/brazo mecánico, túnica morada y ornamentos
dorados. El espacio debe leerse como el INTERIOR de un edificio de oficio de una ciudad
griega; si aparece arquitectura de fondo, es secundaria.`

**Personajes secundarios:** cualquier rol mencionado (escriba, contador, aprendiz, cantero,
jardinero, cocinero, cliente) se representa como animal antropomórfico. Preferencia: gatos
bípedos con túnicas o delantales griegos, pelajes variados (atigrado, negro, gris, calicó,
siamés, naranja, blanco moteado) y texturas diferenciadas. No humanos realistas.

**Escaleras y peldaños:** si aparece una escalera o peldaño, va completamente limpio: sin
símbolos, letras, números, runas, marcas, medallones, flechas ni relieves matemáticos.

**Negativos de estilo:** no panorámica turística, no mercado ni puestos, no multitudes, no
plaza pública como foco, no pintura digital lisa, no neón saturado, no sci-fi duro, no
anime/chibi, no humanos realistas, no cambiar a KatIA por una gata totalmente metálica.

**Regla dura:** cada prompt describe la SITUACIÓN, nunca la SOLUCIÓN. Ningún prompt muestra
el resultado numérico de un ejercicio, ni una cantidad de objetos organizada de forma que se
pueda contar y resolver el ejercicio mirando la imagen.

---

## E00 — Hub: La Ciudad de las Operaciones

`e00-hub-mercado-v4.png` → regenerar como **ciudad de edificios** (mantener nombre de archivo).

**Header de nivel** (`.level-presentation-header` + `.level-presentation-media`, ancho
completo, 16:9).

> Calle en pendiente de una ciudad griega al atardecer, vista contenida a media distancia:
> a ambos lados se levantan seis edificios de piedra distintos entre sí, reconocibles por su
> oficio y no por carteles — un granero de dos pisos con compuerta alta y poleas; una casa de
> cuentas con puerta de doble hoja y ventana enrejada; un taller con mesas visibles por el
> vano y cajones de teselas de colores; un comedor con puertas abiertas de par en par y humo
> saliendo por un respiradero; un invernadero de techo de vidrio empañado; y al fondo, donde
> la calle se abre, el tajo de una cantera con una polea recortada contra el cielo. KatIA en
> primer plano sobre el empedrado, de medio cuerpo, señalando calle arriba como invitando a
> recorrerla. Ningún puesto de mercado, ninguna tela colgada, nadie vendiendo.

**Rompehielos** (mantener `e00-ice1-ladrillos-v4.png`, `e00-ice2-tejas-v4.png`,
`e00-ice3-puestos-v4.png`): son escenas de obra en la calle, previas a entrar a cualquier
edificio. El tercero (`ice3`) debe dejar de mostrar «puestos de la plaza» y pasar a mostrar
**los portones de los seis edificios, unos abiertos y otros cerrados**.

---

## E01 — El Granero Público

`e01-suma-katia-v4.png` — apertura.

> Interior del Granero Público de noche: nave alta de sillería con sacos apilados en dos
> niveles, una rampa de madera, una balanza de suelo con platillos grandes y, junto a la
> puerta, una tablilla de cera colgada de un clavo con dos columnas marcadas a cuchillo.
> KatIA en medio plano junto a la tablilla, con el brazo mecánico apoyado en ella; a un lado,
> un gato escriba de túnica gris con punzón, mirando la tablilla con duda. Una carreta
> descargando al fondo, apenas sugerida. Lámpara de aceite colgante como única luz cálida.
> No mostrar cantidades contables de sacos.

`e01-higos-reunidos-v4.png` → renombrar mentalmente a **«grano que entra»**: primer plano de
la rampa del granero con sacos entrando, sin que se puedan contar.

`e01-deuda-pago-v4.png` → **«el saco que sale»**: la misma rampa, un saco saliendo por la
compuerta y la mano mecánica de KatIA marcando el signo contrario en la tablilla.

---

## E02 — La Casa de Cuentas

`e02-resta-katia-v4.png` — apertura.

> Interior de la Casa de Cuentas: salón estrecho de piedra con dos arcas de hierro al fondo y
> una pared cubierta de tablillas colgadas, atravesada de lado a lado por una LÍNEA HORIZONTAL
> grabada en el muro. Algunas tablillas cuelgan por encima de la línea, otras por debajo. Un
> gato contador anciano, atigrado, de túnica oscura, se niega a colgar una tablilla por debajo
> y la sostiene en el aire; frente al mostrador, un gato cliente joven con una bolsa pequeña.
> KatIA en primer plano lateral, observando la línea del muro. Lámpara de aceite, sombras
> azules. La línea del cero debe ser el elemento gráfico más legible de la escena. Sin números
> escritos en las tablillas.

`e02-ceramica-vendida-v4.png` → **«el pago que sube»**: detalle de una tablilla pasando de
debajo a encima de la línea.

`e02-dracmas-deuda-v4.png` → **«la tablilla que cuelga debajo»**: detalle de una sola tablilla
colgada bajo la línea grabada, con la sombra alargada.

---

## E03 — El Taller de Mosaicos

`e03-multiplicacion-katia-v4.png` — apertura.

> Interior del Taller de Mosaicos: mesas largas de trabajo con teselas de piedra dispuestas en
> filas y columnas incompletas, cajones abiertos separando teselas por color, y al fondo la
> boca de una bodega con estanterías. Un gato aprendiz de delantal bajando a la bodega con una
> cesta vacía; el maestro, un gato calicó mayor, midiendo un mosaico grande con una plantilla.
> KatIA en medio plano junto a la mesa, con la pata mecánica sobre una plantilla de reducción
> a media escala. Luz de lámpara rasante que hace brillar las teselas. Las filas de teselas
> deben verse incompletas o parcialmente tapadas para que no se puedan contar.

`e03-filas-tinajas-v4.png` → **«el mosaico por filas»**: detalle en picado de un mosaico
parcialmente armado, con parte cubierta por un paño.

`e03-deuda-repetida-v4.png` → **«las teselas rotas»**: montoncito de teselas partidas junto al
cincel, al borde de la mesa.

---

## E04 — El Comedor Comunal

`e04-division-katia-v4.png` — apertura.

> Interior del Comedor Comunal en plena noche de servicio: mesas corridas de madera, bancos
> largos, un caldero grande humeante sobre el fuego al fondo y un cucharón colgado. Sobre la
> mesa del frente, hogazas de pan, algunas enteras y otras cortadas por la mitad con un
> cuchillo apoyado al lado. Un gato cocinero de delantal indicando que corten; un gato ayudante
> joven con cara de alarma sosteniendo una pizarra pequeña. KatIA en medio plano junto a las
> hogazas, con la pata mecánica sobre una de las mitades. Vapor, luz cálida del fuego, sombras
> azul noche. No mostrar un número contable de hogazas ni de comensales.

`e04-reparto-exacto-v4.png` → **«raciones iguales»**: detalle de una mesa donde las porciones
se ven equivalentes, sin que se puedan contar.

`e04-reparto-residuo-v4.png` → **«lo que sobra también se reparte»**: detalle de una hogaza
suelta junto al cuchillo, a medio partir, con manos alrededor.

---

## E05 — El Invernadero

`e05-potenciacion-katia-v4.png` — apertura.

> Interior del Invernadero: nave de techo de vidrio empañado sostenido por vigas de madera,
> bandejas de germinación en filas sobre bancos de piedra, regadera de cobre y un registro de
> madera colgado junto a la puerta con muescas talladas. Los esquejes de las bandejas del
> fondo desbordan claramente sus bandejas y se han salido al suelo, mientras los del primer
> plano aún caben — la escena debe hacer sentir el desborde sin que se puedan contar. Un gato
> jardinero de delantal manchado mirando el desborde con las orejas gachas. KatIA en medio
> plano junto al registro de la puerta. Luz de luna filtrada por el vidrio más una lámpara
> cálida.

`e05-crecimiento-niveles-v4.png` → **«dos bandejas, dos crecimientos»**: dos bancos
contiguos, uno con esquejes uniformemente espaciados y otro desbordado, sin cifras.

`e05-exponente-negativo-v4.png` → **«el registro hacia atrás»**: detalle del registro de
madera con muescas que se van haciendo más pequeñas hacia la izquierda.

---

## E06 — La Cantera

`e06-radicacion-katia-v4.png` — apertura.

> La Cantera a cielo abierto al anochecer: un tajo de piedra clara con escalones de corte,
> una polea de madera con cuerda tensada, cinceles y mazos apoyados en una repisa de roca, y
> una plomada colgando quieta en primer plano. En el suelo, dos losas cuadradas de distinto
> tamaño ya cortadas y una tercera losa mal cortada apartada a un lado, con el canto astillado.
> Un gato cantero fornido, de pelaje gris, mirando la losa fallida con el mazo bajado. KatIA en
> medio plano junto a la plomada, con la pata mecánica sujetando una cuerda tendida en
> diagonal sobre una losa. Cielo azul profundo, luz de antorcha cálida. Las losas no deben
> llevar medidas ni marcas numéricas.

`e06-cuadrado-perfecto-v4.png` → **«la losa que encaja»**: detalle cenital de una losa
cuadrada asentada en su hueco.

`e06-raiz-no-entera-v4.png` → **«la diagonal con la cuerda»**: detalle de una cuerda tendida
en diagonal sobre una losa cuadrada, mostrando que la diagonal no coincide con ninguna marca
de la regla apoyada al lado.
