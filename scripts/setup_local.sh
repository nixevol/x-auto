#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PYTHON_BIN="${PYTHON_BIN:-python3}"
if [ ! -d .venv ]; then "$PYTHON_BIN" -m venv .venv; fi
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -r gui/requirements.txt
.venv/bin/python -m playwright install chromium
.venv/bin/python -m compileall -q topic.py gui examples scripts
printf 'Local setup complete. Start with: python scripts/launch_gui.sh\n'
