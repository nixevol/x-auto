"""VPN / 代理工具主题分类示例。

用法：
    python examples/02-topic-classify.py "WireGuard on Linux"
    python examples/02-topic-classify.py --file tweets.txt

只做本地文本分类，不连接 X，也不会执行账号操作。
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from topic import match_topic


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify VPN/proxy topic text")
    parser.add_argument("text", nargs="?", help="text to classify")
    parser.add_argument("--file", type=Path, help="UTF-8 text file, one item per line")
    args = parser.parse_args()
    if bool(args.text) == bool(args.file):
        parser.error("provide exactly one of TEXT or --file")
    texts = args.file.read_text(encoding="utf-8").splitlines() if args.file else [args.text]
    for text in texts:
        if not text.strip():
            continue
        result = match_topic(text)
        print(f"{'VPN_TOPIC' if result.relevant else 'OTHER'}\tscore={result.score}\tterms={','.join(result.matched_terms) or '-'}\t{text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
