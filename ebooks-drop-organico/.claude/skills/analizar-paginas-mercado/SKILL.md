---
name: analizar-paginas-mercado
description: Analiza páginas de venta de productos digitales que ya están funcionando (con señales reales de venta) para extraer su ESTRUCTURA: orden de secciones, puntos que tocan, presentación del precio, confianza, tipos de imagen, FAQ y diseño en móvil. Nunca copia textos ni imágenes. Usar en el módulo 3 antes de redactar la página de producto, o cuando el usuario diga "mira páginas que funcionan", "cómo venden los competidores", "analiza tiendas".
model: haiku
---

# Analizar páginas de venta del mercado (genérica: el nicho entra como dato)

Petición del usuario (15-oct-2026): la página de producto debe basarse en páginas de ecommerce que ya funcionan. Complementa "copiar tiendas que convierten" de Marc [OZQGBv-TaXw] limitándolo a la **estructura**.
Entrada: `nichos/<nicho>/` (ficha, `ebooks-mercado.md`, avatar).
Salida: `nichos/<nicho>/tienda/paginas-mercado.md`.

## 0. Antes
Consulta el grafo y reutiliza las URLs ya vistas en `ebooks-mercado.md`.

## 1. Elegir 5-8 páginas [ESTIMACIÓN] con señal de que funcionan
Cada una debe tener al menos una señal visible: nº de ventas o "X personas lo compraron", reseñas reales numerosas, insignia de más vendido, o anuncio activo durante semanas en la Biblioteca de anuncios de Meta. Mezcla:
- 2-3 del nicho (o temas cercanos) en ES y EN.
- 2-3 de productos digitales de otros nichos con muchas ventas (para patrones generales).
- 1-2 tiendas Shopify de producto digital si se encuentran.
Anota la señal de cada una; si no tiene ninguna, no entra.

## 2. Qué extraer (navegador integrado, secuencial; móvil si es posible con `resize_window` preset mobile)
Por página: orden de secciones de arriba abajo · tipo de titular (beneficio / problema / resultado) · cuántos beneficios y cómo se muestran · cómo enseñan "qué incluye" · tipos de imagen (portada, mockup, páginas interiores, vídeo) · presentación del precio (con/sin IVA, packs, comparativa) · elementos de confianza (garantía, autor, vista previa, reseñas, pago seguro) · temas de la FAQ · llamadas a la acción (cuántas, dónde, botón fijo en móvil) · longitud aproximada · qué se ve en el primer pantallazo del móvil.
Leer con `get_page_text` y, para el diseño, capturas a escala reducida. Rechazar cookies, no iniciar sesión, no comprar.

## 3. Derechos y ética
Solo estructura y patrones descritos con tus palabras. Prohibido copiar textos, titulares completos, imágenes o diseños literales. Señala las prácticas engañosas que veas (contadores falsos, escasez inventada) para **no** imitarlas.

## 4. Salida
Tabla por página (URL, señal de venta, estructura) + **patrones comunes** (lo que hacen casi todas) + **diferencias** con lo que proponen nuestros mentores + **qué aplicar** a nuestra página [ESTIMACIÓN] + "Problemas:" (lo que no se pudo ver = [SIN DATO]).
