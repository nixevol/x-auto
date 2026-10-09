# AI Agent Playbook：X VPN / 代理工具主题

加载技能后先核实任务授权、代码状态与运行模式。帮助用户实现和验证具体需求；不能把计划中的主题迁移描述为已实现功能。

## 可执行范围

- 阅读和修改获准文件，审查 X 账号/profile 集成及数据库迁移。
- 对用户提供的文本或本地文件进行主题评分；先确认 `topic.py` 和新分类示例存在。
- 检查 dry-run 路径无真实平台调用后，执行用户授权的模拟演练。
- 分析脱敏日志、核对服务路径和持久化配置。说明未测试的部分。

本轮仅改文档，不调用 X、AdsPower、BitBrowser、下载器或 Telegram，不切换 live。安装脚本、账号导入、连接测试和媒体下载都可能联网，不属于离线检查。

## 主题约定

主题覆盖 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。

计划接口为 `match_topic(text, extra_keywords=()) -> TopicMatch(relevant, score, matched_terms)`，位于 `topic.py`。只有强词命中且 `score >= 2` 才相关；“速度”“隐私”“网络”等泛词不可单独放行。分数是关键词相关性，不是准确性、许可或安全性证明。

GUI 新增 `topic_keywords` 配置，内置默认强词；动作仍是刷首页 + 可选点赞和 idle。不新增主题搜索，不把 CLI 采集和发帖能力归给 GUI。

计划由 `examples/02-topic-classify.py` 替代旧分类器，支持文本及 `--file` 文件输入，参数以最终代码为准。新路径未落地时，只报告迁移目标，不给出可直接执行的虚假命令。

## 数据与发布

完整循环保留旧 `content_level`，新增 `topic_score`。历史数据不能自动被标为 VPN 素材；必须基于真实文本重新评分并核实授权。

发布候选必须同时满足：

1. `topic_score >= 2`。
2. 数据库中有真实、非空的 `caption` 记录。
3. 素材来源清楚，已获得所需使用和发布授权。

缺少任意条件就跳过，不随机补 caption、不从文件名推断主题、不用旧等级字段替代主题评分。下载示例 `examples/04-gallery-dl-batch.sh` 仅限授权 X 媒体，下载许可与转载许可须分别核实。

## 资源

| 文件 | 用途 |
|---|---|
| [SKILL.md](./SKILL.md) | 技能元数据及整体边界 |
| [tools-catalog.md](./tools-catalog.md) | X 框架工具与主题参考项目 |
| [01-account-setup](./workflows/01-account-setup.md) | 账号、profile 和凭据 |
| [02-content-sourcing](./workflows/02-content-sourcing.md) | 文本来源、授权 X 媒体 |
| [03-topic-classification](./workflows/03-nsfw-classification.md) | 关键词评分；历史路径保留 |
| [04-warmup-loop](./workflows/04-warmup-loop.md) | GUI / CLI 区别及发布门槛 |
| [gui/README.md](./gui/README.md) | 本地面板与配置 |
| [deploy/README.md](./deploy/README.md) | 服务入口和部署限制 |

## 验证与交付

授权真实操作前核实目标账号、环境和模式；长时任务由用户控制的服务运行。验证或限流出现时停止相关操作并交由人工处理，不绕过验证。不要承诺反检测、增长或匿名效果。

代码迁移验证应覆盖强词命中、泛词误报、补充关键词、空文本，以及历史记录缺分数/缺 caption 时不能发布。文档验证检查链接、入口路径、代码与计划的区分；不为了验证文档启动真实服务。

不要输出 cookies、Token、代理凭据或未脱敏数据库；不要提交这些数据。报告实际修改、实际检查和遗留问题，不把模拟日志当成平台成功记录。许可证保持 [LICENSE](./LICENSE) 原文。
