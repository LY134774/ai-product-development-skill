# 需求覆盖与优化记录

本表保留方法与确认范围，不公开私人聊天全文、账号资料、日志或第三方截图。原讨论中的产品案例、价格、模型与供应商结论不是本 Skill 的固定配置。

本版为 v1.1.0，基于 v1.0.0 优化；沿用英文调用名 `product-development-coach`，中文名称为“AI 产品开发工作流”。下列优化属于 v1.1.0，不属于保留首发内容的 v1.0.0 标签。

## 两份原始提示词如何纳入

核对来源为用户提供的《新产品启动与 AI 辅助开发指令》和《产品上线前审计与发布检查指令》。不是将两篇原文机械拼接到入口：保留有效约束，把重复要求合并到对应指南；依赖实际产品的检查按条件执行。“条件化”不代表可以忽略适用项目；必须记录适用性、证据和未验证原因。

以下路径从 Skill 目录起算；入口和指南的可点击索引见[仓库说明](../README.md)。这是人工覆盖核对，不代表每条已通过真实宿主行为测试。

### 新产品启动指令

| 原提示词位置 | 保留的具体内容 | 处理与原因 | 对应位置 |
| --- | --- | --- | --- |
| 第一阶段：需求讨论 | 定位、用户、痛点、问题、场景与流程、类似产品及差异、风险与 TBD；分次问关键问题 | 保留；已有明确小任务不重复产品访谈。外部竞品调查按实际需要，差异优势先视作待验证假设 | references/discovery.md |
| 第二阶段：MVP | 必须/以后/暂不做、P0/P1/P2、一条核心流程、页面与数据、可执行验收 | 保留；不把所有想法塞进第一版 | references/mvp.md |
| 第二阶段：技术选型 | 框架、语言、数据、认证、AI、存储、搜索、支付、邮件、部署与必要服务；用途、理由、简单替代、付费、维护扩展 | 保留并条件化；只比较真正需要的能力，不将技术清单变成必须安装的服务 | references/architecture.md、references/payments.md |
| 技术原则与确认 | 成熟、稳定、文档完善、AI 工具支持、成本与维护、少依赖、确认后采用、不私自换架构 | 合并为通用边界和架构验收；AI 工具支持不等于保证无错误 | SKILL.md、references/architecture.md |
| 第三阶段：文档初始化 | 需求/MVP/架构确认后检查目录；保护全局规则；已有项目规则先比较；五份核心文档 | 保留并澄清：获准初始化时交付五份核心文档；用户指定更小范围或已有文件时按确认范围补充 | references/documents.md、templates/AGENTS.md、README.md、TODO.md、DECISIONS.md、HANDOFF.md |
| 项目规则内容 | 项目目标、栈、代码/数据库/API/认证、安全、支付/AI/文件、测试、资源、文档、人工确认；不编配置、不复制全局规则 | 保留并按项目适用；安全需落实到服务端和测试，不能只靠文字 | references/documents.md、templates/AGENTS.md |
| 待办与决策 | 新想法、Bug、优化和优先级；真实状态；决策编号、日期、背景、备选、确认、原因、影响；变更新增记录 | 保留；未批准提案不能冒充正式决定，旧决定不删除 | references/documents.md、templates/TODO.md、DECISIONS.md |
| README 与交接 | 实际功能、架构、目录、配置名称、启动/测试/部署；进度、问题、修改、环境、下一步 | 保留；不写秘密，模拟或未验证分别说明 | references/documents.md、templates/README.md、HANDOFF.md |
| 第四阶段：开发 | 每次一个明确任务、P0 优先、最小改动、及时测试和更新文档、新想法先记待办 | 合并到开发流程；按项目运行类型/Lint/单元/构建，失败或无法运行如实报告 | references/implementation.md、references/documents.md |
| 核心安全与测试 | 服务端密钥、权限、可信价格、核心登录/数据库/支付验证、收费服务先确认、保护生产数据 | 保留；影响支付行为的代码变更必须相关自动化回归，不把文字改动等同全支付测试 | references/security-abuse.md、references/payments.md、references/implementation.md |
| 第五阶段：上下文与迭代 | 结束前查代码并更新 TODO/决策/交接；接手读五份文档、核实运行并复述进度 | 保留；不依赖聊天记忆判断完成，文档与代码冲突要指出 | references/documents.md、templates/HANDOFF.md |

### 上线前审计指令

| 原提示词部分 | 后续优化的检查范围 | 处理与原因 | 对应位置 |
| --- | --- | --- | --- |
| 1 准备 | 项目规则、README/待办/决策/交接、适用 SEO 文档、目录、实际组件、测试/正式环境；配置只看名称/存在性/必要结构 | 保留；外部账号和云状态无证据写 TBD，不输出秘密 | SKILL.md、references/release-audit.md、references/security-abuse.md |
| 2 MVP 与功能 | 首页/核心任务、注册登录（如有）、保存刷新、手机桌面、表单/空/失败状态、404/500、无效按钮/死链接、假完成 | 保留并按产品界面适配；须实际操作或明确未验证，附复现位置 | references/implementation.md、references/release-audit.md |
| 3 部署与资源 | 平台/地区/运行时/存储位置、CPU/内存/磁盘/带宽/进程、日志增长、资源竞争、单点；任务队列/并发/超时/有限重试/去重/暂停恢复/告警 | 保留并条件化；先看瓶颈，不默认扩容、独立服务或高可用集群 | references/deployment-cache.md、references/operations-growth.md |
| 4 性能与缓存 | 公共页面/图片/静态资源缓存、更新失效、私人数据隔离；框架版本语义、页面/API 耗时、索引/连接/N+1/重复请求、图片脚本负担 | 保留；Next.js 等配置按实际框架核实。压测先定环境、并发、时间、成本、停止条件，生产单独确认 | references/deployment-cache.md |
| 5 安全与防刷 | 鉴权与对象/租户权限、输入/大小/超时/配额/并发、API Key、注入/XSS/CSRF/SSRF/上传/管理接口、脱敏日志；盗用/换 IP/成本滥用 | 保留并按入口检查；IP、前端按钮、防盗链不能替代权限；告警/限流/硬封顶分别说明，无硬封顶评估业务侧预算与暂停办法 | references/security-abuse.md |
| 6 数据与恢复 | 数据库/文件备份范围、测试恢复、持久性、连接池、慢查询/索引、迁移兼容与生产保护 | 保留；存在备份配置不等于恢复成功，生产删除/迁移/恢复不自动执行 | references/deployment-cache.md、references/release-audit.md、templates/OPERATIONS.md |
| 7 支付 | 可信价格/商品/身份、订单关联、回调验签/原始体/密钥用途、幂等/重试/乱序、退款/续费/取消/延迟付款、权益/额度；环境隔离、地区/主体/币种/税费与正式条件 | 保留并条件化；不收费标不适用。提供商字段/权限/受限密钥按当前官方资料核实，不内置固定 Stripe 参数或商家结论 | references/payments.md |
| 8 SEO/GEO | robots/Sitemap/标题描述/canonical/多语言/结构化数据/图片/链接/手机/抓取/noindex/重复；搜索与训练用途分开、内容价值、平台接入台账 | 保留并条件化；llms.txt 选做，不保证推荐/收录，不伪造平台验证或提交结果 | references/seo-geo.md、templates/SEO_GEO.md、SEO_GEO_LEDGER.md |
| 9 统计 | 脚本/上报/来源/核心事件/去重/爬虫、隐私/同意与数据区域 | 保留并条件化；事件名沿用实际业务，不强制照抄；不用分析事件替代到账记录 | references/analytics.md、templates/ANALYTICS.md |
| 10 法律与权益 | 隐私/服务条款、收集处理保留/跨境、适用同意、退款/续费/取消入口、AI/上传内容、适用地区备案/许可 | 保留并条件化；按目标地区和业务查当前权威来源，技术通过不等于法律认证 | references/release-audit.md、references/analytics.md、references/payments.md |
| 11 发布回滚 | 域名/DNS/HTTPS、环境隔离、数据库迁移兼容、静态资源/CDN、监控告警、备份、步骤与回滚 | 保留；本地/预览/正式分开，回滚代码不等于恢复数据 | references/deployment-cache.md、references/release-audit.md、templates/OPERATIONS.md |
| 12 首批用户 | Beta/Early Access/候补名单、介绍演示、开源/SDK/CLI/MCP、相关收录/社区；许可/安装/敏感文件、邮箱告知 | 条件化选少量相关渠道；不强制开源或新增 SDK/MCP，不自动收集邮箱/投递 | references/operations-growth.md、references/release-audit.md |
| 13 监控应急 | 运行与费用指标、阈值/负责人；不可访问/内存/数据库/积压/API/CDN/AI 费用/登录/回调/发布故障的发现、判断、止损、恢复、复盘 | 保留并按组件选择；计划不代表已安装告警，不授予生产处置权限 | references/operations-growth.md、templates/OPERATIONS.md |
| 14 审计报告 | 总结论、P0/P1/P2、TBD、逐项证据、影响/最小修复/工作量/发布前要求/复验；测试通过/失败/未执行；准备/当天/发布后、第一周计划 | 保留并补“暂无法判定”：关键条件缺证据不能强行选 GO；报告完成/就绪/批准/发布成功分别记录 | references/release-audit.md、templates/RELEASE_CHECKLIST.md |
| 15 执行纪律 | 首轮只查与报告；问题先建议、批准后修复并复验；不擅改业务/购买/生产配置/压测/数据库/扣款；N/A 与未知分开 | 合并进共同边界；全面审计逐项加载适用指南，普通开发不跑全套，不因清单多而强加功能 | SKILL.md、references/release-audit.md |

## 其他已确认讨论的覆盖

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

## 本次执行范围与结果

已按确认范围完成入口模式与阶段衔接、条件式专项检查、报告和交接模板、两份提示词覆盖核对。检查脚本改为显式校验，新增无依赖回归用例，验证方法与实际结果见[验证记录](VALIDATION.md)。没有修改用户全局规则、原始提示词、产品代码或外部服务配置，也没有安装依赖。本轮发布范围为原仓库的 v1.1.0 标签及 Release；v1.0.0 保留不变，实际提交和发布结果以远端为准。
