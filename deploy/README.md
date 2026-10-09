# 部署说明：X VPN / 代理主题

本文只说明现有部署入口和核对点。部署服务会运行 X 框架，不能把它当成 VPN 服务部署器。主题内容覆盖 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。

## 入口

- Docker：`deploy/docker-compose.yml`
- systemd：`deploy/x-warmup.service`
- runner：`deploy/scripts/run_live.py`
- 环境模板：`deploy/.env.example`
- 本地 GUI：`scripts/launch_gui.sh`

先审阅这些文件和 `.env`，确认 `WARMUP_MODE=dry-run`。本轮文档修改不启动容器、systemd、浏览器或真实平台连接。

## 凭据

`.env`、cookies、代理凭据、Telegram token 和 `warmup.db` 不得提交或贴入聊天。限制文件权限，使用运行时注入。实际部署前备份数据库，并确认挂载路径和容器用户有权限。

## Dry-run 核对

```bash
docker compose -f deploy/docker-compose.yml build
docker compose -f deploy/docker-compose.yml up -d
docker compose -f deploy/docker-compose.yml logs -f warmup
```

以上命令会联网并启动服务，不属于本轮验证。systemd 配置中的 `ExecStartPre` 和 runner 依赖当前代码，部署前检查入口是否仍存在、数据库路径是否一致。不要仅凭日志中的 `[DRY]` 宣称 X 操作成功。

## 主题数据门槛

迁移目标新增 `topic.py` 和 `examples/02-topic-classify.py`，主题分类支持文本及 `--file`；参数以最终代码为准。完整循环素材表保留 `content_level`，新增 `topic_score`。旧记录不自动标为 VPN。

只有同时满足以下条件才允许进入发布候选：

- `topic_score >= 2` 且命中强关键词；
- 有真实非空 `caption`；
- 来源和 X 发布授权已核实。

`examples/04-gallery-dl-batch.sh` 保留但仅用于授权 X 媒体。没有合格候选就跳过发帖，不随机生成 caption。GUI 仍只刷首页、可选点赞和 idle，不新增主题搜索动作。

## 运维边界

AI 可以审查配置、解释脱敏日志和帮助准备 dry-run；生产常驻进程由用户控制的主机服务运行。不要在聊天会话中切 live、登录账号、绕过 challenge 或执行真实平台操作。发生异常、限流或账号验证时停机并人工处理。

## 验收清单

- [ ] `.env` 未进入 git，权限已收紧。
- [ ] dry-run 模式和健康检查路径已审阅。
- [ ] Docker/systemd 的实际路径、挂载和数据库位置已核对。
- [ ] 主题评分、caption 和授权门槛已有测试记录。
- [ ] 备份和停止方式已验证。
