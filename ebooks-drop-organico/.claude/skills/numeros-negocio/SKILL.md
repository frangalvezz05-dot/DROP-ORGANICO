---
name: numeros-negocio
description: Recalcula el modelo de rentabilidad de un ebook (cualquier nicho) con su precio y sus datos de lanzamiento, y dice si el negocio es viable (margen por venta, punto de equilibrio, visitas y visualizaciones necesarias). Usar en el módulo 9 o cuando el usuario diga "¿sale rentable este nicho?", "números del negocio", "punto de equilibrio", "¿a qué precio vendo?".
model: haiku
---

# Números del negocio (genérica: el nicho entra como dato)

## Entradas
- Precio IVA incluido del nicho (de `nichos/<nicho>/estructura.md`) y tipo de IVA (4 % ebook; 21 % si el pack no es "libro": ver `conocimiento/07-legal/fiscal.md`).
- Datos de lanzamiento, si existen (`nichos/<nicho>/metricas-lanzamiento.md`): visitas, ventas, visualizaciones, clics. Si no, usar las tasas [ESTIMACIÓN] por defecto.
- Costes: leer `conocimiento/09-numeros/datos-costes.md`. **Comprobar la fecha de recogida: si tiene más de 3 meses (hoy menos esa fecha), avisar al principio: "Datos de costes caducados, hay que repetir la búsqueda"** y marcar el resultado como provisional.
- Método de referencia: `conocimiento/09-numeros/modelo.md`. Umbrales: `.claude/skills/metricas-lanzamiento/SKILL.md`.

## Cálculo (ejecutarlo con código, no de cabeza)
1. Coste fijo mensual en 3 escenarios: A sin alta (Shopify + dominio/12), B1 alta con tarifa plana, B2 alta con cuota normal. Importes de `datos-costes.md`.
2. Margen por venta = precio / (1 + IVA) − comisión % × precio − comisión fija.
3. Ventas de equilibrio = coste fijo / margen, redondeado hacia arriba.
4. Visitas = ventas / conversión (0,5 %, 1 %, 2 %). Visualizaciones = visitas / clic de vídeo a tienda (0,5 % y 1 %).
5. Con datos reales de lanzamiento: sustituir las tasas estimadas por las medidas (conversión = ventas/visitas; clic = visitas/visualizaciones) y recalcular. Solo vale con ≥1.000 visitas.

## Veredicto
- VIABLE: en B2 el equilibrio exige menos de ~15 ventas/mes y las visitas necesarias son alcanzables con el ritmo de vídeos del nicho; o conversión medida ≥1 %.
- JUSTO: solo se cubre en A o B1; avisar de que el negocio depende de la tarifa plana (12 meses).
- NO VIABLE: B1 exige >15 ventas/mes o el precio de mercado es ≤9,99 €. Proponer subir precio o plan B del nicho.
Indicar el precio mínimo exigible en el mercado para ese nicho.

## Reglas
Etiquetar cada cifra [DATO] / [ESTIMACIÓN] / [SIN DATO]. Resultado antes de IRPF; decir qué costes no entran (gestor, IRPF). No contactar, pagar ni publicar. Salida: `nichos/<nicho>/numeros.md`, resumen en 10 líneas para Fran, en español sin tecnicismos.
