# Emails del cabezal · revisión y textos corregidos (19-nov)

## Antes de nada: cuatro cosas que no se pueden mandar así
1. **"Aduanas incluidas" sale dos veces** (email 2 y gracias). Regla de los fundadores del 19-nov: nunca se menciona la aduana ni el origen del envío. Solo "Envío gratis".
2. **La guía "Agua dura: pelo y piel":**
   - Solo se puede regalar si ya existe. El 18-nov no estaba hecha.
   - El título lo cambiamos a **"El agua de tu ducha: pelo y piel"**: "agua dura" junto a un filtro da a entender que quita la cal, y el filtro no ablanda el agua.
   - "Cuándo cambiar el filtro" no puede dar un plazo, porque no lo sabemos.
3. **"Filtros de recambio":** no está confirmado que los 5 sean de recambio (uno puede venir montado). Se dice "5 filtros en la caja".
4. **El 10 % del email 3 es una decisión de los fundadores, no del texto:**
   - Tiene que poder sumarse al descuento del pack. Si no, el pack de 2 con el código sale más caro que sin él.
   - Con el 10 % sobre 59,95 €, el margen del pack de 2 baja de unos 29 € a unos 24 €. Sigue dentro de D-009.
   - El código tiene que caducar de verdad a las 48 h (código único de Klaviyo con caducidad).
   - Y ese tiene que ser de verdad el último correo del flujo.
   - Si no se aprueba, el email 3 va sin código (abajo hay versión).

## Revisión email a email
| Email | Sobra o suena a plantilla | Asunto | Objeción sin responder | Para vender más |
|---|---|---|---|---|
| 1 · Carrito 1 h | "Has dejado tu cabezal con filtro a medias y te lo hemos guardado": se alarga y "a medias" suena a regañina | **Lo abriría.** "No es tu champú: es el agua" va contra lo que cree y engancha. Se queda | "¿Qué hace de verdad el filtro?": se responde con "retiene parte del cloro" | Sumar el cepillo y el STOP: hoy solo vende el filtro y le quita valor |
| 2 · Carrito 24 h | "Sabemos lo que se piensa antes de comprar algo así" (relleno). "Sin herramientas raras" depende de si hace falta teflón: con "a mano" y "sin fontanero" basta | **Lo abriría.** Es la duda real. Mejor que el texto previo dé ya la respuesta: "Sí vale: se enrosca a mano…" | "¿Cuántos filtros trae y cuánto duran?". Lo primero se puede decir (5 en la caja); lo segundo, no | Quitar la aduana. Dejar el pack con "menos de 30 € cada uno" |
| 3 · Carrito 48 h | "No queremos darte la lata" está muy visto; mejor "Este es el último correo, prometido". "Cambia el agua": el agua no se cambia; se cambia el cabezal | **Lo abriría:** une el ángulo y la oferta. Se queda | "¿Y si no me convence?" justo en el momento de decidir | Repetir los 14 días con gastos nuestros. Decir que el 10 % vale también en el pack (si se configura así) |
| Gracias | El emoji del regalo y "cuándo cambiar el filtro" (no tenemos el dato) | Es transaccional y se abre igual. Se queda | "¿Gotea? ¿Cómo lo pongo?": se responde con el paso 3 | Quitar la aduana. La guía, solo si existe y con el título nuevo |
| En camino | "Ya queda poco" el día 6 puede ser falso: el plazo es de 6-12 días **laborables**, y el día 6 natural son unos 4 laborables | "Ya queda poco para tu primera ducha con filtro" promete algo que quizá no se cumple. Mejor **"Tu cabezal ya va de camino"** | "¿Dónde está mi pedido?": hay que darle el enlace, no decirle que le llegará | **Que salga cuando se envía el pedido** (evento de pedido enviado en Klaviyo), con el enlace de seguimiento, y no a los 6 días fijos |
| Opinión | "Tu opinión nos ayuda mucho" está muy visto | "¿Qué tal tu cabezal?" vale. Con el nombre se abre más: **"¿Qué tal con tu cabezal, {nombre}?"** | — | **Que salga a los 7 días de la entrega**, no a los 21 del pago: con 6-12 días laborables, algunas lo tendrán desde hace poco. **Consentimiento claro:** "solo la publicamos si nos dices que sí" |

**Mejoras de configuración:**
- **Nombre de respaldo:** si no hay nombre, que ponga "Hola:" y no "Hola, :".
- **Quien compre sale del flujo de carrito** al momento.
- **Personalizar por ángulo:** si Klaviyo guarda en el perfil la UTM del anuncio (utm_content = champu, tinte o piel), el email 1 puede llevar solo el párrafo de su ángulo. Comprobad si la guarda; mientras no, los tres ángulos juntos, como ahora.

## Textos corregidos, listos para pegar

### FLUJO 1 · CARRITO ABANDONADO

**EMAIL 1 (1 hora después)**
```
Asunto: No es tu champú: es el agua
Texto previo: Tu cabezal con filtro te espera en el carrito.
Titular: Lo que el agua le hace a tu pelo

Hola, {nombre}:

Te hemos guardado el cabezal en el carrito.

Si te suena alguna de estas, no es casualidad:
- Pagas las mechas y a las tres semanas el color ya está apagado.
- Cambias de champú y de mascarilla, y el pelo sigue igual.
- Sales de la ducha y la piel te tira, por mucha crema que te pongas.

No es el bote: es el agua. El cloro del agua se come tu color y te reseca la piel.

Este cabezal lleva un filtro en el mango que retiene parte del cloro, para que caiga menos sobre tu pelo y tu piel en cada ducha. Y además:
- un cepillo de silicona para masajearte mientras te lavas;
- un botón STOP para pausar el agua sin tocar el grifo.

¿Alguna duda? Responde a este correo y te contestamos.

— El equipo de Trebolly

[Bloque con el producto del carrito] [Botón: Terminar mi pedido]
```

**EMAIL 2 (24 horas después)**
```
Asunto: ¿Y si no vale para tu ducha?
Texto previo: Sí vale: se enrosca a mano en tu manguera de siempre.
Titular: Las dos dudas de casi todo el mundo

Hola, {nombre}:

«¿Me valdrá para mi ducha?» Sí: se enrosca a mano en la manguera estándar, la de siempre. Sin fontanero.

«¿Y si es otro invento de Instagram?» Entonces no te arriesgas:
- tienes 14 días para devolverlo, con los gastos de nuestra cuenta;
- si llega dañado, te mandamos otro;
- y si no te llega en 15 días laborables, te devolvemos el dinero.

Envío gratis con seguimiento. Llega en 6-12 días laborables.

Cada cabezal trae 5 filtros en la caja. Y si en casa hay más de un baño, el pack de 2 (2 cabezales y 10 filtros) sale a 59,95 €: menos de 30 € cada uno.

— El equipo de Trebolly

[Bloque con el producto del carrito] [Botón: Volver a mi carrito]
```

**EMAIL 3 (48 horas después), con el 10 %** (solo si los fundadores lo aprueban y está configurado)
```
Asunto: Antes de comprar otro bote: un 10 % para ti
Texto previo: Es el último correo. Tu código vale 48 horas.
Titular: Esta vez, cambia de cabezal

Hola, {nombre}:

Este es el último correo, prometido.

Piensa en todo lo que llevas gastado en champús, mascarillas, tintes y cremas. Esta vez no cambies de bote: cambia de cabezal.

Te dejamos un 10 % para terminar tu pedido, también en el pack de 2:
{CÓDIGO}
Vale 48 horas y una sola vez.

Y si no te convence, tienes 14 días para devolverlo, con los gastos de nuestra cuenta.

— El equipo de Trebolly

[Bloque con el producto del carrito] [Botón: Usar mi 10 %]
```

**EMAIL 3, sin descuento** (si no se aprueba el 10 %)
```
Asunto: Antes de comprar otro bote, mira esto
Texto previo: Es el último correo, prometido.
Titular: Esta vez, cambia de cabezal

Hola, {nombre}:

Este es el último correo, prometido.

Piensa en todo lo que llevas gastado en champús, mascarillas, tintes y cremas. Esta vez no cambies de bote: cambia de cabezal.

Filtro en el mango, cepillo de silicona y botón STOP. Envío gratis, y 14 días para devolverlo con los gastos de nuestra cuenta si no te convence.

— El equipo de Trebolly

[Bloque con el producto del carrito] [Botón: Terminar mi pedido]
```

### FLUJO 2 · GRACIAS TRAS LA COMPRA (30 minutos después de pagar)
```
Asunto: Gracias, {nombre}: tu pedido ya está en marcha
Texto previo: Qué pasa ahora y cuándo te llega.
Titular: Has dejado de culpar al champú

Hola, {nombre}:

Gracias por confiar en Trebolly. Has hecho lo que poca gente hace: mirar el agua en lugar de comprar otro bote. Ya estamos preparando tu pedido.

Qué pasa ahora
1. En cuanto sale, te mandamos el número de seguimiento por correo.
2. Llega en 6-12 días laborables. Si no te llega en 15 días laborables, te devolvemos el dinero.
3. Cuando llegue, desenrosca tu cabezal y enrosca el nuevo a mano. Los filtros vienen en la caja.

[SOLO SI LA GUÍA YA EXISTE]
Tu regalo: la guía «El agua de tu ducha: pelo y piel»
Qué hace el filtro (y qué no), cómo ponerlo y una rutina para cuidar el pelo, el color y la piel.
[Botón: Descarga tu guía]
[FIN DEL BLOQUE DE LA GUÍA]

Si necesitas cualquier cosa, responde a este mismo correo.

— El equipo de Trebolly
```
Si hay guía, el texto previo pasa a ser: "Qué pasa ahora, cuándo te llega y tu guía de regalo."

### FLUJO 3 · PEDIDO EN CAMINO (cuando el pedido se envía, con el enlace de seguimiento)
```
Asunto: Tu cabezal ya va de camino
Texto previo: Aquí tienes el seguimiento.
Titular: Ya ha salido

Hola, {nombre}:

Tu pedido ya va de camino. Puedes seguirlo aquí:
[Botón: Seguir mi pedido]

Llega en 6-12 días laborables desde que lo pediste. Y si no te llega en 15 días laborables, te devolvemos el dinero.

Cuando lo tengas: desenrosca tu cabezal, enrosca el nuevo a mano y listo.

¿No te funciona el enlace o tienes cualquier duda? Responde a este correo y lo miramos.

— El equipo de Trebolly
```

### FLUJO 4 · PEDIR OPINIÓN (7 días después de la entrega; si Klaviyo no sabe cuándo se entregó, 25 días después de pagar)
```
Asunto: ¿Qué tal con tu cabezal, {nombre}?
Texto previo: Dos minutos y nos ayudas muchísimo.
Titular: Cuéntanos qué has notado

Hola, {nombre}:

Ya llevas unos días con tu cabezal. ¿Qué tal? Cuéntanos qué has notado: en tu pelo, en tu color o en tu piel al salir de la ducha. Lo bueno y lo que no tanto.

Responde a este correo con tu opinión y, si quieres, una foto. Lo leemos todo.

Solo la publicaremos en la tienda si nos dices que sí, y con tu nombre de pila.

Y si algo no ha ido bien, dínoslo y lo arreglamos.

— El equipo de Trebolly
```
