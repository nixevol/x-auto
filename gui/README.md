# GUI 模式：X VPN / 代理主题

本地 NiceGUI 面板入口为 `python gui/app.py` 或 `bash scripts/launch_gui.sh`，默认地址 `http://localhost:8080`。

## 实际职责

面板管理已有 X 账号、profile、频率和 dry-run，并运行两种动作：

- `scroll_engage`：刷首页，按现有概率可选点赞；
- `idle`：等待。

GUI 不搜索主题、不采集媒体、不发帖、不关注/取关。VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks 只作为内容主题。

## 安装

```bash
bash scripts/install.sh
source .venv/bin/activate
pip install -r gui/requirements.txt
python gui/app.py
```

首次使用保持 dry-run。添加账号和 profile 可能连接本地 AdsPower API；连接测试不是离线模拟，执行前确认目标和授权。

## 设置

现有设置包括 dry-run、间隔、会话时长、点赞概率、并发数和 AdsPower API。迁移目标新增 `topic_keywords`：它只补充主题匹配词，不产生搜索动作。默认强关键词内置；主题相关需命中强词且 `score >= 2`。若当前面板没有此设置，说明代码迁移尚未完成，不能在文档中假装已可用。

## 安全边界

不要把面板暴露到公网。cookies、代理凭据和 `warmup.db` 可能明文保存。GUI dry-run 不代表真实 X 操作成功；不要从聊天会话切 live。challenge、限流和登录失效交由人工处理，不绕过验证。

## 结构

```text
gui/db.py       SQLite 账号、设置和事件
gui/adspower.py 本地浏览器 API 与 dry-run 页面
gui/engine.py   调度器及 scroll_engage / idle
gui/app.py      NiceGUI 面板
```

完整循环、素材主题评分和发布门槛见 [workflows/04-warmup-loop.md](../workflows/04-warmup-loop.md) 与 [workflows/03-nsfw-classification.md](../workflows/03-nsfw-classification.md)。
