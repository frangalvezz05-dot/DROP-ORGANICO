"""Descarga la transcripción completa de vídeos de YouTube a archivos .md.

Uso:  python -I transcribir.py <carpeta_salida> <id1> <id2> ...
Cada archivo: <id>.md con título, URL y texto. Si ya existe, lo salta.
"""
import sys, time
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)
api = YouTubeTranscriptApi()

for vid in sys.argv[2:]:
    dest = out / f"{vid}.md"
    if dest.exists():
        print("YA EXISTE", vid)
        continue
    try:
        tr = api.fetch(vid, languages=["es", "es-ES", "es-419", "en"])
        text = " ".join(s.text.replace("\n", " ") for s in tr)
    except Exception as e:
        print("FALLO", vid, type(e).__name__)
        time.sleep(3)
        continue
    dest.write_text(f"# {vid}\n\nhttps://www.youtube.com/watch?v={vid}\n\n{text}\n", encoding="utf-8")
    print("OK", vid, len(text.split()), "palabras")
    time.sleep(2)
