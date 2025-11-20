# Technology Stack

## Project Type

**world-professors** 是一个 **内容密集型知识平台**,结合了:
- **静态知识库**: 结构化数据存储和版本控制
- **文档生成系统**: 自动化维基页面生成
- **交互式工具集**: CLI工具和辅助脚本
- **未来Web应用**: 可扩展到Web平台(Phase 2+)

## Core Technologies

### Primary Language(s)

**Python 3.11+** (核心开发语言)
- **选择理由**:
  - 数据处理生态成熟(pandas, pydantic)
  - AI/LLM集成便利(langchain, openai)
  - 图数据处理强大(networkx)
  - 快速原型开发(CLI工具、脚本)

**Markdown** (内容展示格式)
- 人类可读、易于版本控制
- 生态丰富(MkDocs, VuePress等)

**YAML/JSON** (数据存储格式)
- YAML: 人类友好的编辑格式
- JSON: 机器处理和验证格式
- 可互相转换

### Key Dependencies/Libraries

**数据验证与模式**:
- **Pydantic v2**: Python数据验证和设置管理
- **jsonschema**: JSON Schema验证
- **pyyaml**: YAML解析和生成

**数据处理**:
- **pandas**: 数据分析和处理
- **networkx**: 图数据结构(能力关系网络)

**CLI开发**:
- **typer**: 现代化CLI框架(基于type hints)
- **rich**: 终端美化输出(表格、进度条、语法高亮)

**模板引擎**:
- **jinja2**: 维基页面生成模板

**AI/LLM集成**:
- **openai / anthropic**: LLM API客户端
- **langchain**: AI应用开发框架(可选,按需引入)

**开发工具**:
- **ruff**: 快速Python linter
- **black**: 代码格式化
- **mypy**: 静态类型检查
- **pytest**: 测试框架

### Application Architecture

**分层架构**:

```
┌─────────────────────────────────────┐
│  Presentation Layer (展示层)         │
│  - Wiki Pages (Markdown)            │
│  - CLI Tools (Typer)                │
│  - [Future] Web UI                  │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Application Layer (应用层)          │
│  - Content Generators                │
│  - Data Validators                   │
│  - Graph Builders                    │
│  - Learning Path Planners            │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Domain Layer (领域层)                │
│  - Data Models (Pydantic)            │
│  - Business Logic                    │
│  - Schemas & Ontologies              │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│  Data Layer (数据层)                  │
│  - YAML Files (Source of Truth)     │
│  - Git (Version Control)             │
│  - [Optional] SQLite (Query Cache)  │
└─────────────────────────────────────┘
```

**设计模式**:
- **Repository Pattern**: 数据访问抽象层
- **Builder Pattern**: 复杂对象构建(如学习路径)
- **Strategy Pattern**: 不同生成策略(Wiki页面、报告等)
- **Plugin Architecture**: 可扩展的内容生成器

### Data Storage

**Primary Storage: Git仓库 + YAML文件**
- **优势**:
  - 版本控制天然支持
  - 人类可读可编辑
  - 分布式协作友好
  - 无需额外数据库服务

**Data Organization**:
```
data/
├── taxonomy/
│   ├── industries.yaml           # 行业分类主索引
│   └── scenarios/
│       └── {industry}/
│           └── {scenario-id}.yaml
├── roles/
│   └── {industry}/
│       └── {scenario}/
│           └── {role-type}/
│               └── {role-id}.yaml
└── capabilities/
    ├── capability-catalog.yaml   # 能力总目录
    └── skills/
        └── {category}/
            └── {skill-id}.yaml
```

**Optional: SQLite (查询优化)**
- **使用场景**: 当数据规模增长后需要复杂查询
- **更新策略**: 从YAML文件定期rebuild
- **用途**:
  - 全文搜索
  - 复杂关联查询
  - 统计分析

**Optional: Graph Database (Neo4j)**
- **使用场景**: 复杂能力关系网络查询
- **当前阶段**: 暂不引入,NetworkX足够
- **未来考虑**: 能力图谱达到1000+节点时

### External Integrations

**LLM API** (AI辅助内容生成):
- **Primary**: Anthropic Claude API
- **Fallback**: OpenAI GPT-4
- **用途**:
  - 辅助生成初版场景/角色定义
  - 从长文本提取结构化数据
  - 内容质量检查和改进建议

**未来集成** (Phase 2+):
- **GitHub API**: 展示开源项目技术栈
- **LinkedIn API**: 职位描述抓取(需授权)
- **行业报告**: 爬取公开行业研究数据

### Monitoring & Dashboard Technologies

**当前阶段**: CLI工具为主
- **typer + rich**: 交互式命令行
- **进度追踪**: rich.progress
- **数据展示**: rich.table

**未来Web Dashboard** (Phase 2):
- **前端框架**: Vue 3 / React (待定)
- **静态站点生成**: VuePress / Docusaurus
- **搜索**: Algolia DocSearch / MeiliSearch
- **可视化**: D3.js / Cytoscape.js (网络图)

## Development Environment

### Build & Development Tools

**包管理**:
- **Poetry**: Python依赖管理和打包
  - 锁定依赖版本
  - 虚拟环境管理
  - 简化发布流程

**项目结构**:
```
world-professors/
├── pyproject.toml          # Poetry配置
├── poetry.lock             # 依赖锁定
├── src/
│   └── world_professors/   # 主包
│       ├── models/         # Pydantic数据模型
│       ├── repositories/   # 数据访问层
│       ├── services/       # 业务逻辑
│       ├── generators/     # 内容生成器
│       └── cli/            # CLI命令
├── tests/                  # 测试
├── scripts/                # 辅助脚本
└── docs/                   # 开发文档
```

**开发命令**:
```bash
# 环境初始化
poetry install

# 运行CLI工具
poetry run wp --help

# 运行测试
poetry run pytest

# 代码质量检查
poetry run ruff check .
poetry run mypy src/

# 格式化代码
poetry run black src/ tests/
```

### Code Quality Tools

**Linting**:
- **ruff**: 极速Python linter(替代flake8, pylint)
- 配置: `pyproject.toml`
- Pre-commit hook自动检查

**Formatting**:
- **black**: 无配置的代码格式化
- 行长度: 100字符
- 强制团队代码风格一致

**Type Checking**:
- **mypy**: 静态类型检查
- 严格模式: 要求所有函数有类型注解
- 配置: `pyproject.toml`

**Testing**:
- **pytest**: 单元测试和集成测试
- **pytest-cov**: 代码覆盖率报告
- 目标覆盖率: > 80%

**Documentation**:
- **Docstring**: Google Style
- **MkDocs**: 项目文档站点(使用material主题)
- **API文档**: 自动从docstring生成

### Version Control & Collaboration

**VCS**: Git + GitHub

**分支策略**: GitHub Flow (简化版)
- `main`: 稳定主分支
- `feature/*`: 功能开发分支
- `fix/*`: Bug修复分支

**Commit规范**: Conventional Commits
```
<type>(<scope>): <subject>

type: feat, fix, docs, style, refactor, test, chore
scope: models, cli, generators, data等
```

**Code Review**:
- 所有代码变更通过Pull Request
- 至少1人review后合并
- CI检查通过(linting, tests)

**CI/CD**: GitHub Actions
- 自动运行tests和linting
- 自动构建文档
- [未来] 自动发布到PyPI

## Technical Requirements & Constraints

### Performance Requirements

**数据加载**:
- 单个场景数据加载: < 100ms
- 全量数据索引构建: < 5s (1000个场景)
- 能力图谱构建: < 2s (500个能力节点)

**内容生成**:
- 单个维基页面生成: < 200ms
- 批量生成100个页面: < 30s
- 学习路径规划: < 1s

**查询性能**:
- 全文搜索响应: < 500ms
- 图谱路径查询: < 1s

### Compatibility Requirements

**平台支持**:
- macOS 12+ (开发主力)
- Linux (Ubuntu 20.04+)
- Windows 10+ (WSL2推荐)

**Python版本**:
- 最低: Python 3.11
- 推荐: Python 3.12
- 使用新特性: Type hints, Pattern matching

**依赖版本策略**:
- 锁定主版本,允许次版本更新
- 定期(季度)依赖安全更新
- 避免使用实验性包

### Security & Compliance

**数据安全**:
- 所有数据开源公开(无敏感信息)
- 用户贡献内容需审核
- API密钥使用环境变量,不入库

**内容合规**:
- 引用来源需标注
- 避免版权问题(优先使用开放许可内容)
- 用户生成内容(UGC)审核机制

**隐私保护** (未来Web应用):
- 用户数据最小化收集
- 匿名化使用统计
- 符合GDPR基本要求

### Scalability & Reliability

**当前阶段(静态内容)**:
- 水平扩展: 通过CDN分发静态页面
- 数据规模: 支持10,000+角色条目
- 可靠性: Git提供天然备份和恢复

**未来考虑(Web服务)**:
- 数据库读写分离
- 静态内容CDN加速
- API限流和缓存
- 服务监控(Sentry, DataDog等)

## Technical Decisions & Rationale

### Decision Log

#### 1. 为何选择YAML而非JSON作为主数据格式?

**决策**: 使用YAML作为人类编辑格式,JSON作为程序处理格式

**理由**:
- ✅ YAML更易读,支持注释,适合人工编辑
- ✅ 可自动转换为JSON用于验证和处理
- ✅ Git diff更友好
- ❌ JSON缺点: 不支持注释、视觉噪音多

**权衡**: YAML解析稍慢,但数据规模小可忽略

#### 2. 为何选择Pydantic而非Dataclasses?

**决策**: 使用Pydantic v2作为数据模型基础

**理由**:
- ✅ 内置强大的数据验证
- ✅ JSON Schema生成和验证
- ✅ 性能优秀(v2基于Rust)
- ✅ 与FastAPI无缝集成(未来Web服务)
- ❌ Dataclasses缺点: 需额外验证库

#### 3. 为何不使用关系数据库(PostgreSQL等)?

**决策**: 初期使用Git+YAML,按需引入SQLite

**理由**:
- ✅ 版本控制天然支持(核心需求)
- ✅ 开放协作友好(Fork + PR)
- ✅ 无部署依赖,降低复杂度
- ✅ 人类可直接编辑
- ❌ RDBMS优势(复杂查询)可通过SQLite缓存补足

**未来重新评估**: 当数据规模 > 10,000条目或查询复杂度增加

#### 4. 为何选择Typer而非Click?

**决策**: 使用Typer作为CLI框架

**理由**:
- ✅ 基于Python Type Hints,代码更简洁
- ✅ 自动生成帮助文档
- ✅ Rich集成(美观输出)
- ✅ 现代化设计理念
- ❌ Click生态更成熟,但语法繁琐

#### 5. 静态站点 vs 动态Web应用?

**决策**: Phase 1使用静态站点(MkDocs),Phase 2+评估动态应用

**理由**:
- ✅ 快速启动,专注内容
- ✅ 部署简单(GitHub Pages免费)
- ✅ 性能优秀,SEO友好
- ✅ 降低运维成本
- ❌ 动态功能受限(个性化、实时搜索)

**未来扩展**:
- 静态站点 + Serverless API(个性化功能)
- 或迁移到Nuxt/Next.js(SSG + SSR)

## Known Limitations

### 当前技术限制

1. **搜索功能**
   - 限制: 静态站点搜索功能弱(基于索引)
   - 影响: 无法实现语义搜索
   - 未来解决: 引入向量数据库(ChromaDB)或Algolia

2. **实时协作**
   - 限制: Git-based工作流不支持实时编辑
   - 影响: 多人同时编辑可能冲突
   - 未来解决: 引入CMS或协作编辑器

3. **个性化推荐**
   - 限制: 静态内容无法个性化
   - 影响: 所有用户看到相同内容
   - 未来解决: 客户端存储 + API服务

4. **性能瓶颈**
   - 限制: Python性能vs Rust/Go
   - 影响: 大规模数据处理较慢
   - 未来解决: 核心算法用Rust重写(PyO3)

### 技术债务管理

**原则**: 优先交付价值,记录技术债务,定期偿还

**债务类型**:
- **代码债**: 快速实现的临时方案
- **测试债**: 覆盖率不足的模块
- **文档债**: 缺少文档的复杂逻辑

**偿还策略**:
- 每个Sprint预留20%时间重构
- 季度技术债务回顾会议
- 关键模块优先偿还

---

## 技术选型原则

1. **简单优于复杂**: 优先选择简单方案,避免过度工程
2. **成熟优于新潮**: 优先选择生态成熟的技术
3. **开源优于闭源**: 优先开源方案,避免vendor lock-in
4. **Python优先**: 统一技术栈,降低学习成本
5. **渐进增强**: 从简单开始,按需引入复杂技术

## 下阶段技术演进

**Phase 1 (当前)**: 基础设施
- ✅ Python + YAML + Git
- ✅ CLI工具 + 静态站点

**Phase 2**: 交互增强
- 🔄 引入Web框架(Vue/React)
- 🔄 Serverless API(用户数据)
- 🔄 全文搜索(MeiliSearch)

**Phase 3**: 智能化
- 🔜 AI内容生成助手
- 🔜 向量数据库(语义搜索)
- 🔜 个性化推荐引擎

**Phase 4**: 规模化
- 🔜 微服务架构
- 🔜 实时协作系统
- 🔜 多租户SaaS平台
