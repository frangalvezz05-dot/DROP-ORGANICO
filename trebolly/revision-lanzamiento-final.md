# Revisión final antes de lanzar en Meta (noche del 18 al 19-nov)
**Marcas:** [NO SEGURO] = no comprobado · [EXPERIENCIA] = criterio propio, sin fuente · [CÁLCULO] = cuenta con vuestros datos.
Lo legal es del asesor (D-044).

## 1. Bloqueantes (en orden)
1. **Apagar el modo de prueba de Shopify Payments.**
   - Se usó hoy para el pedido #1001 y no está en la lista de pendientes.
   - Si sigue activo, ninguna tarjeta real paga. Se pierden todas las ventas y el dinero de los anuncios.
   - Comprobad que el checkout ya no enseña el aviso de modo de prueba.
2. **Borrar el #1001 en CJ antes de la 01:00.**
   - Visteis su coste en CJ, así que el pedido entró allí.
   - Cancelarlo en Shopify no lo saca de «Pedidos de la tienda» de CJ [NO SEGURO].
   - Con el pago automático de la 01:00, CJ pagaría ~35,62 $ y lo enviaría.
3. **Cuenta publicitaria en EUR y hora de Madrid,** comprobado antes de crear nada.
   - Si estuviera en otra moneda u hora, los presupuestos y los cortes del día no serían los planeados. Arreglarlo no es rápido (Meta crea otra cuenta).
   - Comprobad también, en el portfolio Grupo Verion, que el píxel, la página y @trebolly están asignados a «Verion 1». Si no, el conjunto no deja elegir el píxel o el anuncio sale sin Instagram.
4. **Quitar la contraseña ANTES de pulsar Publicar, no después.**
   - Meta revisa la página de destino. Si tiene contraseña, el anuncio puede salir rechazado o con la página marcada como rota [EXPERIENCIA].
   - Probadlo en incógnito y con datos móviles.
5. **Que los 3 salgan juntos (D-080) con una hora de inicio común programada,** no «en cuanto Meta lo apruebe».
   - Meta revisa cada anuncio por separado: uno puede aprobarse en minutos y otro en horas, y empezarían a destiempo.
   - Hay que poner la misma hora de inicio en los 3 conjuntos, varias horas después de publicar, para que la revisión termine antes.
   - Si el vídeo de piel no está a tiempo, no se publica ninguno (D-080), o deciden los fundadores.

## 2. Falta (no está en vuestra lista)
- **Comprobar los emails de Klaviyo contra D-079.**
  - Los emails 2 y 3 del pago abandonado dicen «14 días para devolverlo, con los gastos de nuestra cuenta». D-079 dice que, si cambia de opinión, la vuelta la paga el cliente.
  - El primero sale 1 h después de abandonar el pago: puede salir esta noche. Cambio: «14 días para devolverlo».
- **Saber qué versión del email 3 está activa.**
  - Si es la del 10 %, el código tiene que existir y poder sumarse al descuento automático del pack.
  - Si no se suma, quien use el código pierde el precio del pack y paga más.
- **Que no quede ningún texto del regalo de Black Friday** en la ficha, en las tarjetas de los packs, en la franja o en los emails. Se lanza sin esa oferta.
- **Que la tarjeta de filtros del carrito no esté activa.**
  - No tiene su desglose en CJ (segunda cuota de aduana y vínculo de cantidad).
  - Si está puesta, se apaga hasta comprobarlo.
- **Las tarjetas finales de los vídeos aprobados (champú y tinte) no pueden decir «aduanas».**
  - El guion de montaje decía «Envío gratis con aduanas» hasta el 19-nov.
  - Mirad el último fotograma de cada vídeo.
- **Vídeo de piel:**
  - que la voz no diga «reseca» (D-073). La frase es «Ducha tras ducha, el cloro del agua cae sobre tu piel»;
  - y que esté decidido lo de «retiene parte del cloro» en la parte 2.
- **Página de Facebook Trebolly:** foto, descripción y enlace a la web. Los anuncios salen con su nombre, y no solo se mira Instagram.
- **Filtro de palabras en los comentarios de Facebook e Instagram** para esta noche: nadie va a moderar hasta mañana.
- **Volver a mirar Probar eventos después de poner el nivel de datos en Máximo** (PageView y AddToCart, 2 min), por si el cambio rompe algo.
- **Saldo de la tarjeta.**
  - Los ingresos de Shopify están en pausa hasta el 20 nov, así que CJ y Meta tiran de la tarjeta.
  - Cada pack de 2 son ~32 € en CJ, y la prueba son 90 € en Meta [CÁLCULO].
  - Si el pago automático de CJ falla por falta de saldo, el pedido no sale y corre el plazo de la garantía de 15 días.
- **Shopify y Klaviyo mandan dos emails de «en camino».** La confirmación de envío de Shopify y el flujo «pedido en camino» de Klaviyo llegarían duplicados: apagad uno.
- **Dropea:**
  - hay una app que marca cada pedido como error la noche del lanzamiento;
  - como mínimo, comprobad que no es la ubicación de envío del cabezal y que no manda emails;
  - mi voto es quitarla. Deciden los fundadores.
- **Bizum:** que no salga en el pago mientras esté en verificación. Si sale y falla, se pierde la venta.
- **No es para esta noche:** autenticar trebolly.com para enviar emails en Shopify y Klaviyo. Un remitente @gmail.com suele llegar peor a la bandeja de entrada [EXPERIENCIA].

## 3. Las primeras 24 h
**Antes de dormir (30-60 min después de publicar)**
- Los 3 anuncios «en revisión», «programados» o «activos», y ninguno rechazado.
- La tienda abierta y el #1001 fuera de CJ.

**Por la mañana, en este orden**
1. **Administrador de anuncios:**
   - estado de los 3 anuncios;
   - gasto e impresiones de cada conjunto;
   - Facturación (cobro bien);
   - Calidad de la cuenta (sin restricciones).
2. **CJ, «Pedidos de la tienda»:**
   - pedidos reales pagados a la 01:00;
   - ninguno retenido o sin vincular;
   - que la etiqueta de Dropea no haya bloqueado nada.
3. **Shopify:**
   - pedidos pagados (y con qué UTM);
   - pagos abandonados (si hay muchos y ninguna compra, mirad que el pago funciona).
4. **Administrador de eventos:** eventos de navegador y de servidor, y el Purchase si hay pedidos.
5. **Klaviyo:** que el email de gracias haya salido para los pedidos reales y que el enlace de la guía funcione.
6. **Comentarios de los anuncios:** moderar.
7. **Métricas del embudo, solo para mirar** (CPM, CTR de enlace, visitas ÷ clics, carritos, hook rate). No se toca nada hasta las 48 h.

**Si un anuncio sale rechazado**
- Leed el motivo en Calidad de la cuenta.
  - Si es el texto, se corrige solo ese anuncio. Cuenta como fallo técnico, y los otros dos no se tocan.
  - Si creéis que es un error de Meta, pedid otra revisión; puede tardar hasta un día [EXPERIENCIA].
- Si el rechazo es por la página de destino: mirad la contraseña, la velocidad y que ?view= funciona.

**Si no se gasta nada (0 impresiones con el anuncio aprobado)**
1. Facturación: el pago ha fallado o la cuenta está retenida.
2. Calidad de la cuenta: hay una restricción.
3. La fecha y hora de inicio de los conjuntos (zona horaria).
4. Que la campaña, los conjuntos y los anuncios estén todos activados.

- Una cuenta nueva puede tardar horas en empezar a gastar [EXPERIENCIA].
- Si a las 12 h de la aprobación sigue en 0 y todo lo anterior está bien, se duplica el conjunto (es un fallo técnico).

**Lo que es normal y no se toca**
- Un conjunto gasta menos que los otros (solapamiento).
- Un día se gasta hasta un 75 % más (hasta 17,50 € en un conjunto).
- 0 compras el primer día.

## 4. Incoherencias
1. **Devoluciones:**
   - D-079 dice que, si cambia de opinión, la vuelta la paga el cliente;
   - los emails 2 y 3 dicen «con los gastos de nuestra cuenta»;
   - la bio de Instagram dice «devolución gratis».
   - Hay que dejarlo todo como en D-079, y también la página de la política y las preguntas frecuentes.
2. **La bio de Instagram dice «desde España sin aduanas».** Rompe la regla de los fundadores y no es verdad. Ya estaba en vuestros pendientes, pero tiene que estar hecho antes de publicar: los anuncios llevan a @trebolly.
3. **El cambio de moneda de los números [CÁLCULO]:**
   - CJ cobra 13,85 $ de IVA, que es el 21 % de 59,95 € (12,59 €). Por tanto, usa ~1,10 $/€, y 35,62 $ son ~32,4 €, no 31,0 €.
   - Con eso, el ROAS de equilibrio del pack de 2 es ~3,25, no 3,1.
   - Con 1 unidad (15,34 $ + IVA y gestión, misma reserva) sale ~3,5.
   - Si la mayoría de los pedidos son de 1 unidad, la zona de «mantener» (3,0-3,8) puede estar perdiendo dinero.
   - No cambia D-077, pero mirad la mezcla de packs antes de aplicar la regla. Deciden los fundadores.
4. **«Salen juntos» (D-080) no casa con «en cuanto Meta lo apruebe».** Bloqueante 5.
5. **«La verdad se mide por UTM» y el banner de cookies.**
   - No sé si Shopify guarda la UTM cuando se rechazan las cookies [NO SEGURO].
   - Mirad también las ventas totales de la tienda ÷ el gasto: no hay más tráfico de pago.
6. **El regalo de Black Friday y la tarjeta de filtros, retirados.** Que no quede rastro en la tienda ni en los emails (ver el apartado 2).
