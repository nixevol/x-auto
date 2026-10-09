# Build and start the containerized GUI stack.
$ErrorActionPreference = 'Stop'
$root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
Set-Location $root
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) { throw 'Docker Desktop is required.' }
if (-not (Test-Path '.env')) { New-Item -ItemType File '.env' | Out-Null }
docker compose -f deploy/docker-compose.yml build gui
docker compose -f deploy/docker-compose.yml up -d gui bitbrowser-bridge adspower-bridge
Write-Output 'Docker GUI started: http://127.0.0.1:8080'
Write-Output 'Use docker compose -f deploy/docker-compose.yml logs -f gui for logs.'
