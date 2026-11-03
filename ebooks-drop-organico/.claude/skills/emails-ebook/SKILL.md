---
name: emails-ebook
description: Redacta la secuencia de emails automáticos de un ebook (cualquier nicho): entrega de la muestra gratis con doble confirmación, 4-5 emails de valor y venta, email de compra y post-compra, en ES y EN, cumpliendo LSSI/RGPD. Usar en el módulo 8 tras estructura-ebook y textos-legales, o cuando el usuario diga "emails", "secuencia", "lead magnet", "muestra gratis por email".
model: sonnet
---

# Emails del ebook (genérica)

Base: `conocimiento/07-legal/02-analisis.md` §1.7 (consentimiento, baja, 14 años), `nichos/<nicho>/legal/formulario-email.md`, Dani [8Er-sAVrULo] (1 campaña/semana al empezar; limpiar inactivos ~180 días) [OPINIÓN mentor]. Herramientas: **entrega de la muestra** = la muestra como **producto digital a 0 €** en la tienda (la app de descargas la entrega por email al "comprarla"; vale para quien NO acepta marketing) [ESTIMACIÓN: verificar en la tienda]. **Emails comerciales** = **Shopify Email** (10.000 envíos/mes gratis [DATO, `09-numeros/datos-costes.md`]; solo envía a quien aceptó marketing, que es justo lo que exige la LSSI).
- Precio en los emails: variable `[PRECIO_CON_IVA]` que se rellena con el precio de la tienda (nunca escrito a mano en dos sitios).
- El email 2 (valor sin venta) se trata como **comercial** por prudencia (forma parte de una secuencia que termina en oferta).
Entradas: `avatar.md`, `estructura.md` (qué incluye, muestra), `pagina-producto.md`, precio. Salida: `nichos/<nicho>/emails/<idioma>/secuencia.md` (asunto, preheader, cuerpo, CTA, día de envío) + `montaje-emails.md`.

## Secuencia (tras pedir la muestra)
0. **Confirmación** (doble opt-in): "Confirma tu email para recibir la muestra".
1. **Día 0 – Entrega**: enlace a la muestra + 1 acción para hoy.
2. **Día 1 – Valor**: el error más común del avatar (frase real parafraseada) y cómo evitarlo.
3. **Día 3 – Historia/escena**: situación del avatar → qué cambia con el plan completo.
4. **Día 5 – Oferta**: qué incluye el ebook, precio con IVA, enlace a la página de producto. Sin urgencia falsa.
5. **Día 8 – Objeciones**: FAQ (formato, dispositivos, qué no es: no sustituye a un profesional en nichos sensibles).
Solo los emails 2-5 son comerciales: van **únicamente** a quien marcó la casilla comercial. Quien solo pidió la muestra recibe 0-1.
**Post-compra**: email de confirmación legal (`legal/email-confirmacion.md`) + día 3 "¿cómo vas?" (pide opinión real, sin incentivo a reseñas positivas).

## Reglas
- Cada email declara avatar y ángulo (regla 10) en una línea interna (no visible).
- Pie obligatorio: titular, motivo de recepción y **baja con un clic**.
- Sin promesas de resultado, sin atributos personales, sin precios tachados.
- Asuntos ≤ 45 caracteres; un solo CTA por email.
