---
name: montar-tienda-shopify
description: Monta en BORRADOR la tienda Shopify de un ebook o pack digital (cualquier nicho): tema gratuito, idiomas, mercados aprobados, producto digital con la app oficial de descargas, páginas, formulario de email, contraseña activa. Usa la herramienta de Shopify si está conectada; si no, genera una guía paso a paso para el usuario. Usar en el módulo 3 tras pagina-producto, o cuando el usuario diga "monta la tienda", "sube el producto a Shopify".
model: sonnet
---

# Montar tienda Shopify (genérica: el nicho entra como dato)

Entradas: `nichos/<nicho>/tienda/pagina-producto.md`, `tienda/imagenes/`, PDF del producto, `marca.json`, decisiones del mód. 7 (si existen).
Salida: tienda en borrador + `nichos/<nicho>/tienda/montaje.md` (qué se hizo, qué falta, qué decide el usuario).

## Límites (regla 9; obligatorios)
- **La cuenta de Shopify la crea el usuario.** Claude no crea cuentas.
- Contratar un plan, instalar apps de pago, activar cobros reales o quitar la contraseña de la tienda (publicar) = **"sí" explícito del usuario** antes de cada acción.
- Sin enlaces de afiliado de mentores.

## 0. Comprobar la conexión
Llama a la herramienta de Shopify (`get-shop-info`). Si pide autenticación o falla → **plan B**: escribe en `montaje.md` una guía paso a paso con capturas descritas, para que el usuario lo haga, y para.

## 1. Montaje (todo en borrador)
1. Tema gratuito de Shopify, sin modificar su código [4JGeKANrv7g]; logo, favicon, colores y fuentes de `marca.json`.
2. Idiomas: español (España) e inglés.
3. **Mercados** (mód. 7 aprobado): **España/UE en €**; EE. UU. solo si el usuario lo decide tras el gestor; **Reino Unido cerrado** (IVA UK desde la 1.ª venta).
4. Producto: digital (desmarcar "producto físico"), precio del pack, textos de `pagina-producto.md`, imágenes de `tienda/imagenes/`. Archivo entregado con la app oficial de descargas digitales (gratuita) y límite de descargas razonable [DATO: `conocimiento/03-tienda/datos-shopify.md`, reconfirmar].
5. Pasarela: **solo Shopify Payments** al inicio (decisión del usuario 15-oct-2026); la verificación de identidad la hace el usuario.
6. Páginas: inicio (sencilla, lleva al producto), FAQ, contacto y legales de `nichos/<nicho>/legal/` (skill `textos-legales`): aviso legal, condiciones, privacidad, cookies, **"Desistir del contrato aquí"**; enlazadas en el pie. Banner de cookies con "Rechazar" al mismo nivel.
7. Formulario de email para la muestra gratis con el texto de `legal/formulario-email.md` (casilla comercial aparte, no premarcada; doble opt-in).
8. Impuestos: activar IVA de productos digitales UE, precios **con IVA incluido** (ebook 4 %; pack con plantillas: lo que diga el gestor). Casilla de desistimiento en el checkout (app gratuita de casilla o, si no hay, plan B anotado) con el texto de `legal/checkout-casilla.md`, y email de confirmación con `legal/email-confirmacion.md`.
9. Contraseña de tienda **activada** (se puede probar sin publicar).

## 2. Al terminar
Pasar a `revision-tienda` (pasada técnica).
