# Montaje de la tienda · The Sunday Sheet · guía para Fran (plan B)

_03-nov-2026. La herramienta de Shopify no está conectada, así que esta guía la sigues tú en el panel de Shopify. Todo queda en **BORRADOR** y con la **contraseña de la tienda activada**: nadie ve nada hasta que tú lo decidas._

**Cómo leer esta guía**
- **⚠** = necesita tu "sí" explícito o cuesta dinero. No sigas sin decidirlo.
- **[VERIFICADO]** = comprobado en la ayuda oficial de Shopify (3-nov-2026).
- **[SIN VERIFICAR]** = el nombre del menú sale de lo que sabemos de Shopify, pero no se pudo comprobar (la ayuda oficial bloqueó la lectura o la tienda no está conectada). Si en tu pantalla se llama distinto, busca algo parecido o usa el buscador de arriba del panel de Shopify.
- Lo que va entre `comillas de código` se copia y se pega tal cual (está en inglés porque la tienda es en inglés).
- "Cómo saber que está bien" cierra cada paso.

**Avisos importantes antes de empezar (lo que hoy falta)**
1. **No existen todavía** la carpeta `tienda/imagenes/en/` ni los PDF `ebook/en/the-sunday-sheet.pdf`, `ebook/en/the-sunday-sheet-printables.pdf` ni el PDF de la muestra. Los pasos 4, 5 y 6 se pueden preparar, pero **no terminar** hasta que Claude los genere (módulo de maquetar PDF e imágenes). Los pasos 1, 2, 3, 7, 8, 9 y 10 sí se pueden hacer ya.
2. Nombres de menús de Shopify: la ayuda oficial solo se pudo leer en parte. Lo verificado: la app de descargas ahora se llama **"Digital Products"** (antes "Digital Downloads") y **Shopify Email** ahora se llama **"Shopify Messaging"**. El resto está marcado.
3. **Datos del titular** (nombre, NIF, domicilio, email, teléfono, nombre de la tienda): hasta que no los rellenes en los textos legales, **no se publica nada** (`legal/notas-internas.md`).

---

## 0) Antes de empezar

### Qué tener a mano
| Qué | Para qué |
|---|---|
| Tu email y una tarjeta o forma de pago | Crear la cuenta y pagar el plan (solo tú) |
| DNI/NIE, fecha de nacimiento, dirección en España, IBAN español, un selfie con el documento | Verificar Shopify Payments (paso 1.6). Solo tú |
| Los datos del titular: nombre completo, NIF, domicilio, email de contacto, teléfono | Rellenan los huecos `{{NOMBRE_TITULAR}}`, `{{NIF}}`, `{{DOMICILIO}}`, `{{EMAIL_CONTACTO}}`, `{{TELEFONO}}` de los textos legales |
| Nombre de la tienda (`{{NOMBRE_TIENDA}}`) | Lo pide Shopify al crear la cuenta y aparece en emails y legales. Si aún no lo has decidido, dilo en el chat y lo elegimos |
| La carpeta del proyecto abierta: `nichos/meal-prep/` | De ahí copias los textos |
| Un móvil iPhone y uno Android (tuyos o de un amigo) | Pruebas del paso 11 |
| Un segundo email tuyo (por ejemplo, otro Gmail) | Para hacer compras de prueba |
| Tiempo: unas 3 a 4 horas repartidas en 2 o 3 sesiones | |

### ⚠ Recordatorio: esto SOLO lo haces tú (Claude no lo hace)
- **Crear la cuenta** de Shopify.
- **Contratar el plan** (Basic) y poner tu tarjeta.
- **Instalar apps de pago** (o que pidan crear cuenta aparte).
- Verificar tu identidad en Shopify Payments.
- **Quitar la contraseña de la tienda (publicar)**: solo con tu "sí" explícito en el chat, y solo cuando `revision-tienda` esté aprobada.

### Reglas que no se rompen
- Todo en **borrador**. Contraseña de tienda **activada** siempre hasta publicar.
- Sin enlaces de afiliado. Sin reseñas, estrellas, precios tachados, cuentas atrás ni "quedan N".
- Tienda **solo en inglés**. Mercados: **EE. UU. + Unión Europea**. **Reino Unido cerrado.**

---

## 1) Crear tienda y plan

### 1.1 ⚠ Crear la cuenta (solo Fran)
1. Entra en `shopify.com` y pulsa **Start for free** (o "Empezar gratis").
2. Escribe tu email, una contraseña y el **nombre de la tienda**.
3. Responde las preguntas del asistente como quieras (no importan; elige "Estoy empezando / no vendo aún" si lo hay).
4. **Cómo saber que está bien:** ves el panel de Shopify (**Admin**) con el menú de la izquierda: Home, Orders, Products, Customers, Marketing, Discounts, Content, Markets, Analytics, Online Store…, y abajo **Settings**.

### 1.2 ⚠ Elegir el plan (gasto, solo Fran)
- Plan recomendado: **Basic** (`conocimiento/09-numeros/datos-costes.md`).
- Precio orientativo de las fuentes: unos **24 €/mes pagando el año entero** (288 €/año) o unos **32 €/mes pagando mes a mes** [BUSCADOR, sin verificar]. Hay una oferta de prueba (unos días gratis y luego unos meses a 1 $/mes) pero las fuentes se contradicen: **no cuentes con ella**.
- Haz clic: **Settings (abajo a la izquierda) → Plan**. Verás el precio real en tu pantalla. **Mira el precio y la fecha del primer cobro antes de aceptar. No pagues el año entero hasta tener claro que sigues adelante**: empieza mes a mes.
- **No contrates Starter** (no es un plan de tienda completa).
- **Cómo saber que está bien:** en Settings → Plan pone "Basic".

### 1.3 Datos de la tienda
1. **Settings → Store details**. Rellena nombre de la tienda, email de contacto y **dirección** (tu domicilio, el mismo que en los textos legales).
2. **Store currency:** ponla en **US Dollar (USD)**. ⚠ **Aviso:** Shopify Payments en España cobra y te paga en euros [`conocimiento/03-tienda/datos-shopify.md`]. Puede que Shopify no te deje vender en dólares como moneda principal con una cuenta española, o que convierta el cobro. **Si no te deja elegir USD o ves un aviso, para y dime qué ves**: hay que decidirlo (precio en € para la UE, o activar "monedas locales" en Mercados). No lo fuerces.
3. **Cómo saber que está bien:** en Store details aparece tu dirección y la moneda USD sin avisos rojos.

### 1.4 Idioma
1. **Settings → Languages** [SIN VERIFICAR el nombre exacto]. Idioma por defecto de la tienda: **English**. **No añadas español** (la tienda ES vendrá más tarde y con otros textos).
2. El idioma de tu panel de administrador (para que lo veas en español) se cambia en tu perfil (esquina superior derecha → tu nombre → idioma). Eso no cambia la tienda.
3. **Cómo saber que está bien:** en Languages solo sale English.

### 1.5 Contraseña de la tienda (activarla ya)
1. **Online Store → Preferences** y baja a **Password protection** [SIN VERIFICAR; si no lo ves, busca "password" en el buscador del panel].
2. Marca **Restrict access to visitors with the password**.
3. Escribe una contraseña (anótala; la usarás en las pruebas) y un mensaje corto, por ejemplo: `We're getting ready. Back soon.`
4. Pulsa **Save**.
5. **Cómo saber que está bien:** abre la dirección `xxxx.myshopify.com` de tu tienda en una ventana privada: pide la contraseña.

### 1.6 ⚠ Cobros: Shopify Payments (solo Fran, con tu identidad)
- Decisión tuya del 15-oct-2026: **solo Shopify Payments** al inicio (sin PayPal: así no hay comisión extra de terceros).
- **Settings → Payments → Shopify Payments → Activate / Complete account setup** [SIN VERIFICAR el nombre exacto].
- Te pedirá: nombre legal, fecha de nacimiento, dirección en España, selfie con documento, prueba de domicilio, IBAN español [`datos-shopify.md`]. Elige el tipo de cuenta **Individual / Sole trader** si no estás dado de alta como autónomo (si no sabes si tienes que darte de alta, es **pregunta para el gestor**; Shopify no lo resuelve).
- Desde junio de 2026, en cuentas nuevas tienes **90 días desde el primer pedido** para terminar la verificación, o los pedidos pueden reembolsarse solos [`datos-shopify.md`].
- **No actives cobros reales todavía**: para las pruebas del paso 11 se usa el modo de prueba (**Test mode**) de Shopify Payments, que solo deja usar tarjetas de prueba [SIN VERIFICAR dónde se activa: suele estar en Settings → Payments → Manage].
- **Cómo saber que está bien:** Settings → Payments muestra Shopify Payments como "Active" o "Test mode", y no hay avisos rojos.

---

## 2) Tema gratuito y marca

Datos de `marca.json`: verde hoja `#1F3A2E` (principal) · naranja pimentón `#D9572B` (acento) · crema `#FAF6EF` (fondo suave) · títulos **Inter** · texto **Source Serif 4**.

### 2.1 Elegir el tema
1. **Online Store → Themes** [VERIFICADO: la ayuda dice que el tema por defecto es **Dawn**, gratuito].
2. En **Current theme** deja **Dawn** (gratis). **No compres ningún tema.** ⚠ Un tema de pago = gasto = necesita tu "sí".
3. **No toques el código** (nada de "Edit code" en el tema). Todo se hace con **Customize** (el editor visual).
4. **Cómo saber que está bien:** el tema actual dice "Dawn" y "Free".

### 2.2 Colores
1. En el tema, pulsa **Customize**. A la izquierda, el icono de **Theme settings** (brocha/engranaje) → **Colors**.
2. En el esquema de colores principal (**Scheme 1** o el que se use por defecto):
   - **Background:** `#FAF6EF`
   - **Text:** `#1F3A2E`
   - **Solid button background:** `#1F3A2E` (verde) · **Solid button label:** `#FFFFFF`
   - **Outline button:** `#1F3A2E`
   - **Accent / links:** `#D9572B`
3. Decisión nuestra: el botón "Buy now" va en **verde con letra blanca** (se lee mejor); el naranja se usa en detalles y enlaces, porque con letra blanca el contraste del naranja queda justo. Si prefieres botón naranja, es tu elección.
4. **Cómo saber que está bien:** fondo crema, letras verde oscuro, botón verde.

### 2.3 Fuentes
1. Theme settings → **Typography**.
2. **Headings:** `Inter`. **Body:** `Source Serif 4` [SIN VERIFICAR que esté en la lista de Shopify: si no aparece, elige la serif más parecida de la lista y anótalo en `memoria/decisiones.md`].
3. **Cómo saber que está bien:** los títulos son sin serifa (Inter) y los párrafos con serifa.

### 2.4 Logo y favicon
- Logo: **Theme settings → Logo**. Hoy **no hay logo hecho**. Mientras tanto, el nombre de la tienda en texto sirve. Pídelo en el chat si quieres que Claude prepare uno.
- Favicon: **Theme settings → Favicon** (imagen cuadrada de 32×32 píxeles o más). Igual: pendiente de crear.

### 2.5 Página de inicio (sencilla, lleva al producto)
En **Customize → Home page**:
1. Deja solo estas secciones: **Image banner**, **Featured product** (The Sunday Sheet, cuando exista) y el pie.
2. Banner: titular `The Sunday Sheet`, texto `Meal prep in about 2 hours, with the protein counted`, botón `See what's inside` que enlaza al producto.
3. Borra las demás secciones de ejemplo (colecciones, vídeo, suscripción de ejemplo…).
4. **Cómo saber que está bien:** la portada tiene 2 o 3 bloques y un único botón que lleva al producto. En móvil (icono del móvil arriba del editor) se lee sin cortarse.

---

## 3) Mercados e impuestos

### 3.1 Mercados: EE. UU. + UE, sin Reino Unido
1. **Markets** (menú izquierdo) [SIN VERIFICAR el nombre exacto: hoy se llama **Markets**].
2. Deja o crea **dos mercados**:
   - **United States** (EE. UU.).
   - **European Union**: todos los países de la UE. **No añadas United Kingdom ni ningún otro país.**
3. Si existe un mercado "International" o "Rest of world" activo, **desactívalo / elimínalo**, para que nadie fuera de EE. UU. y la UE pueda comprar (el Reino Unido, en concreto: tiene IVA desde la primera venta y está cerrado, `conocimiento/07-legal/02-analisis.md`).
4. ⚠ **EE. UU.: decisión tuya, con el gestor.** Antes de dejar EE. UU. activo, el gestor debe confirmar el *sales tax* (¿algún estado obliga a recaudar con pocas ventas?; `legal/notas-internas.md` punto 1). Si el gestor aún no ha contestado, **deja EE. UU. creado pero desactivado** y activa solo la UE.
5. En cada mercado, mira la opción de **moneda/precios**: precio en **USD** igual para todos, para que sea **$24.99 en todas partes**. Si Shopify te ofrece "convertir automáticamente" a euros, **desmárcalo** (el precio de la página es 24,99 USD) [SIN VERIFICAR; relacionado con el aviso del paso 1.3].
6. **Cómo saber que está bien:** en Markets solo hay "European Union" y "United States". Con una dirección de Londres, el checkout de prueba no deja comprar (paso 11).

### 3.2 Impuestos
1. **Settings → Taxes and duties** [VERIFICADO: la ayuda dice "Settings > Taxes and duties"].
2. Sección **European Union** (en *Regional settings*) [VERIFICADO] → **Collect VAT**. Elige cómo registrarte:
   - Si **no has superado 10.000 € de ventas a otros países de la UE**, la ayuda oficial dice que puedes cobrar el IVA de tu país (microempresa) o registrarte en OSS [VERIFICADO].
   - ⚠ **Esto lo decide el gestor**, no lo adivines. Si no lo sabes, deja el IVA sin configurar y **no actives la UE** hasta que conteste.
3. **Precios con IVA incluido** en la UE: busca la opción **Include sales tax or VAT in prices** (o "All prices include tax") para el mercado UE [SIN VERIFICAR el nombre]. Debe estar **marcada**: el cliente de la UE ve **$24.99 con IVA incluido**. Para EE. UU. el *sales tax* se **añade** al pagar (no incluido). Es lo que dicen la página de producto y las condiciones.
4. **Producto digital:** en el producto (paso 4) deja marcada la casilla **Charge tax on this product** [SIN VERIFICAR el nombre exacto]. En la UE los productos digitales se gravan en el país del cliente [`datos-shopify.md`].
5. ⚠ **Duda abierta para el gestor (no la resuelvas tú):** el ebook va al 4 % de IVA; el pack imprimible (hojas, listas) podría ir al 21 % (`legal/notas-internas.md` punto 4). Hasta que conteste, **no actives ventas reales** a la UE.
6. **Cómo saber que está bien:** en Taxes and duties aparecen la UE (y EE. UU. si lo has activado) sin avisos rojos, y en una compra de prueba desde la UE el precio final es **$24.99** con la línea "includes VAT".

---

## 4) Producto principal: The Sunday Sheet (campo a campo)

**Dónde:** **Products → Add product**. Todos los textos salen de `tienda/pagina-producto.md`: copia **solo los bloques "TEXTO FINAL"**. Todo lo demás de ese archivo (notas, declaración, revisión) **no se pega**.

Antes de empezar: completa los huecos `{{...}}`. Las rutas de enlaces que usaremos (se crean en el paso 7):
- Condiciones de venta → `/policies/terms-of-service`
- Desistimiento → `/pages/withdraw-from-the-contract`

### 4.1 Campos de arriba abajo
| Campo de Shopify | Qué poner |
|---|---|
| **Title** | `The Sunday Sheet` |
| **Description** | Pega, en este orden, los bloques "TEXTO FINAL" de: **Sección 1** (desde `## Meal prep in about 2 hours...` hasta "Before you buy"; **sin** el titular `# The Sunday Sheet`, que ya es el Title, y sin la línea `[ Buy now ]`, que es el botón de Shopify) · **Sección 2** (What you'll cook) · **Sección 3** (One plate, in full numbers) · **Sección 4** (The printable pack) · **Sección 5** (Why it works + Made for you if…) · **Sección 6** (Look inside + Try one Sunday first; ver aviso en 5.3) · **Sección 9** (aviso en cursiva). La **Sección 8** (acordeones) va aparte, en el paso 4.4. Si el editor no admite tablas, conviértelas en listas con viñetas. |
| **Media** | Las 5 imágenes, en este orden (paso 4.2) |
| **Price** | `24.99` |
| **Compare-at price** | **Vacío.** Nunca precio tachado |
| **Charge tax on this product** | Marcada |
| **Inventory** | Desmarca **Track quantity** (es digital, no se agota) |
| **SKU** | `SUNDAY-SHEET-01` |
| **Shipping** | **Desmarca** "This is a physical product" [VERIFICADO: la ayuda dice que se desmarca "Producto físico" en la sección Envío] |
| **Variants** | Ninguna (un solo producto, un solo precio) |
| **Status** | **Draft** (borrador) |
| **Sales channels** | **Online Store** marcado |
| **Product category** | Busca "Books" / "Digital" y elige la categoría de libros o contenido digital que ofrezca [SIN VERIFICAR el nombre] |
| **Product type** | `Digital ebook` |
| **Vendor** | El nombre de la tienda |
| **Collections** | Vacío (por ahora) |
| **Tags** | `ebook, meal-prep, digital` |
| **Search engine listing → Page title** | `The Sunday Sheet | Meal prep ebook with a 4-week plan` |
| **Search engine listing → Description** | `A 4-week meal prep plan with 60 recipes and 48 complete plates. Calories, protein and cost on every plate. Instant PDF download.` |
| **Search engine listing → URL handle** | `the-sunday-sheet` |

_Los textos de SEO los proponemos nosotros (no vienen de `pagina-producto.md`); no prometen resultados._

### 4.2 Imágenes (cuál va primero)
Carpeta: `nichos/meal-prep/tienda/imagenes/en/` (⚠ todavía no existe; hay que generarla). Súbelas arrastrando a **Media** y ordénalas así:

| Orden | Archivo | Texto alternativo (Alt text) |
|---|---|---|
| **1 (principal)** | `1-portada-vertical` | `The Sunday Sheet cover` |
| 2 | `2-escaparate-vertical` | `The Sunday Sheet on a tablet and a phone` |
| 3 | `3-incluye-vertical` | `What is included in The Sunday Sheet` |
| 4 | `4-perspectivas-vertical` | `Pages from inside The Sunday Sheet` |
| 5 | `5-extras-vertical` | `Printable extras included` |

Para poner el alt text: pulsa la imagen → **Add alt text**. Las versiones **cuadradas** (`3-incluye-cuadrado`, `5-extras-cuadrado`, `4-perspectivas-cuadrado`) van **dentro de la descripción**, justo encima de las secciones 2, 4 y 6 (icono de imagen del editor de texto). Para la sección 3 (plato de ejemplo) hace falta una captura real de la ficha del plato M1 del PDF final.
**Cómo saber que está bien:** en la ficha, la primera imagen es la portada; en móvil se desliza el resto.

### 4.3 Qué NO se pone (a propósito)
Estrellas, nº de reseñas, "bestseller", precio tachado, "ahorras", "valor 97 $", contadores, "quedan N", palabras de adelgazar, comparaciones con otras marcas. Si el tema añade un bloque de reseñas o de "stock bajo", **bórralo** del editor.

### 4.4 Acordeones (Details, Delivery, FAQ, Refunds and terms)
1. **Online Store → Themes → Customize →** en el selector de arriba elige **Products → Default product**.
2. En la sección **Product information**, pulsa **Add block → Collapsible row** [SIN VERIFICAR el nombre: en Dawn se llama así] cuatro veces.
3. Cada una: **Heading** y **Row content** con el texto de la **Sección 8** de `pagina-producto.md`:
   - `Product details`
   - `Delivery`
   - `FAQ` (preguntas y respuestas completas, pregunta en negrita)
   - `Refunds and terms`
4. En ese mismo editor: bloque **Price** visible y botón de compra (ver 4.5). Bajo el botón, el texto "Before you buy" ya va en la descripción.
5. Bajo el botón principal, pon un bloque de texto con `Not sure yet? Try the free sample first` enlazado a `#free-sample` (solo cuando la muestra esté lista; ver paso 5).

### 4.5 Botón "Buy now" y botón fijo en móvil
- En la ficha deja **Buy it now** (con **Add to cart** si el tema lo exige) [SIN VERIFICAR: en Dawn el botón dice "Add to cart"; para cambiarlo, en el editor del tema busca **Edit default theme content** y cambia el texto por `Buy now`].
- Botón fijo en móvil (Sección 10 de la página): si tu tema no lo incluye, **sáltalo**: no es imprescindible [SIN VERIFICAR]. No instales apps para esto (⚠ sería un gasto o una cuenta nueva).

### 4.6 Guardar y comprobar
1. Pulsa **Save**. El producto queda en **Draft**.
2. **Cómo saber que está bien:** en **Products** aparece "The Sunday Sheet · Draft · $24.99". Con **Preview** ves la ficha completa; no hay ningún `{{...}}` ni corchetes `[ ]` sin sustituir (busca con Ctrl+F: `{{` y `[`).

---

## 5) Muestra gratis a 0 €: The Mini Sunday

Fuente: `emails/en/montaje-emails.md` §2. El PDF sale de `ebook/en/muestra/the-mini-sunday.md` (⚠ falta maquetarlo a PDF).

### 5.1 Crear el producto
1. **Products → Add product**.
2. **Title:** `The Mini Sunday`.
3. **Description:** `The free sample of The Sunday Sheet: one protein, one base, one vegetable and three sauces, which makes three different plates. Includes its Sunday sheet, shopping list, storage times, cost and nutrition.`
4. **Price:** `0.00`. **Compare-at price:** vacío.
5. **Shipping:** desmarca "This is a physical product". **Track quantity:** desmarcado.
6. **Tags:** `mini-sample` (importante: el flujo de emails lo usa).
7. **Collections:** ninguna. **No lo pongas en ningún menú.**
8. **URL handle:** `the-mini-sunday`.
9. **Status:** **Draft**. Imagen: la portada de la muestra, cuando exista.
10. **Save.**
11. **Cómo saber que está bien:** "The Mini Sunday · Draft · $0.00", sin colección, con la etiqueta `mini-sample`.

### 5.2 Archivo y correo de entrega
El archivo se sube con la app de descargas (paso 6.4) y el email de entrega lleva el **Email 1** de `emails/en/secuencia.md` (paso 9.2).

### 5.3 Cómo llega la gente a la muestra
- Solo desde el botón **"Send me the sample"** de la sección "Try one Sunday first" de la página del producto (ancla `#free-sample`). El botón enlaza a `/products/the-mini-sunday`.
- ⚠ **Las dos casillas y la doble confirmación quizá no se puedan hacer solo con Shopify** (`montaje-emails.md` §2, puntos 4 y 5). Hay tres opciones; **elige una en el chat**:
  - **A.** Casilla de marketing nativa del checkout (sin marcar) + texto de "tengo 14 años o más" junto al botón de la muestra. Pregunta al gestor si basta.
  - **B.** Una app de formularios con dos casillas. ⚠ Solo con tu "sí" si implica instalar una app o crear una cuenta (posible coste).
  - **C.** No abrir la muestra todavía. La sección "Try one Sunday first" y el enlace bajo el botón se **quedan fuera** (no los pegues en la descripción hasta decidir).
- **Recomendación:** empezar con **C** y decidir A o B con el gestor.

### 5.4 Prueba obligatoria
Haz un pedido real de 0 $ con tu segundo email (paso 11.3). Hay que comprobar que un pedido digital de 0 $ no pide dirección de envío ni método de pago [SIN VERIFICAR].

---

## 6) App de descargas y archivos

### 6.1 ⚠ Instalar la app gratuita (necesita tu "sí")
- La app oficial gratuita se llama hoy **Digital Products** (antes "Digital Downloads") [VERIFICADO en help.shopify.com].
- Instalarla: **Settings → Apps → Shopify App Store** → busca `Digital Products` → **Install** [VERIFICADO]. Comprueba que pone **Free** y que el desarrollador es **Shopify**. Si pide pagar o crear otra cuenta, **para y avísame**.
- **Cómo saber que está bien:** en el menú izquierdo aparece **Apps → Digital Products**.

### 6.2 Qué PDF subir al producto The Sunday Sheet
Dos archivos (⚠ aún no existen; vendrán del módulo de maquetar):
1. `ebook/en/the-sunday-sheet.pdf` (el ebook, unas 165 págs., Letter)
2. `ebook/en/the-sunday-sheet-printables.pdf` (el pack imprimible, unas 30 págs., Letter y A4)

Antes de subirlos, ábrelos tú en el móvil: que se vean bien y el índice tenga enlaces. El límite es 5 GB en total y hasta 50 archivos por producto [VERIFICADO], de sobra.

### 6.3 Subir y configurar (producto de pago)
1. **Apps → Digital Products → Add assets → File** [VERIFICADO].
2. Sube los dos PDF y asócialos al producto **The Sunday Sheet** (si el producto ya existe: pulsa el producto → **Add an asset → File**).
3. Abre los ajustes de entrega (**delivery settings**):
   - **Delivery method:** `Send automatically` [VERIFICADO: el cliente recibe un email con el enlace tras el pago].
   - **Access limit:** `Limited` y escribe `5` en **Times per customer** [VERIFICADO el menú; el 5 es nuestra propuesta; por defecto es ilimitado]. Cuenta cada vez que se abre el enlace, no cada archivo. Pon el mismo número en `{{LIMITE_DESCARGAS}}` de los textos legales.
4. **Save.**
5. **Cómo saber que está bien:** el producto aparece en Digital Products con "digital file" y los dos PDF dentro.

### 6.4 Subir la muestra
Igual, en el producto **The Mini Sunday**, con el PDF de la muestra. Delivery: `Send automatically`. Access limit: `Limited`, `5`.

### 6.5 Descarga también en la página de "gracias"
1. **Apps → Digital Products → Settings → Digital products at checkout → Add** (abre el editor del checkout) [VERIFICADO].
2. Añade el bloque **Digital Products** en la página **Thank you** y en **Order status**. **Save.**
3. Esta función no está disponible en tiendas de desarrollo ni con el plan pausado [VERIFICADO].

### 6.6 Emails de la app
**Apps → Digital Products → Settings → Digital products via email** [VERIFICADO]: ahí se edita **Digital product ready email** (el que lleva el enlace). Texto para la muestra: paso 9.2.

---

## 7) Páginas legales y pie

**Dónde se crean:** las políticas en **Settings → Policies**; las otras páginas en **Content → Pages → Add page** [SIN VERIFICAR el nombre exacto de ambos menús]. Antes de pegar, **rellena todos los `{{...}}`**. Los textos legales son plantillas: **revisarlos con el gestor antes de publicar**.

| Página en la tienda | Archivo con el texto | Dónde se crea | Dirección |
|---|---|---|---|
| **Terms of sale** | `legal/terms-of-sale-en.md` | Settings → Policies → **Terms of service** | `/policies/terms-of-service` |
| **Privacy policy** | `legal/privacy-en.md` | Settings → Policies → **Privacy policy** | `/policies/privacy-policy` |
| **Refund policy** | Una frase que remite a las condiciones: `See sections 6 and 7 of our Terms of sale.` | Settings → Policies → **Refund policy** | `/policies/refund-policy` |
| **Legal notice** | `legal/legal-notice-en.md` | Content → Pages | `legal-notice` |
| **Cookie policy** | `legal/cookies-en.md` (completa la tabla de cookies, ver 7.1) | Content → Pages | `cookie-policy` |
| **Withdraw from the contract here** | `legal/withdraw-here-en.md` (+ formulario, ver 7.2) | Content → Pages | `withdraw-from-the-contract` |
| **Contact** | `Write to us at {{EMAIL_CONTACTO}}.` (+ formulario de contacto del tema) | Content → Pages | `contact` |
| **FAQ** (opcional) | Ya está en la ficha (acordeón). Si la quieres aparte, copia la Sección 8 FAQ | Content → Pages | `faq` |

En cada archivo, no pegues la nota de la primera línea ("Template based on official sources…"); sí la frase "The Spanish version prevails if there is any discrepancy". Deja cada página **Visible** (la tienda sigue con contraseña).

### 7.1 Cookies y banner
1. **Settings → Customer privacy** [SIN VERIFICAR el nombre].
2. Activa el banner de cookies en la **UE** y **EE. UU.** Los botones **Accept** y **Decline** deben tener **el mismo tamaño y relieve**.
3. Completa la tabla de cookies de la página `cookie-policy` con las cookies reales. No cargar el píxel de Meta ni TikTok sin consentimiento [SIN DATO hasta probar].
4. **Cómo saber que está bien:** en ventana privada ves el banner con los dos botones iguales.

### 7.2 Página "Withdraw from the contract here"
1. Crea la página con el texto del archivo.
2. El formulario de 3 pasos (nombre, email, nº de pedido → confirmar → acuse por email con fecha y hora) hay que montarlo: bloque **Contact form** del tema con esos tres campos, o una app gratuita de "withdrawal form" [SIN VERIFICAR coste]. ⚠ Si la app pide pago o cuenta, **necesita tu "sí"**. Mientras tanto vale un formulario de contacto que te envíe un email, y tú respondes con el acuse (fecha y hora) a mano.
3. **Cómo saber que está bien:** al enviar el formulario de prueba recibes el email en `{{EMAIL_CONTACTO}}`.

### 7.3 Menús
1. **Content → Menus** (o **Online Store → Navigation**) [SIN VERIFICAR]. **Footer menu**, en este orden: `Terms of sale` · `Privacy policy` · `Refund policy` · `Legal notice` · `Cookie policy` · `Withdraw from the contract here` · `Contact`.
2. **Main menu** (cabecera): `Home` · `The Sunday Sheet` · `Contact`. **No pongas The Mini Sunday en ningún menú.**
3. **Cómo saber que está bien:** en el pie aparecen los 7 enlaces y todos abren su página.

---

## 8) Checkout: casilla de desistimiento (UE) y email de confirmación

### 8.1 La casilla (obligatoria para vender a la UE)
- **Texto exacto** (`legal/checkout-checkbox-en.md`), **sin marcar** y obligatoria para pagar:
  `I request immediate access to the digital content and I acknowledge that, once the download starts, I lose my right of withdrawal. (Terms of sale)` — "Terms of sale" enlaza a `/policies/terms-of-service`.
- **Dónde va:** junto al botón final del pago, en el checkout.
- **Problema conocido:** en plan Basic, Shopify **no tiene** casilla propia y el checkout solo se personaliza a fondo en Plus (`datos-shopify.md`, `datos-costes.md`; SIN VERIFICAR hoy). La solución son apps de casilla (nombres vistos, no verificados: *ConsentGuard*, *RA Terms & Conditions Checkbox*, *Terms and Conditions Checkbox*).
- ⚠ **Instalar una app = decisión tuya.** Pasos:
  1. Busca en **Settings → Apps → Shopify App Store** una app con plan **gratuito** que (a) ponga una casilla **obligatoria** y **sin marcar** en el checkout, (b) **permita escribir el texto exacto** y (c) **guarde fecha y hora** de la aceptación en el pedido.
  2. Dime cuál y qué cuesta, y espera mi "sí" antes de pulsar Install. Presupuesto prudente: 0 €, con riesgo de 5 a 15 €/mes.
  3. Instalada: escribe el texto y actívala solo para The Sunday Sheet si la app lo permite (**no** debe salir en la muestra de 0 $; si no se puede, es pregunta para el gestor, `montaje-emails.md` §2.3).
- **Plan B si ninguna app sirve:** **no vender a la UE** hasta resolverlo (solo EE. UU., donde la casilla no hace falta), y avisar al gestor.
- **Cómo saber que está bien:** en el checkout de prueba (UE) no puedes pagar sin marcar la casilla, y el pedido guarda la fecha y hora.

### 8.2 Email de confirmación del pedido
1. **Settings → Notifications → Customer notifications → Order confirmation** [SIN VERIFICAR el nombre exacto].
2. Pulsa **Edit code** (es el editor de la plantilla del email; **solo pegas texto, no programas**).
3. Pega el texto de `legal/confirmation-email-en.md` y sustituye los campos entre corchetes por los de Shopify:

| En el texto | Se escribe tal cual |
|---|---|
| `[ORDER NUMBER]` | `{{ order_name }}` |
| `[ORDER DATE AND TIME]` | `{{ created_at }}` |
| `[ORDER TOTAL]` | `{{ total_price | money }}` |
| `[PAYMENT METHOD]` | `{{ transactions.first.gateway }}` (o el bloque de pago que ya trae el email) |
| `[DOWNLOAD LINK]` | El enlace lo envía la app de descargas en su propio email: escribe `Your download link comes in a separate email from the same store.` |
| `[CONSENT DATE AND TIME]` y la frase de la casilla | Los guarda la app de la casilla en el pedido (nota o atributo); copia la variable que indique la app [SIN VERIFICAR] |
| `{{NOMBRE_TIENDA}}`, `{{NOMBRE_TITULAR}}`, `{{NIF}}`, `{{DOMICILIO}}`, `{{EMAIL_CONTACTO}}`, `{{LIMITE_DESCARGAS}}` | Tus datos reales (`5` para el límite si has seguido el paso 6.3) |
| `[Terms of sale]`, `[Withdraw from the contract here]`, `[Privacy]` | Los enlaces del paso 7 |

4. **Importante:** el email debe llegar al cliente **con** el texto de lo que aceptó (es la confirmación que exige la ley para perder el desistimiento). Si no consigues meter fecha, hora y texto de la casilla, **no vendas a la UE** y dímelo.
5. **Asunto:** `Your order confirmation {{ order_name }} · {{NOMBRE_TIENDA}}`.
6. **Save** y envía una prueba (**Send test email**) a tu segundo email.
7. **Cómo saber que está bien:** el email de prueba muestra nº de pedido, total, la frase de la casilla y los enlaces, sin llaves `{{ }}` ni corchetes sin sustituir.

---

## 9) Email: formulario, doble opt-in, secuencia

Fuente: `emails/en/montaje-emails.md` y `emails/en/secuencia.md`. Nada se envía sin tu "sí".

### 9.1 Herramientas
- **Shopify Messaging** (antes "Shopify Email"): disponible en los planes Basic y superiores [VERIFICADO]. Instálala desde **Settings → Apps → Shopify App Store** [SIN VERIFICAR si ya viene instalada]. El precio depende de los mensajes enviados; según nuestras fuentes, 10.000 al mes gratis y luego 1 $ cada 1.000 (`datos-costes.md`). ⚠ **Comprueba el precio real en pantalla antes de enviar.** La ayuda dice que requiere activar *Shopify Network Intelligence* en privacidad [VERIFICADO]; acepta solo si estás de acuerdo.
- **Shopify Flow** para los tiempos (día 1, 3, 5, 8, y parar si compra) [SIN VERIFICAR; ⚠ confirma que es gratis antes de instalar]. Si no es posible: plan manual (9.5).

### 9.2 Email de entrega de la muestra (sin marketing)
En **Apps → Digital Products → Settings → Digital products via email → Digital product ready email** pega el **Email 1** de `secuencia.md`:
- **Subject:** `Your Mini Sunday is here`
- **Preheader:** `One short Sunday, three different plates. Download it here.`
- Botón: `Download The Mini Sunday`
- Cuerpo: el "FINAL TEXT" del Email 1 (sin marketing, porque le llega también a quien no aceptó marketing).
- ⚠ Esa plantilla de la app puede ser una sola para todos los productos digitales [SIN VERIFICAR]. Si no se puede tener una distinta por producto, usa un texto neutro que valga para los dos (gracias + enlace + aviso general) y manda el Email 1 aparte.
- Antes de dejar "Plan for a bit over an hour", **cronometra la muestra** (alguien la cocina una vez).

### 9.3 Formulario, casillas y doble opt-in
Texto: `legal/email-form-en.md`. Título `Get the free sample of The Sunday Sheet`; campo: Email; casilla 1 (obligatoria, sin marcar) `I am 14 or older and I want to receive the free sample by email.`; casilla 2 (opcional, sin marcar, separada) `I also want to receive marketing emails from {{NOMBRE_TIENDA}} with news and offers. I can unsubscribe at any time.`; botón `Send me the sample`; información básica de privacidad debajo.
- **Con Shopify solo:** hay casilla de marketing en el checkout (es la casilla 2). **No** hay casilla propia de "14 años" ni doble confirmación por defecto [SIN VERIFICAR]. Por eso hay que elegir A, B o C (paso 5.3). **Mientras no elijas, la sección de la muestra sigue fuera.**
- **Doble opt-in** (recomendado, no obligatorio): el Email 0 `Confirm your email to get the sample` se manda primero y la muestra se entrega tras el clic. Con un pedido de 0 $ la entrega es inmediata, así que probablemente necesite la opción B o un Flow que marque al cliente tras el clic. Si Shopify no puede, lo admitido es: casilla de marketing clara + baja en un clic en cada email. Consúltalo con el gestor.
- Si no hay forma clara de hacerlo, **no improvises**: déjalo en C.

### 9.4 La secuencia (borrador, desactivada)
| Día | Email | Asunto | Quién lo recibe |
|---|---|---|---|
| 0 | Email 0, confirmar email | `Confirm your email to get the sample` | Todos los que piden la muestra |
| 0 | Email 1, entrega | `Your Mini Sunday is here` | Todos los que confirman |
| 1 | Email 2 | `Keep the sauce out of the container` | Solo marketing aceptado + confirmado + sin compra |
| 3 | Email 3 | `What if Wednesday didn't taste like Monday?` | idem |
| 5 | Email 4 | `What's inside The Sunday Sheet` | idem |
| 8 | Email 5 (último) | `Quick answers about The Sunday Sheet` | idem |
| compra | Email 6, confirmación | (paso 8.2) | Todo comprador |
| +3 días | Email 7 | `How was your first Sunday?` | Solo compradores con marketing aceptado |

Cada uno: **Marketing → Campaigns / Automations → Create** [SIN VERIFICAR]. Copia asunto, preheader y "FINAL TEXT" de `secuencia.md`.
- **Precio:** usa el **bloque de producto** del email (lee el precio de la tienda); nunca lo escribas a mano.
- **Pie de cada email comercial** (sección 2 de `secuencia.md`): motivo de recepción, baja en un clic, titular, domicilio, email de contacto y enlace a privacidad. Si algún `{{...}}` está en blanco, **no se envía**.
- Sin cuentas atrás, "última oportunidad", descuentos ni reseñas.
- Pruebas: manda cada email a tu segundo email (pie, baja, precio, vista en móvil). Asuntos de 45 caracteres o menos.
- **Cómo saber que está bien:** los emails existen en borrador, ninguno enviado ni activado.

### 9.5 Tiempos con Shopify Flow
| Paso | Regla |
|---|---|
| Inicio | Pedido de 0 $ con etiqueta `mini-sample` **y** acepta marketing |
| Espera 1 día | Si tiene 0 pedidos de pago → Email 2 |
| Espera 2 días | Igual → Email 3 |
| Espera 2 días | Igual → Email 4 |
| Espera 3 días | Igual → Email 5. Fin |
| Aparte | Compra The Sunday Sheet **y** acepta marketing → espera 3 días → Email 7 |

Déjalo **apagado**. Si Flow no puede: plan manual, cuatro campañas a mano al segmento "acepta marketing + etiqueta mini-sample + 0 pedidos", en los días de la tabla.

### 9.6 No importar listas
Solo entran en la lista las personas que lo piden por el formulario.

---

## 10) UTM y enlaces para la bio

### 10.1 Para qué
Cada vídeo lleva un enlace con etiquetas (UTM) para saber qué vídeo trae cada visita y venta. Sigue el formato de `contenido/registro.csv` (`utm_source` y `utm_campaign`) y añade `utm_medium` y `utm_content`.

### 10.2 Cómo construir el enlace
`https://TU-TIENDA/products/the-sunday-sheet?utm_source=tiktok&utm_medium=social&utm_campaign=a2&utm_content=G01`

| Parte | Valores |
|---|---|
| `utm_source` | `tiktok` · `instagram` · `youtube` |
| `utm_medium` | `social` |
| `utm_campaign` | el ángulo del vídeo: `a1`, `a2`, `a4`… (de `registro.csv`) |
| `utm_content` | el número del guion: `G01`, `G02`… |

Cambia `TU-TIENDA` por tu dirección real (`xxxx.myshopify.com` o tu dominio).
- TikTok, A2, G01 → `...?utm_source=tiktok&utm_medium=social&utm_campaign=a2&utm_content=G01`
- Instagram, A2, G01 → `...?utm_source=instagram&utm_medium=social&utm_campaign=a2&utm_content=G01`
- YouTube, A2, G01 → `...?utm_source=youtube&utm_medium=social&utm_campaign=a2&utm_content=G01`

**Enlace de la bio** (uno por red, sin `utm_content`): `...?utm_source=tiktok&utm_medium=social&utm_campaign=bio`. La columna `utm` de `contenido/registro.csv` se rellena con la parte que cambia.

### 10.3 Dónde ver los datos
**Analytics → Reports** (sesiones por fuente / campaña) [SIN VERIFICAR el nombre del informe]. Las ventas se cruzan con el registro de contenido (`metricas-lanzamiento`).

### 10.4 Importante mientras haya contraseña
Los enlaces **no funcionan para el público** hasta quitar la contraseña: los visitantes verían la página de contraseña. **No pongas los enlaces en la bio hasta publicar.** ⚠ Publicar = tu "sí".

### 10.5 Probar un enlace
Pégalo en el navegador, entra con la contraseña y comprueba que la ficha abre bien y que la barra de direcciones conserva las etiquetas.

---

## 11) Pruebas antes de publicar

⚠ No quites la contraseña hasta que **todas** estas pruebas salgan bien y `revision-tienda` (técnica y legal) esté aprobada.

### 11.1 Preparar
1. Modo de prueba de pagos activo (paso 1.6) y tarjeta de prueba: usa los datos que indique la ayuda de Shopify sobre el "test mode" [SIN VERIFICAR; normalmente se usa el número `1` como tarjeta, una fecha futura y un CVV de 3 cifras].
2. La contraseña de la tienda a mano.
3. Cada prueba, con tu segundo email, en el producto de pago y en el de 0 $.

### 11.2 Pedido de prueba, producto de pago
1. Ficha → **Buy now** → dirección de la **UE** (por ejemplo, España) y tarjeta de prueba.
2. Comprueba:
   - [ ] El precio final es **$24.99** con IVA incluido.
   - [ ] Sale la **casilla** de desistimiento, sin marcar, y no deja pagar sin marcarla.
   - [ ] Llega el **email de confirmación** con la frase aceptada, fecha y hora.
   - [ ] Llega el **email de la app** con el enlace y se abren los **dos PDF**.
   - [ ] La página de "gracias" muestra el botón de descarga.
3. Repite con dirección de **EE. UU.** (si lo has activado): el *sales tax* se suma al total.
4. Repite con dirección del **Reino Unido**: **no debe dejar comprar**.

### 11.3 Pedido de prueba, muestra a 0 $
1. Entra por `/products/the-mini-sunday` → **Buy now**.
2. Comprueba:
   - [ ] No pide tarjeta ni dirección de envío.
   - [ ] La casilla de desistimiento **no** sale (o, si sale, queda anotado para el gestor).
   - [ ] Llega el Email 1 con el enlace y el PDF se abre.
   - [ ] Con la casilla de marketing **sin marcar**, no entra en la secuencia de venta.

### 11.4 Pago desde el navegador de TikTok e Instagram, en móvil ajeno
Los navegadores internos se comportan distinto: hay reportes de pantalla en blanco y de falta de botones Apple Pay / Google Pay (`datos-shopify.md` §5, anecdótico, sin documentación oficial). Hay que probar con un **móvil que no sea el tuyo**, sin sesiones ni tarjetas guardadas. Pega el enlace con UTM en un mensaje a ti mismo o en la bio de una cuenta de prueba y ábrelo desde ahí.

| Prueba | iPhone | Android |
|---|---|---|
| Abrir el enlace desde TikTok (navegador interno) | ☐ | ☐ |
| Abrirlo desde la bio de Instagram | ☐ | ☐ |
| La página de contraseña se ve bien y deja entrar | ☐ | ☐ |
| La ficha se ve entera (imágenes, precio, botón) sin cortarse ni quedarse en blanco | ☐ | ☐ |
| Los acordeones se abren | ☐ | ☐ |
| **Buy now** abre el checkout | ☐ | ☐ |
| Escribir email, marcar la casilla y pagar con tarjeta de prueba | ☐ | ☐ |
| Aparece "gracias" y se puede descargar el PDF desde el navegador interno | ☐ | ☐ |
| Llega el email y el enlace abre el PDF en el móvil | ☐ | ☐ |

Si falla algo (pantalla en blanco, botón que no responde, pago que no avanza): haz captura, apunta móvil, red y versión, y dímelo en el chat. Posibles arreglos (sin tocar código): quitar animaciones del tema, o un aviso en la ficha ("Open in your browser for a smoother checkout") [SIN VERIFICAR]. Antes de publicar **debe funcionar al menos con tarjeta**.

### 11.5 Comprobaciones generales
- [ ] En móvil la ficha carga rápido (menos de 3 s con wifi) y no hay texto cortado.
- [ ] Todos los enlaces del pie y de la ficha abren su página.
- [ ] No hay `{{...}}`, `[VERIFICAR]` ni textos de ejemplo en ninguna página.
- [ ] No hay reseñas, estrellas, tachados ni contadores.
- [ ] Contraseña **todavía activada**.

### 11.6 Cuando todo salga bien
Se pasa a `revision-tienda`. Solo después, y solo con tu "sí" escrito en el chat, ⚠ **se quita la contraseña** (Online Store → Preferences → desmarcar "Restrict access…") y se activan los productos (Status → Active).

---

## 12) Qué hacer para que Claude lo termine si conectas Shopify

1. En **claude.ai**: **Ajustes → Conectores → Shopify** → **Conectar** e inicia sesión con la cuenta de Shopify que tú creaste. Elige tu tienda y revisa los permisos que pide [SIN VERIFICAR el texto de cada pantalla]; no aceptes más de los necesarios.
2. Vuelve al chat y escribe: **"Shopify conectado"**.
3. Claude comprueba la conexión (`get-shop-info`). Si falla, seguimos con esta guía.
4. Con la conexión, Claude podrá hacer **en borrador**: crear los dos productos con los textos y las imágenes, subir los PDF a la app de descargas (si ya la instalaste tú), crear colecciones y revisar los pedidos de prueba.
5. Sigue siendo **solo tuyo**: crear la cuenta, contratar el plan, instalar apps de pago, verificar tu identidad en Shopify Payments, decidir el IVA con el gestor y **quitar la contraseña**.
6. Cada gasto, publicación o contacto pide tu "sí" explícito en el chat.

---

## Resumen de ⚠ (lo que necesita tu "sí" o cuesta dinero)
1. Crear la cuenta de Shopify (solo tú).
2. Contratar el plan Basic (unos 24 a 32 €/mes; primer cobro).
3. Moneda USD con Shopify Payments en España (posible conflicto; decidir).
4. Verificación de identidad de Shopify Payments (solo tú).
5. Activar EE. UU. (antes, el gestor sobre *sales tax*).
6. IVA UE y OSS: el gestor decide; IVA del pack (4 % o 21 %).
7. Instalar la app Digital Products (gratuita; confirmar que es gratis).
8. App de la casilla de desistimiento (posible coste de 5 a 15 €/mes) o no vender a la UE hasta tenerla.
9. App del formulario de desistimiento y opciones A/B/C de la muestra (posible app o cuenta).
10. Shopify Messaging y Shopify Flow (comprobar precio antes de enviar o activar).
11. Cualquier tema, logo o app de pago.
12. Enviar cualquier email real y activar la secuencia.
13. Quitar la contraseña y publicar.

## Lo que sigue sin existir (bloquea el final del montaje)
- `tienda/imagenes/en/` con las imágenes (5 verticales + versiones cuadradas).
- `ebook/en/the-sunday-sheet.pdf`, `ebook/en/the-sunday-sheet-printables.pdf` y el PDF de The Mini Sunday.
- Logo y favicon.
- Datos del titular y nombre de la tienda (`{{...}}`).
- Respuesta del gestor: IVA, sales tax EE. UU., casilla, doble opt-in.
- Marca "The Sunday Sheet" pendiente de USPTO; cocinar al menos 3 platos y cronometrar la semana 1 y la muestra antes de usar "about 2 hours" en anuncios.
