# 官方资料入口与核实方法

这些是查阅入口，不是供应商推荐或价格承诺。制作时于 2026-11-14 核查了下列核心文档；后续使用仍应打开当前页面，核实版本、适用地区、账号条件和日期。未查到的说未知，不能用旧聊天回答补成确定结论。

## 格式、安装与项目指令

- [Agent Skills 格式规范](https://agentskills.io/specification)：SKILL.md 名称、描述、可选目录、渐进加载。
- [OpenAI：构建 Skills](https://learn.chatgpt.com/docs/build-skills)：当前本地发现位置、安装与 openai.yaml 元数据。Codex 扩展字段不是所有 Agent 都实现的标准。
- [OpenAI：AGENTS.md](https://developers.openai.com/codex/guides/agents-md)：使用时核对当前指令发现方式和层级，不修改用户全局规则。

## SEO/GEO

- [Google：AI 功能与网站](https://developers.google.com/search/docs/appearance/ai-features)：搜索与 AI 展示的基本原则。
- [Google：构建 Sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)：提交、范围和规范。
- [OpenAI：爬虫说明](https://developers.openai.com/api/docs/bots)：搜索、训练、用户发起访问及来源核实。
- [Bing Webmaster Tools](https://www.bing.com/webmasters/) 与 [IndexNow 文档](https://www.indexnow.org/documentation)：实际接入和通知协议需现场核实。
- [百度搜索资源平台](https://ziyuan.baidu.com/)：按账号当前权限查看支持能力，不假设全部接口开放。

## 安全、运行与支付

- [OWASP REST 安全指南](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)：认证、授权、输入、限速等参考。
- [MDN HTTP 缓存](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching)：浏览器、共享缓存、再验证与响应头语义。
- [Stripe Webhooks](https://docs.stripe.com/webhooks)：签名、重复/乱序和事件处理。支付方式、税费、账号资格、地区和价格另查当前官方规则。

以上列出后续可能使用的入口，不表示所有第三方服务已在本次接入，也不表示每个链接的全部下级文档都完成了审核。

## 每次引用要留下什么

记录“待回答的问题 → 来源标题与链接 → 核实日期 → 适用版本/地区/账号 → 支持的结论 → 未能确认的部分”。优先官方文档、当前账号可见设置和真实测试结果，资料相互矛盾时并列说明。

价格与配额要同时核对单位、免费条件、超额行为、保留期限、地区、税费和资源包覆盖范围。模型名称、SDK 参数、框架缓存行为和服务许可需查对应版本；不要固定某个模型为永久最佳选择。

法律、财务、医疗等高风险判断使用当前权威来源，具体适用性不明时建议专业确认；本 Skill 不内置可能过时的法条阈值或合规豁免结论。
