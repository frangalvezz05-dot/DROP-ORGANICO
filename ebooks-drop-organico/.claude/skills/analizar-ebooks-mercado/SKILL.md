---
name: analizar-ebooks-mercado
description: Ingeniería inversa de los ebooks, guías y cuadernos que ya se venden en un nicho (ES y EN): estructura, extensión, ejercicios, extras, precio y señales de venta, sin copiar texto. Usar en el módulo 2 antes de diseñar la estructura de un ebook, o cuando el usuario diga "qué venden los competidores", "cómo son los ebooks de este nicho", "analiza la competencia del ebook".
model: haiku
---

# Analizar ebooks del mercado (genérica: el nicho entra como dato)

Entrada: carpeta del nicho `nichos/<nicho>/` (ficha, avatar, términos de búsqueda en ES y EN).
Salida: `nichos/<nicho>/ebooks-mercado.md`.

## 0. Antes de abrir el navegador
1. Consulta el grafo (`C:\Users\frangalveez\.graphify-venv\Scripts\graphify.exe query "<nicho> ebooks competencia" --budget 2000`).
2. Lee lo que ya exista en `nichos/<nicho>/` (datos de puntuación, `ebooks-mercado.md` previo) y **completa solo lo que falte**.

## 1. Recogida (navegador integrado, secuencial)
Herramientas `mcp__Claude_Browser__*`; leer con `get_page_text`; rechazar cookies; no iniciar sesión; Reddit prohibido.
- Amazon EN (amazon.com) y ES (amazon.es): 2 búsquedas por idioma (una general y una con `&i=digital-text`), con términos del nicho + "workbook/journal/plan/guide" o "cuaderno/guía/plan/ejercicios".
- Tiendas digitales: Gumroad, Payhip, Etsy (búsqueda del nicho).
- Elige 8-12 productos [ESTIMACIÓN] **específicos del nicho** (descarta libros genéricos y narrativos).
- Por producto: formato, páginas, precio, valoraciones, ranking, estructura (días/fases/capítulos), tipos de ejercicio, extras, tono y a quién va dirigido, fecha.

## 2. Derechos de autor (obligatorio)
Solo estructura y datos, descritos con tus palabras. Prohibido copiar párrafos, descripciones o índices completos. Como mucho, títulos de capítulo sueltos de menos de 8 palabras.

## 3. Salida
- Tabla por idioma (un producto por fila, URL incluida).
- **Patrones**: estructura que se repite, extensión típica (digital vs papel), ejercicios más comunes, extras que acompañan a los precios altos.
- **Mínimo del mercado**: lo que todos incluyen (entrada, no diferencia).
- **Huecos** [ESTIMACIÓN]: lo que nadie ofrece.
- **Señales de venta**: si casi nadie tiene reseñas/ranking, titula la lista "ejemplos encontrados", no "líderes", y dilo en una frase.
- "Problemas:" con lo que no se pudo ver. Lo no visto = [SIN DATO]. Nunca inventar.
