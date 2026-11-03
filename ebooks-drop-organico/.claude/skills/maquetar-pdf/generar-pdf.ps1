# Convierte un HTML en PDF con Microsoft Edge (modo sin ventana). Uso:
#   powershell -File generar-pdf.ps1 -Html ruta\archivo.html -Pdf ruta\archivo.pdf
param([Parameter(Mandatory=$true)][string]$Html, [Parameter(Mandatory=$true)][string]$Pdf)

$edge = @("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
          "C:\Program Files\Microsoft\Edge\Application\msedge.exe") | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $edge) { Write-Output "ERROR: no se encuentra Microsoft Edge"; exit 1 }

$htmlFull = (Resolve-Path $Html).Path
$pdfFull = [System.IO.Path]::GetFullPath($Pdf)
if (Test-Path $pdfFull) { Remove-Item $pdfFull -Confirm:$false }

& $edge --headless --disable-gpu --no-pdf-header-footer --virtual-time-budget=8000 --print-to-pdf="$pdfFull" "file:///$($htmlFull -replace '\\','/')" 2>$null
for ($i = 0; $i -lt 20 -and -not (Test-Path $pdfFull); $i++) { Start-Sleep -Milliseconds 500 }

if (Test-Path $pdfFull) { Write-Output ("OK " + $pdfFull + " (" + (Get-Item $pdfFull).Length + " bytes)") }
else { Write-Output "ERROR: no se generó el PDF"; exit 1 }
