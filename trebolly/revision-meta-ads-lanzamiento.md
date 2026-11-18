# Revisión de la campaña de Meta · lanzamiento del 19-nov (cabezal)

**Cómo leerlo:**
- **OK** = se queda. **CAMBIAR** = cambio exacto. **FALTA** = hay que añadirlo.
- **[DATO]** = comprobado con una fuente (al final).
- **[EXPERIENCIA]** = criterio de media buyer, sin fuente.
- **[NO SEGURO]** = no lo he podido comprobar en la interfaz actual de Meta.
- La decisión final es de los fundadores.

## 0. Lo que cambiaría antes de publicar (por orden de importancia)
1. **El listón de CPA baja de 29 € a unos 19 € en el pack de 2** (unos 13 € con 1 unidad). Mejor aún, una sola cifra que vale para cualquier mezcla de packs: **ROAS de equilibrio ≈ 3,1**, medido como ventas en Shopify ÷ importe gastado en Meta.
   - Tu cuenta va bien encaminada.
   - Pero el IVA está mal calculado y faltan dos costes (apartado 5).
2. **FALTA "Beneficiario y pagador"** en cada conjunto. Es obligatorio en los anuncios que se entregan en la UE. Si ya está puesto por defecto en la cuenta, saldrá relleno.
3. **Nivel de datos: Máximo.** Según Shopify, Mejorado y Máximo usan los dos la API de conversiones, así que ver «web y servidor» no dice cuál está puesto.
4. **Regla de las 48 h:** con unos 20 € gastados por conjunto, «≥ 3.000 impresiones» casi nunca se cumple. **Cambiar a ≥ 2.000.**
5. **Ver llegar un Purchase de verdad antes de gastar:**
   - un pedido real de 39,95 €, pagado por un socio y reembolsado antes de que vaya a CJ;
   - cuesta ~1,1 € de comisión.
   - Sé que está decidido que no: os lo argumento en el apartado 2 y decidís vosotros.
6. **Sugerencia de público: mujeres de 25 a 65 años, no de 25 a 55.** El ángulo de tinte incluye cubrir canas, y eso pesa mucho a partir de los 50 [EXPERIENCIA].
7. **Revisar las mejoras de Advantage+ en los tres anuncios justo antes de publicar.** Al duplicar conjuntos o anuncios, algunas vuelven a encenderse [DATO: JumpFly].
8. **Aviso de IA:** si no encontráis la casilla de Meta, el anuncio sale sin ningún aviso. Decidid si ponéis «Creado con IA» en la tarjeta final.

---

## 2. Seguimiento (píxel)

| Punto | Veredicto | Por qué o cambio |
|---|---|---|
| App oficial, píxel nuevo y catálogo sincronizado | **OK** | Es la forma estándar en Shopify. |
| Dos píxeles viejos sin datos | **OK, con una comprobación** | Que no estén conectados a la app ni elegidos en ningún conjunto. Renombradlos «NO USAR» para no equivocaros al elegir. |
| Nivel de datos compartidos | **CAMBIAR → Máximo** | Ver nota 1. |
| Sin código pegado a mano | **OK** | |
| Dominio verificado; ya no se ordenan eventos | **OK** | |
| Banner de cookies con los ajustes de la UE | **OK** | Meta verá menos compras que Shopify, y es normal. |
| Clarity con cookies aceptadas; Klaviyo | **OK** | |
| Publicar el tema y volver a probar | **OK + FALTA** | Las plantillas `?view=champu/tinte/piel` tienen que estar **en el tema que se publica**. Si no, el enlace del anuncio abre la ficha normal. |
| Sin pedido de prueba | **Lo cambiaría (decisión vuestra)** | Ver la respuesta a la pregunta 2, más abajo. |

**Nota 1 · Nivel de datos.**
- Según el centro de ayuda de Shopify:
  - Estándar = solo el píxel del navegador;
  - Mejorado = añade la API de conversiones;
  - Máximo = API de conversiones y píxel, «actualizado con la tecnología publicitaria más reciente de Meta».
- Mejorado y Máximo comparten los mismos datos de la clienta para cruzarlos (nombre, email y ubicación) [DATO].
- La diferencia práctica entre los dos no la he podido comprobar [NO SEGURO].
- Mi voto es Máximo; Mejorado no sería un error.
- En los dos casos, la política de privacidad tiene que decir que se comparten datos con Meta.

**Vuestras comprobaciones a)-g): OK todas.** Matices:
- **c)** Probadlo con la URL real del anuncio (`…?view=champu&utm_source=meta…`), no con la ficha sin parámetros.
- **d)** No sé si la app de Shopify manda eventos de servidor cuando se rechazan las cookies [NO SEGURO]. La prueba d) os lo dirá. Si llegan eventos de servidor sin consentimiento, anotadlo y que lo mire el revisor legal (RGPD).
- **e)** El nombre «Meta Ads Data Advisor» no lo he podido comprobar. Si no aparece con ese nombre, es «Meta Pixel Helper».
- **f)** La calidad de coincidencia necesita tráfico: no saldrá esta noche. Anotadla el día 2 o 3. Para Purchase, con Máximo o Mejorado, lo normal es ≥ 6 sobre 10 [EXPERIENCIA].

**FALTA:**
- **h) Shopify → Ajustes → Eventos de clientes:**
  - el píxel de la app de Meta, «Conectado»;
  - ningún píxel personalizado de Meta (duplicaría compras).
- **i) Prueba desde el navegador de Instagram en el móvil:**
  - compartid la vista previa del anuncio al móvil y tocad «Comprar»;
  - mirad que carga rápido, que sale el banner de cookies y que el pack de 2 está marcado;
  - comprobad que el AddToCart llega a «Probar eventos».
  - Marc insiste en probar en el navegador de la app [kq0bZo65WNM] y en dos móviles [oEFWZdCw5FQ].
- **j) Checkout:** escribid una dirección de Canarias y comprobad que no deja terminar la compra.
- **k) Cuenta publicitaria:**
  - moneda EUR y zona horaria Europa/Madrid (cambiarlas después no es sencillo);
  - método de pago añadido;
  - una tarjeta que admita cargos pequeños repetidos: las cuentas nuevas cobran al llegar a umbrales bajos.

### Respuestas a las preguntas del bloque 2
**1. ¿Falta alguna comprobación?** Sí: de la h) a la k).

**2. ¿Es razonable lanzar sin haber visto llegar nunca un Purchase?**
- **Es un riesgo asumible, pero quitarlo cuesta muy poco.**
- **Lo que suele fallar no es la app, sino cómo está puesta:**
  - el píxel equivocado conectado;
  - el nivel de datos;
  - eventos bloqueados por el consentimiento.
- **Si el Purchase no llega:**
  - la campaña optimiza a ciegas los 90 €;
  - y no lo sabréis hasta la primera venta.
- **El seguro:**
  - un socio hace un pedido real de 39,95 € con su tarjeta;
  - se reembolsa en Shopify y se cancela antes de pagarlo en CJ.
- **Coste:** la comisión de la pasarela, ~1,1 €. Shopify no la devuelve al reembolsar [EXPERIENCIA: comprobadlo en vuestras tarifas].
- **De paso comprueba:**
  - el Purchase con valor y EUR, sin duplicar;
  - el email de gracias de Klaviyo;
  - que el pedido entra en CJ.
- **Si mantenéis el no:** con el primer pedido real, mirad en menos de una hora en el Administrador de eventos que el Purchase ha llegado.

**3. ¿Qué haría si a las 24 h hay carritos y pagos iniciados en Shopify, pero el píxel no los cuenta?**
1. **Separar dos casos:**
   - que los eventos no lleguen a Meta;
   - o que lleguen y Meta no los atribuya a los anuncios.

   Para saberlo: Administrador de eventos → píxel Trebolly → Resumen, AddToCart e InitiateCheckout de las últimas 24 h, de navegador y de servidor.
2. **Comparar con Shopify:** sesiones con carrito y sesiones que llegan al pago.
   - Con el banner de cookies, es normal que Meta cuente un 20-50 % menos [EXPERIENCIA].
   - Cero es una avería.
3. **Si llegan al Administrador de eventos pero no salen en la campaña:**
   - es cosa de la atribución (gente que no viene del anuncio, o falta de consentimiento);
   - no se toca nada.
4. **Si no llegan, es un «fallo técnico» de vuestra regla.** Revisad en este orden:
   - Eventos de clientes («Conectado»);
   - la app (píxel = Trebolly, nivel de datos);
   - la pestaña Diagnóstico del píxel.

   Arreglarlo no exige tocar la campaña.
5. **Si en 24 h no ha llegado ningún evento, ni de navegador ni de servidor:**
   - pausad los tres conjuntos hasta arreglarlo, porque optimizar a Compra sin señal es tirar el dinero;
   - después, reactivad.
   - Por lo que sé de Meta, una pausa corta no reinicia el aprendizaje; una de 7 días o más, sí.

---

## 3. Campaña, ajuste por ajuste

### Campaña
| Ajuste | Veredicto | Por qué o cambio |
|---|---|---|
| Objetivo: Ventas | **OK** | |
| Configuración manual, no la campaña Advantage+ de ventas | **OK** | Ver nota 2. |
| Presupuesto Advantage+ de campaña (CBO) apagado | **OK para la prueba** | Ver nota 3. |
| Categoría especial: ninguna. Pruebas A/B: no. Nombre | **OK** | |
| Límite de gasto de la campaña: 95 € | **OK** | Ver nota 4. |

**Nota 2 · ¿Se pierde algo sin la campaña Advantage+ de ventas?**
- **Con varios conjuntos y presupuesto de conjunto, Meta marca la campaña como «Advantage+ desactivado»:** es una campaña de ventas manual [DATO: Jon Loomer].
- **En una prueba de 90 € no se pierde nada importante.** Lo que aporta Advantage+ es que Meta reparta el dinero y el público, y eso es justo lo que no queréis en una prueba de ángulos.
- **Hay una alternativa que mantiene Advantage+:** 3 campañas con un solo conjunto cada una. Según Jon Loomer, con un solo conjunto el presupuesto de conjunto no lo apaga.
- **No la recomiendo:**
  - tres campañas de 10 € es lo que Dani critica [n5gORsrA_xc];
  - y no se gana nada medible.

**Nota 3 · ABO o CBO.**
- **Dani prefiere CBO** [n5gORsrA_xc, CKiR67QoZ9U], pero lo dice para escalar.
- **En la prueba, ABO:** con CBO y tres conjuntos de 10 €, Meta se gasta casi todo en uno el primer día y los otros dos no dan datos. Ya lo argumentamos en el plan de ángulos.
- **Para escalar, el ganador pasa a una campaña CBO.**

**Nota 4 · Límite de 95 €.**
- **Es un tope, no un presupuesto:** subirlo después no reinicia el aprendizaje [EXPERIENCIA].
- **Al llegar a 95 € se para todo,** aunque no hayan pasado justo 72 h (si algún día se gasta de más). Es lo que queréis.

### Conjunto (× 3)
| Ajuste | Veredicto | Por qué o cambio |
|---|---|---|
| Sitio web · píxel Trebolly · Compra | **OK** | Ver nota 5. |
| Maximizar conversiones, sin objetivo de coste | **OK** | |
| Atribución: 7 días tras clic + 1 día tras visualización | **OK: dejad la de por defecto** | Ver nota 6. |
| 10 €/día · inicio 19-nov 00:00 · sin fin | **OK** | Publicad ya, con el inicio programado: la revisión de Meta puede tardar. |
| Público Advantage+, España sin Canarias, Ceuta ni Melilla | **OK** | Ver nota 7. |
| Sugerencia: mujeres de 25 a 55 | **CAMBIAR → mujeres de 25 a 65** | Ver nota 8. |
| Edad mínima 18 · excluir compradores de 180 días · idioma sin tocar | **OK** | La exclusión hoy está vacía; no molesta. |
| Ubicaciones Advantage+ | **OK** | Ver nota 9. |
| FALTA: Beneficiario y pagador | **FALTA** | Obligatorio para anuncios que se entregan en la UE. Poned el mismo en los tres conjuntos. |

**Nota 5 · Optimizar a Compra.**
- Como el evento aún no tiene actividad, saldrá un aviso, pero se puede elegir igual [EXPERIENCIA].
- Optimizar a Compra desde el primer día es lo correcto: optimizar a carrito atrae a gente que añade y no compra.

**Nota 6 · Atribución.** Ver la respuesta a la pregunta 2 del bloque 3, más abajo.

**Nota 7 · Excluir Canarias, Ceuta y Melilla.**
- Es compatible: la ubicación es un control fijo, no una sugerencia, y Advantage+ sigue encendido.
- Si os deja elegir «personas que viven en esta ubicación», elegidlo [NO SEGURO de que esa opción siga existiendo].

**Nota 8 · Sugerencia de mujeres.**
- **Sí pondría la sugerencia:** con un píxel sin datos, es la única pista que tiene Meta al empezar.
- **Pero hasta los 65:** el ángulo de tinte incluye cubrir canas. Sigue siendo una sugerencia: Meta puede salirse de ella.

**Nota 9 · Ubicaciones.**
- **No quitaría Audience Network ni Messenger:** optimizando a Compra, Meta les da poco dinero si no venden [EXPERIENCIA].
- **Quitarlas después reinicia el aprendizaje.** Si se quitan, que sea antes de publicar.
- **Mi voto:** dejarlas y mirarlas a las 72 h. Si Audience Network se lleva más del 15 % del gasto y menos de la mitad de sus clics acaban en visita a la página, se quita en la siguiente ronda.

### Anuncio (× 3)
| Ajuste | Veredicto | Por qué o cambio |
|---|---|---|
| Identidad: página Trebolly + @trebolly | **OK** | |
| Vídeo único, 9:16 a Stories/Reels y 4:5 al feed | **OK** | Revisad la vista previa de cada ubicación: que los rótulos no queden tapados en Reels. |
| Texto principal, título y descripción | **OK** | Los tres juegos de texto están en el anexo A. |
| Botón «Comprar» | **OK** | |
| Destino `…?view=champu / tinte / piel` | **OK** | En la vista previa, haced clic y mirad que la URL final queda bien: `…?view=champu&utm_source=meta…` (Meta añade sus parámetros con «&»). |
| UTM con {{campaign.name}} y {{ad.name}} | **OK** | Las macros son válidas. `utm_content` coincide con lo que usa Klaviyo para personalizar por ángulo. |
| Mejoras creativas de Advantage+, todas apagadas | **OK + FALTA** | Ver nota 10. |
| Etiqueta de IA al publicar | **FALTA comprobarlo** | Ver nota 11. |
| Comentarios moderados a mano | **OK** | Los comentarios de un anuncio salen en la publicación del anuncio, no en el muro: miradlos en la bandeja de entrada de Meta Business Suite. |
| Sin catálogo dinámico | **OK** | |

**Nota 10 · Mejoras creativas.**
- Revisad el panel en los tres anuncios justo antes de publicar: al duplicar, alguna vuelve a encenderse [DATO: JumpFly].
- Incluye «añadir artículos del catálogo», que puede aparecer porque el catálogo está conectado.
- Desde el 30-oct-2025, Meta hace responsable al anunciante de lo que cambien sus retoques de IA [DATO: ppc.land]. Un texto generado podría prometer algo de salud.

**Nota 11 · Etiqueta de IA.**
- **Dónde está la casilla:**
  - Meta dice que pone la etiqueta «Información sobre IA» a los anuncios hechos con sus herramientas, y que detecta los de herramientas de fuera por marcas estándar [DATO: Meta, feb-2025].
  - Jon Loomer encontró una casilla encima del texto principal. Meta no explica claramente dónde está [NO SEGURO].
- **Si no la encontráis, el anuncio sale sin ningún aviso.** Recomendación: poner «Creado con IA» en pequeño en la tarjeta final.
- **Por qué:** el Reglamento europeo de IA obliga a avisar de los vídeos generados que parecen reales.
  - Es el art. 50, que según el calendario del reglamento se aplica desde el 2-ago-2026.
  - No sé si ha cambiado después.
  - Que lo mire el revisor legal. La decisión es vuestra.

### Públicos personalizados y seguridad
| Ajuste | Veredicto | Por qué o cambio |
|---|---|---|
| Los 7 públicos personalizados del día 1 | **OK** | No cuestan nada y empiezan a llenarse. |
| Todo en pausa, se revisa y se publica de una vez | **OK** | |
| Límite diario de la cuenta (42,65 €) frente al gasto de más (hasta +75 % al día por conjunto) | **OK: no bajaría los diarios** | Ver la respuesta a la pregunta 5, más abajo. |

### Respuestas a las preguntas del bloque 3
1. **Con presupuesto de conjunto, ¿se puede usar la campaña Advantage+ de ventas?**
   - Con varios conjuntos, no: queda como campaña manual.
   - Para esta prueba no se pierde nada que importe (notas 2 y 3).
2. **¿Mejor solo 7 días tras clic en una cuenta nueva?**
   - **No:** dejad la de por defecto.
   - **Por qué:** la ventana de atribución también decide qué compras usa Meta para aprender. En una cuenta con 0 compras, quitarle señal hace que aprenda más despacio [EXPERIENCIA].
   - **Para decidir, usad otra cosa:** la columna de 7 días tras clic («Comparar ventanas de atribución») y las ventas de Shopify.
   - **Ojo, ha cambiado en 2026** (según varias fuentes, no la página de Meta):
     - desde marzo, «clic» solo cuenta los clics en el enlace;
     - los «me gusta» y las reproducciones pasan a «interacción», con 1 día;
     - y desde el 12-ene ya no existen las ventanas de 7 y 28 días tras visualización [DATO: Jon Loomer, AdNova].
   - **Lo más probable es que veáis** «7 días tras clic, 1 día tras interacción y 1 día tras visualización». Si es así, dejadlo.
3. **¿Excluir Canarias, Ceuta y Melilla rompe el Advantage+?** No (nota 7).
4. **¿Sugerencia de mujeres o totalmente abierto?** Sugerencia, de 25 a 65 años (nota 8).
5. **¿Puede la cuenta toparse con su límite diario? ¿Bajar a 9 €?**
   - **Solo se toparía si los tres conjuntos gastan de más el mismo día:** el máximo teórico es 3 × 17,50 = 52,50 €.
   - **En una cuenta nueva, lo normal el primer día es gastar de menos** [EXPERIENCIA].
   - **Bajar a 9 € no lo arregla:** 3 × 15,75 = 47,25 €, que sigue pasando del límite. Para que fuera imposible habría que bajar a 8 €, y perderíais un 20 % de datos.
   - **Si se topa, los anuncios solo se paran hasta medianoche:** no se rompe nada.
   - **En la semana, Meta no pasa de 7 veces el diario de cada conjunto.**
6. **¿Compiten los tres conjuntos entre sí?**
   - **Meta no os hace pujar contra vosotros mismos.** Si dos de vuestros conjuntos entran en la misma subasta, solo participa el que más valor tiene («solapamiento de subastas»).
   - **El efecto es que un conjunto puede gastar menos.** Con un público de millones de personas y 10 € al día, es poco probable.
   - **El síntoma:** un conjunto que gasta menos del 60 % de su presupuesto el día 1 o el 2.
   - **No se puede evitar sin estropear la prueba:** no se toca antes de las 72 h.

---

## 4. Reglas de la prueba y umbrales

| Regla | Veredicto | Por qué o cambio |
|---|---|---|
| 72 h sin tocar salvo fallos técnicos | **OK** | Es lo que dice Dani [nnXqHmYlmvA]. |
| A las 48 h, apagar con 0 carritos, o con CTR ≤ 0,4 % y ≥ 3.000 impresiones | **CAMBIAR la cifra** | Ver nota 12. |
| A las 72 h se juzga todo; ganadores a 10 €/día hasta ~100 €; regla de dos pasos | **OK, con un aviso** | Ver nota 13. |
| Subir un 20 % con ≥ 72 h, ≥ 6 compras y CPA < 29 € | **CAMBIAR** | Ver nota 14. |
| Anuncio que engancha y tienda que no vende | **OK** | |
| Columnas de cada mañana | **OK + FALTA** | Ver nota 15. |

**Nota 12 · Impresiones a las 48 h.**
- A las 48 h llevaréis unos 20 € por conjunto. Con un CPM de 7-10 €, son 2.000-2.900 impresiones, así que con «≥ 3.000» la regla casi nunca se activa.
- **Cambio:** «CTR de enlace ≤ 0,4 % con ≥ 2.000 impresiones».

**Nota 13 · El juicio de las 72 h.**
- Con 30 € por conjunto, esperad entre 0 y 2 compras por ángulo.
- Por eso se juzga con el embudo (gancho, CTR y coste por carrito), no con el CPA.
- 3 compras en 100 € son 33 € por compra: valida que se vende, no que sea rentable (ya estaba anotado).

**Nota 14 · La regla de subir.**
- **Cambio:** de «CPA < 29 €» a **«ROAS ≥ 3,5»** (apartado 5).
- **Si casi todo es pack de 2,** equivale a un CPA ≤ 17 €.
- **El 20 % coincide con Dani** [8Er-sAVrULo].

**Nota 15 · Columnas que faltan.**
- «Visitas a la página ÷ clics»: si sale bajo, la página carga lenta.
- «Inicio de pago → compra».
- Una nota: el importe gastado de Meta no lleva la tarifa ni el IVA. Para el coste real, hay que multiplicarlo por 1,246.

### Umbrales para España en noviembre (antes del Black Friday)
| Métrica | Verde | Ámbar | Rojo | De dónde sale |
|---|---|---|---|---|
| CPM | ≤ 9 € | 9-14 € | > 14 € | Ver nota 16. |
| CTR de enlace | ≥ 1,5 % | 0,8-1,5 % | < 0,8 % | Plan de ángulos v4 [EXPERIENCIA]. Creatify, citando a Triple Whale: por debajo de 0,7-1 %, hay que cambiar el creativo [DATO]. |
| CPC de enlace | ≤ 0,60 € | 0,60-1,00 € | > 1,00 € | Sale de CPM ÷ (CTR × 1.000): 9 € ÷ 15 = 0,60 €. Superads da para España unos 0,46 €, pero contando todos los clics [DATO]. |
| Hook rate (reproducciones de 3 s ÷ impresiones) | ≥ 30 % | 20-30 % | < 20 % | [EXPERIENCIA], ya en el plan. |
| ThruPlay ÷ impresiones | ≥ 10 % | 5-10 % | < 5 % | [EXPERIENCIA] |
| Visitas a la página ÷ clics en el enlace | ≥ 70 % | 50-70 % | < 50 % | [EXPERIENCIA]. Por debajo, la página carga lenta en el navegador de Instagram. |
| Carritos ÷ visitas | ≥ 8 % | 4-8 % | < 4 % | [EXPERIENCIA] |
| Coste por carrito | ≤ 6 € | 6-10 € | > 10 € | 0,3 y 0,5 × el CPA de equilibrio (~19 €). Vuestro «< 4 €» es más exigente: dejadlo como «muy bueno». |
| Coste por inicio de pago | ≤ 10 € | 10-15 € | > 15 € | [ESTIMACIÓN]: suele acabar en compra uno de cada dos pagos iniciados. |
| Compras ÷ visitas | ≥ 2 % | 1-2 % | < 1 % | Dani pone el ejemplo de pasar del 1,5 % al 3 % [CKiR67QoZ9U]. |

**Nota 16 · De dónde sale el CPM.**
- Superads: el CPM medio de España, con todos los objetivos y entre oct-2025 y sep-2026, está un 63 % por debajo de la media mundial (20,6 €), es decir, unos 7,6 € (la cuenta es mía) [DATO].
- Marc: «más de 10 € de CPM me mata el margen» [0gOn8a_xFA8].
- Optimizar a compra, con una cuenta nueva y en noviembre, sale más caro que esa media [EXPERIENCIA].
- El CPM solo no decide nada.

**Ojo con el Black Friday (viernes 27-nov).**
- Raúl, en el vídeo con Adrián, dice que esa semana el CPM puede subir hasta 20 veces [wWC8SoeQ_Fk].
  - Como media me parece exagerado, pero la subida es real [EXPERIENCIA].
- La prueba (19-22 nov) cae justo antes: si el CPM sube día a día, no es culpa del anuncio.
- La regla 6 del apartado 9 ya dice que esa semana solo sigue lo que funciona.

---

## 5. La cuenta de números

**Tienes razón en lo principal.**
- El listón de 29 € no contaba la tarifa ni el IVA de Meta, que suman un 24,6 % sobre cada euro.
- El 3 % existe: desde el 1-jul-2026, Meta cobra una «tarifa por ubicación» del 3 % en los anuncios que se entregan en España.
- El IVA va encima del total [DATO: Dataslayer, Jon Loomer]. 1,03 × 1,21 = **1,246 ✓**.

**Pero hay dos errores y dos olvidos:**
1. **El IVA es de 10,40 €, no de 12,6 €.**
   - 12,6 € es el 21 % de 59,95 €, como si el precio no llevara IVA. Pero el precio a la clienta lo lleva: el IVA que hay dentro es 59,95 × 21 ÷ 121 = **10,40 €**.
   - La AEAT dice que en la ventanilla única de importación cuenta el precio neto pagado por el consumidor [DATO: AEAT].
   - Si CJ os cobra 12,6 €, está calculando el IVA sobre el precio con IVA. Mirad en su factura sobre qué base lo calcula.
2. **¿Los 21,35 $ ya incluyen ese IVA?**
   - En el traspaso pone «coste con envío y aduanas 21,35 $».
   - Si ya lo incluyen, lo estáis contando dos veces y el margen es bastante mayor. Hay que mirarlo en CJ.
3. **Falta el regalo del Black Friday:** unos 1,7 € por pedido de pack de 2 o de 3, hasta el 30-nov (está en la revisión del carrito).
4. **Falta una reserva para incidencias:**
   - garantía de entrega;
   - reenvío si llega dañado;
   - 14 días para devolverlo, con los gastos a vuestra cuenta;
   - reembolsos sin devolución.

   Propongo un 5 % del precio (unos 3 € en el pack de 2) [ESTIMACIÓN], hasta tener datos reales.

**Además:**
- con PayPal o Klarna la comisión es mayor que 2,1 % + 0,30 €: comprobadlo en Ajustes → Pagos;
- si pagáis a CJ en dólares, el banco cobra por el cambio de moneda.

**Fiscal (no es tema de Meta):** vender a consumidores en España sin estar dados de alta en IVA, usando el IOSS de CJ, es una pregunta para un gestor. Si os dais de alta y os registráis como operador intracomunitario, el IVA de Meta podría dejar de ser un coste.

### La cuenta, con el IVA bien calculado
| Pack de 2 | € |
|---|---|
| Precio | 59,95 |
| − IVA dentro del precio | 10,40 |
| − Gestión del IOSS (3 % del IVA) | 0,31 |
| − CJ (21,35 $) | 18,80 |
| − Pasarela (2,1 % + 0,30 €) | 1,56 |
| − Regalo de Black Friday (hasta el 30-nov) | 1,70 |
| **= Margen** | **27,18** |
| − Reserva para incidencias (5 %) | 3,00 |
| **= Margen con reserva** | **24,18** |
| **CPA de equilibrio en Meta** (÷ 1,246) | **21,8 sin reserva · 19,4 con reserva** |

- **Con vuestro IVA de 12,6 €:** 20,0 € sin reserva y 17,6 € con reserva.
- **1 unidad (sin regalo):** 39,95 − 6,93 − 0,21 − 13,51 − 1,14 = 18,16 € de margen.
  - CPA de equilibrio: 14,6 € sin reserva, o **13,0 €** con 2 € de reserva.
- **Pack de 3:** falta su coste en CJ.

**La cifra que vale para cualquier mezcla de packs: el ROAS.**
- **Con reserva:** 59,95 ÷ 19,4 = 3,09 en el pack de 2, y 39,95 ÷ 13,0 = 3,07 con 1 unidad.
- **Sin reserva:** 2,75 en los dos casos.
- **El ROAS de equilibrio sale igual sea cual sea el pack:** ≈ **3,1** con reserva y ≈ **2,75** sin ella.
- **Así no hace falta calcular el CPA ponderado.** La fórmula del apartado 9 (1 × 18 + 2 × 29 + 3 × 40) se queda vieja.

**Cómo se mide:**
- **ROAS = ventas de Shopify (con IVA) ÷ importe gastado en Meta.**
- **Al principio, mejor con las ventas totales de la tienda que solo con las de UTM.** Meta es el único tráfico de pago y la tienda es nueva, así que casi todo vendrá de ahí. Además, las UTM también pueden perder parte de la atribución si no se aceptan las cookies [NO SEGURO].

### Listones que usaría
| Decisión | ROAS (ventas Shopify ÷ gasto en Meta) | CPA si casi todo es pack de 2 | CPA si casi todo es 1 unidad |
|---|---|---|---|
| **Subir un 20 %** (con ≥ 72 h y ≥ 6 compras) | **≥ 3,5** | ≤ 17 € | ≤ 11 € |
| **Mantener sin subir** (como mucho 1 semana) | 2,7-3,5 | 17-22 € | 11-15 € |
| **Cortar o cambiar el creativo** | < 2,7 con ≥ 6 compras, o ≥ 40 € gastados sin ninguna compra y el embudo en rojo | > 22 € | > 15 € |

- **Por qué se mantiene entre 2,7 y 3,1, aunque ahí se pierda un poco:**
  - la primera semana compra datos;
  - y los emails de Klaviyo todavía no han trabajado.
  - Como mucho una semana.
- **40 € es unas 2 veces el CPA de equilibrio.** Adrián también fija un CPA objetivo para que la campaña se apague sola [KgpaT1id63w].

---

## 6.3 · Los 5 errores más típicos en una primera campaña con cuenta nueva
| # | Error | ¿Lo estáis cometiendo? |
|---|---|---|
| 1 | Tocar antes de las 72 h (presupuestos, público, anuncios) por nervios del día 1 | **No:** la regla lo impide. El riesgo es el día 1 con 0 compras: es normal. |
| 2 | Decidir con 1 o 2 compras | **En parte.** Ver nota 17. |
| 3 | Lanzar sin haber visto la medición completa | **Sí:** nunca habéis visto un Purchase (apartado 2). |
| 4 | Dejar que Meta cambie el anuncio (mejoras de Advantage+, catálogo, textos generados) | **No**, si revisáis después de duplicar. Si no, lo que se prueba es otro anuncio, y puede llegar un rechazo por un texto que no habéis escrito. |
| 5 | Cuenta nueva con datos que faltan o pagos que fallan: anuncios parados o cuenta restringida | **En parte.** Ver nota 18. |

**Nota 17 · Decidir con pocas compras.** Con 30 € por conjunto, una compra de más o de menos parte el CPA por la mitad o lo duplica. Se decide con el embudo.

**Nota 18 · Datos de la cuenta.**
- Falta «Beneficiario y pagador».
- Comprobad la tarjeta, la moneda y la zona horaria.
- Lo demás está bien: no cambiar diez cosas a la vez y no crear varias cuentas.

Uno más que no os pasa: lanzar justo antes del Black Friday sin contar con que el CPM sube. Ya está en el plan.

---

## 6.4 · Lista de comprobación antes de pulsar «Publicar» (en el orden de la pantalla)
Los nombres de los botones pueden variar un poco en vuestra interfaz [NO SEGURO].

**Antes de entrar en el Administrador de anuncios**
1. **Configuración de la cuenta publicitaria:**
   - moneda EUR y zona horaria Europa/Madrid;
   - método de pago añadido;
   - límite de gasto de la cuenta de 200 €.
2. **Shopify:**
   - el tema publicado, con las plantillas `?view=champu / tinte / piel` dentro;
   - Eventos de clientes: la app de Meta «Conectada»;
   - la app: píxel Trebolly, nivel Máximo;
   - zonas de envío sin Canarias, Ceuta ni Melilla (probado con una dirección).
3. **Administrador de eventos:**
   - comprobaciones a)-d), con la tienda publicada y la URL real del anuncio;
   - el Purchase visto (o el primer pedido vigilado).

**Campaña**
4. Crear → Ventas → configuración manual.
5. Nombre: TRE-CABEZAL-20261119-ABO.
6. Categorías especiales: ninguna.
7. Tipo de compra: subasta.
8. Prueba A/B: desactivada.
9. Presupuesto: de conjunto (Advantage+ de campaña desactivado).
10. Límite de gasto de la campaña: 95 €.

**Conjunto (repetir en TRE-champu, TRE-tinte y TRE-piel)**
11. Nombre del conjunto.
12. Ubicación de la conversión: sitio web.
13. Objetivo de rendimiento: maximizar el número de conversiones.
14. Conjunto de datos: Trebolly (3642013049295879), no los viejos. Evento: Compra.
15. Puja: mayor volumen, sin objetivo de coste.
16. Atribución: la de por defecto.
17. Presupuesto diario: 10 €. Inicio: 19-nov a las 00:00 (Madrid). Sin fecha de fin.
18. **Público Advantage+:**
    - sugerencia: mujeres de 25 a 65 años;
    - controles: España, excluyendo Canarias, Ceuta y Melilla;
    - edad mínima 18;
    - excluir «Compradores 180 d»;
    - idioma sin tocar.
19. Ubicaciones: Advantage+.
20. **Beneficiario y pagador**, el mismo en los tres.

**Anuncio (repetir en A1-champu-v2, A2-tinte-v2 y A3-piel-v1)**
21. Nombre del anuncio.
22. Identidad: página Trebolly + Instagram @trebolly.
23. Configuración: crear anuncio · imagen o vídeo único · sin catálogo.
24. Contenido: el vídeo 9:16 para Stories y Reels y el 4:5 para el feed. Revisad las zonas seguras en la vista previa.
25. **Mejoras creativas de Advantage+:** abrir el panel y apagarlas una a una, incluida «añadir artículos del catálogo».
26. Texto principal, título y descripción (anexo A).
27. La casilla de contenido generado con IA, si aparece.
28. Destino: sitio web, con la URL `…/products/…?view=<ángulo>`.
29. Botón: Comprar.
30. Parámetros de URL: los UTM, con el `utm_content` del ángulo.
31. Seguimiento: Trebolly marcado en «Eventos del sitio web».
32. Vista previa en el móvil: tocar el botón y comprobar la URL final, la carga y la ficha.

**Publicar**
33. Comparad los tres conjuntos: solo deben cambiar el nombre, el anuncio y el `utm_content`. Publicad todo junto antes de las 00:00.
34. **Por la mañana:**
    - los tres anuncios aprobados y con impresiones;
    - y el gasto de cada conjunto (si uno lleva menos del 60 %, es el solapamiento: no se toca).
    - Un anuncio rechazado es un «fallo técnico» de la regla.

---

## Anexo A · Textos por ángulo, listos para pegar
Las reglas que cumplen:
- **Sin hablar de cómo está la piel o el pelo de quien lo ve** (política de atributos personales).
- **Sin promesas de salud.** El cloro «puede» apagar o resecar: no se dice que lo haga siempre.
- **Sin aduanas ni origen.**
- **Lo que se lee sin desplegar** (los primeros ~125 caracteres) es el gancho.

Para los tres ángulos:
- **Título:** `2 cabezales + 10 filtros · 59,95 €`
- **Descripción:** `Envío gratis · 14 días para devolverlo`
- **Línea opcional, solo si el regalo está activo en la tienda:** `Hasta el 30 de noviembre, +6 filtros de regalo con el pack de 2.`

**A1 · Champú**
```
Tu champú no tiene la culpa. Mira el agua de tu ducha.

Este cabezal lleva un filtro en el mango que retiene parte del cloro. Y además:
· cepillo de silicona para masajear mientras te lavas
· botón STOP para pausar el agua sin tocar el grifo
Se enrosca a mano en la manguera de siempre, sin fontanero.

2 cabezales + 10 filtros: 59,95 €. Envío gratis con seguimiento.
```

**A2 · Tinte**
```
El cloro del agua puede apagar el color del tinte y de las mechas, lavado tras lavado. Mira el agua.

Este cabezal lleva un filtro en el mango que retiene parte del cloro. Y además:
· cepillo de silicona para masajear mientras te lavas
· botón STOP para pausar el agua sin tocar el grifo
Se enrosca a mano en la manguera de siempre, sin fontanero.

2 cabezales + 10 filtros: 59,95 €. Envío gratis con seguimiento.
```

**A3 · Piel**
```
La crema no lo arregla todo. Mira el agua de tu ducha: el cloro puede resecar la piel, ducha tras ducha.

Este cabezal lleva un filtro en el mango que retiene parte del cloro. Y además:
· cepillo de silicona para masajear mientras te lavas
· botón STOP para pausar el agua mientras te enjabonas
Se enrosca a mano en la manguera de siempre, sin fontanero.

2 cabezales + 10 filtros: 59,95 €. Envío gratis con seguimiento.
```

---

## Fuentes
- [Shopify · Facebook data sharing (niveles Estándar, Mejorado y Máximo)](https://help.shopify.com/en/manual/promoting-marketing/analyze-marketing/meta-data-sharing)
- [Dataslayer · Meta location fees (julio de 2026)](https://www.dataslayer.ai/blog/meta-location-fees-the-extra-charge-hitting-your-ad-invoices-in-july-2026)
- [Jon Loomer · Meta location fees](https://www.jonloomer.com/meta-location-fees/)
- [Search Engine Land · Meta traslada los impuestos digitales a los anunciantes](https://searchengineland.com/meta-is-passing-europes-digital-taxes-directly-to-advertisers-471303)
- [Jon Loomer · Advantage+ campaign creation](https://www.jonloomer.com/advantage-plus-campaign/)
- [Jon Loomer · Meta Ads attribution 2026](https://www.jonloomer.com/meta-ads-attribution-2026/)
- [AdNova · Meta attribution change 2026](https://www.adnova.ai/blogs/meta-attribution-change-2026)
- [JumpFly · por qué vuelven a aparecer los ajustes de Advantage+](https://www.jumpfly.com/blog/metas-advantage-settings-why-they-keep-reappearing-and-how-to-stay-in-control/)
- [PPC Land · el anunciante, responsable de los retoques de IA de Meta desde el 30-oct](https://ppc.land/meta-makes-advertisers-solely-responsible-for-its-ai-ad-edits-from-oct-30/)
- [Meta · Expanding GenAI transparency for ads (feb-2025)](https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/)
- [Jon Loomer · casilla de aviso de IA](https://www.jonloomer.com/ai-disclosure-checkbox-chatgpt-attribution/)
- [Superads · CPM en España](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/spain)
- [Superads · CPC en España](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/spain)
- [Creatify · CPC, CPM y CTR buenos en Meta](https://creatify.ai/es/blog/what-is-a-good-cpc-cpm-and-ctr-for-meta-ads)
- [AEAT · ventanilla única de importación, umbral de 150 €](https://sede.agenciatributaria.gob.es/Sede/en_gb/ayuda/manuales-videos-folletos/manuales-practicos/manual-importacion-exportacion-envios-escaso-valor/3-mecanismos-recaudacion-iva/3_1-regimen-ventanilla-unica-importaciones/3_1_4-umbral-150.html)
- Mentores (notas en `ebooks-drop-organico/conocimiento/general/`):
  - Marc: [0gOn8a_xFA8], [kq0bZo65WNM], [oEFWZdCw5FQ];
  - Dani: [nnXqHmYlmvA], [n5gORsrA_xc], [CKiR67QoZ9U], [8Er-sAVrULo];
  - Adrián: [KgpaT1id63w], [wWC8SoeQ_Fk].
