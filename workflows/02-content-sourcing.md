# Workflow 02 · VPN / 代理主题来源

目标是整理 VPN 与代理工具主题的文本及有授权的 X 媒体。主题包括 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。GUI 不执行主题搜索；本流程也不把外部采集能力描述成已授权。

## 来源记录

记录原始 X URL、作者、抓取时间、版本或配置上下文、caption、授权证据和文本内容。`examples/01-twscrape-search.py` 仅是现有搜索入口，运行会连接外部服务，不能在文档验证时执行。

`examples/04-gallery-dl-batch.sh` 保留但只允许下载用户有权使用的 X 媒体。下载许可、编辑许可和 X 发布许可分别核实；不要使用其他站点、私密内容或未授权转载。

## 主题候选示例

- 协议与实现：WireGuard、OpenVPN、V2Ray、sing-box、Mihomo、Xray、Shadowsocks。
- 客户端与规则：Clash、Clash Verge、路由、DNS、配置迁移。
- 教程与排错：安装、版本更新、连接失败、密钥与 peer 配置。

不要把“最快”“绝对匿名”“永久可用”等未经测试的承诺写入 caption。注明版本、测试环境和限制。

## 主题评分迁移

计划使用 `topic.py` 的 `match_topic(text, extra_keywords=()) -> TopicMatch(relevant, score, matched_terms)`。内置强词命中且 `score >= 2` 才相关，泛词不能单独放行。GUI 的 `topic_keywords` 只是补充词配置，不会触发搜索。

## 数据字段

完整循环素材表保留旧 `content_level`，新增 `topic_score`。旧记录不自动赋分；必须有真实文本重新评分。进入发布池前还必须有真实非空 `caption` 和授权证据。

## 完成标准

- [ ] 每项素材有原始 X 来源和授权记录。
- [ ] 文本、版本和测试环境可追溯。
- [ ] 主题评分完成且达到门槛。
- [ ] 不使用随机 caption 填空。

下一步进入保留历史路径的 [03-nsfw-classification.md](./03-nsfw-classification.md)。
