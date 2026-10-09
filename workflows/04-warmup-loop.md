# Workflow 04 · X 主题循环

本流程保留 X 框架，但把内容方向改为 VPN 与代理工具。GUI 和完整 CLI 必须分开理解。

## GUI 行为

GUI 只执行两个动作：

1. `scroll_engage`：刷 X 首页，并按现有配置可选点赞。
2. `idle`：等待。

GUI 不新增主题搜索动作，不采集素材，不关注/取关，不发帖。新增的 `topic_keywords` 仅用于主题词配置，默认强词由代码内置；若配置尚未在实际 GUI 出现，以当前代码为准。

## 完整循环约束

完整循环若后续实现发帖，素材必须同时满足 `topic_score >= 2`、真实非空 `caption` 和来源发布授权。旧 `content_level` 字段保留兼容，但不能代替主题分数；旧数据不能自动标为 VPN。无合格素材时跳过发帖，不生成随机 caption。

主题范围为 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。caption 应注明版本、测试条件和限制，避免未经验证的匿名、速度或稳定性承诺。

## 入口与状态

- `python examples/05-full-warmup-loop.py --dry-run`：现有完整循环演练入口，先审阅代码确认无外部调用。
- `gui/app.py` / `bash scripts/launch_gui.sh`：本地面板入口。
- `deploy/scripts/run_live.py`、`deploy/x-warmup.service`：部署入口，配置和代码需先核对，文档不代替实测。

发生登录失效、challenge、限流或异常时停止相关任务并交由人工处理，不绕过平台验证。不要用聊天会话运行生产长任务，不在本轮执行 live 或真实平台操作。

## 完成标准

- [ ] GUI 仅有刷首页、可选点赞和 idle。
- [ ] dry-run 与真实平台调用边界已核实。
- [ ] 主题分数、caption 和授权门槛均已检查。
- [ ] 日志脱敏，凭据未进入仓库。
