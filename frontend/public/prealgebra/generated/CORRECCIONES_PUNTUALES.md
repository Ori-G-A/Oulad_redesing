# Correcciones puntuales - imagenes de Prealgebra

Ruta base: `frontend/public/prealgebra/generated`

Usa este archivo cuando las correcciones sean pequenas y especificas.
No llenes una ficha por cada imagen: registra solo las imagenes que realmente vas a corregir.

## Como usarlo

1. Escoge la imagen en el catalogo compacto.
2. Agrega una fila en `Correcciones activas`.
3. Copia el bloque minimo a la sesion de generacion.
4. Genera solo esa imagen.
5. Marca la fila como `Aprobada` cuando quede lista.

## Correcciones activas

| Estado | Imagen | Version destino | Cambio puntual | Mantener | No hacer |
|---|---|---|---|---|---|
| Aprobada | n3-fabrica: m00-hub-fabrica-v5.png, m01-conmutativa-katia-canon-v10.png, m02-asociativa-katia-canon-v10.png, m03-distributiva-katia-canon-v10.png, m04-elemento-neutro-katia-canon-v10.png, m05-inversos-katia-canon-v10.png | v5 / canon-v10 | Se descarto regenerar a KatIA desde prompt libre. Se usaron fondos nuevos sin personaje y composicion con `frontend/public/prealgebra/katia-canon-sprite-hard.png` para conservar la identidad original. | Composicion pedagogica, maquinas de fabrica, paleta nocturna bronce/morado/teal, objetos de cada escena. | No volver a usar las v4 como referencia de personaje; no chibi/kawaii/gatita bebe; no suavizar a pintura digital; no cambiar tunica ni ocular. |
| Aprobada | n4-puerto: c00-hub-puerto-katia-canon-v10.png, c01-divisibilidad-katia-canon-v10.png, c02-multiplos-katia-canon-v10.png, c03-primos-katia-canon-v10.png, c04-factorizacion-katia-canon-v10.png, c05-mcd-katia-canon-v10.png, c06-mcm-katia-canon-v10.png | canon-v10 | Se descarto regenerar a KatIA desde prompt libre. Se usaron fondos nuevos sin personaje y composicion con `frontend/public/prealgebra/katia-canon-sprite-hard.png` para conservar la identidad original. | Composicion pedagogica, puerto griego cercano, cargamento/rutas/tablillas, paleta nocturna farol/morado/teal. | No volver a usar las v4 como referencia de personaje; no chibi/kawaii/gatita bebe; no suavizar a pintura digital; no hacer puerto turistico ni panorama epico. |

## Bloque minimo para pegar

```text
Imagen:
Version destino:

Cambio puntual:

Mantener:

No hacer:
```

## Prompt de control

```text
Trabaja solo la imagen indicada.
No redisenes el set completo.
No cambies imagenes ya aprobadas.
Aplica unicamente el cambio puntual descrito.
Genera una sola version nueva con el nombre indicado en Version destino.
```

## Cambios globales aprobados

Usar solo cuando una decision aplique a varias imagenes.

| Alcance | Decision | Excepciones |
|---|---|---|
| N3/N4 con KatIA | Las v4 quedan rechazadas como referencia de identidad de KatIA. La solucion aprobada para las escenas con KatIA es generar fondos sin personaje y componer encima el sprite canonico `frontend/public/prealgebra/katia-canon-sprite-hard.png`. | Las v4 pueden usarse solo como referencia aproximada de composicion/entorno, nunca de rostro, proporcion corporal o acabado de KatIA. |

## Catalogo compacto

### n1-agora

```text
b01-bienvenida-v4.png
b02-pregunta-detonadora-v4.png
b03-escalera-necesidad-v4.png
b04-naturales-v4.png
b05-enteros-v2.png
b05-enteros-v4.png
b06-racionales-v4.png
b07-irracionales-v4.png
b08-reales-v4.png
b09-complejos-v4.png
b10-clasificador-i-v4.png
b11-clasificador-ii-v4.png
b12-detective-falsedades-v4.png
b13-diagnostico-v4.png
```

### n2-mercado

```text
e00-hub-mercado-v4.png
e00-ice1-ladrillos-v4.png
e00-ice2-tejas-v4.png
e00-ice3-puestos-v4.png
e01-deuda-pago-v4.png
e01-higos-reunidos-v4.png
e01-suma-katia-v4.png
e02-ceramica-vendida-v4.png
e02-dracmas-deuda-v4.png
e02-resta-katia-v4.png
e03-deuda-repetida-v4.png
e03-filas-tinajas-v4.png
e03-multiplicacion-katia-v4.png
e04-division-katia-v4.png
e04-reparto-exacto-v4.png
e04-reparto-residuo-v4.png
e05-crecimiento-niveles-v4.png
e05-exponente-negativo-v4.png
e05-potenciacion-katia-v4.png
e06-cuadrado-perfecto-v4.png
e06-radicacion-katia-v4.png
e06-raiz-no-entera-v4.png
```

### n3-fabrica

```text
m00-hub-fabrica-v4.png
m00-ice1-balanza-bloques-v4.png
m00-ice2-balanzas-orden-v4.png
m00-ice3-retirar-pieza-v4.png
m01-conmutativa-katia-v4.png
m01-suma-conmuta-negativos-v4.png
m02-asociativa-katia-v4.png
m02-suma-asocia-negativos-v4.png
m03-distributiva-katia-v4.png
m03-distribuye-factor-negativo-v4.png
m04-cero-deja-negativo-v4.png
m04-elemento-neutro-katia-v4.png
m05-inversos-katia-v4.png
m05-opuesto-descargar-prensa-v4.png
m05-reciproco-recomponer-plancha-v4.png
```

### n4-puerto

```text
c00-hub-puerto-v4.png
c00-ice1-naranjas-reparto-v4.png
c00-ice2-postes-primos-v4.png
c00-ice3-carretas-tela-v4.png
c01-canicas-amigos-v4.png
c01-divisibilidad-katia-v4.png
c01-entradas-feria-v4.png
c02-corredor-completo-v4.png
c02-multiplos-katia-v4.png
c03-compuesto-vecinos-v4.png
c03-contar-divisores-v4.png
c03-primos-katia-v4.png
c04-cadena-larga-v4.png
c04-division-sucesiva-v4.png
c04-factorizacion-katia-v4.png
c05-mcd-factores-comunes-v4.png
c05-mcd-katia-v4.png
c06-mcm-factores-v4.png
c06-mcm-katia-v4.png
```
