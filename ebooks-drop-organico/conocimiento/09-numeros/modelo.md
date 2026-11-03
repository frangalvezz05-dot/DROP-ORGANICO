# Modelo de rentabilidad (módulo 9 · paso 3)

Datos de entrada: `datos-costes.md` (recogidos 2026-11-03). Umbrales: `.claude/skills/metricas-lanzamiento/SKILL.md` (≥1.000 visitas para que un resultado sea válido; conversión visita→compra ≥1 % y ≥10 ventas = MANTENER).
Todo es margen **antes de IRPF**. Cifras redondeadas; ventas al mes redondeadas hacia arriba.

## 1. Coste fijo mensual
| Concepto | A) Sin alta de autónomo | B1) Alta, tarifa plana (12 primeros meses) | B2) Alta, cuota normal |
|---|---|---|---|
| Shopify Basic (mensual, 32 €) [BUSCADOR] | 32,00 | 32,00 | 32,00 |
| Dominio .com (15 €/año) [BUSCADOR] | 1,25 | 1,25 | 1,25 |
| Apps de descarga, email, casilla | 0 | 0 | 0 |
| Cuota autónomo | 0 | 88,64 | 205,88 |
| **Total/mes** | **33,25 €** | **121,89 €** | **239,13 €** |

Con Shopify en pago anual (24 €/mes): A = 25,25 €; B1 = 113,89 €; B2 = 231,13 €. Cambia poco el resultado (menos de 1 venta al mes).
Escenario A: ojo, vender sin darse de alta puede no ser legal si hay actividad habitual con ánimo de lucro; lo decide el gestor (ver `conocimiento/07-legal/consulta-gestor.md`). Se modela para saber cuánto cuesta no depender del alta. [ESTIMACIÓN]

## 2. Margen por venta (IVA 4 % incluido en el precio; comisión 2,4 % + 0,25 €)
Margen = precio / 1,04 − 2,4 % × precio − 0,25 €.
| Precio | Base sin IVA | IVA 4 % | Comisión de pago | **Margen por venta** | Margen % del precio |
|---|---|---|---|---|---|
| 9,99 € | 9,61 | 0,38 | 0,49 | **9,12 €** | 91 % |
| 14,99 € | 14,41 | 0,58 | 0,61 | **13,80 €** | 92 % |
| 19,99 € | 19,22 | 0,77 | 0,73 | **18,49 €** | 92 % |
| 24,99 € | 24,03 | 0,96 | 0,85 | **23,18 €** | 93 % |
Si la comisión real fuese 2,9 % + 0,30 €, el margen baja solo 0,1-0,2 € por venta. El producto digital no tiene coste de producto ni envío, así que el margen por venta no es el problema: lo es la cuota fija y el tráfico. Riesgo: si el pack mixto tributase al 21 %, el margen cae ~14 % del precio (p. ej. a 14,99 € pasaría de 13,80 a ≈ 11,6 €).

## 3. Punto de equilibrio y tráfico necesario
Ventas/mes = coste fijo / margen. Visitas = ventas / conversión. Visualizaciones = visitas / clic de vídeo a tienda (1 % y 0,5 %).
Conversión 0,5 / 1 / 2 % y clic 0,5-1 % son [ESTIMACIÓN] (sin fuente fiable; ver `datos-costes.md`).
| Escenario | Precio | Ventas/mes | Visitas conv. 0,5 % | Visitas conv. 1 % | Visitas conv. 2 % | Visualizaciones/mes (conv. 1 %; clic 1 % → clic 0,5 %) |
|---|---|---|---|---|---|---|
| A (sin alta) | 9.99 € | 4 | 800 | 400 | 200 | 40.000 - 80.000 |
| A (sin alta) | 14.99 € | 3 | 600 | 300 | 150 | 30.000 - 60.000 |
| A (sin alta) | 19.99 € | 2 | 400 | 200 | 100 | 20.000 - 40.000 |
| A (sin alta) | 24.99 € | 2 | 400 | 200 | 100 | 20.000 - 40.000 |
| B1 (alta, tarifa plana) | 9.99 € | 14 | 2.800 | 1.400 | 700 | 140.000 - 280.000 |
| B1 (alta, tarifa plana) | 14.99 € | 9 | 1.800 | 900 | 450 | 90.000 - 180.000 |
| B1 (alta, tarifa plana) | 19.99 € | 7 | 1.400 | 700 | 350 | 70.000 - 140.000 |
| B1 (alta, tarifa plana) | 24.99 € | 6 | 1.200 | 600 | 300 | 60.000 - 120.000 |
| B2 (alta, cuota normal) | 9.99 € | 27 | 5.400 | 2.700 | 1.350 | 270.000 - 540.000 |
| B2 (alta, cuota normal) | 14.99 € | 18 | 3.600 | 1.800 | 900 | 180.000 - 360.000 |
| B2 (alta, cuota normal) | 19.99 € | 13 | 2.600 | 1.300 | 650 | 130.000 - 260.000 |
| B2 (alta, cuota normal) | 24.99 € | 11 | 2.200 | 1.100 | 550 | 110.000 - 220.000 |
Lectura: la última columna es con conversión 1 %; con 0,5 % se multiplica por 2 y con 2 % se divide entre 2. Cuántos vídeos son depende de las visualizaciones medias por vídeo [SIN DATO]: p. ej. B2 a 14,99 € (180.000-360.000 visualizaciones/mes) son 180-360 vídeos si cada uno hace 1.000 visualizaciones, o 18-36 si cada uno hace 10.000 [ESTIMACIÓN].

## 4. Contraste con los umbrales de `metricas-lanzamiento`
- Una prueba válida exige ≥1.000 visitas en la página. Equilibrio con conversión 1%: A necesita 200-400 visitas (menos que el mínimo de validez); B1 600-1.400; B2 1.100-2.700. Por eso con el escenario A el equilibrio llega antes que una medición válida.
- El umbral de MANTENER (≥10 ventas) solo cubre costes en B1 a ≥19,99 € y en B2 a ≥24,99 € [a 24,99 €: 11 ventas]. A 9,99 € no cubre ni B1 con 10 ventas.
- 10 ventas × 14,99 € = 138 € de margen: cubre A y B1 pero no B2 (239 €).

## 5. Conclusión
1. El margen por venta es muy alto (≈ 91-93 %); el reto es la cuota fija y el tráfico, no el coste del producto.
2. Sin alta (A) basta con 2-4 ventas al mes; con alta y cuota normal (B2) hacen falta 11-27 ventas, es decir 2.200-5.400 visitas a conversión 0,5 %, o 110.000-540.000 visualizaciones mensuales con conversión 1 %.
3. Precio mínimo recomendable: 14,99 € (B2 exige 18 ventas; a 9,99 € exige 27 y es casi inviable con tráfico orgánico). El punto dulce es 19,99-24,99 € si el mercado lo acepta.
4. Para elegir nicho: exigir que los competidores ya vendan packs/ebooks a ≥15 € (idealmente 19-25 €) con prueba de pago; descartar nichos donde el precio de mercado sea ≤9,99 €.
5. Aprovechar la tarifa plana (12 meses) y pedir al gestor si cabe retrasar el alta mientras se valida; con precio ≥19,99 € el equilibrio en B1 son 7 ventas/mes (700 visitas a conversión 1 %).
