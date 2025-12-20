"""Repository for role entities."""

from pathlib import Path

from world_professors.models.role import Role, RoleType
from world_professors.repositories.base import BaseRepository


class RoleRepository(BaseRepository[Role]):
    """Repository for managing role entities.

    Provides specialized query methods for roles including
    filtering by scenario, type, industry, and capabilities.
    """

    def __init__(self, data_dir: Path) -> None:
        """Initialize role repository.

        Args:
            data_dir: Root data directory (expects roles in roles/by-industry/)
        """
        # Prefer legacy test layout: data/roles/by-industry/**.yaml
        # If absent, fall back to a simpler layout: data/roles/**.yaml
        legacy_dir = data_dir / "roles" / "by-industry"
        primary_dir = data_dir / "roles"
        roles_dir = legacy_dir if legacy_dir.exists() else primary_dir
        super().__init__(roles_dir, Role)

    def get_by_scenario(self, scenario_ref: str) -> list[Role]:
        """Get all roles for a specific scenario.

        Args:
            scenario_ref: Scenario ID

        Returns:
            List of roles linked to the scenario
        """
        return [r for r in self.load_all() if r.scenario_ref == scenario_ref]

    def get_by_type(self, role_type: RoleType) -> list[Role]:
        """Get all roles of a specific type.

        Args:
            role_type: Role type enum value

        Returns:
            List of roles of the specified type
        """
        return [r for r in self.load_all() if r.type == role_type]

    def get_by_industry(self, industry: str) -> list[Role]:
        """Get all roles in a specific industry.

        Args:
            industry: Industry name (inferred from directory structure or scenario_ref)

        Returns:
            List of roles in the industry

        Note:
            This method relies on scenario_ref format: {industry}-{scenario}-{num}
        """
        roles = []
        for role in self.load_all():
            # Extract industry from scenario_ref (e.g., "tech-saas-001" -> "tech")
            scenario_industry = role.scenario_ref.split("-")[0]
            if scenario_industry == industry.lower().replace(" ", "-"):
                roles.append(role)
        return roles

    def get_ai_enhanced_roles(self) -> list[Role]:
        """Get all AI-enhanced roles.

        Returns:
            List of roles with type=ai-enhanced
        """
        return self.get_by_type(RoleType.AI_ENHANCED)

    def get_emerging_roles(self) -> list[Role]:
        """Get all emerging roles.

        Returns:
            List of roles with type=emerging
        """
        return self.get_by_type(RoleType.EMERGING)

    def get_traditional_roles(self) -> list[Role]:
        """Get all traditional roles.

        Returns:
            List of roles with type=traditional
        """
        return self.get_by_type(RoleType.TRADITIONAL)

    def get_ai_agent_roles(self) -> list[Role]:
        """Get all AI agent roles.

        Returns:
            List of roles with type=ai-agent
        """
        return self.get_by_type(RoleType.AI_AGENT)

    def get_by_capability(self, capability_id: str) -> list[Role]:
        """Get all roles requiring a specific capability.

        Args:
            capability_id: Capability ID to search for

        Returns:
            List of roles that require this capability
        """
        roles = []
        for role in self.load_all():
            capability_ids = {rc.capability_id for rc in role.required_capabilities}
            if capability_id in capability_ids:
                roles.append(role)
        return roles

    def get_by_ai_tool(self, tool_name: str) -> list[Role]:
        """Get all roles using a specific AI tool.

        Args:
            tool_name: Name of AI tool (case-insensitive partial match)

        Returns:
            List of roles that use this tool
        """
        tool_name_lower = tool_name.lower()
        roles = []
        for role in self.load_all():
            for ai_tool in role.ai_tools:
                if tool_name_lower in ai_tool.name.lower():
                    roles.append(role)
                    break  # Don't add the same role multiple times
        return roles

    def list_scenarios(self) -> list[str]:
        """Get list of all scenario references.

        Returns:
            Sorted list of unique scenario_ref values
        """
        scenarios = {r.scenario_ref for r in self.load_all()}
        return sorted(scenarios)

    def list_traditional_roles(self) -> list[str]:
        """Get list of all traditional role names referenced.

        Returns:
            Sorted list of unique traditional role names (excluding None)
        """
        traditional = {
            r.traditional_role
            for r in self.load_all()
            if r.traditional_role is not None
        }
        return sorted(traditional)

    def search(self, query: str) -> list[Role]:
        """Search roles by name or description.

        Args:
            query: Search query (case-insensitive)

        Returns:
            List of matching roles
        """
        query_lower = query.lower()
        return [
            r
            for r in self.load_all()
            if query_lower in r.name.lower() or query_lower in r.description.lower()
        ]

    def get_role_count_by_type(self) -> dict[RoleType, int]:
        """Get count of roles by type.

        Returns:
            Dictionary mapping RoleType to count
        """
        counts: dict[RoleType, int] = {
            RoleType.TRADITIONAL: 0,
            RoleType.AI_ENHANCED: 0,
            RoleType.EMERGING: 0,
            RoleType.AI_AGENT: 0,
        }

        for role in self.load_all():
            counts[role.type] += 1

        return counts
