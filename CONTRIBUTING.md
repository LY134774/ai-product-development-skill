# 参与贡献

感谢帮助改进 AI 产品开发工作流。欢迎提交真实使用案例、错误报告、文档修复和自动化测试。

## 开发步骤

1. 先阅读 [README.md](README.md)、[Skill 入口](skills/product-development-coach/SKILL.md) 及 [验证记录](docs/VALIDATION.md)。
2. 从新分支提交改动，不提交密码、API Key、实际客户数据或私人聊天内容。
3. 保持 Skill 入口精简；按阶段把细节放入 `references/`，可复用项目示例放入 `templates/`。
4. 涉及行为规则修改时，在 `evals/cases.json` 增补正向或反向场景，并说明具体观察方法。
5. 运行全部本地检查：

```bash
python -B scripts/validate.py
python -B -O scripts/validate.py
python -B scripts/test_validate.py
python -B scripts/validate_evals.py
```

6. 提交 Pull Request，解释修改动机、影响文件、验证结果和任何没能执行的真实 Codex 测试。

## 贡献原则

- 不假设所有产品都需要 SEO、支付、对象存储或自动化运营。
- 价格、平台能力、API 参数和法规须附带当前官方资料与核实日期。
- 保留“需求先确认、最小 MVP、先审计后修复、生产操作需授权”等核心边界。
- 不把静态文档审计写作线上实测；缺证据明确标记。
- 不改变既有 Skill 调用名及路径，除非是有迁移方案的重大版本升级。

提交反馈可使用 GitHub Issues 的错误报告或功能建议模板。安全漏洞请避免公开可直接利用的敏感细节，先联系仓库维护者进行私下沟通。
