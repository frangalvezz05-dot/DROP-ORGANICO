---
name: organico-ebook
description: Dirige el negocio de venta de ebooks con tráfico orgánico (TikTok, Reels, Shorts) coordinando al equipo de agentes ejecutores y auditores, fase a fase, con aprobación de Fran antes de publicar o gastar. Usar cuando Fran diga "empieza la fase X", "siguiente fase", "ciclo diario", "estudia a los referentes", "busca ebook", "haz los vídeos", "revisa cómo vamos".
---

# Orquestador orgánico de ebooks

## Antes de cada fase
1. Leer `memoria/lecciones.md` y `memoria/decisiones.md`.
2. Consultar el grafo (`graphify-out/`) para lo que digan los referentes sobre esa fase. No releer transcripciones enteras.

## Ciclo de cada fase
1. **Ejecutar**: el agente ejecutor de la fase produce su entregable en `entregables/`.
2. **Auditar**: `revisor-metodo` (¿se ajusta al método de los referentes?) y `revisor-legal` (¿es legal?) en paralelo. Cada uno da: APROBADO / CAMBIOS (lista concreta) / BLOQUEADO (motivo).
3. **Corregir**: si hay CAMBIOS, el ejecutor corrige una vez y se vuelve a auditar. Máximo 2 vueltas; si sigue sin aprobarse, preguntar a Fran.
4. **Aprobar**: enseñar a Fran un resumen corto (qué, por qué, qué falta). Esperar su "sí" antes de cualquier publicación, pago, cuenta o contacto.
5. **Aprender**: `diagnosticador` escribe en `memoria/lecciones.md` qué funcionó, qué no y qué cambiar.

## Fase 0 — Estudio de referentes
1. Listar vídeos de los últimos 12 meses de cada canal (`yt-dlp --flat-playlist --dateafter now-1year`).
2. Descargar subtítulos automáticos en español como texto (`yt-dlp --skip-download --write-auto-subs --sub-langs es --convert-subs srt`) a `corpus/<referente>/`, un archivo por vídeo con fecha y título en el nombre. Priorizar vídeos de método (producto, contenido, ganchos, tienda, métricas); saltar vlogs y directos repetidos.
3. Construir el grafo: `/graphify corpus`.
4. Buscar el **referente de ebooks**: alguien que venda ebooks/productos digitales con orgánico y lo explique en vídeos. Criterios: explica el proceso completo, muestra resultados con pruebas (no solo afirmaciones), contenido de los últimos 12 meses, preferiblemente en español. Proponer 3 candidatos a Fran con pros y contras; él elige. Descargar sus vídeos y actualizar el grafo.
5. Extraer `memoria/metodo.md` con esta estructura y citando de qué vídeo sale cada punto:
   - Elección de producto/nicho · Validación · Oferta y precio · Web/página de venta · Perfil de redes · Formatos de vídeo y ganchos · Frecuencia de publicación · Métricas y reglas de decisión · Errores típicos · Qué adaptar de físico a ebook.
   - Marcar coincidencias entre referentes (más fiables) y contradicciones (Fran decide).
6. Repasar con `revisor-metodo` que no quede nada suelto.

## Adaptación físico → ebook (puntos a revisar siempre)
- No hay proveedor ni envío: el margen es casi total, pero la competencia y el precio percibido son distintos.
- TikTok Shop no admite productos digitales: la venta va a una web externa (Shopify con app de descarga digital, Hotmart, Gumroad, etc.). Comprobar condiciones actuales antes de elegir.
- El ebook debe ser propio o con licencia de reventa verificada.
- Derecho de desistimiento en contenido digital (UE): requiere consentimiento expreso y aceptación de la pérdida del derecho antes de la descarga.
