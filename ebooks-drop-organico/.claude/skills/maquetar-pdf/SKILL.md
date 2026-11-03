---
name: maquetar-pdf
description: Maqueta un ebook o su muestra en PDF por código (HTML + CSS impreso con el navegador Edge de Windows, sin coste ni cuentas) en dos formatos (pantalla principal + imprimible), con plantilla editorial fija, kit de marca del nicho, portada con motivo SVG, componentes visuales, índice con enlaces y espacios para escribir. Usar en el módulo 2 tras revisor-calidad, o cuando el usuario diga "maqueta el ebook", "haz el PDF", "portada", "diseño del ebook".
model: sonnet
---

# Maquetar PDF (genérica: el nicho entra como dato)

Entradas: textos aprobados en `nichos/<nicho>/ebook/<idioma>/`, kit de marca `nichos/<nicho>/marca.json` (si no existe, créalo con la plantilla de abajo y pide aprobación al usuario), `estructura.md`.
Salida por idioma: `muestra-pantalla.html/.pdf` y `muestra-imprimible.html/.pdf` (o `<nombre>-...` si no es la muestra).
Archivos de la skill: `plantilla.css` (componentes comunes), `plantilla-pantalla.css`, `plantilla-imprimible.css`, `lineas.js` (líneas de escribir), `componentes.html` (iconos y motivos SVG para copiar), `generar-pdf.ps1` (HTML → PDF con Edge).
Nada de estos archivos depende de un nicho: lo específico (textos, colores, título) va en el HTML y en `marca.json`.

## 0. Regla: dos formatos (pantalla principal + imprimible)
- **Pantalla (principal)**: es lo que se vende y se lee en móvil/tablet. Página estrecha tipo libro 148×210 mm (A5), cuerpo 13 pt, interlineado 1,5, márgenes 15 mm, párrafos cortos. Contiene portada, índice, capítulos, tarjetas (en versión visual) y avisos. Enlaza `plantilla.css` + `plantilla-pantalla.css`.
- **Imprimible**: solo lo que se rellena o se pega en la pared: hojas de ejercicios, tarjetas SOS/de acción y trackers. A4 (ES/UE) o Letter (EN: añadir `@page { size: Letter; }` en el `<style>` del HTML). Sin portada ni índice. Enlaza `plantilla.css` + `plantilla-imprimible.css`.
- La versión pantalla remite al imprimible con una nota ("Para imprimir"). Los trackers anchos (7 columnas) van en horizontal en el imprimible y en filas (tabla vertical) en pantalla.
- Si un párrafo supera ~70 palabras, pártelo en el HTML sin cambiar el contenido. [ESTIMACIÓN]
- Cifras de diseño de pantalla (13 pt, 1,5, 15 mm, ~50-55 caracteres por línea): [ESTIMACIÓN], pensadas para lectura en pantalla pequeña; se validan mirando el PDF en móvil.

## 1. Kit de marca (`marca.json`, por nicho)
```json
{"color_principal":"#...","color_acento":"#...","color_fondo_suave":"#...","fuente_titulos":"Inter","fuente_texto":"Source Serif 4","tono_visual":"...","tamano_pagina":{"es":"A4","en":"Letter"}}
```
Colores con contraste legible (texto oscuro sobre fondo claro; blanco sobre principal y sobre acento). Kit coherente en todo el pack (Kate [-jPA44GaAAc]). Los tintes (cajas de ejercicio, conexiones de pasos) se derivan solos del color de acento con `color-mix`.

## 2. HTML
Un HTML por formato e idioma. Enlaza los dos CSS (ruta relativa a `.claude/skills/maquetar-pdf/`), define las variables de marca en `:root`, copia de `componentes.html` el sprite de iconos y el motivo de portada, y termina con `<script src=".../lineas.js"></script>`.
Estructura de pantalla: `section.portada` → `nav.indice` → `section.capitulo` (uno por capítulo, con `id`) → tarjeta → cierre. Marcas del texto → HTML:
- `[ESPACIO: n líneas]` → `<div class="espacio" style="--lineas:n"></div>` (`lineas.js` dibuja las n líneas).
- `[TRACKER: ...]` → `table.tracker` (imprimible: `.t7` horizontal; pantalla: tabla en filas).
- Avisos de contenido → `aside.caja-i.aviso`.
- Antes de rellenar, comprueba que cada bloque cabe en su página (Kate [HtsOEJfAaNo]); si no, divide.

## 3. Componentes visuales (en `plantilla.css`)
Iconos: `<svg class="ico"><use href="#ico-ejercicio"/></svg>` (también `ico-sos`, `ico-aviso`, `ico-consejo`; sprite en `componentes.html`).
- **Portada**: `section.portada` con `<svg class="motivo">` a sangre (ondas + círculo, por código, sin imágenes de terceros; se puede regenerar con otras formas según `tono_visual`) y `div.texto` con `h1`, `.subtitulo`, `.detalle` y **una sola** `.etiqueta` ("Muestra gratuita"). No usar páginas con nombre en CSS (crean una página en blanco); la portada es la primera página (`@page :first`).
- **Regla de portada: presentar siempre 3 propuestas de portada distintas (claro ilustrado / tipográfica / oscura premium u otras), con PNG, y que el usuario elija; comprobar legibilidad en miniatura (título legible a 150 px de ancho).** Cada propuesta: HTML propio por código (sin imágenes de terceros, nada que imite portadas existentes) en `nichos/<nicho>/ebook/<idioma>/portadas/portada-<A|B|C>.html` + PNG con Edge. El motivo gráfico concreto va en el HTML del nicho, no en la plantilla.
- **Apertura de capítulo**: `div.apertura` (bloque de color principal) con `.etiqueta` y `h1`, más motivo `svg.motivo`.
- **Pasos numerados**: `<ol class="pasos">`; números grandes en círculo de color acento con hilo de unión.
- **Frase destacada**: `<blockquote class="destacada"><p>…</p></blockquote>`, una por sección y solo con una frase que el texto ya tenga (se coloca esa frase como cita, sin duplicarla).
- **Cajas con icono**: `div.caja-i.ejercicio` (tinte suave; `largo` si tiene 5+ líneas y puede partirse entre páginas), `.consejo`, `.sos-uso` (cuándo usarlo), `.aviso`; cada una con `<div class="cabecera">{icono}Etiqueta</div>`.
- **Separador**: `<hr class="sep">` entre secciones. **Tarjeta**: `.tarjeta` con `.tarjeta-top`, `.tarjeta-titulo`, `ol`, `.tarjeta-nota`, `.tarjeta-pie`. **Mini tarjetas**: `.minis > .mini(.mini-on)`.
- Jerarquía: h1 27 pt / h2 18 pt con barra de acento / h3 14 pt (pantalla) [ESTIMACIÓN]. Los títulos no quedan huérfanos al final de página.

## 4. PDF
`powershell -File .claude\skills\maquetar-pdf\generar-pdf.ps1 -Html <ruta.html> -Pdf <ruta.pdf>` para cada formato (Windows). **En la nube (Linux)**: `node .claude/skills/maquetar-pdf/generar-pdf.js <ruta.html> <ruta.pdf>` (Chromium/Playwright; mismo resultado, probado 03-nov con la muestra: 20 págs = 20 págs); para PNG: `node generar-pdf.js <ruta.html#ancla> <salida.png> 559 794 2`. Si Google Fonts está bloqueado en la red, instalar las fuentes OFL desde npm (`@fontsource/inter`, `@fontsource/source-serif-4`) y enlazarlas en local. Revisa nº de páginas y mira cada página (por ejemplo, abriendo el PDF en el navegador del panel o con una hoja de contactos); corrige saltos feos: páginas con mucho blanco al final, títulos o cajas partidos, números de paso huérfanos. El navegador Edge no genera PNG de páginas de un PDF: para imágenes de la portada o de páginas interiores, `msedge --headless --screenshot` sobre una copia temporal del HTML con ventana de 559×794 px (proporción 148×210).

## 5. Reglas editoriales
- Pantalla: cuerpo 13 pt, interlineado 1,5 [ESTIMACIÓN]. Imprimible: cuerpo 11 pt, interlineado 1,4, dentro de los rangos de Butterick (cuerpo 10-12 pt en impreso, interlineado 120-145 %, 45-90 caracteres por línea; https://practicaltypography.com/summary-of-key-rules.html).
- Jerarquía de 3 niveles, numeración de página (no en la portada), espacios para escribir con líneas.
- Fuentes: **solo licencia libre para incrustar** (Inter y Source Serif 4 son OFL, de Google Fonts; el CSS las carga de Google Fonts al generar, hace falta internet). Si se cambia de fuente, comprobar su licencia y anotarla.
- Cada entregable declara a qué avatar y ángulo sirve (regla del proyecto).

## 6. Lista objetiva antes de entregar
Dos PDF por idioma (pantalla e imprimible) · tamaño de página correcto (148×210 mm / A4 o Letter) · índice con enlaces que funcionan · espacios para escribir · páginas imprimibles · contraste legible · fuentes con licencia · sin texto cortado ni desbordado (portada incluida) · una sola etiqueta en portada · sin página en blanco · sin títulos huérfanos · sin párrafos de más de ~70 palabras · sin imágenes de terceros.
