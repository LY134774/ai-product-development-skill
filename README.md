# AI 产品开发工作流

`product-development-coach` 是面向个人开发者、小团队和编程新手的中文 Agent Skill：从一个想法开始，讨论需求、缩小 MVP、确认技术方案，再逐项开发、验证、交接、审计和运营。

它是一套工作方法和文档模板，不是可直接运行的网站，也不会替你自动购买云服务或自动上线。

本版 `v1.1.0` 包含名称调整、模式衔接、专项检查细节、模板与验证脚本的优化。英文调用名暂保留，避免改变现有安装路径；`v1.0.0` 保留首发内容，历史版本不覆盖。

## 什么时候用

| 你当前的情况 | 可以直接这样说 | 预期结果 |
| --- | --- | --- |
| 只有一个想法 | `$product-development-coach 我想做一个产品，先帮我讨论需求。` | 用户、痛点、场景、待验证假设 |
| 功能越来越多 | `帮我确定 MVP，哪些先做，哪些以后做？` | 一条可跑通的核心流程、范围和验收标准 |
| 不知道怎么选技术 | `按我的 MVP 比较技术方案和全部成本，先不要安装。` | 推荐、简单替代、成本与风险，等待确认 |
| 方案已确认 | `初始化当前项目的文档，保留已有 AGENTS.md。` | 先展示目标文件和内容，再创建获准的文档 |
| 正在开发 | `按已确认方案完成当前这一个功能。` | 最小改动、相关验证、文档状态更新 |
| 中途冒出新想法 | `只记到 TODO，不要打断当前任务。` | 记录价值和优先级，不写新功能 |
| 准备换聊天或模型 | `检查实际代码，更新交接文档。` | 可核对的已完成、未完成、命令和下一步 |
| 新聊天接手 | `先读项目文档和代码，告诉我现在做到哪里。` | 状态复述和下一项任务，不重新发明架构 |
| 需要自然流量 | `先判断是否需要 SEO/GEO，再审计公开页面。` | 证据、优先级、平台台账；不承诺排名 |
| 要接统计工具 | `比较国内、海外和混合市场的统计方案。` | 可达性、事件口径、数据区域、费用核实 |
| 页面旧内容不更新 | `先定位浏览器、CDN、服务端和数据缓存。` | 层级证据和最小修复，不盲目清空全部缓存 |
| API 被刷或账单异常 | `审计限流、额度、并发和成本控制。` | 风险路径与分级处置建议 |
| 接入收费功能 | `审计服务端定价、支付回调和会员权益。` | 订单状态、幂等、退款和测试证据 |
| 准备上线 | `先做上线审计，不要部署。` | 阻塞问题、未验证项、发布与回滚方案 |
| 已经上线 | `根据真实数据制定监控和增长计划。` | 指标定义、故障应对、一个可验证增长实验 |

不必记住模块名。说明当前阶段和目标即可，Skill 会按需选择参考文档。自动触发取决于宿主工具，显式输入 `$product-development-coach` 更明确。普通翻译、闲聊和无关小问题不需要启动整套流程。

## 安装

在支持 Skill Installer 的 Codex 聊天中发送以下指令（这是聊天指令，不是终端命令）：

```text
$skill-installer install https://github.com/LY134774/ai-product-development-skill/tree/v1.1.0/skills/product-development-coach
```

也可以请 Codex：“从上面的 GitHub 地址安装 product-development-coach”。安装前先审阅文件。无需配置第三方 API、MCP 或密钥。具体发现位置以 [OpenAI 官方说明](https://learn.chatgpt.com/docs/build-skills) 为准。

以上地址固定安装 `v1.1.0`。需要后续开发内容时可选择 `main`；主分支会继续变化。需要首发版本时使用 `v1.0.0`，该标签不包含本版优化。

已安装 Git 的用户可以在一个尚不存在的目标目录下载本版：

```bash
git clone --branch v1.1.0 --depth 1 https://github.com/LY134774/ai-product-development-skill.git
```

然后把 `skills/product-development-coach` 整个文件夹放到宿主支持的 skills 目录。例如 Codex 当前支持用户级 `~/.agents/skills/` 和项目级 `.agents/skills/`。目标同名文件夹已经存在时先比较，不能直接覆盖。此命令只下载，不自动安装。未出现时按宿主说明刷新或重启。

## 文件怎么分工

- [SKILL.md](skills/product-development-coach/SKILL.md)：使用时机、路由、共同规则。
- [references](skills/product-development-coach/references)：每个阶段的输入、步骤、产出、验收与停止条件。
- [templates](skills/product-development-coach/templates)：获准初始化项目时交付五份核心文档，已有文件按确认差异补充；SEO、统计、审计与运维模板按适用阶段选择，小修复不补整套。
- [使用示例](skills/product-development-coach/references/examples.md)：常见对话与阶段切换。
- [需求覆盖表](docs/REQUIREMENTS.md)：本版包含的需求和对应文件。
- [验证说明](docs/VALIDATION.md)：检查方法、证据范围和限制。
- [官方资料入口](skills/product-development-coach/references/sources.md)：查最新规范、接口、价格和平台政策时使用。

采用标准 `SKILL.md` 入口；`agents/openai.yaml` 是 Codex 的补充元数据。其他支持 Agent Skills 的工具可以读取通用入口，但自动调用、审批和文档规则加载方式由各宿主决定。本仓库未逐一验证所有宿主。

## 怎样检查这份 Skill

已有 Python 3.9 或更新版本时，在仓库根目录运行，无需安装依赖：

```bash
python -B scripts/validate.py
python -B -O scripts/validate.py
python -B scripts/test_validate.py
```

前两条核对文件和格式，最后一条在临时副本故意制造错误，检查验证器是否能拦住。内容覆盖及三类人工场景核对见[验证说明](docs/VALIDATION.md)；这些检查不等于安装后的自动触发或真实产品测试。

## 工作边界

先确认需求和技术方案，后开发。建议与执行分开；本地检查、预览、提交、部署、上线分别报告。全局 AGENTS.md 不修改；项目已有同名文件先读取、比较和征求确认。

支付、登录、权限、数据库、生产配置、安装依赖和新增外部服务需要明确授权。已获得的具体授权在原范围内有效，不能借此扩大操作范围。敏感信息只使用安全的配置机制，不放进聊天、仓库或日志。

不会硬编码“某供应商永远最便宜”“某产品永久免费”“免 Cookie 就免合规”等结论；使用时核对官方资料并记录日期。文档和审计不构成法律、财务或安全认证。

## 语言与许可

v1.1.0 以中文为主；英文翻译留待后续，不提供未完成的英文文件。按 [MIT](LICENSE) 许可开源；可复制的 Skill 文件夹内也包含许可证。
