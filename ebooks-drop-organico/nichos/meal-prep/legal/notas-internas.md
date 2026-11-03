# Notas internas (NO publicar) · textos legales meal-prep

_03-nov-2026. Aquí van las dudas, etiquetas y montaje que no pueden estar en el texto público._

## Para el gestor (pregunta 7 de `consulta-gestor.md` y relacionadas)
1. **Sales tax EE. UU.** [SIN DATO]: el texto dice "sales tax added at checkout where applicable". Confirmar: ¿algún estado obliga a recaudar con pocas ventas (p. ej. 200 transacciones en NJ)? ¿Vender a EE. UU. desde el inicio o esperar? ¿Qué calcula Shopify solo? (fiscal.md §5, estimación: por debajo de 100.000 USD por estado casi siempre, pero hay estados con umbral de transacciones.)
2. **Política de reembolso EE. UU.** [SIN DATO]: "ventas definitivas salvo que el archivo no funcione o no sea lo descrito (se arregla o se reembolsa)". Confirmar que es válida y no choca con leyes estatales ni con las normas de Shopify Payments / contracargos (chargebacks).
3. **Garantía de conformidad** (arts. 115 bis ss. TRLGDCU): plazos y remedios exactos [SIN DATO] (consumo... §5); por eso el texto no cita plazos. Redacción "arreglar primero, reembolsar después" es nuestra [ESTIMACIÓN].
4. **IVA**: texto dice "IVA incluido" sin cifra. Ebook 4 % [DATO fiscal.md §4]; el pack imprimible (hojas, listas, etiquetas) puede no ser "libro" y tributar al 21 % [SIN DATO] (pregunta 4). `estructura.md` §2.3 calcula neto 24,03 $ (4 %); resolver. Si el imprimible tributa al 21 % habría que subir el precio UE o separar productos.
5. **Precio en dólares a clientes UE**: la tienda cobra 24,99 USD "IVA incluido" en la UE [ESTIMACIÓN]; confirmar que Shopify lo muestra así y la conversión de divisa. La futura tienda ES (14,90 €) irá con otros textos/precio; no incluida aquí.
6. **Registro OSS / IVA UE** (pregunta 6) y facturas (pregunta 8): no afectan al texto.
7. **Casilla y botón de desistimiento** (preguntas 10-11): el texto exacto es el de la skill (ES) y traducción nuestra (EN). Si la casilla en EN sirve también para EE. UU. (no necesaria, no perjudica) [ESTIMACIÓN].
8. **Aviso legal con nombre y NIF** (pregunta 13).
9. **Privacidad**: plazos de conservación [SIN DATO]; marco UE-EE. UU. / cláusulas tipo por proveedor [ESTIMACIÓN]; base 6.1.f para prueba de consentimientos [ESTIMACIÓN]. Edad mínima 14 (LOPDGDD art. 7 es España); otros países UE tienen 13-16 [SIN DATO]; en EE. UU. la COPPA fija 13. Sección de derechos de estados de EE. UU. redactada de forma mínima y prudente ("no vendemos tus datos"); confirmar si basta y si el uso de Meta Pixel/TikTok cuenta como "compartir" para publicidad en estados como California.
10. **Plataforma europea ODR**: vigencia [SIN DATO]; enlace omitido.
11. **Nicho nutrición**: aviso "no sustituye a médico o dietista-nutricionista" y "comprobar alérgenos" (instrucción de Fran). Revisar que las páginas de producto y los anuncios no prometan pérdida de peso, salud ni "detox" (Ley 3/1991; normas de Meta). En España, la publicidad de alimentos con alegaciones nutricionales (Reglamento CE 1924/2006) puede aplicar a frases como "alto en proteína" [SIN DATO]; consultar.

## Coherencia (punto 15) con `estructura.md`
- 336 págs. ebook (A5), 34 págs. imprimible (Letter, apto blanco y negro) — cifras reales del PDF (03-nov), 60 recetas, 48 platos, plan de 4 semanas, 24,99 $: coinciden con `estructura.md` §2.1-2.3. Las "unas 165 / unas 30" son estimaciones hasta cerrar el PDF: **actualizar al maquetar**.
- `pagina-producto.md` del nicho meal-prep **no existe aún**: comprobar al crearla (precio, páginas, formato, mercados EE. UU. + UE, sin Reino Unido).
- No se cita en texto público la cifra de combinaciones (2.106) ni "2.000 recetas" (estructura §2.1).
- Muestra gratis: contenido concreto de la muestra a confirmar (estructura.md, sección de muestra); el texto solo dice "muestra gratis".

## Datos que solo rellena Fran (no inventar)
{{NOMBRE_TITULAR}} · {{NIF}} · {{DOMICILIO}} · {{EMAIL_CONTACTO}} · {{TELEFONO}} · {{NOMBRE_TIENDA}} · {{DOMINIO}} · {{FECHA_ACTUALIZACION}} · {{APP_ENTREGA}} · {{APP_EMAIL}} · {{LIMITE_DESCARGAS}}. Mientras falten, NO publicar.

## Montaje (para `montar-tienda-shopify`)
- Casilla junto al botón "Pedido con obligación de pago" / "Order with obligation to pay": bloquea el pago si no se marca y guarda texto, fecha y hora en el pedido para copiarlos al email de confirmación.
- Variables del email = campos de la plantilla de notificación de Shopify (mapear al montar). El correo ES y EN se usan según el idioma de la tienda.
- Página "Withdraw from the contract here": formulario + paso "Confirmar" + email automático de acuse.
- Cookies: banner de Shopify (Customer Privacy) con Aceptar/Rechazar iguales; Meta Pixel y TikTok no se cargan sin consentimiento [SIN DATO hasta probar]. Rellenar la lista real de cookies.
- Formulario de muestra: doble opt-in; baja con un clic.
- Pie de la tienda: enlaces a aviso legal, condiciones, privacidad, cookies y desistir.
- Mercados: EE. UU. + UE; Reino Unido cerrado. No mostrar reseñas hasta que existan.
