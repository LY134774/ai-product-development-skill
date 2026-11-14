## v1.2.0 · 可靠性与开源协作增强

- 为 Pull Request 和 main 推送增加 GitHub Actions 自动检查。
- 新增 11 条行为契约场景，包括新产品启动、项目交接、支付安全、上线审计和不应触发 Skill 的普通问题。
- 新增无依赖的场景文件验证脚本与独立评测说明。
- 新增英文快速入门、贡献指南、更新记录和反馈模板。
- 保留原 14 份参考指南、10 份项目模板及已有安全/确认边界。

**验证范围：** 自动检查静态格式、目录链接、既有回归测试与场景契约数据；暂未在真实 Codex 新会话自动触发、真实产品或生产支付中验证，不能把静态场景通过等同于 AI 真实行为通过。

**安装：** 在支持 Skill Installer 的 Codex 对话中输入：

```text
$skill-installer install https://github.com/LY134774/ai-product-development-skill/tree/v1.2.0/skills/product-development-coach
```

更新已有安装前先比较本地修改，不直接覆盖。
