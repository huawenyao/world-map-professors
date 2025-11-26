#!/usr/bin/env python3
"""MCP Server entry point for World Professors Standard Library.

This module implements a stdio-based MCP server that can be used with
Claude Desktop and other MCP-compatible clients.

Usage:
    python -m world_professors.mcp.main [--data-dir PATH]

The server exposes the following tools:
    - wp_list_industries: List all industries
    - wp_get_industry: Get industry by ID
    - wp_list_scenarios: List scenarios
    - wp_get_scenario: Get scenario by ID
    - wp_list_workflows: List workflows
    - wp_get_workflow: Get workflow by ID
    - wp_list_agents: List agents
    - wp_get_agent: Get agent by ID
    - wp_get_agent_full_spec: Get full agent specification
    - wp_list_tools: List tools
    - wp_get_tool: Get tool by ID
    - wp_list_capabilities: List capabilities
    - wp_get_capability: Get capability by ID
    - wp_get_scenario_overview: Get scenario overview
    - wp_search: Search across entities
    - wp_get_stats: Get library statistics
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from world_professors.mcp.server import MCPServer


class StdioMCPServer:
    """Stdio-based MCP server implementation."""

    def __init__(self, data_dir: str = "data") -> None:
        """Initialize the server."""
        self.server = MCPServer(data_dir)

    def run(self) -> None:
        """Run the server, reading from stdin and writing to stdout."""
        for line in sys.stdin:
            try:
                request = json.loads(line.strip())
                response = self._handle_request(request)
                print(json.dumps(response, ensure_ascii=False))
                sys.stdout.flush()
            except json.JSONDecodeError:
                error_response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32700, "message": "Parse error"},
                    "id": None,
                }
                print(json.dumps(error_response))
                sys.stdout.flush()
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "error": {"code": -32603, "message": str(e)},
                    "id": None,
                }
                print(json.dumps(error_response))
                sys.stdout.flush()

    def _handle_request(self, request: dict[str, Any]) -> dict[str, Any]:
        """Handle a JSON-RPC request."""
        method = request.get("method", "")
        params = request.get("params", {})
        request_id = request.get("id")

        if method == "initialize":
            return self._handle_initialize(request_id)
        elif method == "tools/list":
            return self._handle_list_tools(request_id)
        elif method == "tools/call":
            return self._handle_call_tool(request_id, params)
        else:
            return {
                "jsonrpc": "2.0",
                "error": {"code": -32601, "message": f"Method not found: {method}"},
                "id": request_id,
            }

    def _handle_initialize(self, request_id: Any) -> dict[str, Any]:
        """Handle initialize request."""
        return {
            "jsonrpc": "2.0",
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {
                    "name": "world-professors",
                    "version": "0.1.0",
                },
                "capabilities": {
                    "tools": {},
                },
            },
            "id": request_id,
        }

    def _handle_list_tools(self, request_id: Any) -> dict[str, Any]:
        """Handle tools/list request."""
        return {
            "jsonrpc": "2.0",
            "result": {
                "tools": self.server.get_tools_schema(),
            },
            "id": request_id,
        }

    def _handle_call_tool(
        self, request_id: Any, params: dict[str, Any]
    ) -> dict[str, Any]:
        """Handle tools/call request."""
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        result = self.server.handle_tool_call(tool_name, arguments)

        return {
            "jsonrpc": "2.0",
            "result": {
                "content": [
                    {
                        "type": "text",
                        "text": json.dumps(result, ensure_ascii=False, indent=2),
                    }
                ],
            },
            "id": request_id,
        }


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="World Professors MCP Server - Industry Agent Standard Library"
    )
    parser.add_argument(
        "--data-dir",
        type=str,
        default="data",
        help="Path to data directory (default: data)",
    )
    parser.add_argument(
        "--export-tools",
        action="store_true",
        help="Export tools schema as JSON and exit",
    )

    args = parser.parse_args()

    server = MCPServer(args.data_dir)

    if args.export_tools:
        print(server.to_json())
        return

    # Run stdio server
    stdio_server = StdioMCPServer(args.data_dir)
    stdio_server.run()


if __name__ == "__main__":
    main()
