---
name: avatar-angulos
description: Construye el AVATAR (una persona concreta, método 3 Circles, con frases reales del cliente) y el BANCO DE ÁNGULOS de un nicho de ebook, en español e inglés por separado. Es la pieza más importante del proyecto: el ebook, la web, los emails y los guiones salen de aquí. Usar tras puntuar-nicho (modo ligero para finalistas, modo completo para el nicho elegido) o cuando el usuario diga "avatar", "ángulos", "ganchos", "a quién le vendemos".
model: sonnet
---

# Avatar y ángulos

Fuentes del método: `conocimiento/01-nichos/elevate-publishers/01-analisis.md` (3 Circles [rO4h5ofNWic][IZCVZQtV2TI], consciente/inconsciente [GEfbMGW_45U], value equation [43UQKmwsvO0]) y `travis-nicholson/01-analisis.md` (vender resultado [HJgCfeX42F4], fuentes de problemas [78FdQGWrxIY]). Consulta el grafo antes de releerlas.

## Modos
- **Ligero** (cada finalista): miedo central + deseo central + 5 frases reales por idioma + 5 ganchos por idioma. Máx. 1 página.
- **Completo** (solo el nicho elegido): todo lo de abajo. Al terminar, **pasa el resultado al agente `critico` (Opus) para revisión** antes de enseñarlo al usuario.

## 1. Recoger la voz del cliente (por idioma, nunca traducida)
Delega la recogida en UN subagente `model: haiku` con el **navegador integrado** (secuencial, `get_page_text`, rechazar cookies, sin iniciar sesión). WebFetch no sirve: Amazon y otras webs lo bloquean. Fuentes, por este orden:
1. Reseñas de los libros/ebooks líderes en Amazon (.es para ES, .com para EN), sobre todo de 1-3 estrellas.
2. Comentarios de vídeos de YouTube del tema (y TikTok si el navegador deja entrar).
3. Títulos de hilos de gummysearch.com (solo EN). Reddit está prohibido en el navegador: no forzar.
Para cada frase guarda: texto literal, enlace, fecha, idioma, y a qué círculo apunta. **Sin nombre de usuario** (RGPD). Objetivo: ligero ≥5, completo ≥10 por idioma. Si no llegas, dilo: no inventes ni rellenes.

## 2. 3 Circles (una sola persona, no un segmento)
Construye de fuera hacia dentro, cada dato con su frase o fuente:
- **Exterior**: edad, situación, ocupación, dinero. Es lo que menos decide.
- **Medio**: estilo de vida, valores, dónde pasa el tiempo, qué guarda o comparte.
- **Centro**: miedos, frustraciones, deseos, lo que no dice en voz alta.
Escribe al final al **comprador en una frase**: "[persona] que [situación] y teme [miedo], quiere [deseo]".
**Test**: si el centro no tiene al menos 2 miedos respaldados por frases reales → el nicho es un tema, no una idea. Avísalo.
Si ES y EN dan personas distintas, documenta las dos: no fuerces una sola.

## 3. Banco de ángulos
1. Lista **todos los problemas** del camino hasta el resultado deseado.
2. Clasifica cada uno según la value equation: resultado soñado, probabilidad percibida, tiempo, esfuerzo.
3. Convierte cada problema en solución/promesa **sin prometer resultados garantizados** (sobre todo en salud y finanzas).
4. Separa ángulos para:
   - **Inconsciente** (no busca un libro): nombra su dolor exacto con sus palabras. Es el ángulo principal para TikTok/Reels.
   - **Consciente** (ya busca solución): resultado concreto + plazo + diferencia frente a la competencia.
5. **Modas**: si hay una tendencia actual dentro del nicho, añádela como ángulo con fecha de caducidad estimada.
6. **Ganchos**: ≥10 por idioma en modo completo. Cada gancho indica ángulo, frase real en la que se apoya y nivel de conciencia.
7. **Hueco y diferencial**: qué critican las reseñas negativas y cómo un ebook de acción lo resuelve mejor.

## 4. Salida → `pruebas/<ejecucion>/avatar-<nicho>.md`
Secciones: voz del cliente (tabla con enlaces), avatar ES, avatar EN, comprador en una frase, banco de ángulos, ganchos, hueco y diferencial, riesgos (claims prohibidos, normas de plataforma), y qué falta por saber.

## Reglas
- Nunca frases inventadas ni "parafraseadas como si fueran reales". En textos públicos se usará paráfrasis; en este archivo, la literal con enlace.
- Nada de prácticas engañosas: testimonios falsos, escasez falsa, ocultar que es publicidad o que hay IA.
- Etiquetas: [DATO] / [OPINIÓN mentor] / [ESTIMACIÓN] / [SIN DATO].
