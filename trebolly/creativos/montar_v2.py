# Monta los prompts v2 de Flow a partir de bloques fijos (iguales letra por letra en todos)
STYLE_HANDS = "Vertical 9:16 smartphone video, handheld close-up filmed on an iPhone, slight natural camera shake, realistic, unpolished, authentic UGC look. Calm, warm, pleasant mood."
STYLE_PROPPED = "Vertical 9:16 smartphone video filmed on an iPhone propped on the bathroom shelf, almost static framing with tiny natural movement, realistic, unpolished, authentic UGC look. Calm, warm, pleasant mood."
BANO = "A real bathroom of a normal Spanish flat: plain white wall tiles with grey grout, a walk-in shower with a clear glass screen, a chrome wall bracket and a silver flexible hose, soft morning daylight from a small frosted window."
MARTA_V = "Marta (use the saved character so the face matches exactly), a Spanish woman around 35 with natural skin texture and shoulder-length honey-blonde balayage hair."
FRAME_SHOWER = "Tight framing on her head, wet hair and hands only; her shoulders and body stay out of frame."
ROBE = "She wears a thick white cotton bathrobe closed up to the neck."
PRODUCT = ("The shower head matches the reference image exactly: a matte graphite-grey handheld shower head of normal size with a deep cylindrical head; "
 "its round face is recessed, with a light silver-grey inner dish, a dark grey central nozzle disc full of small spray holes and a ring of black cone-shaped silicone bristles around the edge; "
 "a short angled neck joins the head to a straight graphite handle with a polished chrome collar near the top carrying one small round grey STOP button; "
 "the lower part of the handle unscrews and holds a white filter cartridge with a blue end cap; threaded end at the bottom of the handle.")
OLD_HEAD = "The old shower head is a plain round chrome shower head with a flat face, no bristles and no buttons; water comes only out of its face."
PHYS_WATER = "Water comes only out of the nozzle disc as a soft, dense spray of fine jets. The shower head keeps exactly the same size, shape and colour throughout."
CLEAN = "Rigid objects never bend or melt. Natural hands with five fingers. Real-time natural-speed movement, natural look without lens flares. Plain unbranded objects; no text, letters, labels or logos anywhere."
SOUND = "Ambient sound only: water and a quiet tiled bathroom. No music, no voices, no speech."
PHOTO_LIFE = "Photorealistic lifestyle photograph taken with a good smartphone camera, natural and believable, not a studio advert. Soft natural daylight, gentle contrast, true colours, fine water droplets where there is water, shallow depth of field."
PHOTO_PACK = "Photorealistic e-commerce product photograph, crisp micro-detail, true colours."
PHOTO_NEG = "No text, no letters, no logos, no brand names, no watermarks, no celebrities, no extra buttons on the shower head, no chrome rim around the face, no bent or melted parts, natural hands with five fingers."
MARTA_P = "Marta: Spanish woman around 35, shoulder-length honey-blonde balayage hair, natural skin with light freckles, no makeup."

clips = [
 ("B01","Gancho champú y piel: estante lleno de botes, con el cabezal en el soporte","foto 3 de CJ","sin personaje (solo una mano)",
  [STYLE_PROPPED,BANO,"Close-up. [00:00-00:03] From the very first second, the small white shower shelf is crowded with about ten plain shampoo, shower-gel and hair-mask bottles with blank labels; just above the shelf, the product hangs in the chrome wall bracket, in sharp focus. [00:03-00:06] A woman's hand with natural skin and short plain nails comes in from the right and slowly pushes several bottles to one side with the back of her hand. [00:06-00:08] Her hand stays still next to the bottles; the product stays in the bracket.",PRODUCT,"The product hangs still and no water comes out.",CLEAN,SOUND]),
 ("B02","Gancho tinte: mira las puntas bajo el cabezal viejo (pelo igual que en el resto)","ninguna (cabezal viejo)","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,FRAME_SHOWER,"[00:00-00:03] From the very first second, water from an old shower head falls on Marta's wet honey-blonde balayage hair, seen from behind and slightly to the side. [00:03-00:06] She lifts a strand of the blonde ends with her fingers and looks at it closely. [00:06-00:08] She lets the strand fall and stays still under the water.",OLD_HEAD,CLEAN,SOUND]),
 ("B03","Problema piel: en albornoz, se pasa la mano por el antebrazo","ninguna","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,ROBE,"Medium close-up from the chest up. [00:00-00:03] From the very first second, Marta stands in front of the glass shower screen in the bathrobe, her wet hair combed back. [00:03-00:06] She slowly runs her hand down her opposite forearm and looks at it, thoughtful. [00:06-00:08] She pulls the bathrobe collar a little closer.",CLEAN,SOUND]),
 ("B04","Quitar el cabezal viejo (manos)","ninguna (cabezal viejo)","sin personaje",
  [STYLE_HANDS,BANO,"Close-up of hands only. [00:00-00:03] From the very first second, two hands hold an old shower head attached to the silver flexible shower hose. [00:03-00:06] The hands unscrew the old shower head from the hose by turning it anticlockwise. [00:06-00:08] The old shower head comes off and the threaded hose end is free.",OLD_HEAD.replace("; water comes only out of its face",", and no water is running"),CLEAN,SOUND]),
 ("B05","Enroscar el nuestro a mano","foto 3 de CJ","sin personaje",
  [STYLE_HANDS,BANO,"Close-up of hands only. [00:00-00:03] From the very first second, one hand holds the product by the handle, with the threaded end at the bottom, and the other hand holds the free end of the silver flexible hose. [00:03-00:06] The hands screw the threaded end onto the hose by turning it clockwise, by hand, without tools. [00:06-00:08] The hands place the shower head in the chrome wall bracket and let go.",PRODUCT,"No water is running. The shower head keeps exactly the same size, shape and colour throughout.",CLEAN,SOUND]),
 ("B06","El filtro dentro del mango","fotos 3 y 8 de CJ","sin personaje",
  [STYLE_HANDS,BANO,"Macro close-up of hands only, in front of the white tiles. [00:00-00:03] From the very first second, one hand holds the upper part of the product while the lower section of the handle has already been unscrewed, showing the threads. [00:03-00:06] A white filter cartridge with a blue end cap slides out of the open handle into the other hand. [00:06-00:08] The hand slides the cartridge back into the handle.",PRODUCT,"No water is running. The shower head keeps exactly the same size, shape and colour throughout.",CLEAN,SOUND]),
 ("B07","El chorro nuevo sobre el pelo con mechas","foto 3 de CJ","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,FRAME_SHOWER,"[00:00-00:03] From the very first second, Marta holds the product above her head and its soft spray falls on her wet honey-blonde balayage hair, seen from behind. [00:03-00:06] She runs the fingers of her other hand through her wet hair. [00:06-00:08] She tilts her head back slightly, relaxed.",PRODUCT,PHYS_WATER,CLEAN,SOUND]),
 ("B08","El cepillo de silicona en el cuero cabelludo","foto 3 de CJ","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,FRAME_SHOWER,"Close-up from behind. [00:00-00:03] From the very first second, Marta presses the face of the product gently on her wet scalp, water running. [00:03-00:06] She moves it in small slow circles; the black cone-shaped silicone bristles massage the scalp between the wet strands. [00:06-00:08] Water runs down her hair.",PRODUCT,PHYS_WATER,CLEAN,SOUND]),
 ("B09","Botón STOP: pausar el agua mientras se enjabona el pelo","foto 3 de CJ","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,FRAME_SHOWER,"Close-up on Marta's hand holding the product at head height while her other hand lathers shampoo into her hair. [00:00-00:03] From the very first second, the spray is running. [00:03-00:05] Her thumb presses the small round STOP button on the chrome collar and the spray stops, leaving only a few drops falling from the face. [00:05-00:08] With the water paused, she keeps lathering her hair.",PRODUCT,PHYS_WATER,CLEAN,SOUND]),
 ("B10","Ángulo piel: el chorro suave sobre el antebrazo","foto 3 de CJ","sin personaje (solo el brazo)",
  [STYLE_HANDS,BANO,"Close-up of a woman's forearm and hand only, natural skin with light freckles. [00:00-00:03] From the very first second, the soft spray from the product, held in her other hand, falls on her forearm and the back of her hand. [00:03-00:06] Drops run down her skin as she slowly turns her arm under the water. [00:06-00:08] She moves the spray up to her wrist.",PRODUCT,PHYS_WATER,CLEAN,SOUND]),
 ("B11","Cierre: sale tranquila en albornoz","ninguna","Marta",
  [STYLE_PROPPED,BANO,MARTA_V,ROBE,"Medium close-up from the chest up. [00:00-00:03] From the very first second, Marta steps out of the shower in the bathrobe, her wet hair combed back. [00:03-00:06] She runs her fingers through the ends of her hair and smiles softly to herself, relaxed. [00:06-00:08] She stays still for a moment, calm.",CLEAN,SOUND]),
 ("B12","El pack de 2. PREFERENTE: animar la foto F02 aprobada (fotograma inicial)","F02 aprobada como fotograma inicial + foto 3 de CJ","sin personaje",
  [STYLE_HANDS,"Animate the start image. [00:00-00:03] Everything is still, exactly as in the start image. [00:03-00:06] Two hands enter from the bottom and gently straighten the two shower heads, then leave the frame. [00:06-00:08] Everything stays still. Everything else stays exactly as in the start image: the same two shower heads and exactly ten filter cartridges in the same positions.",PRODUCT,"No water is running. The shower heads keep exactly the same size, shape and colour throughout.",CLEAN,SOUND]),
 ("B12-alt","El pack de 2 sin fotograma inicial (solo si no se puede animar F02)","fotos 3 y 7 de CJ","sin personaje",
  [STYLE_HANDS,"Top-down close-up on the white bathroom counter next to the washbasin, white tiles at the edge. [00:00-00:03] From the very first second, two identical products lie side by side on the counter. [00:03-00:06] Two hands place exactly ten identical white filter cartridges with blue end caps below them, in two neat rows of five. [00:06-00:08] The hands leave the frame and everything stays still.",PRODUCT,"No water is running. The shower heads keep exactly the same size, shape and colour throughout.",CLEAN,SOUND]),
 ("B13","Plano héroe del chorro. PREFERENTE: animar la foto F01 aprobada","F01 aprobada como fotograma inicial (o foto 3 de CJ)","sin personaje",
  [STYLE_HANDS,BANO,"Close-up, one hand holds the product at an angle in front of the white tiles, backlit by the window light. [00:00-00:03] From the very first second, a soft, dense spray of fine jets comes out of the nozzle disc, catching the light. [00:03-00:06] The camera moves slowly closer to the face, the black cone-shaped bristles and the dark nozzle disc. [00:06-00:08] The spray keeps going, even and steady.",PRODUCT,PHYS_WATER,CLEAN,SOUND]),
]
photos = [
 ("F00","NUEVA · Retrato de Marta para crear el personaje (no se publica)","ninguna","1:1",
  ["Portrait photograph: Marta facing the camera from the shoulders up, standing in the bathroom described below, in a thick white cotton bathrobe closed up to the neck, wet hair combed back, neutral friendly expression, looking at the camera.",BANO,MARTA_P,PHOTO_LIFE,PHOTO_NEG]),
 ("F01","Tienda · foto 1 (principal)","foto 3 de CJ","1:1, 2048x2048",
  ["Product photograph on a plain very light warm-grey background: one hand holds the product diagonally by the lower handle, the hose out of frame below; a soft, dense spray of fine jets comes out of the nozzle disc; the product fills about 75 % of the frame. Soft even studio light with a gentle shadow.",PRODUCT,PHOTO_PACK,PHOTO_NEG]),
 ("F02","Tienda · foto 2 y estático E4 (pack de 2)","fotos 3 y 7 de CJ","1:1 y 4:5",
  ["Top-down photograph on the white bathroom counter next to the washbasin: two identical products side by side and, below them, exactly ten identical white filter cartridges with blue end caps in two neat rows of five. White wall tiles softly visible at the edge.",BANO,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F03","Tienda · foto 3 y estático E2 (tinte)","foto 3 de CJ + personaje Marta","1:1 y 4:5",
  ["Marta from behind and slightly to the side, under the shower, holding the product above her head; a soft, dense spray of fine jets falls on her wet honey-blonde balayage hair. Tight framing on her head, wet hair and hands; her shoulders and body stay out of frame.",BANO,MARTA_P,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F04","Tienda · foto 4 (cepillo)","foto 3 de CJ","1:1",
  ["Close-up from behind: the face of the product pressed gently on Marta's wet scalp, the black cone-shaped silicone bristles between the wet balayage strands, water running down. Tight framing on her head and hands.",BANO,MARTA_P,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F05","Tienda · foto 5 (filtro en el mango)","fotos 3 y 8 de CJ","1:1",
  ["Close-up of two hands in front of the white tiles: one hand holds the upper part of the product, the lower section of the handle unscrewed and held in the other hand, and a white filter cartridge with a blue end cap half out of the open handle.",BANO,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F06","Tienda · foto 6 (STOP)","foto 3 de CJ","1:1",
  ["Close-up of Marta's hand holding the product at head height, her thumb on the small round STOP button on the chrome collar, no water coming out, shampoo foam in her wet hair softly out of focus behind. Tight framing on her hand and head.",BANO,MARTA_P,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F07","Tienda · foto 7 y estático E3 (piel)","foto 3 de CJ + personaje Marta","1:1 y 4:5",
  ["Marta just out of the shower in a thick white cotton bathrobe closed up to the neck, wet hair combed back, holding the product in one hand at chest height in sharp focus and touching her forearm with the other hand, smiling softly.",BANO,MARTA_P,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
 ("F08","Tienda · foto 3 y estático E1 (champú, ángulo principal)","foto 3 de CJ","1:1 y 4:5",
  ["The small white shower shelf crowded with about ten plain shampoo, shower-gel and hair-mask bottles with blank labels; just above them, in sharp focus, the product hangs in the chrome wall bracket. Plenty of empty plain tile wall at the top for a headline.",BANO,PRODUCT,PHOTO_LIFE,PHOTO_NEG]),
]
out=["# Prompts de Google Flow del cabezal · v2 (revisión del 18-nov)\n",
"Montados con bloques fijos, iguales letra por letra en todos (script: `montar_v2.py`). Sustituyen a los v1 solo si los fundadores los aprueban.\n",
"**Antes de gastar un crédito:** comparar el bloque del producto con la foto 3 de CJ. La v1 decía \"thin chrome rim\" (aro cromado en la cara). En todas las fotos que hemos revisado (M, B, Q, las de \"Así funciona\" y los packs), el cromado es un **collar en el mango** con el botón STOP, la cabeza es un **cilindro profundo** y las cerdas son **conos negros**. Si la foto 3 dice otra cosa, manda la foto y se cambia el bloque.\n",
"**Bloques que cambian respecto a la v1:**\n",
"- **Producto:** cabeza cilíndrica, cara hundida con plato gris plata, disco central oscuro, conos negros, collar cromado con el STOP, mango que se desenrosca y cartucho blanco con tapa azul.\n",
"- **Cámara:** \"filmed by a family member\" fuera.\n  - Las escenas de Marta se graban con el móvil apoyado en la balda: es como se graba el UGC y evita la escena rara de alguien grabando en la ducha.\n  - Las de manos, en mano.\n",
"- **Física del agua:** solo en los clips donde sale nuestro cabezal con agua. Mencionar \"water\" o \"shower head\" en un clip que no los lleva invita a la IA a meterlos.\n",
"- **Sonido:** sin radio. Una radio generada puede meter voces o palabras inventadas que chocan con la voz en off. La música con licencia se pone en el montaje.\n",
"- **Desnudez:** en la ducha, encuadre cerrado en cabeza, pelo y manos. Albornoz cerrado en vez de toalla. Nada de hombros ni espalda desnudos (riesgo de desnudez insinuada en Meta, más aún con una cuenta nueva).\n",
"- **Antes y después:** el pelo es el mismo en todos los clips. Fuera \"dull and dry\" (B02) y \"bright and healthy\" (F03): juntos forman un antes y después fabricado (regla 4).\n\n"]
out.append("## Clips de vídeo (Veo, 9:16, 8 s, sin diálogo)\n")
for cid,title,ref,who,parts in clips:
    txt=" ".join(parts)
    out.append(f"### {cid} · {title}\n- Referencia: {ref} · {who} · {len(txt)} caracteres\n```\n{txt}\n```\n")
out.append("## Fotos (Nano Banana en Flow): una por chat nuevo\n")
for pid,title,ref,fmt,parts in photos:
    txt=" ".join(parts)
    out.append(f"### {pid} · {title}\n- Formato {fmt} · referencia: {ref} · {len(txt)} caracteres\n```\n{txt}\n```\n")
open('/home/user/DROP-ORGANICO/trebolly/creativos/prompts-flow-v2.md','w').write("\n".join(out))
import shutil; shutil.copy(__file__,'/home/user/DROP-ORGANICO/trebolly/creativos/montar_v2.py')
print(len(clips),len(photos))
