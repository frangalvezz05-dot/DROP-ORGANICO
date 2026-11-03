---
name: imagenes-producto
description: Genera por código las 5 imágenes de producto de un ebook/pack digital para la tienda (portada, escaparate, lista de lo que incluye, perspectivas, extras) con páginas reales del PDF y el kit de marca, sin imágenes de terceros. Usar en el módulo 3 antes de pagina-producto, o cuando el usuario diga "imágenes de producto", "mockups".
model: haiku
---

# imagenes-producto

Genérica: funciona con cualquier nicho. Nada específico de un tema vive aquí; todo sale de `nichos/<nicho>/`.

## Entradas
- `nichos/<nicho>/marca.json` (colores, fuentes).
- `nichos/<nicho>/ebook/<idioma>/`: `*pantalla-portada.png`, `*interior*.png` (páginas reales; si hay menos de 3, se capturan del `*pantalla.html` con anclas), `*tarjeta*.png` (extra imprimible, se recorta solo) y el HTML de pantalla.
- `nichos/<nicho>/estructura.md` (§ pack "qué incluye").
- `nichos/<nicho>/avatar.md` (comprador en una frase).
- `nichos/<nicho>/tienda/imagenes/<idioma>/contenido.json`, que escribe el agente a partir de lo anterior (ver el de `ruptura-contacto-cero` como modelo): `avatar`, `angulo`, `textos` (títulos y pies cortos de cada imagen), `incluye` (5 elementos: `t`, `d`, `icono` entre libro/tarjeta/calendario/plantilla/imprimir/check/estrella), `extras` (lista corta de nombres) y `anclas` (ids del HTML para capturar páginas si faltan).

## Salida
`nichos/<nicho>/tienda/imagenes/<idioma>/`: 10 PNG (`1-portada`, `2-escaparate`, `3-incluye`, `4-perspectivas`, `5-extras`, cada uno `-cuadrado` 1080x1080 y `-vertical` 1080x1350) + `info.md` (avatar y ángulo a los que sirven).

## Los 5 tipos
Fuente: Adrián Sáenz, invitado Alex, vídeo [VyGaE-cp1GI] **[OPINIÓN mentor]**; no verificado con datos de conversión propios.
1. **Portada**: la portada sola, grande, sobre fondo de marca.
2. **Escaparate**: portada en marco de tablet genérico + marco de móvil genérico con una página interior.
3. **Qué incluye**: lista de elementos del pack con iconos SVG propios.
4. **Perspectivas**: 3 páginas interiores reales en abanico.
5. **Extras**: tarjeta/plantilla real del pack + lista de extras en mini.

## Cómo ejecutar
```
powershell -NoProfile -ExecutionPolicy Bypass -File .claude\skills\imagenes-producto\generar-imagenes.ps1 -Nicho <nicho> -Idioma <es|en>
```
`generar-imagenes.ps1` lee marca.json y contenido.json, localiza las páginas reales, rellena `plantilla.html` y hace una captura con Edge headless (sin instalar nada) de cada composición en los dos formatos.

## Reglas
- Sin fotos ni ilustraciones de terceros: solo páginas reales del ebook, el kit de marca y SVG propios.
- Marcos de dispositivo GENÉRICOS (rectángulo redondeado liso, sin muesca, botón ni logo) que no imiten la forma registrada de ninguna marca. Sin logos de marcas.
- Textos cortos, legibles en miniatura. Colores y fuentes solo de marca.json.
- Declarar avatar y ángulo en `info.md` junto a las imágenes.
- Revisar siempre al menos 2 PNG a ojo (texto cortado, páginas en blanco, solapes) antes de darlo por bueno.
- La portada de la muestra puede llevar la etiqueta "muestra gratuita": para la tienda usar la portada del producto de pago.
