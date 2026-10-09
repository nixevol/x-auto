# Always-On：运行边界

关机或进程退出后 GUI 不会继续运行。面板适合本地 dry-run 和由用户明确控制的短时任务；不要为了“7×24”而把生产账号交给无人值守循环。

## 可用入口

```bash
bash scripts/launch_gui.sh
# 需要用户自行确认环境后才考虑保持进程
caffeinate -i -s bash scripts/launch_gui.sh
```

Linux/macOS 的 systemd、Docker 和 cron 配置入口位于 `deploy/README.md`、`deploy/x-warmup.service` 和 `deploy/docker-compose.yml`。这些服务会持续运行进程，部署前检查 `deploy/scripts/run_live.py` 的模式、数据库路径和外部连接；默认保持 dry-run，不在本文件切换 live。

## 判断标准

- 账号和 profile 属于用户本人或用户已获授权的范围。
- 日志、cookies、代理凭据和数据库权限已收紧。
- GUI 仍只刷首页、可选点赞和 idle。
- 发生 challenge、限流、异常或登录失效时停止并人工处理。
- 主题评分、caption 和授权门槛不因常驻运行而跳过。

本仓库不承诺真人行为、账号增长、匿名性或平台可用性。不要把本地面板暴露到公网，不执行真实平台操作。
