# Design: Data Models Foundation

## Architecture Overview

数据模型层采用 **三层架构**:

```
┌─────────────────────────────────────────┐
│  Application Layer (应用层)              │
│  - CLI Tools                            │
│  - Generators                           │
│  - Services                             │
└─────────────────────────────────────────┘
                 ↓ 使用
┌─────────────────────────────────────────┐
│  Domain Model Layer (领域模型层)         │
│  - Pydantic Models (运行时验证)          │
│  - Business Logic Methods               │
│  - Type Hints & Validation              │
└─────────────────────────────────────────┘
                 ↓ 定义
┌─────────────────────────────────────────┐
│  Schema Layer (Schema层)                │
│  - JSON Schema (静态验证)                │
│  - YAML Templates                       │
│  - Documentation                        │
└─────────────────────────────────────────┘
                 ↓ 描述
┌─────────────────────────────────────────┐
│  Data Storage Layer (存储层)             │
│  - YAML Files (Source of Truth)        │
│  - Git Version Control                 │
└─────────────────────────────────────────┘
```

## Core Models Design

### 1. Base Model (基础模型)

所有实体继承的抽象基类:

```python
# src/world_professors/models/base.py

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class Metadata(BaseModel):
    """元数据模型"""
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    author: Optional[str] = None
    version: str = "1.0"
    schema_version: str = "1.0"  # 数据schema版本

    model_config = ConfigDict(
        extra='allow',  # 允许额外字段(扩展性)
        validate_assignment=True
    )

class BaseEntity(BaseModel):
    """所有实体的基类"""
    id: str = Field(..., pattern=r'^[a-z0-9-]+$')
    name: str = Field(..., min_length=1, max_length=200)
    description: str = Field(..., min_length=1)
    metadata: Optional[Metadata] = Field(default_factory=Metadata)

    model_config = ConfigDict(
        extra='forbid',  # 默认不允许额外字段(严格模式)
        validate_assignment=True,
        str_strip_whitespace=True
    )

    @property
    def display_name(self) -> str:
        """显示名称"""
        return self.name

    def to_yaml(self) -> str:
        """导出为YAML字符串"""
        import yaml
        return yaml.dump(
            self.model_dump(exclude_none=True, by_alias=True),
            allow_unicode=True,
            sort_keys=False
        )
```

### 2. Scenario Model (场景模型)

```python
# src/world_professors/models/taxonomy.py

from pydantic import Field, field_validator
from typing import List, Optional
from enum import Enum

class ValueFlowStage(BaseModel):
    """价值流阶段"""
    stage: str = Field(..., min_length=1)
    activities: List[str] = Field(default_factory=list)

    @field_validator('activities')
    @classmethod
    def validate_activities(cls, v):
        if not v:
            raise ValueError("activities不能为空")
        return v

class Scenario(BaseEntity):
    """业务场景模型"""
    industry: str = Field(..., description="所属行业")
    sub_industry: Optional[str] = Field(None, description="子行业")
    tags: List[str] = Field(default_factory=list)

    # 价值流
    value_flow: List[ValueFlowStage] = Field(default_factory=list)

    # 关键信息
    key_metrics: List[str] = Field(default_factory=list)
    traditional_pain_points: List[str] = Field(default_factory=list)
    ai_opportunities: List[str] = Field(default_factory=list)

    # 关联
    related_scenarios: List[str] = Field(
        default_factory=list,
        description="相关场景ID列表"
    )

    @field_validator('id')
    @classmethod
    def validate_scenario_id(cls, v):
        """验证场景ID格式: {industry}-{scenario}-{num}"""
        parts = v.split('-')
        if len(parts) < 3:
            raise ValueError(
                f"场景ID格式错误: {v}, 应为 {{industry}}-{{scenario}}-{{num}}"
            )
        return v

    @field_validator('related_scenarios')
    @classmethod
    def no_self_reference(cls, v, info):
        """禁止自引用"""
        if hasattr(info, 'data') and info.data.get('id') in v:
            raise ValueError("related_scenarios不能包含自身ID")
        return v

    @property
    def full_path(self) -> str:
        """完整路径"""
        if self.sub_industry:
            return f"{self.industry}/{self.sub_industry}/{self.id}"
        return f"{self.industry}/{self.id}"
```

### 3. Role Model (角色模型)

```python
# src/world_professors/models/role.py

from pydantic import Field, field_validator
from typing import List, Optional, Dict
from enum import Enum

class RoleType(str, Enum):
    """角色类型"""
    TRADITIONAL = "traditional"
    AI_ENHANCED = "ai-enhanced"
    EMERGING = "emerging"
    AI_AGENT = "ai-agent"

class CapabilityLevel(str, Enum):
    """能力等级"""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class Priority(str, Enum):
    """优先级"""
    MUST_HAVE = "must-have"
    SHOULD_HAVE = "should-have"
    NICE_TO_HAVE = "nice-to-have"

class RequiredCapability(BaseModel):
    """要求的能力"""
    capability_id: str = Field(..., pattern=r'^cap-[a-z]+-\d{3}$')
    level: CapabilityLevel
    priority: Priority = Priority.SHOULD_HAVE

class Responsibilities(BaseModel):
    """职责分配"""
    core: List[str] = Field(
        default_factory=list,
        description="AI不可替代的核心职责"
    )
    delegated_to_ai: List[str] = Field(
        default_factory=list,
        description="委托给AI的职责"
    )
    collaborative: List[str] = Field(
        default_factory=list,
        description="人机协作职责"
    )

class AITool(BaseModel):
    """AI工具"""
    name: str
    purpose: str
    vendor: List[str] = Field(default_factory=list)
    cost: Optional[str] = None  # free | freemium | paid

class WorkflowStep(BaseModel):
    """工作流步骤"""
    step: str
    human_time: Optional[str] = None
    ai_time: Optional[str] = None
    automation_level: Optional[str] = None  # manual | assisted | automated

class TransformationImpact(BaseModel):
    """转型影响"""
    efficiency_gain: Optional[str] = None
    quality_improvement: Optional[str] = None
    new_capabilities: List[str] = Field(default_factory=list)
    obsolete_skills: List[str] = Field(default_factory=list)

class SalaryRange(BaseModel):
    """薪资范围"""
    min: int = Field(..., gt=0)
    max: int = Field(..., gt=0)
    currency: str = Field(default="CNY")
    region: str = Field(default="China")

    @field_validator('max')
    @classmethod
    def max_greater_than_min(cls, v, info):
        if 'min' in info.data and v < info.data['min']:
            raise ValueError("max必须大于min")
        return v

class Role(BaseEntity):
    """角色模型"""
    type: RoleType
    scenario_ref: str = Field(..., description="关联场景ID")

    # AI增强角色特有
    traditional_role: Optional[str] = Field(
        None,
        description="对应的传统角色名称(ai-enhanced类型必填)"
    )

    # 职责与能力
    responsibilities: Optional[Responsibilities] = None
    required_capabilities: List[RequiredCapability] = Field(default_factory=list)

    # AI工具与工作流
    ai_tools: List[AITool] = Field(default_factory=list)
    typical_workflow: List[WorkflowStep] = Field(default_factory=list)

    # 转型影响
    transformation_impact: Optional[TransformationImpact] = None

    # 薪资信息
    salary_range: Optional[SalaryRange] = None

    @field_validator('id')
    @classmethod
    def validate_role_id(cls, v):
        """验证角色ID格式: {industry}-{scenario}-{type}-{name}"""
        parts = v.split('-')
        if len(parts) < 4:
            raise ValueError(
                f"角色ID格式错误: {v}, 应为 {{industry}}-{{scenario}}-{{type}}-{{name}}"
            )
        return v

    @field_validator('traditional_role')
    @classmethod
    def validate_traditional_role(cls, v, info):
        """ai-enhanced类型必须指定traditional_role"""
        if 'type' in info.data and info.data['type'] == RoleType.AI_ENHANCED:
            if not v:
                raise ValueError("ai-enhanced类型必须指定traditional_role")
        return v

    @property
    def capability_ids(self) -> List[str]:
        """提取所有能力ID"""
        return [cap.capability_id for cap in self.required_capabilities]
```

### 4. Capability Model (能力模型)

```python
# src/world_professors/models/capability.py

from pydantic import Field, field_validator
from typing import List, Optional, Dict
from enum import Enum

class CapabilityCategory(str, Enum):
    """能力类别"""
    COGNITIVE = "cognitive"
    TECHNICAL = "technical"
    INTERPERSONAL = "interpersonal"
    DOMAIN_SPECIFIC = "domain-specific"

class Transferability(str, Enum):
    """可迁移性"""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class AIImpact(str, Enum):
    """AI影响程度"""
    ENHANCED = "enhanced"       # 被增强
    AUGMENTED = "augmented"     # 被扩展
    AUTOMATED = "automated"     # 被自动化
    OBSOLETE = "obsolete"       # 过时

class LevelDefinition(BaseModel):
    """等级定义"""
    description: str
    skills: List[str] = Field(default_factory=list)
    tasks: List[str] = Field(default_factory=list)

class LearningResources(BaseModel):
    """学习资源"""
    courses: List[str] = Field(default_factory=list)
    books: List[str] = Field(default_factory=list)
    practice: List[str] = Field(default_factory=list)

class Milestone(BaseModel):
    """学习里程碑"""
    month: int = Field(..., ge=1, le=60)
    goal: str

class LearningPath(BaseModel):
    """学习路径"""
    prerequisites: List[str] = Field(
        default_factory=list,
        description="前置能力ID列表"
    )
    estimated_time: Optional[str] = None
    resources: Optional[LearningResources] = None
    milestones: List[Milestone] = Field(default_factory=list)

class TransferabilityProfile(BaseModel):
    """可迁移性画像"""
    across_industries: Transferability = Transferability.MEDIUM
    across_scenarios: Transferability = Transferability.MEDIUM

class Capability(BaseEntity):
    """能力模型"""
    category: CapabilityCategory
    sub_category: Optional[str] = None
    aliases: List[str] = Field(default_factory=list)

    # 等级定义
    levels: Dict[str, LevelDefinition] = Field(default_factory=dict)

    # 学习路径
    learning_path: Optional[LearningPath] = None

    # 关系
    related_capabilities: List[str] = Field(
        default_factory=list,
        description="相关能力ID列表"
    )
    applicable_roles: List[str] = Field(
        default_factory=list,
        description="适用角色(描述性)"
    )

    # 特性
    transferability: Optional[TransferabilityProfile] = None
    ai_impact: Optional[AIImpact] = None

    @field_validator('id')
    @classmethod
    def validate_capability_id(cls, v):
        """验证能力ID格式: cap-{category}-{num}"""
        import re
        if not re.match(r'^cap-[a-z]+-\d{3}$', v):
            raise ValueError(
                f"能力ID格式错误: {v}, 应为 cap-{{category}}-{{num}}"
            )
        return v

    @field_validator('levels')
    @classmethod
    def validate_levels(cls, v):
        """至少定义两个等级"""
        if len(v) < 2:
            raise ValueError("至少需要定义两个能力等级")

        valid_levels = {'beginner', 'intermediate', 'advanced', 'expert'}
        invalid = set(v.keys()) - valid_levels
        if invalid:
            raise ValueError(f"无效的等级名称: {invalid}")

        return v

    @field_validator('related_capabilities')
    @classmethod
    def no_self_reference(cls, v, info):
        """禁止自引用"""
        if hasattr(info, 'data') and info.data.get('id') in v:
            raise ValueError("related_capabilities不能包含自身ID")
        return v
```

### 5. Practice Models (实践模型)

```python
# src/world_professors/models/practice.py

from pydantic import Field
from typing import List, Optional, Dict
from enum import Enum

class AIPatternType(str, Enum):
    """AI模式类型"""
    AUTOMATION = "automation"
    AUGMENTATION = "augmentation"
    GENERATION = "generation"
    ORCHESTRATION = "orchestration"

class AIPattern(BaseEntity):
    """AI应用模式"""
    type: AIPatternType
    applicable_scenarios: List[str] = Field(
        default_factory=list,
        description="适用场景标签"
    )
    implementation_steps: List[str] = Field(default_factory=list)
    success_factors: List[str] = Field(default_factory=list)
    common_pitfalls: List[str] = Field(default_factory=list)
    examples: List[str] = Field(
        default_factory=list,
        description="案例ID引用"
    )

class ProcessState(BaseModel):
    """流程状态"""
    process: str = Field(..., description="流程描述")
    pain_points: List[str] = Field(default_factory=list)
    metrics: Dict[str, str] = Field(default_factory=dict)

class ROI(BaseModel):
    """投资回报"""
    cost: Optional[str] = None
    benefit: Optional[str] = None
    payback_period: Optional[str] = None

class TransformationCase(BaseEntity):
    """流程变革案例"""
    title: str = Field(..., min_length=1)
    industry: str
    scenario_ref: str = Field(..., description="关联场景ID")
    summary: str

    # 变革前后对比
    before: ProcessState
    after: ProcessState

    # 实施细节
    ai_tools_used: List[str] = Field(default_factory=list)
    roi: Optional[ROI] = None
    lessons_learned: List[str] = Field(default_factory=list)
```

## JSON Schema Design

为每个模型生成对应的JSON Schema,用于:
1. 编辑器自动补全(VS Code)
2. 静态验证(CI/CD)
3. 文档生成

```python
# src/world_professors/schemas/generator.py

def generate_json_schema():
    """生成JSON Schema文件"""
    from world_professors.models import Scenario, Role, Capability
    import json

    schemas = {
        'scenario': Scenario.model_json_schema(),
        'role': Role.model_json_schema(),
        'capability': Capability.model_json_schema(),
    }

    for name, schema in schemas.items():
        output_path = f"src/world_professors/schemas/{name}-schema.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(schema, f, indent=2, ensure_ascii=False)
```

## Repository Pattern (数据访问层)

```python
# src/world_professors/repositories/base.py

from pathlib import Path
from typing import Generic, TypeVar, List, Optional
from pydantic import BaseModel
import yaml

T = TypeVar('T', bound=BaseModel)

class BaseRepository(Generic[T]):
    """基础Repository"""

    def __init__(self, data_dir: Path, model_class: type[T]):
        self.data_dir = data_dir
        self.model_class = model_class
        self._cache: Dict[str, T] = {}

    def load(self, file_path: Path) -> T:
        """加载单个文件"""
        if not file_path.exists():
            raise FileNotFoundError(f"文件不存在: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        return self.model_class(**data)

    def load_all(self, pattern: str = "**/*.yaml") -> List[T]:
        """批量加载"""
        files = self.data_dir.glob(pattern)
        return [self.load(f) for f in files]

    def save(self, entity: T, file_path: Path) -> None:
        """保存"""
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(
                entity.model_dump(exclude_none=True),
                f,
                allow_unicode=True,
                sort_keys=False
            )

    def get_by_id(self, entity_id: str) -> Optional[T]:
        """根据ID查询(需子类实现索引)"""
        raise NotImplementedError
```

```python
# src/world_professors/repositories/scenario_repo.py

class ScenarioRepository(BaseRepository[Scenario]):
    """场景Repository"""

    def __init__(self, data_dir: Path):
        super().__init__(data_dir / "taxonomy/scenarios", Scenario)
        self._build_index()

    def _build_index(self):
        """构建ID索引"""
        scenarios = self.load_all()
        self._cache = {s.id: s for s in scenarios}

    def get_by_id(self, scenario_id: str) -> Optional[Scenario]:
        return self._cache.get(scenario_id)

    def get_by_industry(self, industry: str) -> List[Scenario]:
        return [
            s for s in self._cache.values()
            if s.industry == industry
        ]
```

## Validation Service (验证服务)

```python
# src/world_professors/services/validator.py

from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class ValidationResult:
    """验证结果"""
    file_path: Path
    is_valid: bool
    errors: List[str]
    warnings: List[str]

class DataValidator:
    """数据验证器"""

    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.scenario_repo = ScenarioRepository(data_dir)
        self.role_repo = RoleRepository(data_dir)
        self.capability_repo = CapabilityRepository(data_dir)

    def validate_file(self, file_path: Path) -> ValidationResult:
        """验证单个文件"""
        errors = []
        warnings = []

        try:
            # 根据路径判断类型并验证
            if 'scenarios' in str(file_path):
                entity = self.scenario_repo.load(file_path)
            elif 'roles' in str(file_path):
                entity = self.role_repo.load(file_path)
                # 额外验证引用完整性
                errors.extend(self._validate_role_references(entity))
            elif 'capabilities' in str(file_path):
                entity = self.capability_repo.load(file_path)
                # 检查循环依赖
                warnings.extend(self._check_circular_dependencies(entity))

            is_valid = len(errors) == 0

        except Exception as e:
            errors.append(str(e))
            is_valid = False

        return ValidationResult(file_path, is_valid, errors, warnings)

    def _validate_role_references(self, role: Role) -> List[str]:
        """验证角色的引用完整性"""
        errors = []

        # 检查scenario_ref是否存在
        if not self.scenario_repo.get_by_id(role.scenario_ref):
            errors.append(f"场景引用无效: {role.scenario_ref}")

        # 检查capability引用
        for cap in role.required_capabilities:
            if not self.capability_repo.get_by_id(cap.capability_id):
                errors.append(f"能力引用无效: {cap.capability_id}")

        return errors

    def _check_circular_dependencies(self, capability: Capability) -> List[str]:
        """检查能力的循环依赖"""
        warnings = []
        # TODO: 实现深度优先搜索检测环
        return warnings
```

## CLI Design (命令行接口)

```python
# src/world_professors/cli/commands/validate.py

import typer
from rich.console import Console
from rich.table import Table
from pathlib import Path

app = typer.Typer()
console = Console()

@app.command()
def file(
    file_path: Path = typer.Argument(..., help="要验证的文件路径"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="详细输出")
):
    """验证单个YAML文件"""
    from world_professors.services.validator import DataValidator
    from world_professors.config import settings

    validator = DataValidator(settings.data_dir)
    result = validator.validate_file(file_path)

    if result.is_valid:
        console.print(f"✅ [green]{file_path}[/green] 验证通过")
    else:
        console.print(f"❌ [red]{file_path}[/red] 验证失败")
        for error in result.errors:
            console.print(f"  • {error}", style="red")

    if result.warnings and verbose:
        console.print("⚠️  警告:", style="yellow")
        for warning in result.warnings:
            console.print(f"  • {warning}", style="yellow")

@app.command()
def directory(
    dir_path: Path = typer.Argument(..., help="要验证的目录"),
    pattern: str = typer.Option("**/*.yaml", help="文件匹配模式")
):
    """批量验证目录中的文件"""
    from world_professors.services.validator import DataValidator
    from world_professors.config import settings

    validator = DataValidator(settings.data_dir)
    files = list(dir_path.glob(pattern))

    results = [validator.validate_file(f) for f in files]

    # 生成报告表格
    table = Table(title="验证报告")
    table.add_column("文件", style="cyan")
    table.add_column("状态", style="magenta")
    table.add_column("错误数", justify="right")

    for result in results:
        status = "✅ 通过" if result.is_valid else "❌ 失败"
        table.add_row(
            str(result.file_path.relative_to(dir_path)),
            status,
            str(len(result.errors))
        )

    console.print(table)

    # 统计
    total = len(results)
    passed = sum(1 for r in results if r.is_valid)
    console.print(f"\n总计: {total} 个文件, {passed} 通过, {total - passed} 失败")
```

## Testing Strategy

### 单元测试

```python
# tests/unit/models/test_role.py

import pytest
from world_professors.models.role import Role, RoleType

def test_role_id_validation():
    """测试角色ID格式验证"""
    # 有效ID
    role = Role(
        id="fin-wm-ai-advisor",
        name="AI财富顾问",
        type=RoleType.AI_ENHANCED,
        scenario_ref="fin-wm-001",
        description="描述",
        traditional_role="传统财富顾问"
    )
    assert role.id == "fin-wm-ai-advisor"

    # 无效ID
    with pytest.raises(ValueError):
        Role(
            id="invalid",  # 格式错误
            name="测试",
            type=RoleType.TRADITIONAL,
            scenario_ref="fin-wm-001",
            description="描述"
        )

def test_ai_enhanced_requires_traditional_role():
    """测试AI增强型必须指定传统角色"""
    with pytest.raises(ValueError, match="必须指定traditional_role"):
        Role(
            id="fin-wm-ai-advisor",
            name="AI顾问",
            type=RoleType.AI_ENHANCED,
            scenario_ref="fin-wm-001",
            description="描述"
            # 缺少traditional_role
        )
```

### 集成测试

```python
# tests/integration/test_data_loading.py

def test_load_scenario_and_roles():
    """测试加载场景及其角色"""
    from world_professors.repositories import ScenarioRepository, RoleRepository

    scenario_repo = ScenarioRepository(DATA_DIR)
    role_repo = RoleRepository(DATA_DIR)

    # 加载场景
    scenario = scenario_repo.get_by_id("fin-wm-001")
    assert scenario is not None

    # 加载该场景下的角色
    roles = role_repo.get_by_scenario(scenario.id)
    assert len(roles) > 0

    # 验证角色引用完整性
    for role in roles:
        assert role.scenario_ref == scenario.id
```

## Performance Considerations

### 缓存策略

```python
from functools import lru_cache

class CachedRepository(BaseRepository[T]):
    @lru_cache(maxsize=1000)
    def get_by_id(self, entity_id: str) -> Optional[T]:
        """带缓存的查询"""
        return super().get_by_id(entity_id)
```

### 延迟加载

```python
class LazyScenario(Scenario):
    """延迟加载版本"""
    _roles: Optional[List[Role]] = None

    @property
    def roles(self) -> List[Role]:
        if self._roles is None:
            role_repo = RoleRepository(DATA_DIR)
            self._roles = role_repo.get_by_scenario(self.id)
        return self._roles
```

## Migration & Versioning

### Schema版本管理

```python
# src/world_professors/migrations/base.py

class Migration:
    """迁移基类"""
    from_version: str
    to_version: str

    def upgrade(self, data: dict) -> dict:
        """升级数据"""
        raise NotImplementedError

    def downgrade(self, data: dict) -> dict:
        """降级数据"""
        raise NotImplementedError

# 示例迁移
class Migration_1_0_to_1_1(Migration):
    from_version = "1.0"
    to_version = "1.1"

    def upgrade(self, data: dict) -> dict:
        # 添加新字段with默认值
        if 'metadata' not in data:
            data['metadata'] = {'schema_version': '1.1'}
        return data
```

## Documentation Generation

```python
# scripts/generate_schema_docs.py

def generate_model_docs():
    """生成模型文档"""
    from world_professors.models import Scenario, Role, Capability

    models = [Scenario, Role, Capability]

    for model in models:
        schema = model.model_json_schema()

        # 生成Markdown文档
        doc = f"# {model.__name__} Schema\n\n"
        doc += f"{model.__doc__}\n\n"
        doc += "## Fields\n\n"

        for field_name, field_info in schema['properties'].items():
            doc += f"### `{field_name}`\n"
            doc += f"- **Type**: `{field_info.get('type')}`\n"
            doc += f"- **Description**: {field_info.get('description', 'N/A')}\n"

            if 'enum' in field_info:
                doc += f"- **Allowed values**: {', '.join(field_info['enum'])}\n"

            doc += "\n"

        # 保存文档
        output_path = f"docs/schemas/{model.__name__.lower()}.md"
        Path(output_path).write_text(doc, encoding='utf-8')
```

## Summary

本设计文档定义了:
1. **三层架构**: Schema → Model → Repository
2. **5个核心模型**: Base, Scenario, Role, Capability, Practice
3. **Pydantic验证**: 类型检查、自定义验证器、引用完整性
4. **Repository模式**: 数据访问抽象和缓存
5. **CLI工具**: 验证命令和报告生成
6. **测试策略**: 单元测试和集成测试
7. **性能优化**: 缓存和延迟加载
8. **版本管理**: Schema迁移机制

下一步: 在 tasks.md 中拆解实施任务。
