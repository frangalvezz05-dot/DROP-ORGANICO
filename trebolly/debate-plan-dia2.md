# Debate del plan del día 2 (viernes 20-nov)
**Marcas:** [DATO] · [CÁLCULO] (con vuestros datos) · [EXPERIENCIA] (criterio propio, sin fuente) · [NO SEGURO].
Lo legal lo lleva el asesor. Deciden los fundadores.

## Los 5 desacuerdos que más pesan
1. **El miedo a «reiniciar el aprendizaje» está sobrevalorado ahora.**
   - Con 0 compras, Meta no ha aprendido nada para el evento Compra: un reinicio no cuesta casi nada [EXPERIENCIA].
   - Por eso, si el cloro no se puede probar, el texto de los anuncios activos se corrige ya, no en la ronda 2.
   - Y añadir anuncios dentro de los conjuntos no es un problema.
2. **El email 3 con el 10 % más el regalo del BF baja el pack de 2 a 17,0-19,1 € de margen** [CÁLCULO]. Queda por debajo del mínimo de 20 €: durante el BF, el email 3 va sin código.
3. **El tope de la campaña (100 €) se alcanza el domingo por la mañana** (~93 € a las 07:00) [CÁLCULO]. La ronda 2 necesita antes una decisión de presupuesto por fases.
4. **Champú ya no es una duda:**
   - su CTR (1,22 %) frente al de piel (3,57 %) da una diferencia que ya es significativa (z = 2,27; p = 0,02) [CÁLCULO];
   - apagarlo el sábado a las 07:00 si el día 2 no cambia el panorama ahorra ~10 €;
   - su dinero no se reparte durante la semana del BF.
5. **Velocidad: una sola medición no vale.**
   - 68 → 71 y 6,2 → 6,5 s están dentro de lo que varía PageSpeed de una vez a otra [EXPERIENCIA].
   - Antes de más trabajo de velocidad, la prueba de las cookies, que dice si la pérdida es de medición o de abandono.

## 1) Punto por punto
| # | Veredicto | Por qué / cambio exacto |
|---|---|---|
| 1 Cloro | **De acuerdo, con 3 cambios** | Ver nota 1. |
| 2 BF desde el sábado | **De acuerdo (cambio mi postura)** | Ver la pregunta 2. |
| 3 Línea bajo la compra | **De acuerdo** | Quita dudas justo cuando se decide, y cuesta 10 minutos. |
| 4 Estrellas de CJ | **Cambiaría** | Ver nota 4. |
| 5 Pago en el navegador de Instagram | **De acuerdo + 1** | Ver nota 5. |
| 6 Prueba de cookies | **De acuerdo, y la primera** | Decide si merece la pena el punto 9. |
| B 48 h | **De acuerdo con las reglas nuevas** | Más el corte de champú (ver el punto 7). |
| 7 Champú | **Apagarlo, pero el sábado, no el domingo** | Ver nota 7. |
| 8 Ronda 2 | **Dentro de los conjuntos de piel y tinte, no en uno nuevo** | Ver la pregunta 3. |
| 9 Velocidad, ronda 2 | **Cambiaría el orden y una medida** | Ver nota 9. |
| D | **Adelantaría el vídeo de la galería** | Ver nota D. |

**Nota 1 · Cloro.**
- **(a)** Si no aparece el material, se corrige ya también el texto de los anuncios activos (punto 1 de los desacuerdos).
- **(b) Un anuncio de AliExpress o Amazon que diga «vitamina C» es lo que dice el vendedor, no una prueba.**
  - Como mucho, sirve para «lleva vitamina C» o «reduce el cloro».
  - Nunca para «filtra el cloro antes de que llegue».
  - Lo que dice Aquapure («12 etapas», «99,9 %») no vale como fuente.
- **(c) Las frases de cloro de los vídeos van casi todas en off** (la voz de M2 en champú, D-T3 en tinte, el antebrazo en piel).
  - Se cambian con la voz clonada, sin generar el vídeo de nuevo.
  - Solo la toma 2 de la parte 2 de piel lleva la boca a la vista.

**Nota 4 · Estrellas de CJ.**
- 9 opiniones «del proveedor» convencen poco y pueden hacer que alguien busque al proveedor y encuentre el producto más barato [EXPERIENCIA].
- Si van, que sean pequeñas y sin enlace. El texto de la fuente, el asesor.
- El carrusel de fotos de AliExpress, no:
  - si se rotula, deja ver de dónde viene;
  - si no, presenta como nuestras unas fotos que no lo son.
- La prueba social verdadera llegará con el email de opinión (primeras opiniones, a principios de diciembre).

**Nota 5 · Pago en el navegador de Instagram.**
- Además, mirad qué se ve en la primera pantalla del pago en el móvil: el nombre y los días de la línea de envío (que no diga «internacional» ni el origen) y el total.
- Que ninguno de los 2 dejara el correo quiere decir que se fueron en la primera pantalla.

**Nota 7 · Champú.**
- Con 5 de 410 frente a 19 de 532, la diferencia ya no es azar (z = 2,27).
- Si el sábado sigue con CTR < 1,5 % y CPC > 1,5 €, se apaga entonces.
- Cada día de champú cuesta ~10 €, el 1-2 % de todo el presupuesto del negocio, para aprender poco.

**Nota 9 · Velocidad.**
1. Primero la prueba de cookies: si la pérdida es de medición, la velocidad no es el cuello de botella.
2. Medir 3 veces.
3. La traza.
- **Ojo con mover pz-*.css al `<head>`:** pasan a bloquear todo el primer pintado (el FCP).
  - Mejor cargarlos una sola vez, justo donde hacen falta, o meter en la página solo el CSS de la primera pantalla.
- **Lo que más pesa es compiled_assets (1,29 s).** La única palanca es quitar los `{% stylesheet %}` de las secciones que no se usan. Riesgo medio: en una copia del tema.

**Nota D.**
- **El vídeo de piel, como 2.ª foto de la galería, hoy:** es subir un mp4 a la ficha. Aquapure lleva 9 vídeos [DATO, de vuestro estudio], y que la ficha enseñe a la misma Marta del anuncio da continuidad [EXPERIENCIA].
- **«Qué lleva dentro»,** solo con lo que esté comprobado (depende del cloro).
- **30 días,** después de aclarar lo del cloro.
- **La manguera,** lo último.

## 2) ¿BF desde el sábado o desde el domingo? El sábado: tenías razón
- **Yo defendía el domingo para tener una lectura limpia de las 72 h.** Pero esa lectura decide los ángulos con datos del anuncio (gancho, CTR, CPC y llegada al pago), y la oferta solo cambia la tienda, igual para los tres.
- **Con 0 compras y ~10 sesiones al día no hay ninguna conversión limpia que proteger** [CÁLCULO].
- **Cada día de la semana del BF sin oferta, frente a dos rivales con oferta, sí cuesta.**
- **Condiciones para el sábado a las 00:00:**
  1. un pedido en modo de prueba del pack de 2 y otro del de 3, y en CJ: 2 × Suit 1 + 6 filtros y 3 × Suit 1 + 12;
  2. el carrito: con 1 cabezal, subir de pack; con 2 o 3, nada;
  3. el email 3 sin el 10 %;
  4. el título actual de los anuncios dice «10 filtros» y la tienda dirá 16. Es una sorpresa a favor, y se arregla con los anuncios nuevos del domingo.

## 3) La ronda 2 y el dinero
**Dónde:**
- **Dentro de los conjuntos de piel y tinte,** no en un conjunto nuevo.
- **En cada uno, 2 anuncios nuevos:** el mismo vídeo con el texto del BF y un estático ✗/✓.
- **El ✗/✓ solo con lo verdadero:** filtro en el mango, cepillo, STOP, 5 filtros y garantía de entrega. Nada de «✓ sin cloro» si no está comprobado.
- **El anuncio viejo se pausa cuando se aprueben los nuevos.**
- **Por qué no un conjunto «TRE-BF»:** sería un cuarto conjunto con el mismo público. Más competencia entre vuestros propios anuncios y 30 € al día partidos en trozos de 10. Y el reinicio, con 0 compras, no cuesta nada.

**Presupuesto por fases (deciden los fundadores; hay que subir el tope de la campaña):**
| Fase | Fechas | Diario | Acumulado aprox. | Qué se decide |
|---|---|---|---|---|
| 1. Prueba | 19-22 nov | 30 € (20 € desde el sábado sin champú) | ~90-100 € | Ángulos (dom 07:00) |
| 2a. BF | dom 22 – jue 26, 07:00 | 20 € (piel + tinte) | ~170 € | Control el jueves antes del pico |
| 2b. BF (solo con señal) | jue 26 – lun 30 | 20 € | ~250 € | Futuro del producto el 1-dic |

- **Señal para seguir el jueves:** ≥ 1 compra, o un coste por pago iniciado ≤ 7 € con ≥ 5 pagos iniciados.
  - Sin señal, se pausa durante el pico del BF (jueves a domingo; Raúl, con Adrián, habla de CPM de hasta 20 veces más [wWC8SoeQ_Fk]).
  - El lunes se decide.
- **Tope de la campaña:** 180 € el domingo, y 260 € si se pasa el control.
- **Esto deja 250-750 € del presupuesto total** para escalar este producto o probar otro.

## 4) ¿Probabilidad de que sea rentable? ~20 % [EXPERIENCIA]. ¿Cuándo está muerto?
**A favor:**
- un CTR del 3,57 % en piel y tinte (más del doble del listón verde del 1,5 %);
- piel tiene un coste por pago iniciado de ~5,3 € (con solo 2 pagos iniciados).

**En contra:**
- **El CPM:** con 20 €, hacen falta 2,7 compras por cada 100 clics; con 26 €, 3,5. En tráfico frío, lo normal es 1-2 [EXPERIENCIA]. Con un CPM de 10 € bastaría 1,3, y con 14 €, 1,9 [CÁLCULO]. Solo funciona si el CPM baja hacia 10-14 € o si sube el ticket.
- **Aquapure vende el mismo cabezal,** lleva anuncios desde enero, con 2 millones de alcance, y tiene mucha prueba social.
  - Dani: «Meta le va a dar la puja al vendedor que ya está ahí»; si hay competidores enormes, hay que buscar otro ángulo o avatar [nnXqHmYlmvA].
- **El cloro, nuestro mecanismo principal, quizá no se pueda probar.**
- **El CPM de la semana del BF.**

**Cuándo se da por muerto, con cifras:**
- **El listón del coste por pago iniciado:** CPA de equilibrio (18,5-20,9 €) × las compras que salen de cada pago iniciado (35-50 %) = 6,5-10,4 € [CÁLCULO]. Verde, ≤ 7 €; rojo, > 10 €.
- **Jueves 26 (~170 € acumulados):** 0 compras y coste por pago iniciado > 10 € (o < 5 pagos iniciados) → pausa y decisión el lunes.
- **Lunes 30 (~250 €):** < 3 compras, o ROAS < 1,5 → el producto está muerto y se pasa a otro.
  - Eso, con la medición comprobada (cookies) y el pago probado.
  - Si hay ≥ 8 pagos iniciados y 0 compras, el problema es el pago o la confianza, no el producto: se arregla antes de matarlo.
- **Sigue en diciembre (fase 3, hasta ~400 €)** con ≥ 3 compras, coste por pago iniciado ≤ 7 € y ROAS ≥ 2. A partir de ahí, se trabaja el ticket y el CPM.

## 5) Lo que nadie ha dicho
**El mayor riesgo es la promesa.**
- Si el cartucho no reduce el cloro, los 3 ángulos venden algo que el producto no hace: devoluciones, malas opiniones y comentarios negativos en Meta.
- Y sin cloro, lo que nos diferencia de Aquapure (mismo cabezal) es poco.
- La promesa nueva tiene que salir de lo que es verdad y se ve:
  - el cepillo y el STOP;
  - y un público de mujeres que cuidan su pelo.

**Lo que más rendiría y no estamos haciendo:**
1. **Un tope de pérdidas por fases escrito como decisión** (apartado 3). Protege 250-750 € para un segundo intento. Para un negocio de 500-1.000 €, es lo que más vale.
2. **Bajar el CPM con más variedad de creativos sobre el ángulo que funciona.** 2-3 ganchos nuevos del mismo vídeo, cambiando solo los 3 primeros segundos (Dani, un solo elemento [s1hMMVWgf00]), en diciembre.
   - El CPM es la palanca más grande: de 20 a 10 € reduce a la mitad la conversión que hace falta.
3. **Captar el correo sin descuento,** con la guía en PDF como pop-up.
   - Ninguno de los 2 pagos iniciados dejó el correo.
   - Así se pueden recuperar con un email de bienvenida que recuerde el regalo del BF (que acaba de verdad el 30 nov) sin tocar el margen.

**Más cosas que no se habían dicho:**
- **El email 3 con el 10 % y el regalo rompen el margen** (17,0-19,1 €).
- **El tope de 100 € se alcanza el domingo.**
- **Piel y tinte tienen el mismo CTR:** a las 72 h no habrá un ganador claro entre ellos. Lo decidirán las compras.
- **Con 10 €/día, cada conjunto tiene ~0,5 compras al día:** la optimización a Compra va casi a ciegas y los resultados van a dar saltos.
- **En diciembre, juntar piel y tinte en un solo conjunto,** para concentrar la señal (Dani, CBO [n5gORsrA_xc]).

## 6) Lista final por impacto
| # | Qué | Quién | Cuándo |
|---|---|---|---|
| 1 | Material del cartucho → según el resultado, textos de la ficha, los emails y **los anuncios activos** | Claude (búsqueda y textos) + fundadores (sí) | Hoy |
| 2 | Email 3 sin el 10 % durante el BF | Claude (con el sí) | Hoy |
| 3 | Pago en el navegador de Instagram + línea de envío del pago | Fundadores (móvil) | Hoy |
| 4 | Prueba de cookies (medición o abandono) | Fundadores | Hoy |
| 5 | Oferta del BF montada y probada (modo de prueba, CJ, tarjetas y carrito) | Claude + fundadores (sí) | Hoy; activa el sáb a las 00:00 |
| 6 | Línea bajo la compra + garantía y protección | Claude | Hoy |
| 7 | Vídeo de piel como 2.ª foto de la galería | Claude | Hoy o el sábado |
| 8 | Champú: apagarlo si el día 2 lo confirma | Fundadores | Sáb 07:00 |
| 9 | Presupuesto por fases y tope de 180 € (control el jueves 26) | Fundadores | Sábado |
| 10 | Ronda 2: 2 anuncios nuevos en piel y tinte (vídeo con texto del BF + ✗/✓ sin cloro) | Claude (textos) + fundadores (publicar) | Dom 07:00 |
| 11 | Voces del cloro en los vídeos → frases nuevas con la voz clonada (si no se prueba el cloro) | Claude | Dom-lun |
| 12 | Velocidad, ronda 2 (después de las cookies, 3 mediciones y la traza) | Claude | Después del domingo |
| 13 | Captación de correo con la guía en PDF | Claude | Después |
| 14 | Estrellas de CJ (pequeñas, si van) | Fundadores | Después |
| 15 | Diciembre: fechas límite, «uno para ti y otro para regalar», 30 días (después del cloro), juntar los conjuntos, ganchos nuevos y manguera | Claude + fundadores | 1-dic |
