---
name: plan-publicacion
description: Prepara el plan de publicación orgánica de un ebook (cualquier nicho): cuentas, calentamiento, calendario de 14 días por ángulo, enlace a la tienda, registro de métricas por vídeo y reglas de decisión (regla de fases, variantes del 5 % mejor, cuándo cambiar de ángulo o de nicho). Usar en el módulo 5 tras guiones-organicos, o cuando el usuario diga "calendario", "cuándo publico", "¿este vídeo funciona?", "registro de vídeos".
model: haiku
---

# Plan de publicación (genérica)

Base: `conocimiento/05-contenido/02-critica.md`, `.claude/skills/metricas-lanzamiento/SKILL.md`, `conocimiento/09-numeros/modelo.md`.
Entradas: guiones de `nichos/<nicho>/contenido/<idioma>/`. Salida: `nichos/<nicho>/contenido/plan.md` + `registro.csv`.

## Límites (regla 9)
Claude **no crea cuentas ni publica**. Deja cada vídeo listo (guion, texto, descripción, hashtags, etiqueta IA) y el usuario lo sube. Calentar cuentas lo hace el usuario.

## 1. Cuentas
- 1 cuenta por idioma y plataforma (TikTok, Instagram, YouTube), nombre de marca del nicho, foto = logo de `marca.json`, bio con la promesa (sin promesas prohibidas) y enlace a la página de producto (no a la home) [Marc kq0bZo65WNM].
- TikTok: enlace en bio solo con requisitos de la plataforma (Marc dice 1.000 seguidores [-5U7E20GXL8], **verificar**); mientras, CTA a Instagram o a la muestra gratis.
- Calentamiento (usuario, 10-15 min/día, 3-5 días): ver enteros vídeos del nicho, guardar y comentar; no usar la cuenta personal [OPINIÓN Marc ZB2fSfh9rZA].

## 2. Calendario (14 días por ángulo)
2 vídeos/día por cuenta, misma pieza en las 3 plataformas. Días 1-4: 1 guion de cada formato; días 5-14: variantes de lo que mejor vaya (gancho distinto, un solo cambio por variante [Dani s1hMMVWgf00]). No repetir el mismo vídeo idéntico (variar ≥30 % [OPINIÓN Marc SQFnF0cgRwk]).

## 3. Registro (`registro.csv`)
fecha, plataforma, idioma, id_guion, ángulo, formato, gancho, visitas_24h, visitas_72h, % visto completo, seguidores ganados, clics al enlace, visitas tienda (UTM `utm_source=<plataforma>&utm_campaign=<angulo>`), ventas, nota "por qué" [Dani YFpMEAuSgXQ].

## 4. Reglas de decisión
- **< 300 visitas** a las 72 h = sin alcance: revisar cuenta/gancho [Marc SQFnF0cgRwk].
- **Regla de fases** [Marc oposIsO1i90]: 0-1.000 → cambiar segundo 1; 1.000-2.000 → segundo 2; 2.000-3.000 → segundo 3; >5.000 → A/B de música, texto o fondo.
- **Top 5 %** de vídeos (por clics a la tienda, no solo visitas) → 5-10 variantes cada uno [Dani 8Er-sAVrULo].
- A los **14 días**: si ningún vídeo pasa 1.000 visitas → cambiar de ángulo; las decisiones de precio o nicho se toman solo con `metricas-lanzamiento` (≥1.000 visitas a la tienda).
- Cada lunes: resumen de la semana en `plan.md` (qué funcionó y por qué) → alimenta `guiones-organicos`.
