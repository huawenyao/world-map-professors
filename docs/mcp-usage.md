# World Professors MCP 服务使用指南

## 概述

World Professors 提供 MCP (Model Context Protocol) 服务，允许 AI 助手查询行业 Agent 标准库。

## 可用工具

### 行业查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_industries` | 列出所有行业 | 无 |
| `wp_get_industry` | 获取行业详情 | `industry_id` |

### 场景查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_scenarios` | 列出场景 | `industry` (可选) |
| `wp_get_scenario` | 获取场景详情 | `scenario_id` |
| `wp_get_scenario_overview` | 获取场景完整概览 | `scenario_id` |

### 流程查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_workflows` | 列出工作流程 | `scenario_ref` (可选) |
| `wp_get_workflow` | 获取流程详情 | `workflow_id` |

### Agent 查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_agents` | 列出 Agent | `scenario_ref`, `agent_type` (可选) |
| `wp_get_agent` | 获取 Agent 详情 | `agent_id` |
| `wp_get_agent_full_spec` | 获取 Agent 完整规格 | `agent_id` |

### 工具查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_tools` | 列出工具 | `category` (可选) |
| `wp_get_tool` | 获取工具详情 | `tool_id` |

### 能力查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_list_capabilities` | 列出能力 | `category` (可选) |
| `wp_get_capability` | 获取能力详情 | `capability_id` |

### 通用查询
| 工具名称 | 描述 | 参数 |
|---------|------|------|
| `wp_search` | 搜索所有实体 | `query`, `entity_type` (可选) |
| `wp_get_stats` | 获取统计信息 | 无 |

## 配置 Claude Desktop

在 Claude Desktop 配置文件中添加：

```json
{
  "mcpServers": {
    "world-professors": {
      "command": "python",
      "args": ["-m", "world_professors.mcp.main", "--data-dir", "/path/to/data"],
      "cwd": "/path/to/world-professors",
      "env": {
        "PYTHONPATH": "src"
      }
    }
  }
}
```

## Python 直接调用

```python
from world_professors.mcp import create_server

server = create_server("data")

# 列出所有 Agent
result = server.handle_tool_call("wp_list_agents", {})
print(result)

# 获取特定 Agent 的完整规格
spec = server.handle_tool_call("wp_get_agent_full_spec", {
    "agent_id": "agt-fin-wm-advisor"
})
print(spec)

# 搜索
results = server.handle_tool_call("wp_search", {
    "query": "代码",
    "entity_type": "agent"
})
print(results)
```

## 使用示例

### 查询金融行业有哪些 Agent

```
用户: 金融行业有哪些可用的 Agent？

AI调用: wp_list_agents(scenario_ref="scn-fin-wealth-mgmt")

返回:
{
  "agents": [
    {
      "id": "agt-fin-wm-advisor",
      "name": "财富管理投顾Agent",
      "agent_type": "domain-expert"
    }
  ]
}
```

### 获取 Agent 需要的工具和能力

```
用户: 编程助手 Agent 需要什么能力和工具？

AI调用: wp_get_agent_full_spec(agent_id="agt-tech-sd-coding")

返回:
{
  "agent": {...},
  "capabilities": [
    {"id": "cap-tech-001", "name": "编程能力", "level": "expert"},
    ...
  ],
  "tools": [
    {"id": "tool-code-generator", "name": "代码生成器", "required": true},
    ...
  ]
}
```

### 搜索相关内容

```
用户: 有哪些和测试相关的内容？

AI调用: wp_search(query="测试")

返回:
{
  "results": [
    {"type": "agent", "name": "测试Agent"},
    {"type": "tool", "name": "测试用例生成器"},
    {"type": "capability", "name": "软件测试能力"},
    ...
  ]
}
```

## 数据结构

### Agent 完整规格

```json
{
  "agent": {
    "id": "agt-xxx",
    "name": "Agent名称",
    "agent_type": "domain-expert",
    "scenario_ref": "scn-xxx",
    "description": "..."
  },
  "capabilities": [
    {"id": "cap-xxx", "name": "能力名", "level": "expert"}
  ],
  "tools": [
    {"id": "tool-xxx", "name": "工具名", "required": true}
  ],
  "workflows": [
    {"id": "wf-xxx", "name": "流程名", "steps_count": 5}
  ],
  "constraints": {
    "compliance": ["规则1", "规则2"],
    "boundaries": ["边界1"],
    "escalation_rules": 3
  }
}
```

## 最佳实践

1. **先搜索再查询**: 使用 `wp_search` 找到感兴趣的实体，再用具体查询获取详情
2. **使用完整规格**: 需要 Agent 配置时，使用 `wp_get_agent_full_spec` 获取完整信息
3. **场景导向**: 通过 `wp_get_scenario_overview` 了解场景全貌
