# 03 - Puntuación de mercado v2 (m1-prueba-1)

_14-oct-2026. Modelo: Sonnet. Skill `puntuar-nicho` v2, pasos 3 y 4. 6 nichos, ES y EN por separado._

## Método
- Fuentes (todas del 14-oct-2026): **a** = `datos-v2-a.md`, **b** = `datos-v2-b.md` (principales, [PÁGINA]); **n** = `datos-navegador.md` (apoyo); **gs** = gummysearch en `02-filtros.md` (apoyo de Dolor solo EN); **GPE** = Gumroad/Payhip/Etsy de `datos\*.md`. Cualquier otro dato de `datos\*.md` es [BUSCADOR] y no se usa.
- Estabilidad = [SIN DATO] (Trends 429). Hueco = [SIN DATO] en los 6 nichos (reseñas de Amazon piden login). No puntúan. Quedan Dolor 30 + Pago 30 + Precio 15 = **cobertura 75 %** por idioma; nota = media ponderada sobre ese 75 %.
- Dolor: solo vídeos específicos del nicho y de los últimos 2 años; los Shorts sin antigüedad se admiten con aviso. Pago y Precio: solo ebooks digitales específicos (tapa blanda y genéricos no cuentan).
- Tipos: [P] página, [B] buscador (−1, solo precios GPE), [E] interpolación propia.

## Exclusiones (una línea cada una)
- Dormir ES: humor 5,3 M (no trata el problema); meditación 1,9 M (audio, no guía); "vencer el insomnio" 2,1 M (insomnio general); "Cómo dejar de pensar demasiado" y "Master Your Sleep" (genéricos).
- Ruptura ES: videoclip 301 K y sus comentarios (música); vídeo de 4 años; "21 días" 124 val. (tapa blanda). Ruptura EN: Short en español (#5).
- TDAH ES: Short 839 K y sus comentarios (cerebro TDAH, padres); vídeo de 5 años; líder "Cómo estudiar..." (4 val.): va dirigido a padres, no a universitarios. TDAH EN: vídeo de 5 años; "ADHD is Awesome" y "Learning Outside the Lines" (genéricos).
- Sueldo: "Never Split the Difference" y "Lean In for Graduates" (negociación y carrera generales); vídeos de 3 y 5 años.
- Cachorro ES: "Educación canina para toda la familia" 252 val. (general); vídeo de 7 años. Cachorro EN: vídeos de 4-5 años; Cesar Millan (perros en general).
- Presupuesto: vlog "Cómo organizo mi dinero" (finanzas generales); "Forever Paycheck" (jubilación); vídeo 3,8 M de 3 años.

## Notas ES / EN
| Nicho | Criterio | ES | EN | Fuente y tipo |
|---|---|---|---|---|
| **Cachorro** | Dolor | 4 | 3 | ES: 524 K, 344 K, 48 K, 2,4 K, 2,5 K + comentario de miedo [P a]. EN: sin vídeo válido (todos >2 años); solo r/puppy101 475 K, +14 % [P gs] |
| | Pago | 3 | 5 | ES: Sandra Ferrer 96 val., rank Kindle 45.481 [P a]. EN: Art of Raising a Puppy 4,7 K, Ken Phillips 2,4 K [P a] |
| | Precio | 2 | 2,5 | ES: mediana Kindle 4,99 €; Payhip 47 € sin ventas [P n,GPE]. EN: mediana 4,04 €, 13,47 € con 4,7 K val.; Gumroad 5-21 USD [B] |
| **Sueldo** | Dolor | 3 | 4 | ES: 38 K, 11 K, 181 K, 1,8 K, 1 K [P a]. EN: 382 K, 450 K, 9,3 M [P a]; comentarios sin dolor |
| | Pago | 1 | 3 | ES: Kindle "sin resultados" [P a]. EN: "How to Negotiate Your First Job" 70 val. [P n] |
| | Precio | SD | 2 | ES: sin ebooks. EN: mediana Kindle 4,04 €; Gumroad 15-47 USD sin ventas [B] |
| **Presupuesto** | Dolor | 3,5 | 3,5 | ES: 788 K, 484 K, 830, 11 [P a]. EN: 32 K, 44 K, 11 K, 2,3 K, 162 [P a] + r/povertyfinance 2,9 M, +20,9 % [P gs] |
| | Pago | 1 | 5 | ES: valoraciones visibles máx. 2, ranking SD [E a]. EN: Avery Breyer 1,4 K, rank 103.627 [P a] |
| | Precio | 3 | 2 | ES: 4,20 € y 8,60 € (n=2) [P a,n]. EN: mediana 4,49 €; Etsy muchas ventas a 2-10 USD [B] |
| **Dormir** | Dolor | 3 | 3,5 | ES: 110 K y 2,1 K (n=2) [P b]. EN: 218 K y 2,1 K (n=2) + 1 comentario de dolor [P b] |
| | Pago | 1 | 1 | ES: 1 val., rank 341.790. EN: 1 val., rank 1,07 M [P b] |
| | Precio | 1 | 2 | ES: mediana 3,99 €. EN: mediana 2,69 €; Gumroad/Payhip 5-30 USD sin ventas [B] |
| **TDAH** | Dolor | 3 | 4,5 | ES: solo Short 97 K (n=1) [P b]. EN: 254 K, 171 K, 119 K, 72 K + 2 comentarios de dolor; r/adhd_college 23 K, +49,7 % [P b,gs] |
| | Pago | 1 | 3 | ES: 1-2 val. [P b]. EN: How to Conquer College 28 val., rank 1,41 M [P b] |
| | Precio | 1 | 1,5 | ES: 3,43-4,27 €. EN: mediana 0 € (muchos gratis/KU); packs 18 USD [B] |
| **Ruptura** | Dolor | 3 | 4 | ES: 68 K, 18 K (n=2) [P b]. EN: 474 K, 174 K, 543, 4 [P b] + r/ExNoContact 195 K, +16,9 % [P gs] |
| | Pago | 3 | 5 | ES: Gabriel Arana 35 val., rank 104.960 [P b]. EN: Natalie Lue 674 val., rank 671.951 [P b] |
| | Precio | 1,5 | 2 | ES: 0 € (KU) y 8,60 €. EN: 7,15 € con ventas visibles; Payhip 8,99 USD [P b,GPE] |

## Resultado
| Nicho | Mercado ES | Mercado EN | Cobertura ES/EN | F5 (≥3,0 y ≥2,0) | Media |
|---|---|---|---|---|---|
| Cachorro | 3,20 | 3,70 | 75/75 % | **SÍ** | 3,45 |
| Ruptura | 2,70 | 4,00 | 75/75 % | **SÍ** | 3,35 |
| Presupuesto | 2,40 | 3,80 | 75/75 % | **SÍ** | 3,10 |
| Sueldo | no decidible (2,0 parcial) | 3,20 | **60**/75 % | NO (ES no decidible) | - |
| TDAH | 1,80 | 3,30 | 75/75 % | NO (ES <2,0) | - |
| Dormir | 1,80 | 2,20 | 75/75 % | NO (EN <3,0) | - |

**Top 3: Cachorro (3,45), Ruptura (3,35), Presupuesto (3,10).** Todos lideran en EN; la diferencia entre ellos (≤0,35) no es significativa [ESTIMACIÓN]. Ninguno supera el techo teórico de 90 % de cobertura.

## Comparación con v1
En v1 ningún nicho pasaba F5 (≥3,5/≥2,5) y ES salía hundido por [SIN DATO]=1. En v2 [SIN DATO] no puntúa, ES tiene vídeos y Kindle verificados, y se excluyen resultados genéricos. Cachorro sube de 2,56/3,08 a 3,20/3,70 y Presupuesto de 2,03/3,11 a 2,40/3,80. Las notas no son comparables del todo: v1 incluía Avatar y Ángulos.

## Ajustes pendientes
1. **Hueco y Estabilidad siguen sin datos** (login de Amazon, Trends 429): 25 % del peso inutilizable. Con umbral de 70 %, basta un [SIN DATO] en Dolor, Pago o Precio para dejar un idioma "no decidible" (Sueldo ES).
2. **Ventana de 2 años en Dolor** descarta vídeos evergreen de 4-5 años y millones de visitas (Cachorro EN, Presupuesto), pero admite Shorts sin fecha. Es asimétrica: proponer 5 años o tratar la antigüedad [SIN DATO] igual para todos.
3. **Muestras mínimas de Dolor**: hay notas con n=1 o n=2 (TDAH ES, Dormir, Ruptura ES). Con mínimo de 3 vídeos específicos pasarían a [SIN DATO] y Ruptura ES quedaría no decidible, cayendo del top 3. El resultado es frágil.
4. **Anclas de Pago incoherentes**: "valoraciones O ranking" da 5 a Ruptura EN (674 val., rank 672 K) y 3 a TDAH EN (28 val., rank 1,4 M). Falta una regla única, con ranking Kindle como criterio principal, y abrir siempre la ficha del líder.
5. **Precio**: los precios "0,00 (KU)" arrastran la mediana; hay que leer el precio de compra. Las ventas de Gumroad/Payhip/Etsy solo salen del buscador [B].
6. **Dolor EN con apoyo gummysearch solo en 4 de 6 nichos** (no hay en Sueldo ni Dormir): sesgo entre nichos.
