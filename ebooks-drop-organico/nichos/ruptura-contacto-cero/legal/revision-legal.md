# Revisión legal · ruptura-contacto-cero (Kit SOS contacto cero)

_03-nov-2026 · actúa como `revisor-legal` (Sonnet) · revisados los 8 textos de `legal/` y `tienda/pagina-producto.md`. Base: `02-analisis.md` §1-2, `consumo-datos-publicidad.md`, `fiscal.md`._

## Tabla de los 13 puntos
Textos = los 8 archivos de `legal/`. Página = `tienda/pagina-producto.md` (solo se anotan cambios, no se reescribe).

| # | Punto | Textos, vuelta 1 | Textos, vuelta 2 | Página de producto | Fuente |
|---|---|---|---|---|---|
| 1 | Huecos del titular rellenos | FALLO (esperado) | FALLO: huecos sin rellenar + `{{APP_ENTREGA}}`/`{{APP_EMAIL}}`. **No publicar hasta rellenar** | FALLO: `[PENDIENTE: correo de soporte]` en ES-09, ES-12 (y EN) | SKILL; 02-analisis §1 |
| 2 | Precio con IVA, coherente | FALLO: nota interna "para el titular" dentro de condiciones §4 | OK (sin cifra a mano; IVA "incluido"; tarifa del pack pendiente del gestor) | OK en ES-05 (bloque del tema, "IVA incluido"). Aviso: `estructura.md` §2.2 calcula con IVA 21 % frente al 4 % de `fiscal.md` | consumo §4; fiscal §3 |
| 3 | Información precontractual | OK | OK | FALLO: ES-13/EN-13 dicen "PENDIENTE MÓDULO 7" | consumo §1 |
| 4 | Excepción de desistimiento (casilla + reconocimiento + email con copia literal) | OK (casilla sin premarcar; email con copia literal y fecha/hora; 14 días si falla) | OK | FALLO: ES-05 y ES-13 no mencionan la casilla ni la excepción | 02-analisis §1 nº 5 |
| 5 | Página "Desistir del contrato aquí" | OK | OK | FALLO: sin enlace | consumo §3 [SIN DATO si obliga] |
| 6 | Páginas legales en el pie; cookies con Rechazar | OK en texto (cookies: Aceptar y Rechazar iguales); pie y banner NO VERIFICABLES hasta montar la tienda | igual | FALLO: la página no enlaza condiciones, privacidad ni desistimiento | consumo §6 |
| 7 | Formulario de email | OK (casilla 2 aparte, doble opt-in, baja con un clic, 14 años) | OK | ES-11/EN-11 aún "PENDIENTE módulo 8 y RGPD": enlazar a `formulario-email.md` | LSSI 21-22 |
| 8 | Prácticas desleales | FALLO: etiquetas [SIN DATO]/[ESTIMACIÓN] dentro del texto público en 4 sitios | OK (sin urgencia, contadores, reseñas ni promesas; "Pasos de 10 minutos" es proceso, no resultado) | OK. Cuidado: ES-08 "Muchos cuadernos…" lleva la etiqueta `[ESTIMACIÓN sobre muestra de 10]`; no copiarla a Shopify | Ley 3/1991 art. 23.4, 27.7-8 |
| 9 | Mercados aprobados | OK (ES: España/UE; Reino Unido no) | OK | OK en ES. EN (EE. UU.): decisión de vender allí [SIN DATO] ("EE. UU. si se decide") | 02-analisis §1 nº 2 |
| 10 | Vídeos con IA etiquetados | NO APLICA | NO APLICA | NO APLICA | consumo §9 |
| 11 | Anuncios sin atributos personales | NO APLICA | NO APLICA | NO APLICA a la página. ES-07/EN-07 (preguntas "¿te suena…?") ya marcadas solo-página: vigilar que no pasen a anuncios | Meta 27-jun-2024 |
| 12 | Nicho sensible: aviso y recursos | OK (aviso y 112/024/016, sin 016 para hombres, en aviso legal, condiciones, email y formulario) | OK | OK (ES-08b). Teléfonos [DATO] de `avatar.md` §8 sin reverificar: revisar vigencia antes de publicar | avatar §8 |
| 13 | Derechos | OK (no se afirma autoría; prohibida la reventa) | OK | FALLO: no hay registro de edición humana del ebook [SIN DATO]; fuentes Inter y Source Serif 4 (OFL) por comprobar al incrustar (`ebook/revision.md`) | 02-analisis §2 |

## Vuelta 1: FALLOS en mis textos y corrección
1. `condiciones-venta.md` §4: nota interna "para el titular" dentro del texto público. Quitada (pasa al comentario final).
2. `condiciones-venta.md` §8: enlace a la plataforma europea de litigios con [SIN DATO] dentro del texto. Enlace quitado (vigencia no verificada); duda al comentario.
3. `condiciones-venta.md` §11: afirmación sobre normas del país de residencia sin fuente. Sustituida por "sin perjuicio de los derechos que la ley reconozca al consumidor".
4. `privacidad.md` (tabla y §4): dos etiquetas [SIN DATO]/[ESTIMACIÓN] dentro del texto público. Quitadas; siguen en el comentario.
5. `checkout-casilla.md`: instrucciones de montaje visibles. Movidas al comentario.

## Vuelta 2
Revisados de nuevo los 8 textos tras las correcciones: sin etiquetas dentro del texto público (comprobado por script), sin promesas de resultado. Quedan solo pendientes que no puede corregir Claude: huecos del titular y apps (punto 1), tarifa de IVA del pack, lista real de cookies.

## Cambios exactos propuestos para `tienda/pagina-producto.md` (no aplicados)
- ES-05 y EN-05, nota: sustituir "[PENDIENTE MÓDULO 7: condiciones, desistimiento]" por "Antes de pagar marcas una casilla para acceder de inmediato al contenido digital. Consulta las Condiciones de venta y la página Desistir del contrato aquí." (EN: "Before paying you tick a box to access the digital content immediately. See the Terms of sale and the Withdraw from the contract here page.")
- ES-09/ES-12 y EN: sustituir "[PENDIENTE: correo de soporte]" por `{{EMAIL_CONTACTO}}`.
- ES-12 "¿Es de pago único?": sustituir "[PENDIENTE MÓDULO 7: confirmar con condiciones]" por "Pago único, sin suscripción."
- ES-13: sustituir "PENDIENTE MÓDULO 7…" por: "Precio con IVA incluido. Entrega digital inmediata por email. Si pagas y empiezas la descarga tras aceptar la casilla de acceso inmediato, pierdes el derecho de desistimiento; si no se cumplen los requisitos legales, tienes 14 días. Garantía legal de conformidad. Enlaces: Condiciones de venta · Desistir del contrato aquí · Privacidad · Aviso legal · Cookies." EN-13 equivalente tras redactar las condiciones en inglés.
- Pie de la tienda: enlaces a los cinco textos; ES-11/EN-11: enlazar el botón de la muestra a `formulario-email.md`.
- ES-08: la etiqueta `[ESTIMACIÓN…]` no debe publicarse; si el contraste con la competencia no se puede probar, cambiar "Muchos cuadernos de este tema te piden…" por "Algunos cuadernos de este tema te piden…".
- `estructura.md` §2.2: corregir "IVA 21 %" por la tarifa que confirme el gestor (4 % ebook; pack mixto pendiente).
- Registrar la edición humana del ebook (qué se editó) antes de publicar.

## Veredicto: CAMBIOS
Los 8 textos están corregidos y no tienen fallos propios pendientes. La página de producto necesita los cambios de arriba. **No publicar hasta rellenar los huecos del titular, elegir las apps de entrega y email, y revisar con un profesional las dudas de `consulta-gestor.md` (nº 4, 10, 11, 12, 13).** No hay riesgo para BLOQUEADO: hay desistimiento, avisos y base de datos.

Revisión basada en fuentes oficiales; no es asesoramiento jurídico. Confirmar con un profesional las dudas de `consulta-gestor.md`.
