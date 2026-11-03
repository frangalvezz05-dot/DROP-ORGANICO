# Email setup · The Sunday Sheet (EN) · 03-nov-2026
_Steps for the shop owner. Everything is created as a **draft**. Nothing is sent, published or paid without Fran's explicit "yes". The Shopify tools were not connected in this session, so every item marked [VERIFICAR] has not been checked in the real store._

Source texts: `secuencia.md` (FINAL TEXT blocks). Legal base: `../../legal/email-form-en.md`, `../../legal/confirmation-email-en.md`.

## 1. Which tool does what
| Piece | Tool | Why |
|---|---|---|
| The sample (The Mini Sunday) | **Product at $0** + official Shopify downloads app (`{{APP_ENTREGA}}`) | The app emails the download link when the "order" is placed. It works for people who do **not** accept marketing, so the sample never depends on marketing consent [ESTIMACIÓN: verificar en la tienda] |
| Emails 2 to 5 and 7 (commercial) | **Shopify Email** (10,000 emails a month free) | It only sends to customers who accepted marketing, which is what the LSSI requires |
| Email 0 (confirm) | Store notification or form app [VERIFICAR] | Transactional |
| Email 6 (order confirmation) | Shopify order confirmation notification | Text in `confirmation-email-en.md` |
| Timing and exits (days 1, 3, 5, 8; stop on purchase) | **Shopify Flow** (wait + condition + "Send marketing email") [VERIFICAR] | Shopify Email's ready-made automations are limited to its own templates (welcome, abandoned cart...), so a 4-step series with an exit on purchase probably needs Flow |

## 2. The sample as a $0 product
1. Create the product **The Mini Sunday**: price **$0.00**, digital, no shipping, tag `mini-sample`, not in any collection and not in the menu. Only reachable from the button of the "Try one Sunday first" section of the product page (anchor `#free-sample`). In draft until Fran approves.
2. Attach the PDF with the downloads app. Edit the app's email with the **Email 1** text of `secuencia.md` (no marketing content in it). Test with a real $0 order from a test address [VERIFICAR: that a $0 digital order does not ask for a shipping address or a payment method].
3. The checkbox "I request immediate access... I lose my right of withdrawal" (`checkout-checkbox-en.md`) is written for the **paid** product. For a free sample it should not appear. [VERIFICAR] if it can be limited to The Sunday Sheet; if it can't, ask the gestor if showing it on the free sample is acceptable.
4. Box 1 (14 or older) and box 2 (marketing, not pre-ticked) of `email-form-en.md`: Shopify checkout natively has an "Email me with news and offers" box (box 2) but **no** custom box for "I am 14 or older" unless the plan allows it [VERIFICAR]. Options, in this order:
   - **A.** Box 2 = the native checkout marketing box (unticked). Box 1 = confirmation text next to the sample button on the product page plus a line in the confirmation email. Ask the gestor if this is enough.
   - **B.** A Shopify form app that allows two boxes. Only with Fran's "yes" if it means installing an app or creating an account.
   - **C.** Don't open the sample until A or B is confirmed. The product page's sample section and the link under the main button stay hidden (as already noted in `pagina-producto.md`).
5. Double opt-in: Email 0 is sent first and the sample is delivered only after the click. A $0 checkout delivers instantly, so double opt-in probably needs the form + confirmation route (option B) or a Flow that tags the customer after the click. If Shopify can't do it, say so to Fran: double opt-in is *recommended*, not mandatory, so the fallback is a clearly worded box 2 and the one-click unsubscribe in every email [VERIFICAR with the gestor].

## 3. Variables
| In the text | Filled with | Where it comes from |
|---|---|---|
| `[PRICE]` / `[PRECIO_CON_IVA]` | The price of the product, with VAT included for EU customers | Use a **product block** in Shopify Email so the price is read from the store. Never type it by hand |
| `[PRICE_PER_MEAL]` | Price ÷ 40 planned meals, rounded to the cent ($24.99 gives $0.62) | Calculate when the price changes. If the price changes and this is forgotten, remove the sentence (point 15) |
| `[DOWNLOAD LINK]` | Link of the downloads app | Automatic |
| `{{NOMBRE_TIENDA}}`, `{{NOMBRE_TITULAR}}`, `{{DOMICILIO}}`, `{{EMAIL_CONTACTO}}`, `{{APP_ENTREGA}}`, `{{LIMITE_DESCARGAS}}` | Holder details | `../../legal/notas-internas.md` (owner fills them; if blank, DO NOT send) |
| `[Unsubscribe in one click]`, `[Privacy policy]` | Shopify Email unsubscribe link; privacy page URL | Automatic / store URL |

## 4. Series in Shopify Flow (draft, off)
| Step | Rule | Email |
|---|---|---|
| Trigger | Customer places the $0 order for The Mini Sunday (tag `mini-sample`) **and** accepts marketing | — |
| Wait 1 day | Condition: customer has 0 paid orders | Email 2 |
| Wait 2 days | Same condition | Email 3 (day 3) |
| Wait 2 days | Same condition | Email 4 (day 5) |
| Wait 3 days | Same condition | Email 5 (day 8). Series ends |
| Separate flow | Customer pays for The Sunday Sheet **and** accepts marketing → wait 3 days | Email 7 |
If marketing consent is withdrawn at any point, the flow stops (Shopify Email doesn't send to unsubscribed customers). If Flow can't do it [VERIFICAR], fallback: send the four emails by hand as campaigns to the segment "accepts marketing + tag mini-sample + 0 orders", on the days of the table, and check the segment before each one.

## 5. Checks before activating
1. Holder blanks filled. Footer has name, address and contact in each commercial email.
2. Send a test of each email to Fran's own address: footer, unsubscribe link, price block, preview on mobile.
3. Subjects 45 characters or fewer (checked: the longest is 43).
4. The price in the emails equals the price of the page and the checkout. Same phrases as `pagina-producto.md` (points 2 and 15).
5. The sample is timed (a person cooks it once) before "a bit over an hour" stays in Email 1.
6. Sample page and form: only after options A, B or C of section 2 are decided.
7. Don't import any list. Only people who ask through the form go in.

## 6. After launch
- Measure clicks to the product page and purchases from email (opens are unreliable). See `metricas-lanzamiento`.
- One manual campaign a week at most at the start, and clean up people who never open or click after about 180 days [OPINIÓN mentor: Dani, 8Er-sAVrULo].
- Do not add a discount or a countdown to improve conversion without checking points 8 and the Omnibus rule with the gestor first.

## 7. Resumen para Fran (en español)
- **Muestra gratis** = un producto de 0 $ con la app de descargas: la entrega llega aunque la persona no acepte marketing.
- **Emails de venta** con Shopify Email (gratis hasta 10.000 al mes), y los tiempos (días 1, 3, 5, 8, y parar si compra) con Shopify Flow. Hay que **comprobarlo en la tienda**: no estaba conectada.
- **El precio** no se escribe a mano: se usa el bloque de producto del email. El "0,62 $ por comida" se recalcula si cambia el precio (precio ÷ 40).
- **Punto delicado**: la doble confirmación y las dos casillas (ser mayor de 14 y marketing aparte) quizá no se puedan hacer solo con Shopify. Hay tres opciones (A, B, C) en la sección 2; la B puede implicar instalar una app o crear cuenta y necesita tu "sí". Hasta decidirlo, la sección de la muestra queda oculta.
- **Nada se envía ni se publica** sin tu "sí".
