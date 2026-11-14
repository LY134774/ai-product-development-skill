# v1.0.0 需求覆盖表

本表保留方法与确认范围，不公开私人聊天全文、账号资料、日志或第三方截图。原讨论中的产品案例、价格、模型与供应商结论不是本 Skill 的固定配置。

| 需求 | 实现位置（相对 Skill 目录） | 使用时机 |
| --- | --- | --- |
| 新产品先讨论，不急着建文件 | references/discovery.md | 只有想法、方向不清 |
| MVP、P0/P1/P2、页面/流程/数据/验收 | references/mvp.md | 确定第一版 |
| 架构需确认，成熟简单、减少外部服务 | references/architecture.md | MVP 后选型 |
| COS/CDN 分工与计费路径 | references/architecture.md | 文件与分发决策 |
| 何时独立搜索、何时用数据库 | references/architecture.md | 搜索质量/性能有需求 |
| 本地与独立存储、持久磁盘 | references/architecture.md | 保存上传或生成文件 |
| 保留全局规则、项目/模块规则分层 | references/documents.md | 初始化或接手项目 |
| TODO、编号日期决策、交接和 README | references/documents.md、templates | 开发全过程 |
| 新想法只记待办、不打断当前任务 | references/documents.md | 中途新想法 |
| 检查代码再交接，不虚报完成 | references/documents.md | 换聊天/模型 |
| 最小改动、复现、相关测试、页面验证 | references/implementation.md | 已确认任务实现 |
| 国内/海外/混合统计、基础与行为分析 | references/analytics.md | 统计选型 |
| 多平台不直接相加、费用逐项核实 | references/analytics.md | 重复口径或成本疑问 |
| 无 Cookie/反向代理不自动免合规 | references/analytics.md | 数据采集与存储 |
| SEO/GEO、公开边界、Sitemap、多语言、结构化数据 | references/seo-geo.md | 公开搜索流量 |
| 爬虫用途、日志、收录/引用/真人分开 | references/seo-geo.md | 发现与效果核验 |
| 平台与优化台账、内容质量、自动化分阶段 | references/seo-geo.md | 搜索接入与持续优化 |
| 部署平台、长驻任务、资源限制、504 | references/deployment-cache.md | 上线或故障 |
| 缓存层级、匿名缓存、跨用户隔离 | references/deployment-cache.md | 性能或旧内容 |
| 限流、防刷、CDN 费用、告警/封顶差异 | references/security-abuse.md | 公开 API 与异常流量 |
| 服务端价格、回调签名、幂等与权益 | references/payments.md | 收费链路 |
| 额度、订阅、一次性、退款、沙盒/正式差异 | references/payments.md | 商业化和支付审计 |
| 上线先审计、修复按确认、发布授权与回滚 | references/release-audit.md | 发布前 |
| 早期验证、漏斗、监控、内容、开源、收录与增长 | references/operations-growth.md | 上线后 |
| 明确触发、不每次跑全套 | SKILL.md、references/examples.md | 每次调用 |
| 规范格式、Codex 元数据、MIT、安装说明 | SKILL.md、agents/openai.yaml、LICENSE、仓库 README | 安装与分发 |

## 内容取舍

推荐一起做：明确验证证据、记录未确认事项、每阶段有结束条件，减少上下文交接误差。

可以以后做：英文翻译、更广宿主实测、插件分发、按真实使用反馈扩充场景。当前没有擅自制作插件或接入服务。

暂不建议做：把一套技术栈写死、固化价格/模型排名、把朋友案例当所有项目规则、默认自动部署/批量发文、全局覆盖 AGENTS.md。
