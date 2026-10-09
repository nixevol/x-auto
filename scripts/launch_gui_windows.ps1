# Start the X VPN/proxy topic GUI in a detached Windows process.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$pythonw = Join-Path $root '.venv\Scripts\pythonw.exe'
if (-not (Test-Path $pythonw)) {
    throw "Virtual environment not found: $pythonw"
}
$env:PYTHONUTF8 = '1'
$env:GUI_HOST = '127.0.0.1'
$env:GUI_PORT = '8080'
$env:GUI_SHOW_BROWSER = 'false'
$p = Start-Process -FilePath $pythonw -ArgumentList '-X','utf8','gui\app.py' -WorkingDirectory $root -PassThru
Start-Sleep -Seconds 3
$listener = Get-NetTCPConnection -LocalPort 8080 -State Listen -ErrorAction SilentlyContinue
if (-not $listener) {
    Stop-Process -Id $p.Id -ErrorAction SilentlyContinue
    throw 'GUI failed to start: port 8080 is not listening.'
}
Write-Output 'GUI started: http://127.0.0.1:8080'
Write-Output "PID: $($p.Id)"
Write-Output "Stop: Stop-Process -Id $($p.Id)"
