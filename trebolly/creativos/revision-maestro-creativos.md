# Revisión del PROMPT MAESTRO de creativos del cabezal (18-nov)
**Mentores, de las notas del proyecto:**
- Marc: [YOgCnLtNgHE] (duración, cortes, palabras del público) y [MwbtxthKR_I] (vídeo con IA).
- Dani: [4sk8JrKfT3M] (creativos con IA a partir de la foto del producto), [nnXqHmYlmvA] (72 h por creativo y un solo avatar), [s1hMMVWgf00] (variar un solo elemento) y [n5gORsrA_xc] (segmentar por creativo).
- Adrián, con su invitado Raúl: [fUnHXOfbVcI] (un dolor por anuncio) y [egP7kkfO0rY] (anuncios de imagen).

Los prompts corregidos, completos y listos para pegar, están en `prompts-flow-v2.md`. Los ha generado el script `montar_v2.py`, así que los bloques son iguales letra por letra en todos.

## El fallo más grave: el producto está mal descrito
- El bloque de la v1 dice "**thin chrome rim**" (un aro cromado fino en la cara), y la lista de revisión pide "aro cromado fino".
- En todas las fotos que hemos revisado (M, B, Q, las tres de "Así funciona" y los packs) el producto es así:
  - el cromado es un **collar en el mango**, donde está el botón STOP;
  - la cabeza es un **cilindro profundo**;
  - la cara está **hundida**, con un plato gris plata, un disco central oscuro con agujeros y una corona de **conos negros** de silicona;
  - el mango **se desenrosca por abajo** y dentro va un cartucho **blanco con tapa azul**.
- Es el mismo error que ya corregimos el 17-18 de noviembre.
- Con la v1, la IA pondrá un aro cromado en la cara, y cada clip fallará la lista de revisión: créditos tirados.
- **Antes de gastar un crédito, comparar el bloque nuevo con la foto 3 de CJ. Si la foto dice otra cosa, manda la foto.**

## 1) Apartados 1-9
| Apartado | Veredicto | Por qué |
|---|---|---|
| 1 Lo que ya vende | **SÍ** | El análisis es bueno: los rivales llevan meses activos con vídeo vertical, en un baño real, montándolo y usándolo. "Respuesta a un comentario" no, porque sería inventado: de acuerdo. |
| 2 Reglas | **CAMBIADO** | En la lista de revisión, "aro cromado fino" pasa a "collar cromado en el mango con un botón STOP, cabeza cilíndrica y conos negros". Se añade: "sin hombros ni espalda desnudos" y "el pelo, igual en todos los clips". |
| 3 Biblia | **CAMBIADO** | Cinco cambios: el bloque del producto (arriba); la cámara, que pasa de "filmed by a family member" al móvil apoyado en la balda; la física del agua, solo donde hay agua; el sonido, sin radio; y el encuadre seguro en la ducha. |
| 4 Voz | **SÍ** | Voz en off de España con subtítulos. Elegirla de acento castellano, porque muchas voces por defecto son latinoamericanas. |
| 5 Banco de clips | **CAMBIADO** | Se cambian B01, B02, B03, B06, B09, B10, B11 y B12, y se añade un retrato F00 para crear el personaje (ver el apartado 3). |
| 6 Anuncios | **CAMBIADO** | Los guiones no caben en el tiempo, el gancho de piel choca con Meta, hay un antes y después escondido, y lo que va en cada conjunto no cuadra con lo acordado (apartados 2 y 4). |
| 7 Estáticos | **CAMBIADO** | El formato "foto real + una frase" sí vale. Pero en E3 el producto sale desenfocado: en 3 s no se entiende qué se vende. |
| 8 Fotos de la tienda | **CAMBIADO** | Falta la foto del ángulo principal (champú) en la galería: F08 va en el puesto 3. F03, con el pelo neutro. F07, en albornoz y con el producto enfocado. |
| 9 Producción | **CAMBIADO** | Hay que cambiar el orden: primero F01 (el ancla del producto) y F00 (la cara). Los planos de producto, mejor animando fotos ya aprobadas que generándolos desde cero. |

## 2) Las 8 preguntas
**1. Duración: 30 s, más 15 s de reserva.**
- Marc no baja de 20 s (la mayoría de los vídeos que analiza rondan los 44 s) y descarta los de 6-12 s [YOgCnLtNgHE].
- Los rivales duran 45 s o más, pero son personas reales hablando a cámara. Con clips de IA, cada plano extra es un riesgo más de que se note.
- 30 s es el equilibrio. Si gana un ángulo, se prueba una versión de 45 s.
- **Ojo:** el apartado 9 mete en cada conjunto el vídeo de 30 s, el corte de 15 s y el estático. Acordamos **un anuncio por conjunto** (curso de Adrián: "un vídeo por conjunto"; ver el cierre de `tienda-creativos-extras.md`). Con 10 €/día, tres anuncios se reparten el gasto, Meta se lo da casi todo a uno, y además mezclar vídeo con estático compara formatos, no ángulos. Entonces:
  - En cada conjunto, solo el vídeo de 30 s, en 9:16 y 4:5.
  - El corte de 15 s y el estático, de reserva.

**2. Una sola protagonista: SÍ.** Dani: un solo avatar, y todos los creativos para esa persona [nnXqHmYlmvA]. Además hace que todo parezca la misma marca.
- Falta una cosa: **F03 la muestra de espaldas, y con eso no se puede crear un personaje.** Hace falta un retrato de frente (F00, nuevo), que no se publica.

**3. Banco de clips:**
- **No hace falta un plano de "uno para cada baño":** B12 basta, y cada clip extra es un riesgo más.
- **Cambios:**
  - B01 lleva nuestro cabezal en el soporte: así el producto se ve desde el primer segundo, y se usa para champú y para piel.
  - B03 y B11, en albornoz.
  - B10, en el antebrazo.
  - B09, enjabonándose el pelo.
  - B06, con la foto 8 de CJ como segunda referencia (el filtro).
  - B12 y B13, animando las fotos F02 y F01 ya aprobadas.

**4. Guiones:** reescritos en el apartado 4.
- **No caben en el tiempo.** El de champú tiene unas 90 palabras en 30 s, y el tramo de 9 a 13 s mete 21 palabras en 4 s (5 por segundo). A 2,5 palabras por segundo caben unas 70.
- **Primer gancho de cada ángulo:**
  - Champú: la voz "Champú nuevo, mascarilla nueva… y el pelo igual", con el texto "Tu champú no tiene la culpa".
  - Tinte: "90 € de mechas… y a las pocas semanas, apagadas".
  - Piel: "Llevas años cambiando de gel. Prueba a filtrar el agua".
- Los otros ganchos, de reserva: se cambia solo el gancho tras 72 h (Dani [s1hMMVWgf00]).

**5. Estáticos:**
- Sí a "foto real + una frase". Adrián prueba anuncios de imagen [egP7kkfO0rY].
- Dani usa un círculo o una flecha que señala el producto para que quede claro qué se vende [4sk8JrKfT3M]. Yo exigiría al menos que el producto salga nítido y grande en cada estático (E3 no lo cumple).
- No tengo ningún dato de qué estático funciona hoy en España en este nicho. Los rivales van casi todo en vídeo, así que los estáticos, de reserva.

**6. Riesgos con Meta:**
- **"Sales de la ducha y la piel te tira"** afirma algo físico de quien lo ve. Ya acordamos cambiarlo y sigue en el gancho A y en el guion: fuera.
- **"El cloro del agua te reseca la piel"** tiene el mismo problema. En general: "El cloro del agua reseca la piel, ducha tras ducha".
- **"Tus mechas" y "tu color"** no son atributos personales protegidos: valen.
- **"La ducha que deja de resecarte la piel"** (la promesa aprobada) tiene un riesgo medio por el "te". Con una cuenta nueva, mejor "Menos cloro sobre la piel en cada ducha" en el anuncio, y la promesa fuerte en la ficha.
- **El riesgo mayor que no estaba en la lista es la desnudez insinuada.** La toalla, el "bare shoulder" (B10) y el "soapy shoulder" (B09), con una cuenta nueva, pueden tumbar el anuncio. Se resuelve con encuadre cerrado en la cabeza y el pelo, albornoz cerrado y antebrazo.
- **Antes y después escondido:** B02 ("ends look dull and dry") seguido de F03 o B07 ("bright and healthy") es un antes y después fabricado (regla 4). El pelo, igual en todo.

**7. Voz: ElevenLabs.** Es lo que más delata un anuncio barato.
- Comprobar que el plan permite uso comercial.
- Elegir una voz de España, no latinoamericana.
- En esta sesión está conectado ElevenLabs: si los fundadores dan el sí, puedo generar aquí las 6 locuciones con sus créditos.

**8. Lo que se había pasado por alto:**
1. **El bloque del producto** (arriba).
2. **B06 sin la foto del filtro:** F05 usa las fotos 3 y 8 de CJ, pero B06 solo la 3. Así la IA se inventa el cartucho.
3. **"Opened in two parts"** puede salir abierto a lo largo, como una almeja. El mango se desenrosca por abajo: ahora lo dice el prompt.
4. **Contar 10 filtros.** La IA cuenta mal y "10 filtros" es una promesa. Animar la foto F02 ya aprobada (donde ya se han contado 10) en vez de generar B12 desde cero.
5. **La radio** puede meter voces o palabras inventadas que chocan con la voz en off. Fuera; la música con licencia se pone en el montaje (la biblioteca de sonidos de Meta es gratis para anuncios).
6. **El STOP "stops completely"** promete que corta del todo, y eso no está confirmado. Ahora "se para y caen unas gotas", que vale en los dos casos.
7. **El orden:** F01 primero. Si el producto no sale idéntico en una foto, no saldrá en vídeo, y la foto es gratis.
8. **Comprobar que Veo 3.1 Lite acepta referencias y fotograma inicial.** Si no los acepta, el producto no saldrá fiel y conviene el modelo que sí lo haga, aunque cueste más créditos por clip.
9. **Las palabras del público.** Marc saca los ganchos de las palabras que usa la gente en los vídeos y comentarios del nicho [YOgCnLtNgHE]. Antes de cerrar los guiones, leer los comentarios de los anuncios de Aquapure y Oasis y apuntar las expresiones que se repiten (por ejemplo, cómo llaman al pelo apagado o a la cal), para usarlas en los ganchos de reserva.

## 3) Los 22 prompts, uno por uno
Todos cambian por el bloque del producto, la cámara, el sonido y la física. Lo específico de cada uno:
| Prompt | ¿Cabezal distinto? | ¿Físicamente raro? | ¿Delata IA o choca con reglas? | Cambio |
|---|---|---|---|---|
| B01 | — | La frase del agua sin agua en el plano | El producto no sale en los primeros 3 s | Nuestro cabezal en el soporte, enfocado; botes con etiquetas en blanco y también geles (sirve para piel) |
| B02 | — | — | "Dull and dry" es el "antes" de un antes y después | Pelo neutro, encuadre cerrado |
| B03 | — | — | La toalla, desnudez insinuada | Albornoz cerrado, encuadre de pecho arriba |
| B04 | — | — | — | Solo la cámara y el sonido |
| B05 | El aro cromado | — | — | El extremo con rosca, visible |
| B06 | El aro cromado y sin foto del filtro | "Opened in two parts" | — | Fotos 3 y 8; el mango se desenrosca por abajo; cartucho con tapa azul |
| B07 | El aro cromado | — | — | Encuadre cerrado en la cabeza |
| B08 | El aro cromado | — | — | Conos negros, encuadre cerrado |
| B09 | El aro cromado | — | El hombro enjabonado; "stops completely" | Se enjabona el pelo; "caen unas gotas" |
| B10 | El aro cromado | — | El hombro desnudo | El antebrazo y la mano |
| B11 | — | "Picks up a second towel" no aporta | La toalla | Albornoz; se toca las puntas |
| B12 | El aro cromado | Contar 10 | — | Animar F02 (B12-alt, por si no se puede) |
| B13 | El aro cromado | — | — | Mejor animando F01 |
| F00 | — | — | — | **Nueva:** retrato de frente para el personaje |
| F01 | El aro cromado | Un cabezal flotando que echa agua sin manguera | — | Una mano lo sostiene y la manguera queda fuera de plano |
| F02 | El aro cromado | Contar 10 | — | "Exactly ten… two rows of five", tapas azules |
| F03 | El aro cromado | — | "Bright and healthy" es el "después" | Pelo neutro, encuadre cerrado |
| F04 | El aro cromado | — | — | Conos negros |
| F05 | El aro cromado | "Opened in two parts" | — | El mango se desenrosca por abajo |
| F06 | El aro cromado | — | Espuma en el hombro | La espuma, en el pelo |
| F07 | El aro cromado | — | Toalla; producto desenfocado (E3) | Albornoz; producto en la mano, enfocado |
| F08 | El aro cromado | — | — | Etiquetas en blanco; pasa a la galería en el puesto 3 |

Los textos completos están en `prompts-flow-v2.md`. Se han alargado unos 500 caracteres por el bloque del producto: si Flow los corta, se acorta la escena, nunca el bloque del producto.

## 4) Guiones de voz (a unas 2,5 palabras por segundo, castellano de España)
**Champú, 30 s** (unas 68 palabras)
| s | Plano | Voz | Texto en pantalla |
|---|---|---|---|
| 0-3 | B01 | Champú nuevo, mascarilla nueva… y el pelo igual. | Tu champú no tiene la culpa. |
| 3-6 | B07 | ¿Y si el problema es el agua? | Mira el agua |
| 6-9 | B04 → B05 | Quitas tu cabezal y enroscas este. A mano. | Se enrosca a mano |
| 9-13 | B06 | Lleva un filtro en el mango que retiene parte del cloro. | Filtro en el mango |
| 13-17 | B08 | El cepillo de silicona te masajea mientras te lavas. | Cepillo de silicona |
| 17-20 | B09 | Y con el STOP pausas el agua. | Botón STOP |
| 20-24 | B11 | Mismo champú. Agua con menos cloro. | — |
| 24-30 | B12 + tarjeta | Dos cabezales y diez filtros, 59,95 €. Envío gratis. | Tarjeta |

**Tinte, 30 s** (unas 63 palabras)
| s | Plano | Voz | Texto en pantalla |
|---|---|---|---|
| 0-6 | B02 | Noventa euros de mechas… y a las pocas semanas, apagadas. | 90 € de mechas… y a las pocas semanas, apagadas. |
| 6-9 | B13 | El cloro del agua se come tu color. | El cloro del agua se come tu color |
| 9-12 | B04 → B05 | Cambia el cabezal: se enrosca a mano. | Se enrosca a mano |
| 12-16 | B06 | Su filtro en el mango retiene parte del cloro. | Filtro en el mango |
| 16-20 | B07 | Menos cloro sobre tu color, en cada ducha. | Menos cloro sobre tu color |
| 20-23 | B08 | Y el cepillo te masajea mientras te lavas. | Cepillo de silicona |
| 23-25 | B11 | (respiro) | — |
| 25-30 | B12 + tarjeta | Dos cabezales y diez filtros, 59,95 €. Envío gratis. | Tarjeta |

**Piel, 30 s** (unas 64 palabras)
| s | Plano | Voz | Texto en pantalla |
|---|---|---|---|
| 0-3 | B01 (con geles) | Llevas años cambiando de gel… | Llevas años cambiando de gel. |
| 3-6 | B03 | Prueba a filtrar el agua. | Prueba a filtrar el agua |
| 6-9 | B13 | El cloro del agua reseca la piel, ducha tras ducha. | El cloro reseca la piel |
| 9-12 | B04 → B05 | Cambias el cabezal. Se enrosca a mano. | Se enrosca a mano |
| 12-16 | B06 | Su filtro en el mango retiene parte del cloro. | Filtro en el mango |
| 16-20 | B10 | Menos cloro sobre la piel, cada día. | Menos cloro sobre la piel |
| 20-24 | B09 | Y con el STOP pausas el agua mientras te enjabonas. | Botón STOP |
| 24-25 | B11 | (respiro) | — |
| 25-30 | B12 + tarjeta | Dos cabezales y diez filtros, 59,95 €. Envío gratis. | Tarjeta |

**Cortes de 15 s** (de reserva):
- Champú: "Champú nuevo, mascarilla nueva… y el pelo igual. ¿Y si es el agua? Este cabezal lleva un filtro en el mango. Dos por 59,95 €, envío gratis."
- Tinte: "Noventa euros de mechas… y a las pocas semanas, apagadas. El cloro del agua se come tu color. Filtro en el mango. Dos por 59,95 €, envío gratis."
- Piel: "Llevas años cambiando de gel. Prueba a filtrar el agua. Filtro en el mango, cepillo y botón STOP. Dos por 59,95 €, envío gratis."

**Por qué estos cambios en los textos:**
- "Y tu champú, por fin, hace su trabajo" promete un resultado. "Mismo champú. Agua con menos cloro" vende lo mismo sin prometerlo y repite el gancho.
- "Te gastas un dineral en mechas" pasa a "Noventa euros de mechas", que es más concreto y más corto.
- "Prueba a cambiar el agua" no tiene sentido: el agua no se cambia, se filtra.
- En cada guion hay una idea por plano, y el precio se dice igual en los tres. Así solo cambia el ángulo (Dani [s1hMMVWgf00]).

## 5) Lo que falta para que vendan más que los de los rivales
1. **El producto en los 3 primeros segundos** en los tres vídeos (B01 cambiado, B02 seguido de un golpe a B13 si hace falta). Sin sonido, en 3 s tiene que entenderse qué se vende.
2. **El primer fotograma con el gancho ya escrito.** Es la miniatura en el feed.
3. **Música con licencia** debajo de la voz, en volumen bajo. La biblioteca de sonidos de Meta es gratis para anuncios.
4. **Cambio de plano cada 3 s como mucho** (Marc [YOgCnLtNgHE]). En los guiones no hay tramos de más de 4 s.
5. **Leer el abandono por segundo** cuando haya datos (Marc [YOgCnLtNgHE]): donde se cae la gente, se cambia ese plano y solo ese.
6. **La misma tarjeta final y la misma oferta** en los tres: así se compara el ángulo y no la oferta.
7. **La etiqueta de IA al publicar.** Bien que esté en la regla 5. Marc propone lo contrario [MwbtxthKR_I], y no lo seguimos.
8. **Galería:** F08 (el ángulo principal) en el puesto 3, y el clip B05 + B08 + B09 en bucle en el puesto 2 cuando exista.

**Orden de producción propuesto:**
1. F01 (el producto).
2. F00 (la cara) y crear el personaje.
3. F02 y F05, comprobando a mano que hay 10 filtros y que el mango está bien.
4. B13 animando F01, como prueba de fidelidad en vídeo.
5. B06.
6. B09.
7. El resto, de uno en uno.
8. Las voces.
9. El montaje.
10. Los estáticos.
11. La galería, con el sí de los fundadores.
