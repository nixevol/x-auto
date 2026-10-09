# Local Windows setup and start helper.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $root
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) { throw 'Python 3.10+ is required.' }
if (-not (Test-Path '.\.venv\Scripts\python.exe')) { python -m venv .venv }
$venv = (Resolve-Path '.\.venv\Scripts\python.exe').Path
& $venv -m pip install --upgrade pip
& $venv -m pip install -r requirements.txt
& $venv -m pip install -r gui\requirements.txt
& $venv -m playwright install chromium
& $venv -m compileall -q topic.py gui examples scripts
Write-Output 'Local setup complete.'
Write-Output 'Starting the GUI through the Windows scheduled-task launcher...'
& powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\launch_gui_windows.ps1
