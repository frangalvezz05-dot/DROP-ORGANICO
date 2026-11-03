---
name: pagina-producto
description: Redacta la página de producto de un ebook o pack digital (cualquier nicho) en ES y EN: orden de secciones basado en páginas que ya funcionan y en las reglas destiladas de Adrián Sáenz y Marc Verdú, textos desde el avatar y los ángulos, sin prácticas engañosas. Usar en el módulo 3 tras analizar-paginas-mercado e imagenes-producto, o cuando el usuario diga "página de producto", "textos de la tienda", "descripción del ebook".
model: sonnet
---

# Página de producto (genérica: el nicho entra como dato)

Entradas (`nichos/<nicho>/`): `tienda/paginas-mercado.md` (base estructural), avatar y ángulos, `estructura.md` (pack y precio), `marca.json`, muestra del ebook, `tienda/imagenes/`.
Salida: `nichos/<nicho>/tienda/pagina-producto.md` (una sección por idioma, lista para pegar en Shopify).
Opcional: llamar **antes** de redactar a `mentor-tienda-adrian-saenz` y `mentor-tienda-marc-verdu` (1 vez cada uno por nicho).

## 0. Antes
Consulta el grafo (`conocimiento/03-tienda/02-critica.md` y análisis de Adrián y Marc). Declara al principio a qué avatar y ángulo sirve la página (regla 10).

## 1. Orden de secciones
Parte de los **patrones comunes** de `paginas-mercado.md`. Si no existe, usa este orden por defecto [ESTIMACIÓN: adaptación a digital del orden de Marc OZQGBv-TaXw]:
1. Título con beneficio (sin prometer resultados garantizados).
2. Imágenes: portada + "qué incluye" + páginas interiores (5 tipos de Adrián [VyGaE-cp1GI]).
3. 3-4 beneficios concretos, desde los problemas del avatar.
4. Qué incluye (formato, páginas, plantillas, dispositivos donde se lee, descarga inmediata).
5. Precio **con IVA incluido** [DATO, mód. 7] y botón de compra (fijo en móvil). Cerca del botón: formato, nº de páginas, idioma, dispositivos para abrirlo y enlace a condiciones y desistimiento (información precontractual). Garantía = conformidad del contenido (que funcione y sea lo descrito), nunca de resultados.
6. Vista previa del ebook (páginas reales de la muestra).
7. Descripción problema → dolor → solución con el lenguaje del avatar (paráfrasis, nunca frases literales de comentarios con datos de su autor).
8. FAQ que resuelve dudas reales (de las frases del avatar y de `paginas-mercado.md`) [wWC8SoeQ_Fk].
9. Garantía y condiciones: "PENDIENTE MÓDULO 7" visible.
10. Aviso de contenido según la ficha del nicho.
Cada cambio frente al orden de Marc se anota como [ESTIMACIÓN] con su motivo.

## 2. Reglas
- Prohibido: estrellas o reseñas hasta que haya reales; contadores, escasez o urgencias falsas; textos o imágenes de otras tiendas; promesas de resultado; precios tachados falsos.
- Coherencia: el mismo precio, nombre y contenido en toda la página, el ebook y el pago (causa nº 11 de "visitas sin ventas" de Marc [oEFWZdCw5FQ]).
- Textos cortos, pensados para móvil; frases prohibidas de `redactar-ebook` también aquí.
- ES (España) y EN se **adaptan**, no se traducen literalmente.
- Al terminar, pasar por `revision-tienda` (técnica); el `critico` revisa una sola vez al final.
