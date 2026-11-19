# Velocidad de la ficha y métricas del día 1 · revisión (19-nov)
**Marcas:** [EXPERIENCIA] = criterio propio, sin fuente · [NO SEGURO] = no comprobado · [CÁLCULO] = con vuestros datos. Deciden los fundadores.

## Lo que más importa
1. **Si la pérdida de clics es real, no hay conversión que la arregle** [CÁLCULO].
   - Con el CPA de equilibrio de 19,6 € y un CPC de 0,57 € (piel), hacen falta 2,9 compras por cada 100 clics.
   - Si solo llega el 31 % de los clics, hacen falta 9,3 compras por cada 100 visitas. Lo normal es 1-3 [EXPERIENCIA]; Dani pone el ejemplo de pasar del 1,5 % al 3 % [CKiR67QoZ9U].
   - Por eso la velocidad y la medición van antes que cualquier decisión sobre los anuncios.
2. **La regla de las 48 h ya no se cumple con estos CPM:**
   - «≥ 2.000 impresiones» se calculó con un CPM de 7-10 €, pero el real es de 20-26 €. Cada conjunto hace ~410-560 impresiones al día, así que a las 48 h llevará ~800-1.100.
   - «0 carritos» con 1-3 visitas mata un anuncio por azar: con un 8 % de carritos por visita, la probabilidad de 0 carritos con 3 visitas es del 78 %.
3. **Tinte:** si Audience Network se quitó solo en tinte, los tres conjuntos ya no son iguales, y además se reinició su aprendizaje.

## 1) Los dos cambios: sí, con matices
- **fetchpriority=high: sí, pero ganará poco.**
  - El retraso de carga ya es de 240 ms y la carga de 190 ms; el problema está en el renderizado (1.950 ms).
  - Comprobad que en ?view=champu, tinte y piel la imagen con fetchpriority es la que realmente se ve primero (si cada vista ordena las fotos de otra forma, puede no serlo).
- **Fuentes asíncronas: sí. Probablemente es el cambio que más baja el retraso de renderizado.**
  - Un `<link rel=stylesheet>` en el body bloquea el pintado de todo lo que va detrás, galería incluida. Encima, Google Fonts abre conexión con otro dominio.
- **Riesgos:**
  - **Parpadeo de fuente:** el texto sale primero en la fuente del sistema y luego cambia. Con display=swap ya podía pasar.
  - **CLS:** puede subir de 0 a algo si la fuente cambia de medidas al cargar; por debajo de 0,1 sigue estando bien [EXPERIENCIA]. Miradlo con la red lenta.
  - **onload:** funciona en los navegadores de Instagram y Facebook (iOS usa el motor de Safari y Android, Chromium). Si no hay JS, entra el `<noscript>`. Riesgo muy bajo.
  - **5 secciones con 5 preload:** si la URL es la misma, el navegador la reutiliza, pero es sobrante. Si cada sección pide familias o pesos distintos, son 5 peticiones. Mejor una sola en el `<head>`.
- **La puntuación de PageSpeed varía bastante de una vez a otra:** medid 3 veces cada URL y quedaos con la del medio [EXPERIENCIA].
- **El LCP de 6,2 s es simulado** (móvil lento y 4G lento).
  - El desglose (TTFB de 10 ms + 240 + 190 + 1.950 = 2,4 s) parece medido sin esa simulación [NO SEGURO].
  - En un móvil normal estará más cerca de 2,5-4 s [EXPERIENCIA]. Aun así, merece la pena arreglarlo.

## 2) Para bajar los 1,95 s de retraso de renderizado (de más impacto a menos, y con su riesgo)
1. **Ver qué frena el pintado (5 min, sin riesgo).**
   - PageSpeed → «Ver traza», o Chrome → Rendimiento con la red y la CPU ralentizadas: qué termina justo antes del pintado del LCP.
   - Prueba rápida: desactivar JavaScript. Si la foto sale al momento, algo de JS la está escondiendo.
2. **Animaciones o slider que esconden la foto. Impacto alto si es la causa; riesgo bajo.**
   - Las animaciones al hacer scroll del tema, o un pz-slider que pone la foto en opacidad 0 hasta que arranca, retrasan el LCP justo así.
   - La primera foto tiene que verse sin esperar a ningún JS.
3. **pz-tienda.css, pz-ola.css y pz-extra.css, una sola vez y en el `<head>`. Impacto medio-alto; riesgo bajo-medio** (cambia el orden del CSS: revisad la ficha entera).
   - Mientras estén en el body y por delante de la galería, la bloquean.
4. **Fuentes. Impacto medio; riesgo bajo.**
   - Una sola petición en el `<head>`, solo con los pesos que se usan.
   - Quitar una familia si es posible (Fraunces, si es solo para un detalle).
   - preconnect a fonts.gstatic.com con crossorigin.
   - Mejor aún: alojarlas en el propio tema o usar la biblioteca de fuentes de Shopify, si las tiene [NO SEGURO]. Así no se abre otra conexión.
5. **HTML de 277 KB. Impacto bajo-medio; riesgo bajo.** Quitar los `<link>` repetidos y los `<style>` en línea que estén duplicados.
6. **compiled_assets/styles.css (296 KB). Impacto medio en PageSpeed; riesgo medio.**
   - Shopify junta ahí el CSS de los `{% stylesheet %}` de todas las secciones del tema, se usen o no [EXPERIENCIA].
   - Hay que borrar las secciones que no se usan en ninguna plantilla, comprobándolo antes.
7. **JS de terceros. Impacto bajo-medio.**
   - Si el pop-up de Klaviyo sigue en borrador y los flujos salen del pago abandonado (que llega desde Shopify), el JS de Klaviyo en la web solo sirve para «producto visto» y para el pop-up. Apagarlo es decisión de los fundadores.
   - Quitad los preconnect que sobren.
8. **No tocar:** base.css, overflow-list.css y el CSS del pago rápido (accelerated-checkout). Quitarlo supone quitar los botones de pago exprés, y eso puede costar ventas.

- **Antes de publicar cada ronda:** probad en una copia del tema, en 2 móviles y en el navegador de Instagram.
- **Después de publicar:**
  - el carrito, el pago y el banner de cookies;
  - en Probar eventos, que llegan ViewContent y AddToCart;
  - y que Klaviyo y Clarity siguen activos (si van por app embed, son del tema).

## 3) ¿Tocar el tema con la campaña en marcha?
- **El aprendizaje de Meta no se reinicia.** Solo se reinicia con cambios en la campaña, el conjunto o el anuncio (presupuesto, público, creativo, evento o URL de destino) [EXPERIENCIA]. No cambiéis la URL de los anuncios.
- **La comparación entre ángulos sigue siendo justa:** los tres llevan a la misma tienda.
- **Lo que sí cambia son las cifras absolutas** (visitas por clic y conversión). Apuntad la hora exacta de cada publicación y leed el antes y el después por separado.
- **Mi voto:**
  - publicar ya la ronda 1 (bajo riesgo), probada antes en la copia;
  - la ronda 2 (mover el CSS al `<head>` y recortar styles.css), solo probada en la copia, y mejor después de la lectura de las 72 h. La excepción: que la ronda 1 no mejore la llegada de clics.
- **Comprobad que la URL de los anuncios es exactamente el dominio principal.** Si trebolly.com redirige a www.trebolly.com, o al revés, cada clic suma una redirección que retrasa la carga [EXPERIENCIA].

## 4) La pérdida entre clics y visitas
- **Con 35 clics no se puede repartir la culpa.** 11/35 = 31 %, con un margen de error del 19 al 48 % [CÁLCULO, intervalo de Wilson al 95 %].
- **Lo que esperaría** [EXPERIENCIA]:
  - sin banner y con una web rápida llega el 70-85 %;
  - con el banner de la UE, Meta solo cuenta a quien acepta (en España suele ser algo más de la mitad, según el diseño del banner).
  - Por tanto, con banner, ~40-50 % sería normal. Un 31 % sugiere que también se pierde gente por la carga, pero la muestra no lo demuestra.
- **Shopify cuenta 10 sesiones y Meta 11 visitas, una cifra casi igual.** Eso apunta a que las dos dependen del consentimiento, o a que de verdad no llega más gente.
- **Cómo distinguirlo:**
  1. **Prueba de 5 minutos:** abrid la URL del anuncio (con sus UTM, sin hacer clic en el anuncio) desde el móvil, rechazad las cookies y mirad si Shopify os cuenta en «Vista en vivo».
     - Si os cuenta, Shopify mide sin consentimiento, y sus sesiones son la llegada real. En ese caso, 10 de 35 sería pérdida por velocidad.
     - Si no os cuenta, Shopify también depende de las cookies y no sirve para separar las dos causas.
  2. **Antes y después de la velocidad:** con el mismo banner, si la proporción de visitas por clic sube después de publicar la ronda 1, la diferencia es lo que se perdía por velocidad.
     - Hacen falta ~100 clics por lado para que se vea con claridad [EXPERIENCIA].
  3. **Carga real:** abrid la ficha 5 veces desde un DM de Instagram, con 4G, y cronometrad cuándo sale la foto.
     - Por encima de 3 s, la velocidad pesa [EXPERIENCIA].

## 5) Píxel, sin código propio
- **Lo hecho está bien:** la coincidencia avanzada automática.
- **El nombre del nivel de datos:** si la app ofrece uno por encima de «Optimizado (Recomendado)», poned ese. No sé cómo se llaman hoy [NO SEGURO].
- **No persigáis la calidad de coincidencia de PageView.** Una visita anónima solo tiene IP, navegador y cookies.
  - La que importa es la de Purchase.
  - Con pedidos reales (email, teléfono, dirección) suele estar en 7-9 [EXPERIENCIA]; el 5,7 sale de pedidos de prueba.
  - Miradla con los primeros pedidos reales.
- **«Poca cobertura de PageView por la API de conversiones»:**
  - con la app oficial no se arregla sin herramientas de pago para el servidor, y no hace falta: se optimiza a Compra;
  - lo que hay que vigilar es la cobertura de Purchase por servidor, con pedidos reales.
- **Haced las acciones que proponga el Administrador de eventos** (Calidad de los datos) que se puedan resolver con los interruptores de la app.

## 6) Métricas del día 1
- **CPM de 20-26 €:**
  - es 2-3 veces la media de España (~7,6 €, Superads) y el doble del límite de Marc (10 €) [0gOn8a_xFA8];
  - con cuenta nueva, optimizando a compra y la semana antes del Black Friday, es esperable;
  - suele bajar en los primeros días [EXPERIENCIA]. No decidáis por el CPM del día 1.
- **Champú:**
  - un CPC de 2,15 € necesitaría un 11 % de compras por clic: hoy no sería viable [CÁLCULO];
  - pero son 5 clics y un CTR de 1,22 % (ámbar, no rojo);
  - el CPM más alto viene de su CTR más bajo (Meta cobra más por enseñar un anuncio que recibe menos clics).
  - **Candidato a apagar a las 72 h, sí; a las 48 h, no.**
- **Piel:**
  - el mejor embudo (1,34 € por visita según Meta, 2 llegan al pago);
  - mirad en Shopify, en «Pagos abandonados», en qué paso se fueron esos 2 (envío o pago) y desde qué provincia;
  - comprobad que les ha llegado el email 1 de Klaviyo.
  - Si se ha ido por el paso del pago o por un error, es un problema de la tienda, no del anuncio.
- **Piel «recibe más»:**
  - con D-077, subir exige ≥ 6 compras y un ROAS ≥ 3,8;
  - a las 72 h, como mucho se mantiene a 10 €/día. No se sube por el CTR.
- **Cambios de regla propuestos (deciden los fundadores):**
  - 48 h: «CTR de enlace ≤ 0,4 % con ≥ 800 impresiones o ≥ 15 € gastados», en vez de 2.000 impresiones;
  - 48 h: «0 carritos con ≥ 15 visitas (o ≥ 25 clics) mientras los otros tienen».
- **Tinte y Audience Network:**
  - quitarla fue razonable (9 de 20 clics, y casi ninguno llega);
  - pero, si fue solo en tinte, la comparación ya no es igual: o se quita en los 3 a la vez, o se lee tinte aparte desde la hora del cambio.
