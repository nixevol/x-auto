"""X 运营的 VPN / 代理工具主题筛选，不需要模型或网络请求。"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Iterable


# 强主题词各计 2 分；宽泛词只作为 Clash 的上下文，不单独判定相关。
TOPIC_TERMS = {
    "vpn": r"vpn(?:s)?",
    "wireguard": r"wire[\s-]*guard",
    "openvpn": r"open[\s-]*vpn",
    "v2ray": r"v2[\s-]*ray",
    "v2rayn": r"v2rayn",
    "v2rayng": r"v2rayng",
    "clash verge": r"clash[\s-]*verge(?:[\s-]*rev)?",
    "clash meta": r"clash[\s-]*meta",
    "clash for windows": r"clash[\s-]*for[\s-]*windows",
    "clash for android": r"clash[\s-]*for[\s-]*android",
    "sing-box": r"sing[\s-]*box",
    "mihomo": r"mihomo",
    "xray-core": r"xray[\s-]*core",
    "shadowsocks": r"shadowsocks(?:r)?",
    "trojan-go": r"trojan[\s-]*go",
    "hysteria2": r"hysteria[\s-]*2",
    "tuic": r"tuic",
    "ipsec": r"ipsec",
    "tailscale": r"tailscale",
    "zerotier": r"zerotier",
    "代理客户端": r"代理客户端",
    "代理内核": r"代理内核",
    "虚拟专用网络": r"虚拟专用网络",
}
CONTEXT_TERMS = (
    "proxy", "proxies", "tun", "tunnel", "subscription", "routing", "rules", "yaml",
    "代理", "节点", "订阅", "分流", "规则", "配置", "内核", "客户端",
)
CLASH_GAMES = ("clash of clans", "clash royale", "部落冲突", "皇室战争")


@dataclass(frozen=True)
class TopicMatch:
    relevant: bool
    score: int
    matched_terms: tuple[str, ...]


def _normalize(text: str) -> str:
    return unicodedata.normalize("NFKC", text).casefold()


def _contains(text: str, pattern: str) -> bool:
    # 只约束 ASCII 字母数字边界，让“配置VPN节点”也能识别，同时不匹配 myvpnservice。
    return re.search(r"(?<![a-z0-9])(?:" + pattern + r")(?![a-z0-9])", text) is not None


def parse_keywords(value: str) -> tuple[str, ...]:
    """界面配置支持换行、英文/中文逗号分隔；空值仍使用内置规则。"""
    return tuple(dict.fromkeys(part.strip() for part in re.split(r"[,，\n\r]+", value) if part.strip()))


def match_topic(text: str, extra_keywords: Iterable[str] = ()) -> TopicMatch:
    normalized = _normalize(text)
    matches = [term for term, pattern in TOPIC_TERMS.items() if _contains(normalized, pattern)]
    if _contains(normalized, "clash") and not any(game in normalized for game in CLASH_GAMES):
        if matches or any(_contains(normalized, re.escape(term)) for term in CONTEXT_TERMS):
            matches.append("clash")
    # Xray 和 Trojan 有医学/恶意软件含义，仅在代理语境使用。
    if matches or any(_contains(normalized, re.escape(term)) for term in CONTEXT_TERMS):
        for term in ("xray", "trojan"):
            if _contains(normalized, term):
                matches.append(term)
    for keyword in extra_keywords:
        term = _normalize(keyword.strip())
        if term and _contains(normalized, re.escape(term)):
            matches.append(term)
    matches = list(dict.fromkeys(matches))
    score = len(matches) * 2
    return TopicMatch(score >= 2, score, tuple(matches))


def ensure_topic_schema(conn) -> None:
    """增量迁移：旧内容保留但默认未审核，不会自动参与关注和发帖。"""
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS creators (
            handle TEXT PRIMARY KEY, followers INTEGER, bio TEXT,
            topic_score REAL NOT NULL DEFAULT 0, follow_priority INTEGER DEFAULT 5,
            notes TEXT, discovered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS media_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT, local_path TEXT UNIQUE,
            content_level INTEGER, topic_score REAL NOT NULL DEFAULT 0,
            caption TEXT, posted_count INTEGER DEFAULT 0
        );
        CREATE TABLE IF NOT EXISTS follow_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT, account TEXT,
            target_handle TEXT, ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    for table, columns in {
        "creators": {"topic_score": "REAL NOT NULL DEFAULT 0", "notes": "TEXT"},
        "media_items": {"topic_score": "REAL NOT NULL DEFAULT 0", "caption": "TEXT"},
    }.items():
        existing = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
        for name, definition in columns.items():
            if name not in existing:
                conn.execute(f"ALTER TABLE {table} ADD COLUMN {name} {definition}")
    conn.commit()
