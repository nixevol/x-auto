#!/usr/bin/env bash
# Example 04 · X authorized media batch
# Download media only from X accounts and URLs for which you have permission.

set -euo pipefail

OUT_DIR="${OUT_DIR:-./downloads}"
CONFIG_FILE="${CONFIG_FILE:-$HOME/.config/gallery-dl/config.json}"
TWITTER_USERS_FILE="${TWITTER_USERS_FILE:-twitter_users.txt}"

mkdir -p "$OUT_DIR"
if [ ! -f "$CONFIG_FILE" ]; then
  mkdir -p "$(dirname "$CONFIG_FILE")"
  cat > "$CONFIG_FILE" <<'JSON'
{
  "extractor": {
    "base-directory": "./downloads/",
    "twitter": {
      "videos": true,
      "include": "media",
      "filename": "{user[name]}_{tweet_id}_{num}.{extension}",
      "directory": ["twitter", "{user[name]}"],
      "retweets": false,
      "quoted": false,
      "replies": false,
      "cookies": null,
      "sleep-request": [2, 5]
    }
  },
  "output": {"mode": "auto", "progress": true}
}
JSON
  echo "[+] config created at $CONFIG_FILE"
fi

if [ -f "$TWITTER_USERS_FILE" ]; then
  while IFS= read -r user || [ -n "$user" ]; do
    [ -z "$user" ] && continue
    [[ "$user" =~ ^# ]] && continue
    user="${user#@}"
    echo "▶ @$user"
    gallery-dl "https://x.com/${user}/media" || true
  done < "$TWITTER_USERS_FILE"
fi

echo "[done] check $OUT_DIR; review topic relevance and permission before indexing"
