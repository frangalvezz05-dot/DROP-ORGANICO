# El abandono en el pago y los textos de la ronda 2 (viernes 20-nov, noche)
**Marcas:** [CÁLCULO] · [EXPERIENCIA] criterio propio · [NO SEGURO].

## Lo que cambia con los datos nuevos
- **21 visitas reales de los anuncios:** piel 10, champú 7, tinte 4.
- **Piel: 2 de 10 llegan al pago (20 %) con ~17,5 € → ~8,7 € por pago iniciado.** Está en ámbar: verde ≤ 7 € y rojo > 10 € [CÁLCULO].
- **El fallo está en la primera pantalla del pago, no en el anuncio.**
- **La regla del lunes ya se cumple:** «≥ 2 carritos reales» ya lo tiene piel. Hay que cambiarla para que cuente solo lo que pase desde el sábado (ver «Lunes»).
- **Con n = 2, todo lo que sigue son hipótesis ordenadas, no certezas.**

## 1) Por qué se van en la primera pantalla del pago (de más a menos probable) [EXPERIENCIA]
1. **«Quiero probarlo» no dice «pagar».**
   - Suena a prueba o a muestra, y lleva directamente a un formulario de pago de 59,95 €.
   - Quien quería «ver» se encuentra pagando y se va.
2. **Sorpresa con el total.** El pack de 2 viene marcado; si no se dieron cuenta, esperaban 39,95 € y ven 59,95 €.
3. **Falta PayPal.** En España, con una tienda que no conocen, mucha gente busca PayPal por la protección al comprador (y Bizum, todavía no).
4. **Desconfianza en una tienda nueva justo cuando hay que dar la tarjeta.** El pago de Shopify, sin logo ni colores, parece otra web.
5. **Lentitud del pago dentro del navegador de Instagram.**
6. **El plazo de entrega:** poco probable en esta pantalla, porque el envío solo aparece después de escribir la dirección.

## 2) Qué comprobar desde el móvil y qué cambiar
**Comprobar (desde el anuncio, en el navegador de Instagram, en un iPhone y en un Android):**
- **Cuánto tarda en abrirse el pago.**
- **Qué botones de pago rápido salen.** Apple Pay y Google Pay pueden no salir dentro de Instagram [NO SEGURO]; si no salen, PayPal pesa más.
- **El resumen del pedido:**
  - que se lea «Pack de 2 cabezales + 10 filtros · 59,95 €»;
  - que salga la línea «6 filtros de regalo · 0,00 €»;
  - y la foto.
- **Que estén los enlaces a las políticas** (devoluciones, privacidad, condiciones) y que la moneda y el idioma sean los correctos.
- **Al escribir una dirección:** que el envío diga «Envío gratis (6-12 días laborables)» y nada de «internacional» ni del origen.

**Cambiar:**
1. **PayPal activado** si la cuenta está lista.
   - Cuesta ~0,5-1,7 € más por pedido de pack de 2 (comisión de PayPal y, quizá, la de Shopify por pasarela externa) [NO SEGURO: miradlo en Ajustes → Pagos].
   - El margen sigue por encima de 20 €.
2. **El pago con la marca:** logo, color de los botones (el ámbar) y fondo, en el editor del pago.
3. **Que el contacto siga siendo el email.** Sin el email no hay pago abandonado que recuperar.
4. **La casilla del código de descuento:** Marc la quita [Dh__yIvnEUM] porque manda a la gente a buscar códigos.
   - En el plan Basic creo que no se puede ocultar [NO SEGURO].
   - Que al menos el pop-up del 10 % siga en borrador, para no animar a buscarlos.

## 3) «Quiero probarlo», ¿directo al pago o al carrito lateral? Al carrito lateral, con otro nombre
- **Un solo botón:** «Comprar · 59,95 €». El precio cambia con el pack elegido.
- **Que abra el carrito lateral, donde se ve:**
  - «Pack de 2 + 6 filtros de regalo · 59,95 €»;
  - la garantía de entrega y la protección incluida (el pago de Shopify Basic no deja ponerlas);
  - el botón «Finalizar compra» y los de pago rápido.
- **Por qué:**
  1. ve el total y el regalo antes del formulario: sin sorpresa;
  2. se quita la duda de «probarlo»;
  3. con 1 cabezal, sigue saliendo la tarjeta para subir al pack de 2;
  4. son 2 botones menos, y una decisión menos (Marc [hkVPQYlIz_0]).
- **Condición:** que el carrito se abra en menos de 1 s.
  - El script del regalo tiene que comprobar si queda stock al cargar la ficha, no al pulsar el botón.
  - O que el carrito se abra al momento y el regalo se compruebe después.

## 4) Cómo recuperar a quien se va sin dejar el email
- **Campaña de retargeting: no.**
  - Meta necesita un público de al menos ~100 personas para mostrar anuncios [EXPERIENCIA], y hay 2.
  - Además, partir 15 €/día lo debilita.
  - El público Advantage+ ya incluye a quien ha interactuado.
- **Captar el email antes del pago, sin descuento:** pop-up de Klaviyo a los 15-20 s o a mitad de la ficha.
  - «¿Te guardamos el regalo? Déjanos tu email y te avisamos antes de que se acaben los 15 regalos.» Es verdad, porque el stock existe.
  - Con este tráfico rendirá poco, pero cuesta casi nada.
- **Lo que más rinde: que no se vayan** (puntos 1-3), no recuperarlos después.

## 5) El plan, con cambios
**Esta noche:**
1. Apagar champú y tinte.
2. Activar PayPal.
3. Renombrar el botón («Comprar · 59,95 €») y que abra el carrito lateral.
4. Arreglar los 3 s (el script del regalo).
5. Marca en el pago (logo y colores).
6. Probar desde Instagram en iPhone y Android.
7. El pop-up sin descuento es opcional.

**Sábado 07:00:**
- piel a 15 €/día y tope de la campaña a ~110 €;
- los 2 anuncios nuevos dentro de piel (textos abajo);
- mirad cuántos regalos quedan (deben ser 15).

**Lunes 23 por la noche, con lo que pase desde el sábado:**
- **≥ 1 venta, o ≥ 2 pagos iniciados nuevos con email** (los que salen como abandonados en Shopify) → pausa del 24 al 30 y vuelta el 1-2 de diciembre con los ~95 € que quedan.
- **0 ventas y 0-1 pagos iniciados con email** → se paran los anuncios, se pasa a orgánico y se decide el producto.
- **Por qué pausar del 24 al 30:** con un CPM de 30-40 € hacen falta 4,5-5,3 compras por cada 100 clics para no perder dinero [CÁLCULO].

## 6) Textos de la ronda 2
**«Filtra el cloro» no va:** sigue sin comprobarse. En su lugar va lo verdadero: «el agua pasa por un filtro en el mango antes de tocar tu piel». Si los fundadores quieren mantener «filtra el cloro», es decisión suya; mi voto es no ponerlo hasta comprobarlo.

**Si se acaban los 15 regalos antes del lunes:** se pausan los anuncios con «solo 15 regalos» el mismo día.

### Anuncio de vídeo (vídeo de piel)
- **Título:** «Pack de 2 · 59,95 € · 6 filtros de regalo»
- **Descripción:** «Solo 15 regalos · Hasta el lunes 23 · Envío gratis»
- **Botón:** «Comprar»
- **Texto principal:**
```
Llevas años cambiando de gel y de crema. ¿Y si es la ducha?

Este cabezal lleva un filtro en el mango: el agua pasa por él antes de tocar tu piel. Y además:
· cepillo de silicona para masajearte mientras te lavas
· botón STOP para pausar el agua mientras te enjabonas
Se enrosca a mano en tu manguera, sin herramientas.

Hasta el lunes 23 a las 23:59: pack de 2 (2 cabezales + 10 filtros) por 59,95 € con 6 filtros de regalo. Solo 15 regalos.
Envío gratis con seguimiento.
```

### Anuncio estático (pack de 2 con los 6 filtros)
- **Texto en la imagen:**
  - «Pack de 2 · 59,95 €»
  - «+6 filtros de regalo»
  - «Hasta el lunes 23 · Solo 15 regalos»
- **Título:** «2 cabezales + 16 filtros · 59,95 €»
- **Descripción:** «29,98 € cada cabezal · Envío gratis»
- **Botón:** «Comprar»
- **Texto principal:**
```
2 cabezales con filtro en el mango, cepillo de silicona y botón STOP: uno para cada baño.

Hasta el lunes 23 a las 23:59: 6 filtros de regalo con el pack de 2. Solo 15 regalos.
Envío gratis con seguimiento · Garantía de entrega: si no llega en 15 días laborables, te devolvemos el dinero.
```
