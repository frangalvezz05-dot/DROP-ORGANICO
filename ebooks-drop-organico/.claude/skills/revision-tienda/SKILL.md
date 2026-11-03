---
name: revision-tienda
description: Revisa una tienda Shopify de producto digital (cualquier nicho) antes de lanzar, en dos pasadas: técnica (móvil, velocidad, enlaces, entrega, mercados, coherencia, pago desde el navegador de TikTok/Instagram) y legal (tras el módulo 7: IVA, desistimiento, políticas, garantía). Usar en el módulo 3 tras montar-tienda-shopify, o cuando el usuario diga "revisa la tienda", "¿está lista para lanzar?".
model: haiku
---

# Revisión de la tienda (genérica)

Entradas: tienda en borrador (con contraseña), `nichos/<nicho>/tienda/montaje.md`, `pagina-producto.md`.
Salida: `nichos/<nicho>/tienda/revision.md` (lista OK / FALLO con cambio propuesto).
Haiku recorre la lista con el navegador integrado; para el punto "prácticas engañosas" lanza un subagente `model: sonnet`. Al final de la pasada técnica, el `critico` (Opus) revisa una sola vez con la página incluida.

## Pasada 1 · Técnica (ahora)
1. Vista móvil (`resize_window` preset mobile): primer pantallazo, botón de compra visible/fijo, textos legibles, imágenes que cargan.
2. Velocidad aparente (carga de la página de producto) y enlaces que funcionan.
3. Coherencia: mismo precio, nombre y contenido en página, ebook y pago (Marc [oEFWZdCw5FQ]).
4. Mercados abiertos = solo los aprobados (por defecto España/UE; Reino Unido cerrado).
5. Entrega: en un pedido de prueba llega el email con el archivo y se descarga bien.
6. **Pago desde el navegador de TikTok e Instagram** en un **móvil ajeno**, **iOS y Android**, entrando con la contraseña de la tienda [kq0bZo65WNM]. Documentar qué pasa. Si probarlo exige un plan de pago o una compra real, **parar y pedir "sí" al usuario** (lo hace el usuario).
7. Causas de "visitas sin ventas" de Marc [oEFWZdCw5FQ] aplicables a digital (tráfico de robots, mensajes incoherentes, lentitud, dudas sin resolver).
8. Prácticas engañosas (subagente Sonnet): reseñas, contadores, escasez, precios tachados, promesas.
9. Declaración de avatar y ángulo en la página (regla 10).

## Pasada 2 · Legal (después del módulo 7)
Solo: precio con IVA, configuración de impuestos, casilla de desistimiento de contenido digital y email de confirmación, botón de desistimiento, políticas, garantía, consentimiento del formulario de email, mercados definitivos.

## Veredicto
LISTA PARA PUBLICAR (solo tras la pasada 2 y con "sí" del usuario) / CAMBIOS.
