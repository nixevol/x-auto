#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
command -v docker >/dev/null || { echo 'Docker is required.' >&2; exit 1; }
touch .env
docker compose -f deploy/docker-compose.yml build gui
docker compose -f deploy/docker-compose.yml up -d gui bitbrowser-bridge adspower-bridge
printf 'Docker GUI started: http://127.0.0.1:8080\n'
