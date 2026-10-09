# Workflow 03 · VPN / 代理主题分类

文件名为历史路径 `03-nsfw-classification.md`，正文已迁移为文本主题分类，不再使用旧的图像成人分类内容。

## 目标

判断文本是否与 VPN、WireGuard、OpenVPN、Clash、Clash Verge、V2Ray、sing-box、Mihomo、Xray、Shadowsocks 主题直接相关，并保留可解释的分数和命中词。

计划接口：

```python
match_topic(text, extra_keywords=()) -> TopicMatch(
    relevant: bool,
    score: int,
    matched_terms: tuple[str, ...],
)
```

默认强关键词内置。只有命中至少一个强词且 `score >= 2` 才 `relevant=True`；“网络”“速度”“安全”“隐私”等泛词不应单独通过。`extra_keywords` 只能补充明确的主题词，不能降低门槛。

## 示例入口

计划用 `examples/02-topic-classify.py` 替代旧图片分类示例，支持直接文本及 `--file` 文件输入。最终 CLI 可能调整，先检查文件是否存在和 `--help`；旧 `examples/02-nudenet-classify.py` 不再作为主题入口。

## 素材迁移

完整循环表继续保留 `content_level` 以兼容旧 schema，并新增 `topic_score`。旧数据缺少可信主题文本时保持未审核，不自动标为 VPN。发布选择必须同时满足：

- `topic_score >= 2`；
- 数据库中存在真实非空 `caption`；
- 来源和 X 发布授权已核实。

缺少任何条件则跳过。主题分数不证明协议安全、服务质量、匿名性或授权。

## 离线验证清单

- 强词单独命中但分数不足时不相关。
- 多个强词命中达到 2 分时相关。
- 泛词、空文本和大小写变化得到预期结果。
- 补充关键词只影响允许的额外主题词。
- 旧记录无 `topic_score` 或无 caption 时不能发布。

完成后进入 [04-warmup-loop.md](./04-warmup-loop.md)。
