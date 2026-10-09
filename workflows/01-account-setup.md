# Workflow 01 · 账号与 profile

目标是登记用户有权运营的 X 账号，并把账号、浏览器 profile 与连接环境一一对应。不要购买、批量注册或共享账号；不要在文档中保存密码、cookies 或代理凭据。

## 准备

- 手动登录 X 并完成平台要求的验证。
- 开启 AdsPower / BitBrowser Local API，核对实际地址。
- 每个账号使用独立、可审计的 profile 和授权连接配置，避免串号。

## 现有入口

```bash
python scripts/onboard.py
python scripts/add_account.py --handle HANDLE --profile-id PROFILE_ID --browser adspower
python scripts/check_prereqs.py
```

这些入口可能访问本地浏览器服务；dry-run 之前先阅读脚本。`examples/03-adspower-control.py` 只用于理解或在用户明确授权后测试本地 API。

## 数据与安全

`warmup.db` 中的账号状态和 profile 关联应可追溯。cookies、代理地址和本地数据库可能明文保存，限制文件权限，禁止提交仓库或粘贴到聊天中。challenge、登录失效或账号状态异常时停止调度，交由人工处理，不绕过验证。

## 完成标准

- [ ] 账号由用户确认有权运营。
- [ ] profile 与 handle 映射已人工核对。
- [ ] Local API 地址已通过本地测试核实。
- [ ] dry-run 能运行，live 未在聊天或文档验证中启动。

完成后进入 [02-content-sourcing.md](./02-content-sourcing.md)。
