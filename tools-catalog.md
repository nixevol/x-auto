# 工具目录：X 框架与 VPN / 代理主题

本目录区分本仓库的 X 操作依赖与内容选题参考。外部项目未在本轮联网验证，不列实时 stars、成功率或维护保证；参考项目并不意味着本仓库集成其功能。

## X 框架

| 工具 | 用途 | 本仓库入口 |
|---|---|---|
| [AdsPower Local API](https://github.com/AdsPower/localAPI) | 启停已有浏览器 profile | `examples/03-adspower-control.py`、`gui/adspower.py` |
| BitBrowser Local API | 已有 profile 连接，按本地 API 配置核对 | `scripts/onboard.py`、`gui/adspower.py` |
| [Playwright Python](https://github.com/microsoft/playwright-python) | 浏览器控制 | GUI 和完整循环 |
| [twscrape](https://github.com/vladkens/twscrape) | X 搜索、用户时间线参考 | `examples/01-twscrape-search.py` |
| [gallery-dl](https://github.com/mikf/gallery-dl) | 授权 X 媒体下载 | `examples/04-gallery-dl-batch.sh` |
| [NiceGUI](https://github.com/zauberzeug/nicegui) | 本地可视化控制面板 | `gui/app.py` |
| SQLite | 本地账号、设置及素材记录 | `gui/db.py`、完整循环 |

上游 [Adspower-twitter-warmup](https://github.com/CryptoBusher/Adspower-twitter-warmup) 可作为编排参考，不据其经验承诺账号安全。GUI 只刷首页、可选点赞及 idle；搜索和发布属于单独审阅的 CLI 路径。

## 主题资料来源

| 主题 / 项目 | 可整理的内容 |
|---|---|
| VPN | 协议、威胁模型、隐私边界和连接排错 |
| [WireGuard](https://www.wireguard.com/) | 密钥、peer、路由与配置概念 |
| [OpenVPN](https://github.com/OpenVPN/openvpn) | 客户端/服务端配置与版本更新 |
| Clash | 规则、配置兼容性；引用时注明具体实现和版本 |
| [Clash Verge Rev](https://github.com/clash-verge-rev/clash-verge-rev) | Clash Verge 系列桌面客户端使用说明 |
| [V2Ray](https://github.com/v2fly/v2ray-core) | 配置、路由和发布说明 |
| [sing-box](https://github.com/SagerNet/sing-box) | 入站/出站、DNS 和配置版本变化 |
| [Mihomo](https://github.com/MetaCubeX/mihomo) | 规则、代理内核与配置迁移 |
| [Xray](https://github.com/XTLS/Xray-core) | 网络代理内核配置和更新 |
| [Shadowsocks](https://shadowsocks.org/) | 协议与客户端配置参考 |

以各项目官方文档和许可证为准。不要直接转载未授权图片，不分享订阅链接、密钥或用户配置中的凭据。说明测试环境和版本，避免把内容选题写成未经验证的性能或匿名承诺。

## 本地主题评分迁移

计划新增 `topic.py`，提供 `match_topic(text, extra_keywords=()) -> TopicMatch(relevant, score, matched_terms)`。默认强词内置；强词命中且 `score >= 2` 才相关，无需图片识别模型。GUI 的 `topic_keywords` 只补充关键词，不产生新搜索动作。

计划分类入口 `examples/02-topic-classify.py` 支持文本及 `--file` 文件输入，使用前检查最终实现。完整循环保留 `content_level` 并新增 `topic_score`；发布要求分数至少 2、真实 caption 和授权素材。旧记录不自动变成新主题内容。

选型建议：先用现有 profile 与 GUI dry-run 核对账号流程，再整理授权文本并验证主题评分；需要发布时另行核对完整循环及 [部署说明](./deploy/README.md)。本仓库不提供 VPN 服务安装、订阅管理、测速或网络故障自动修复。
