# Genera las 5 imágenes de producto (x2 formatos) con Edge headless. Uso:
#   powershell -File generar-imagenes.ps1 -Nicho ruptura-contacto-cero -Idioma es
param([Parameter(Mandatory)][string]$Nicho, [Parameter(Mandatory)][string]$Idioma)
$ErrorActionPreference = 'Stop'
$edge = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
$skill = $PSScriptRoot
$raiz = (Resolve-Path (Join-Path $skill '..\..\..')).Path
$nd = Join-Path $raiz "nichos\$Nicho"
$eb = Join-Path $nd "ebook\$Idioma"
$out = Join-Path $nd "tienda\imagenes\$Idioma"
New-Item -ItemType Directory -Force $out | Out-Null
$utf8 = New-Object System.Text.UTF8Encoding($false)
function Uri($p) { ([Uri](Resolve-Path $p).Path).AbsoluteUri }
function Dim($p) { Add-Type -AssemblyName System.Drawing; $i = [System.Drawing.Image]::FromFile($p); $r = @{w = $i.Width; h = $i.Height }; $i.Dispose(); $r }
function Edge($url, $w, $h, $png) {
  $ud = Join-Path $env:TEMP ('edge-img-' + [guid]::NewGuid().ToString('N'))
  $a = @('--headless', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', "--window-size=$w,$h", '--virtual-time-budget=4000', "--user-data-dir=$ud", "--screenshot=$png", $url)
  Start-Process $edge -ArgumentList $a -Wait -WindowStyle Hidden
  Remove-Item $ud -Recurse -Force -ErrorAction SilentlyContinue
}
$marca = Get-Content (Join-Path $nd 'marca.json') -Raw -Encoding UTF8 | ConvertFrom-Json
$cont = Get-Content (Join-Path $out 'contenido.json') -Raw -Encoding UTF8 | ConvertFrom-Json
# páginas reales: portada, interiores y tarjeta ya capturadas del HTML de pantalla
$portada = Get-Item (Join-Path $eb 'portadas\portada-producto.png') -ErrorAction SilentlyContinue
if (-not $portada) { $portada = Get-ChildItem $eb -Filter '*pantalla-portada.png' | Select-Object -First 1 }
if (-not $portada) { throw "Falta *pantalla-portada.png en $eb" }
$int = @(Get-ChildItem $eb -Filter '*interior*.png' | Where-Object { $_.Name -notmatch 'tarjeta' } | Sort-Object Name)
$tarj = Get-ChildItem $eb -Filter '*tarjeta*.png' | Select-Object -First 1
$html = Get-ChildItem $eb -Filter '*pantalla.html' | Select-Object -First 1
$n = 0
# si faltan interiores, se capturan del HTML con anclas (contenido.json -> anclas)
while ($int.Count -lt 3 -and $html -and $cont.anclas -and $n -lt $cont.anclas.Count) {
  $f = Join-Path $out ("_interior-auto-$n.png")
  $w = Join-Path $out '_wrap.html'
  $src = (Uri $html.FullName) + '#' + $cont.anclas[$n]
  [IO.File]::WriteAllText($w, "<html><body style='margin:0;background:#fff;padding:30px 32px'><iframe src='$src' style='border:0;width:495px;height:734px'></iframe></body></html>", $utf8)
  Edge (Uri $w) 559 794 $f
  Remove-Item $w -Force
  $int += Get-Item $f; $n++
}
if ($int.Count -lt 3) { throw 'Hacen falta al menos 3 páginas interiores (PNG o anclas en contenido.json)' }
if (-not $tarj) { $tarj = $int[0] }
# recorta los márgenes blancos de la tarjeta (la hoja imprimible suele ser A4 con la tarjeta pequeña)
$imp = Get-ChildItem $eb -Filter '*imprimible.html' | Select-Object -First 1
$sc = 1
if ($cont.ancla_tarjeta -and $imp) {  # captura a doble resolucion desde el HTML (nitida)
  $big = Join-Path $out '_tarjeta-2x.png'
  $ud = Join-Path $env:TEMP ('edge-img-' + [guid]::NewGuid().ToString('N'))
  Start-Process $edge -ArgumentList @('--headless', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=2', '--window-size=900,1200', '--virtual-time-budget=4000', "--user-data-dir=$ud", "--screenshot=$big", ((Uri $imp.FullName) + '#' + $cont.ancla_tarjeta)) -Wait -WindowStyle Hidden
  $tarj = Get-Item $big; $sc = 2
}
Add-Type -AssemblyName System.Drawing
$bm = New-Object System.Drawing.Bitmap $tarj.FullName
$x0 = $bm.Width; $y0 = $bm.Height; $x1 = 0; $y1 = 0; $started = $false; $blank = 0
for ($y = 0; $y -lt $bm.Height; $y += 2) {
  $rowHit = $false
  for ($x = 0; $x -lt $bm.Width; $x += 2) { $c = $bm.GetPixel($x, $y); if ($c.R -lt 245 -or $c.G -lt 245 -or $c.B -lt 245) { $rowHit = $true; if ($x -lt $x0) { $x0 = $x }; if ($x -gt $x1) { $x1 = $x } } }
  if ($rowHit) { if (-not $started) { $started = $true; $y0 = $y }; $y1 = $y; $blank = 0 }
  elseif ($started) { $blank++; if ($blank -gt 30 * $sc) { break } }  # solo el primer bloque: ignora lo que haya debajo
}
$m = 12 * $sc; $x0 = [Math]::Max(0, $x0 - $m); $y0 = [Math]::Max(0, $y0 - $m); $x1 = [Math]::Min($bm.Width - 1, $x1 + $m); $y1 = [Math]::Min($bm.Height - 1, $y1 + $m)
$rect = New-Object System.Drawing.Rectangle $x0, $y0, ($x1 - $x0 + 1), ($y1 - $y0 + 1)
$crop = $bm.Clone($rect, $bm.PixelFormat)
$tarjFile = Join-Path $out '_tarjeta-recorte.png'
$crop.Save($tarjFile); $crop.Dispose(); $bm.Dispose()
$tarj = Get-Item $tarjFile
$d = [ordered]@{
  color_principal = $marca.color_principal; color_acento = $marca.color_acento; color_fondo_suave = $marca.color_fondo_suave
  fuente_titulos = $marca.fuente_titulos; fuente_texto = $marca.fuente_texto
  portada = @{ src = (Uri $portada.FullName); w = (Dim $portada.FullName).w; h = (Dim $portada.FullName).h }
  interiores = @($int | Select-Object -First 3 | ForEach-Object { Uri $_.FullName })
  tarjeta = @{ src = (Uri $tarj.FullName); w = (Dim $tarj.FullName).w; h = (Dim $tarj.FullName).h }
  incluye = $cont.incluye; extras = $cont.extras; textos = $cont.textos
}
$trabajo = Join-Path $out '_trabajo'
New-Item -ItemType Directory -Force $trabajo | Out-Null
Copy-Item (Join-Path $skill 'plantilla.html') $trabajo -Force
[IO.File]::WriteAllText((Join-Path $trabajo 'datos.js'), ('window.DATOS=' + ($d | ConvertTo-Json -Depth 6) + ';'), $utf8)
$base = Uri (Join-Path $trabajo 'plantilla.html')
$nombres = @{ '1' = 'portada'; '2' = 'escaparate'; '3' = 'incluye'; '4' = 'perspectivas'; '5' = 'extras' }
foreach ($t in 1..5) {
  foreach ($f in @(@('c', 1080, 1080, 'cuadrado'), @('v', 1080, 1350, 'vertical'))) {
    $png = Join-Path $out ("{0}-{1}-{2}.png" -f $t, $nombres["$t"], $f[3])
    Edge ($base + "?t=$t&f=" + $f[0]) $f[1] $f[2] $png
    Write-Host $png
  }
}
Get-ChildItem $out -Filter '_*.png' | Remove-Item -Force
Remove-Item $trabajo -Recurse -Force
# info.md (avatar y ángulo) se genera desde contenido.json
$info = "# Imágenes de producto ($Nicho, $Idioma)`n`nGenerado: $(Get-Date -Format yyyy-MM-dd)`n`n**Avatar**: $($cont.avatar)`n`n**Ángulo**: $($cont.angulo)`n`nFormatos: 1080x1080 (c) y 1080x1350 (v). Páginas reales del ebook; sin imágenes de terceros; marcos de dispositivo genéricos.`n"
[IO.File]::WriteAllText((Join-Path $out 'info.md'), $info, $utf8)
