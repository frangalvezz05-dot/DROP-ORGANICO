---
name: guiones-organicos
description: Escribe guiones de vídeos cortos orgánicos SIN CARA (TikTok, Reels, Shorts) para vender un ebook de cualquier nicho, en ES y EN: gancho con frase real del avatar, estructura emoción → solución → ebook, texto en pantalla, escenas (con prompts para IA o B-roll libre), CTA y etiqueta IA. Usar en el módulo 5 tras avatar-angulos, o cuando el usuario diga "haz los guiones", "ganchos", "vídeos para TikTok", "contenido orgánico".
model: sonnet
---

# Guiones orgánicos sin cara (genérica)

Base: `conocimiento/05-contenido/02-critica.md` (decisiones), análisis de Marc y Dani, `07-legal/02-analisis.md` (§1.10-11). Consulta primero el grafo.
Entradas: `nichos/<nicho>/avatar.md` (avatar, ángulos, ganchos), `frases.md`, `estructura.md` (qué incluye el ebook, muestra gratis), capturas reales del ebook si existen.
Salida: `nichos/<nicho>/contenido/<idioma>/guiones-<lote>.md` + `prompts-escenas.md`.

## Cabecera obligatoria de cada guion (Dani [_e96MM2Qo5s])
`Avatar · Ángulo · Formato · Objetivo (alcance / clic / muestra) · Por qué debería funcionar · Variante de (si lo es)`

## Estructura (20-40 s; un plano cada ~3 s [OPINIÓN Marc YOgCnLtNgHE])
1. **Segundo 1 — gancho**: texto en pantalla + primera imagen. Usa palabras reales del avatar (`frases.md`, parafraseadas y sin datos del autor). Emoción o situación concreta, nunca el producto [Marc _Gn95sdhsIw].
2. **Segundos 2-3 — retención**: concretar la escena ("día 9 sin escribirle…").
3. **Cuerpo**: 2-4 planos con valor real (consejo accionable sacado del ebook, error común, lista).
4. **Último tercio — producto**: el ebook como siguiente paso (capturas reales de páginas, sin mockups engañosos).
5. **CTA**: uno solo: "guía en el enlace del perfil" o "comenta X y te digo dónde está la muestra gratis" (según `plan-publicacion`).

## Formatos permitidos (sin persona realista)
POV con texto · lista "cosas que nadie te dice" · mini-lección · hojeo del ebook · frase del público + respuesta. Escenas: B-roll de objetos/lugares (móvil boca abajo, café, calle, cuaderno), generado con IA o de bancos libres (Pexels/Pixabay: comprobar licencia). **Si una imagen es realista y hecha con IA → marcar "ETIQUETA IA: sí"** (TikTok/Meta/YouTube).

## Prohibido
Promesas de resultado ("recupera", "garantizado", ingresos), diagnósticos o atributos personales de quien mira ("¿tienes ansiedad?"), urgencia o escasez falsas, reseñas/testimonios inventados, imitar a personas reales, copiar el texto de otros creadores (sí su estructura), borrar metadatos para evitar detección.

## Lote estándar
Por idioma y ángulo: **10 guiones** = 4 formatos distintos + 3 ganchos alternativos por guion (para variantes). Música: indicar "audio en tendencia del país, elegir en la app" (no nombrar canciones con derechos para uso fuera de la app).

## Prompts de escenas (`prompts-escenas.md`)
Por guion: plano, descripción, prompt en inglés para el generador de vídeo/imagen IA, duración, y alternativa con B-roll libre. Estilo coherente con `marca.json`.

## Al terminar
Pasar los guiones al agente `mentor-contenido-marc-verdu` (una llamada por lote) y al `revisor-legal` (puntos 8, 10, 11, 12). Corregir y anotar cambios.
