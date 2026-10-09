---
name: x-vpn-warmup
version: 0.6.0
description: Use when building or debugging an X (Twitter) content workflow focused on VPN and proxy tools, including WireGuard, OpenVPN, Clash, Clash Verge, V2Ray, sing-box, Mihomo, Xray and Shadowsocks. Covers existing account/profile integration, authorized X media, text topic scoring and dry-run warmup workflows.
homepage: https://github.com/huangji6693-max/x-nsfw-warmup-skill
license: MIT
metadata:
  openclaw:
    emoji: 🦞
    category: marketing-and-sales
    tags: [twitter, x, vpn, proxy, wireguard, sing-box, account-warmup]
    requires:
      bins: [python3, pip]
    install:
      - id: pip-deps
        kind: pip
        module: -r requirements.txt
        label: Install Python dependencies
      - id: playwright-chromium
        kind: shell
        command: playwright install chromium
        label: Install Chromium for Playwright
  claude-code:
    type: knowledge-skill
    auto-load-on:
      - "VPN 主题运营"
      - "代理工具内容"
      - "X 养号"
      - "AdsPower"
      - "WireGuard"
      - "sing-box"
---

# X VPN / 代理工具主题技能

保留 X 账号池、浏览器 profile、内容来源和循环框架，内容方向改为 VPN 与代理工具。仓库地址保持历史名称；AI 客户端的加载方式取决于客户端，不保证自动注册或安装成功。

## 四层职责

| 层 | 职责 | 入口 |
|---|---|---|
| L1 账号池 | 已授权账号登记、状态和 cookies 管理 | `scripts/onboard.py`、`scripts/add_account.py` |
| L2 浏览器 | AdsPower / BitBrowser profile 与 Local API | `examples/03-adspower-control.py`、`gui/adspower.py` |
| L3 内容 | 主题文本、来源授权、关键词评分 | `examples/01-twscrape-search.py`、授权 X 媒体下载脚本 |
| L4 循环 | GUI 刷首页与 idle；CLI 完整循环另行审阅 | `gui/engine.py`、`examples/05-full-warmup-loop.py` |

VPN 工具是运营主题，与账号连接所用的代理配置不是同一件事。本仓库不提供 VPN 服务部署、订阅管理或测速能力。

## 主题迁移目标

以下为待代码落实的接口约定，执行前检查实现状态：

- `topic.py` 提供 `match_topic(text, extra_keywords=()) -> TopicMatch(relevant, score, matched_terms)`。
- 默认内置强词覆盖 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。相关判断要求强词命中且 `score >= 2`。
- GUI 新增 `topic_keywords` 补充关键词，仍只有 `scroll_engage` 和 `idle`，不新增主题搜索动作。
- `examples/02-topic-classify.py` 替代旧分类器，支持文本及 `--file` 文件输入；CLI 细节以最终代码为准。
- 素材表保留 `content_level`，新增 `topic_score`。旧记录保持未审核状态，不自动赋予新主题分数。
- 发帖只选 `topic_score >= 2`、已有真实非空 `caption`、来源及发布授权已核实的素材。无候选则跳过，不生成随机替代文案。
- `examples/04-gallery-dl-batch.sh` 仅用于授权 X 媒体。

## 工作流

1. [账号准备](./workflows/01-account-setup.md)：导入自己管理的账号和 profile。
2. [内容来源](./workflows/02-content-sourcing.md)：整理主题文本及授权证据。
3. [主题分类](./workflows/03-nsfw-classification.md)：解释分数和命中词；保留历史文件路径。
4. [循环](./workflows/04-warmup-loop.md)：区分 GUI 与完整 CLI，验证发布门槛。

安装和模拟入口见 [QUICKSTART](./QUICKSTART.md)；工具参考见 [tools-catalog](./tools-catalog.md)。不引用不存在的账号注册示例、不承诺封号率或增长效果。

## AI 助手执行边界

先读 [AI-AGENT-PLAYBOOK](./AI-AGENT-PLAYBOOK.md)。可在授权范围内修改代码、静态审查、分析脱敏日志、运行离线主题评分和已核实无平台调用的 dry-run。文档修改不授权真实平台操作。

长时循环应由用户控制的本地服务运行，不能用聊天会话充当生产进程。不得自动切 live、绕过验证、扩大下载来源或伪造验证结果。遵守 X 规则、当地法规和素材许可；许可证以 [LICENSE](./LICENSE) 原文为准。
