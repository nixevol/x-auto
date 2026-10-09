# X VPN / 代理工具运营技能包

面向 X（Twitter）上的 VPN、网络隐私和代理工具内容运营，保留账号池、指纹浏览器、内容来源和运行循环的 X 框架。主题涵盖 **VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks**，适合整理版本更新、配置教程、故障排查和工具比较。

仓库目录及 GitHub 地址保留历史名称，不代表当前内容方向。

## 入口

- [QUICKSTART.md](./QUICKSTART.md)：安装和模拟运行。
- [gui/README.md](./gui/README.md)：本地可视化面板。
- [SKILL.md](./SKILL.md)：AI 助手加载入口。
- [AI-AGENT-PLAYBOOK.md](./AI-AGENT-PLAYBOOK.md)：执行边界和验证要求。
- [tools-catalog.md](./tools-catalog.md)：X 工具与主题参考项目。
- [deploy/README.md](./deploy/README.md)：部署配置核对及已知限制。

## 快速开始

以下 Bash 命令在 macOS / Linux 或 Windows WSL2 中执行；先阅读安装脚本。

```bash
git clone https://github.com/huangji6693-max/x-nsfw-warmup-skill.git
cd x-nsfw-warmup-skill
bash scripts/install.sh
source .venv/bin/activate
pip install -r gui/requirements.txt
bash scripts/launch_gui.sh
```

面板地址为 `http://localhost:8080`。先保持 dry-run，导入自己有权运营的账号。命令行账号导入入口是 `scripts/onboard.py`，完整循环演练入口是 `python examples/05-full-warmup-loop.py --dry-run`。

## 一键搭建与运行

### Windows 本机运行（推荐配合宿主机指纹浏览器）

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup_local_windows.ps1
```

脚本会创建 `.venv`、安装依赖、安装 Chromium、编译检查，并把 GUI 注册为当前用户计划任务。面板地址为 `http://127.0.0.1:8080`。停止面板：

```powershell
Stop-ScheduledTask -TaskName "X VPN Warmup GUI"
```

### Linux / macOS 本机运行

```bash
bash scripts/setup_local.sh
bash scripts/launch_gui.sh
```

### Docker 运行

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start_docker_windows.ps1
```

或在 Linux/macOS 执行 `bash scripts/start_docker.sh`。Docker 面板仍是 `http://127.0.0.1:8080`；默认 dry-run，不会自动登录或执行真实 X 操作。

测试账号密码不写入项目。已导入凭据库的条目名为 `X测试账号-EmilyCastrsdz5` 和 `X测试账号-BrianWheelyctr`，实际使用应先在 AdsPower/BitBrowser 中手动登录并创建 profile，再在 GUI 的“指纹浏览器”页面导入 profile。

GUI 只执行 **scroll_engage（刷 X 首页 + 主题相关内容的可选点赞）和 idle**；不会新增主题搜索动作，也不负责采集、发帖、关注或取关。模拟运行并不证明真实平台操作可用。

## 主题迁移约定与实现状态

本轮文档定义以下目标；使用前应核对代码是否已完成迁移，不能把这些约定当成现有版本已经实现的能力。

- 新增 `topic.py`，接口为 `match_topic(text, extra_keywords=()) -> TopicMatch(relevant, score, matched_terms)`。
- 内置默认强关键词；只有命中强词且 `score >= 2` 才判为相关。通用词如“网络”“速度”“安全”不能单独触发相关判断。
- GUI 新增 `topic_keywords` 配置，用于补充主题词；不把关键词配置解释成搜索功能。
- 新示例 `examples/02-topic-classify.py` 替代旧分类器，面向文本及 `--file` 文件输入；具体参数以最终实现为准。
- 完整循环素材表保留旧 `content_level` 字段，新增 `topic_score`。旧数据不能自动标为 VPN 素材，也不能靠旧字段进入发布池。
- 发帖仅选择 **`topic_score >= 2`、具有真实非空 `caption` 记录、来源及发布授权已核实**的素材。没有符合条件的记录就跳过，不能用随机文案补齐。
- `examples/04-gallery-dl-batch.sh` 保留，使用范围仅为有授权的 X 媒体。

## 工作流和现有示例

| 阶段 | 文档 | 现有代码入口 |
|---|---|---|
| 账号与 profile | [01-account-setup](./workflows/01-account-setup.md) | `scripts/onboard.py`、`scripts/add_account.py` |
| 主题来源与授权 | [02-content-sourcing](./workflows/02-content-sourcing.md) | `examples/01-twscrape-search.py`、`examples/04-gallery-dl-batch.sh` |
| 文本主题评分 | [03-topic-classification](./workflows/03-nsfw-classification.md) | 迁移目标：`topic.py` 和新 02 示例 |
| 循环与发布门槛 | [04-warmup-loop](./workflows/04-warmup-loop.md) | `examples/05-full-warmup-loop.py` |

第 03 个工作流保留历史文件名以维持入口可用，正文已改为主题分类。浏览器控制示例位于 `examples/03-adspower-control.py`。

## 使用边界

仅操作自己有权管理的账号和素材，遵守 X 的自动化、内容和反垃圾规则以及当地法规。主题匹配不证明教程准确、服务安全或具备转载授权；不要发布“绝对匿名”“保证速度”等未经验证的承诺。代理软件仅作为内容主题，本仓库不安装或配置 VPN 服务。

cookies、代理凭据及数据库可能明文保存，应限制本地访问；不要提交凭据或把未鉴权面板暴露到公网。部署前备份数据库，迁移后先做本地验证。本次文档修改不执行真实平台操作。

## 许可证

以 [LICENSE](./LICENSE) 原文为准，本轮不修改许可证。
