# Trebolly · Revisión de la lista de montaje del borrador 2 (18-nov)
Mentores citados (de las notas del proyecto):
- Adrián [4JGeKANrv7g]: montar la tienda.
- Raúl, invitado de Adrián [wWC8SoeQ_Fk].
- Marc [Dh__yIvnEUM]: tienda desde cero.
- Marc [oEFWZdCw5FQ]: visitas sin ventas.
- Marc [hkVPQYlIz_0]: revisión de una tienda.
- Marc [kq0bZo65WNM]: navegador interno.
- Dani [rDxEVZSQydI].

## 0) Antes de empezar: qué es del tema y qué es de la tienda
La copia del tema solo aísla lo que vive **dentro del tema**: secciones, textos de las plantillas, colores, letras, franja y portada.

Esto otro es **de la tienda** y lo comparten los dos borradores, además del tema publicado:
- descripción y fotos del producto
- menús
- colecciones
- páginas (su contenido)
- políticas
- descuentos
- envíos
- notificaciones

Consecuencias:
1. **Menús:** crear menús NUEVOS ("Menú cabezal" y "Pie cabezal") y elegirlos en los ajustes del borrador 2. Si se edita el menú actual, cambia también en "Prueba Claude" y en el tema publicado.
2. **Colección:** crear una colección nueva "Cabezal", sin editar la de la nutria.
3. **Textos nuevos de la ficha:** en las secciones de la plantilla (tema), no en la descripción del producto (tienda). Si no, los dos borradores enseñan lo mismo y la comparación no vale.
4. **Páginas:** crear páginas nuevas (Preguntas frecuentes, Contacto, Quiénes somos) en vez de editar las de la nutria.

## 1) Qué falta para que la tienda esté completa
**A. El plazo real: lo más importante.**
- 6-12 días es lo que tarda CJPacket en el transporte. A eso hay que sumar los días que CJ tarda en preparar el pedido, y más si el producto está en "stock de fábrica", es decir, en el proveedor y no en el almacén de CJ.
- La ficha de CJ suele mostrar el tiempo de preparación ("processing time"). Leerlo de ahí; no hace falta preguntar nada.
- Si la preparación es de 1-3 días, del pedido a la entrega van 7-15 días laborables. Entonces:
  - "Llega en 6-12 días" no sería verdad contando desde el pedido.
  - La garantía de 15 días se activaría justo en los envíos más lentos. Cada vez cuesta unos 20 €: se devuelve el dinero y el producto llega igual.
- Opciones (deciden los fundadores):
  - (a) Texto "Preparación en X días y entrega en 6-12 días laborables desde que sale", con la garantía contada desde el pedido y su número ajustado a la suma: 6-12 + X + margen.
  - (b) Contar la garantía desde que sale el pedido.
- Recomiendo la (a): es la más clara para el cliente. En la franja, en los títulos y junto al botón seguirá sin haber días.

**B. Zonas de envío.**
- Se vende solo a la península y Baleares. Pero la zona "España" de Shopify incluye Canarias, Ceuta y Melilla, que están fuera del IVA europeo: la "aduana incluida" no se cumpliría.
- Quitar esas provincias de la zona de envío.
- Añadir la pregunta "¿Enviáis a Canarias, Ceuta o Melilla?" con la respuesta "De momento, solo a la península y Baleares".

**C. Páginas legales y de confianza.** Adrián [4JGeKANrv7g] y Marc [Dh__yIvnEUM] piden políticas rellenadas con tus datos, no genéricas.
- Aviso legal con el titular, NIF, dirección y email.
- Privacidad.
- Cookies, con el aviso de cookies activado. Marc: "es obligatorio" [Dh__yIvnEUM].
- Términos y condiciones, revisando que no hablen de descargas digitales: la nutria llevaba un PDF.
- Contacto: email y tiempo de respuesta.
- "Quiénes somos": corta y real. Adrián menciona "Nuestra historia" [4JGeKANrv7g], y responde a "¿quién está detrás?".
- Todas enlazadas en el pie. El contenido legal lo revisa el asesor.

**D. Aviso de cookies y píxel.** Con el aviso de cookies, quien rechace no envía eventos a Meta, y Meta contará menos compras de las reales. Es un motivo más para leer las ventas en Shopify, como ya acordamos.

**E. Pago (checkout).** Marc [Dh__yIvnEUM] y Dani [rDxEVZSQydI]:
- Logo y botón con el color agua.
- Pocos campos.
- Apple Pay y Google Pay activados en Shopify Payments.
- Idioma español.
- Precios con IVA incluido.
- El teléfono: Marc lo quita y luego lo pide para el proveedor. Comprobar en el pedido de prueba si CJ acepta el pedido sin teléfono; si no, ponerlo obligatorio.

**F. Descuentos.**
- Que solo estén activos los del pack de 2 y el pack de 3, que no se combinen con ningún código y que no quede ninguno de la nutria.
- Probar qué pasa al meter 4 cabezales.

**G. Restos de la nutria fuera del tema.** Buscar "nutria", "7 noches" y "peluche" también en:
- título y descripción de la tienda (Preferencias), que es lo que sale al compartir el enlace por WhatsApp
- imagen para compartir en redes
- nombre y email del remitente de las notificaciones
- blog, si lo hay

Esto no es SEO: es que no salga la nutria al compartir el enlace.

**H. Remitente y dominio del email.** Remitente "Trebolly" y dominio trebolly.com autenticado para enviar emails, en Shopify y en Klaviyo. Si no se autentica, los emails de confirmación y seguimiento llegan peor y pueden ir a spam.

**I. Stock.** La app de CJ puede sincronizar el inventario. Si algo falla y pone 0, la ficha enseña "Agotado". Marc [Dh__yIvnEUM] desactiva el seguimiento de cantidad para evitarlo. Activar "seguir vendiendo sin stock" o comprobar que el número que llega es el real (9.179).

**J. Carrito lateral en vez de página de carrito.** Raúl [wWC8SoeQ_Fk]: es un paso menos. Horizon lo trae de serie.

**K. Logo, favicon y "Tecnología de Shopify".** Logo real y favicon en la paleta. Quitar el enlace "Tecnología de Shopify" del pie (Adrián [4JGeKANrv7g], Marc [Dh__yIvnEUM]).

**L. Navegador de Instagram y Facebook.** Los anuncios abren la tienda en el navegador interno de la app. Marc avisa de que en TikTok el pago falla ahí [kq0bZo65WNM]. Probar en Instagram: mandarse el enlace por mensaje directo, abrirlo y llegar hasta el pago.

**M. WhatsApp.** Si hay un número de empresa, ponerlo en Contacto y en las preguntas frecuentes, pero no como botón flotante: en el móvil tapa el botón fijo de compra.

## 2) Mejoras por punto
**B1 Ficha:**
- Nombres de los packs con lo que incluyen: "1 cabezal + 5 filtros", "2 cabezales + 10 filtros" y "3 cabezales + 15 filtros". Raúl: enseñar lo que trae el paquete sube la conversión [wWC8SoeQ_Fk].
- Tarjeta del pack de 2, como mucho dos líneas: la etiqueta "Recomendado" y "El segundo cabezal, por 20 €". "Sale a 29,98 € cada uno" va en pequeño. "Uno para cada baño" sale de la tarjeta y pasa a las ventajas o a las preguntas. Con cuatro frases en una tarjeta no se lee nada en el móvil. Marc: "el cliente pasa unos 30 segundos", reducir decisiones [hkVPQYlIz_0].
- Pregunta nueva: Canarias, Ceuta y Melilla (punto 1B).
- "¿Cada cuánto se cambia el filtro?" → "Depende del agua de tu zona y de cuánto lo uses. Vienen 5 en cada caja." Sin plazos.
- "¿Quién está detrás?": los mismos datos que el aviso legal.

**B2 Caja de compra.** Hay demasiadas líneas. Orden:
1. Precio.
2. Plazos con Klarna.
3. Packs.
4. Botón.
5. Iconos de pago.
6. Rejilla 2 × 2 con cuatro frases: "Envío gratis con seguimiento", "Garantía de entrega", "14 días para devolverlo" y "Si llega dañado, otro gratis".

"Número de seguimiento por email en cuanto sale" pasa al desplegable de Envío, para no repetir dos líneas de envío. Es el orden de Marc: precio, pago a plazos, selector, botón, desplegables [hkVPQYlIz_0].

**B3 Franja → SÍ, tal cual.**

**B4 Portada → SÍ** (Marc [Dh__yIvnEUM]: portada mínima con un banner al producto). Sin colecciones ni productos destacados de la nutria.

**B5 Colores y letras:**
- Quitar el ámbar de las estrellas: no vamos a enseñar estrellas, y tener el color preparado invita a usarlo.
- Mirar que Fraunces y Bricolage Grotesque están en la biblioteca de fuentes de Shopify. Si alguna no está, usar la más parecida de la biblioteca antes que cargar una fuente externa, porque eso ralentiza la web (Marc [oEFWZdCw5FQ]).
- Adrián dejaría los colores y las letras de serie [4JGeKANrv7g]. Marc elige el color por la psicología del producto, con el azul para la seguridad [Dh__yIvnEUM]. Nuestra paleta encaja con lo que dice Marc.

**B6 Opiniones → SÍ.** Que el producto no tenga puntuación guardada en Shopify, para que Google no enseñe estrellas.

**B7 Menú, pie y colección →** ver el apartado 0: menús y colección nuevos, no editados. En el pie, las páginas legales del punto 1C.

**C8 Pack de 3 → SÍ** (3 × 39,95 = 119,85; 119,85 − 39,90 = 79,95). Afecta a todo, incluido "Prueba Claude": si esa plantilla tiene escrito "84,95 €", hay que corregirla también o la comparación engaña.

**C9 Fotos → SÍ.** La de garantías, en la versión con "Garantía de entrega" y sin días. Las fotos también son de la tienda: las ven los dos borradores.

**C10 Envío →** el nombre del método depende de cómo se resuelva el punto 1A, y además hay que quitar Canarias, Ceuta y Melilla (1B).

**C11 Políticas →** opción (c). Además:
- Explicar cómo se pide la garantía de entrega: desde cuándo se cuenta y cómo se reclama.
- Explicar qué hacer si llega dañado: por ejemplo, "mándanos una foto en las 48 h siguientes a recibirlo". El plazo lo deciden los fundadores.
- Que no quede la ampliación de Navidad ni "14 días por ley el resto del año".

**C12 Emails →** sumar el punto 1H. El email de envío con el número de seguimiento (Dani [rDxEVZSQydI]) sale solo si CJ lo pasa a Shopify (C13).

**C13 CJ →** sumar:
- Inventario: punto 1I.
- Saldo o pago automático para que los pedidos del fin de semana no se queden parados.
- Mirar el tiempo de preparación en la ficha de CJ: punto 1A.

**D14 Comprobar →** sumar:
- Instagram (punto 1L).
- Las plantillas `?view=tinte` y `?view=piel`.
- Precio del pack de 3.
- Qué pasa con 4 unidades.
- Que los enlaces de las políticas salen en el pago.

## 3) Orden de montaje
1. **Fundadores, en paralelo a todo:**
   - Conectar CJ: packs, envío, pago e inventario.
   - Leer el tiempo de preparación en la ficha de CJ.
   - Datos para el aviso legal y el contacto.
   - Número de WhatsApp, si lo hay.
2. **Decisiones (un solo sí):**
   - Cómo se cuenta y se escribe el plazo (1A).
   - Qué hacer si llega dañado (C11).
   - Permiso para duplicar el tema.
3. **Cosas de la tienda que necesitan los dos borradores (un sí aparte):**
   - Zonas de envío y nombre del método.
   - Descuento del pack de 3 y revisión de descuentos.
   - Políticas y páginas legales.
   - Aviso de cookies.
   - Restos de la nutria en preferencias, redes y remitente.
   - Notificaciones y Klaviyo.
   - Dominio del email.
   - Menús, colección y páginas nuevas.
4. **Borrador 2, de lo general a lo concreto:**
   - Colores y letras.
   - Cabecera y pie (con los menús nuevos), franja y carrito lateral.
   - Ficha principal, después las de tinte y piel.
   - Página de preguntas frecuentes.
   - Portada.
5. **Comprobaciones en el móvil:**
   - Dos móviles, con datos (sin wifi).
   - El navegador de Instagram.
   - Precios: pack de 2, pack de 3 y 4 unidades.
   - Botón fijo.
   - Enlaces legales en el pago.
6. **Comparar y elegir** (abajo). Publicar, quitar la contraseña y hacer el pedido de prueba con el evento Compra, aceptando las cookies, solo con el sí de los fundadores.

## 4) Cómo comparar "Prueba Claude" y el borrador 2
- Sin tráfico no hay datos de venta. Una prueba A/B de temas con 30 €/día de anuncios (unas pocas decenas de visitas al día) tardaría semanas. Se elige con una lista igual para los dos, mirada en el mismo móvil.
- **Lo que se ve en la primera pantalla del móvil sin deslizar.** Marc [oEFWZdCw5FQ]: la parte de arriba es la que más pesa. ¿Se ven la foto, el título, el precio, los packs y el botón?
- **Deslizamientos hasta el botón y toques hasta el pago.** Menos es mejor.
- **Velocidad:** Lighthouse de Chrome en modo móvil sobre la vista previa de cada uno (PageSpeed no entra mientras haya contraseña). Comparar cuánto tarda en salir la foto principal.
- **Cumplimiento de lo acordado:**
  - sin días arriba
  - sin "retiene la cal"
  - sin estrellas ni contador
  - packs con lo que incluyen
  - textos del STOP y de la cal
  - ningún resto de la nutria
- **Coherencia con las políticas y los emails:** mismos plazos y mismas garantías en todas partes.
- Ojo: si "Prueba Claude" aún tiene contenido de la nutria, se compara la ESTRUCTURA, no los restos.

## Cierre con la otra IA (18-nov)
**1) Plazo:** se mantienen "6-12 días laborables" y la garantía de 15.
- Datos de la ficha de CJ (leída el 17-nov): preparación de 1-3 días en el 60,2 % de los pedidos; entrega en 4-8 días en el 74 % y en 9-10 días en el 19 %. Todo en días naturales.
- 13 días naturales son unos 9-10 laborables, así que 6-12 laborables desde el pedido se cumple en la mayoría de los casos.
- Riesgo: el producto está en stock de fábrica, y el otro 40 % de los pedidos tarda más en prepararse, sin dato de cuánto.
- Regla: en cada pedido se apuntan la fecha del pedido, la de salida y la de entrega. Si alguno de los primeros pedidos pasa de 12 laborables, se cambia a la opción (a) con el número real.

**2) Canarias, Ceuta y Melilla:** ya estaba resuelto (D-042, desde el 11-nov). Solo falta comprobar en el pedido de prueba que una dirección de Canarias no deja pagar.

**3) Lo que es de la tienda y no del tema:**
- Menús nuevos, páginas nuevas y textos en la plantilla: sí.
- Colección: NO se crea una nueva. La actual, con identificador `pilates-en-casa`, es ya la del cabezal y 10 secciones del tema la usan.
- Añadido: ese identificador sale en la dirección de la colección. Cambiarlo cuando ya se haya elegido el tema definitivo, con redirección, y actualizar esas 10 secciones a la vez.
- Añadido: buscar también "pilates" entre los restos.

**Ya estaba hecho:**
- Aviso de cookies.
- Dominio de email en Klaviyo. Falta mirar el remitente de las notificaciones de Shopify.
- Apple Pay, Google Pay, Klarna y PayPal.
- Producto sin seguimiento de inventario y vendiendo sin stock.
- Políticas base. Faltan los cambios acordados.

**Plan de montaje cerrado.** Se empieza con el sí de los fundadores.
