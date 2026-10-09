# 快速开始：X VPN / 代理工具主题

目标是接入已有账号并验证模拟循环。主题迁移接口见 [README](./README.md)，本轮文档不代表代码已完成迁移；不要在核对前启用 live。

## 准备

1. 使用自己有权运营的 X 账号，在 AdsPower / BitBrowser profile 中手动完成登录和验证。
2. 开启浏览器 Local API，记录 API 地址和 profile ID；账号与 profile 对应关系不能混用。
3. 准备 Python 3.10+。Bash 脚本使用 macOS / Linux 或 Windows WSL2；WSL2 访问 Windows 浏览器 API 的地址需要单独核实，不能默认 localhost 可达。

## 安装与面板

在仓库根目录执行，先阅读 `scripts/install.sh`：

```bash
bash scripts/install.sh
source .venv/bin/activate
pip install -r gui/requirements.txt
bash scripts/launch_gui.sh
```

打开 `http://localhost:8080`。在账号页添加账号及 profile，保持设置中的 dry-run 开启，再在仪表盘启动模拟调度。浏览器连接测试和 profile 导入会访问本地 API，不应当作离线模拟操作。

GUI 仍只有刷首页、可选点赞和 idle，不提供主题搜索、发帖或关注。迁移后新增的 `topic_keywords` 用于补充主题词，默认强词内置；只有强词命中且分数至少为 2 的内容才相关。若设置项尚未出现，说明当前代码未完成这项迁移。

## 命令行替代入口

```bash
python scripts/onboard.py
python scripts/check_prereqs.py
python examples/05-full-warmup-loop.py --dry-run
```

向导用于导入 profile 并登记 handle；检查脚本可能连接本地服务，执行前阅读脚本。完整循环的 dry-run 用于演练，不能证明 live 可用。

主题分类示例计划使用 `examples/02-topic-classify.py`，支持文本及 `--file` 文件输入。先确认文件存在，再按最终实现的帮助使用；不要沿用旧图片分类流程。

## 素材与下一步

使用 VPN、WireGuard、OpenVPN、Clash Verge、sing-box 等技术文章和自己制作或获准使用的 X 媒体。`examples/04-gallery-dl-batch.sh` 仅用于授权 X 媒体，不运行其他站点采集流程。

完整循环发布前必须具备 `topic_score >= 2`、真实非空 `caption` 记录和来源发布授权。旧 `content_level` 只保留兼容，旧素材需重新核实并评分；不能自动转入新主题发布池。

详细说明：[GUI](./gui/README.md)、[来源](./workflows/02-content-sourcing.md)、[主题分类](./workflows/03-nsfw-classification.md)、[部署](./deploy/README.md)。排错时提供脱敏日志；不要删除数据库重来，也不要分享 cookies 或代理凭据。
