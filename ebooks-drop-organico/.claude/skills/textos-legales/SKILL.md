---
name: textos-legales
description: Redacta los textos legales de una tienda online de ebooks o packs digitales (cualquier nicho) para España/UE: aviso legal, condiciones de venta, privacidad, cookies, desistimiento (excepción de contenido digital + botón "desistir del contrato aquí"), texto de la casilla del checkout, email de confirmación y consentimiento del formulario de email. Con huecos {{...}} para los datos del titular. Usar en el módulo 7, antes de montar-tienda-shopify, o cuando el usuario diga "páginas legales", "política de privacidad", "condiciones", "desistimiento".
model: sonnet
---

# Textos legales (genérica: el nicho y el producto entran como datos)

Base: `conocimiento/07-legal/02-analisis.md` (§1 obligatorio, §2 recomendable), `consumo-datos-publicidad.md` y `fiscal.md`. Consulta primero el grafo.
**Aviso fijo** al principio de cada salida: "Plantilla basada en fuentes oficiales (BOE, AEPD) consultadas el 03-nov-2026. No es asesoramiento jurídico: revisar con un profesional antes de publicar."

Entradas: `nichos/<nicho>/00-ficha.md`, `estructura.md` (qué incluye el pack, formato, páginas), precio, idiomas, mercados aprobados, app de email y de entrega elegidas.
Salida: `nichos/<nicho>/legal/` con un archivo por texto, en ES (y EN si la tienda tiene inglés; el ES manda en caso de discrepancia).

## Huecos que rellena SOLO el usuario (nunca inventarlos)
{{NOMBRE_TITULAR}} · {{NIF}} · {{DOMICILIO}} · {{EMAIL_CONTACTO}} · {{TELEFONO}} (opcional si hay otro medio rápido; [ESTIMACIÓN], confirmar con profesional) · {{NOMBRE_TIENDA}} · {{DOMINIO}} · {{FECHA_ACTUALIZACION}}.
Si falta un hueco, se deja visible en MAYÚSCULAS y la tienda no se publica (lo comprueba `revisor-legal`).

## Textos y contenido mínimo
1. **aviso-legal.md** (LSSI art. 10): titular, NIF, domicilio, email; actividad; condiciones de uso; propiedad intelectual (ebook con edición humana; prohibida la reventa y redistribución); ley aplicable española.
2. **condiciones-venta.md** (TRLGDCU art. 97-98): identidad y contacto; características del producto (formato PDF, nº páginas, idioma, dispositivos y programas para abrirlo = funcionalidad e interoperabilidad, sin DRM salvo que lo haya); precio final **con IVA incluido** (4 % ebook; si el pack lleva plantillas, nota "pendiente de gestor"); forma de pago (Shopify Payments); entrega inmediata por email/enlace de descarga y límite de descargas; **desistimiento**: explicar la excepción del art. 103.m con sus 3 requisitos y que si no se dan hay 14 días; modelo de formulario de desistimiento; garantía legal de conformidad del contenido digital (arts. 115 bis ss.) sin promesas de resultado; reclamaciones (email) y resolución de litigios; mercados donde se vende (por defecto España/UE; Reino Unido no).
3. **privacidad.md** (RGPD art. 13): responsable; finalidades separadas (gestionar la compra / enviar la muestra pedida / emails comerciales solo con consentimiento); bases jurídicas; plazos; encargados (Shopify, app de email, pasarela) y transferencias a EE. UU. (marco de privacidad UE-EE. UU. o cláusulas tipo: [ESTIMACIÓN] confirmar con cada proveedor); derechos y cómo ejercerlos; reclamación ante la AEPD; edad mínima 14 años (LOPDGDD art. 7).
4. **cookies.md**: técnicas vs analíticas/publicitarias; banner con **Aceptar y Rechazar al mismo nivel**, sin casillas premarcadas, retirada igual de fácil; lista de cookies que pone el tema y las apps (rellenar tras montar).
5. **checkout-casilla.md**: casilla propia, **no premarcada**, junto al botón "Pedido con obligación de pago":
   "Solicito acceder al contenido digital de inmediato y acepto que, al empezar la descarga, pierdo mi derecho de desistimiento." (+ enlace a condiciones).
6. **email-confirmacion.md** (soporte duradero, art. 98.7): resumen del pedido, precio con IVA, enlace de descarga, **copia literal del consentimiento y del reconocimiento** con fecha y hora, enlace al botón de desistimiento y a las condiciones.
7. **desistir-aqui.md** (Dir. 2023/2673, recomendado): página "Desistir del contrato aquí" con formulario (nombre, email, nº pedido) → paso "Confirmar desistimiento" → acuse por email con contenido, fecha y hora. Explicar cuándo procede (si no se cumplió la excepción).
8. **formulario-email.md** (LSSI 21-22): formulario de la muestra gratis: casilla aparte, no premarcada, para emails comerciales; texto de información básica de privacidad; **doble opt-in** recomendado; baja con un clic en cada email.

## Reglas de redacción
- Lenguaje claro; nada de "garantizado", "resultados asegurados", ni presentar derechos legales como ventaja propia (Ley 3/1991).
- Nichos sensibles (salud mental, finanzas, salud): añadir en condiciones y en la página un aviso "contenido informativo, no sustituye a un profesional" y, si procede, recursos de ayuda verificados del nicho.
- Sin reseñas mostradas hasta que existan; si se muestran, texto de cómo se verifican (TRLGDCU art. 20.4).
- Etiqueta cada afirmación dudosa con [ESTIMACIÓN] o [SIN DATO] en un comentario al final, nunca dentro del texto público.

## Al terminar
Pasar a `revisor-legal`. Copiar la lista de dudas abiertas a `conocimiento/07-legal/consulta-gestor.md` si aparece alguna nueva.
