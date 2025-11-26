"""Tool model for AI tools and APIs."""

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator

from world_professors.models.base import BaseEntity


class ToolCategory(str, Enum):
    """Tool category classification."""

    DATA_RETRIEVAL = "data-retrieval"
    COMPUTATION = "computation"
    GENERATION = "generation"
    ACTION = "action"
    INTEGRATION = "integration"


class InterfaceType(str, Enum):
    """Tool interface type."""

    REST_API = "rest-api"
    GRAPHQL = "graphql"
    FUNCTION_CALL = "function-call"
    MCP_TOOL = "mcp-tool"
    SDK = "sdk"
    CLI = "cli"


class AuthenticationType(str, Enum):
    """Authentication type."""

    NONE = "none"
    API_KEY = "api-key"
    OAUTH2 = "oauth2"
    BASIC = "basic"
    BEARER = "bearer"


class PricingModel(str, Enum):
    """Pricing model."""

    FREE = "free"
    FREEMIUM = "freemium"
    SUBSCRIPTION = "subscription"
    USAGE_BASED = "usage-based"
    ENTERPRISE = "enterprise"


class Parameter(BaseModel):
    """API/Function parameter definition."""

    name: str = Field(..., min_length=1)
    location: str = Field(
        default="body",
        description="Parameter location: path, query, header, body",
    )
    type: str = Field(default="string")
    required: bool = False
    description: str | None = None
    default: Any = None
    enum: list[str] | None = None


class Endpoint(BaseModel):
    """API endpoint definition."""

    name: str = Field(..., min_length=1)
    method: str = Field(default="GET", pattern=r"^(GET|POST|PUT|DELETE|PATCH)$")
    path: str = Field(..., min_length=1)
    description: str | None = None

    # Parameters
    parameters: list[Parameter] = Field(default_factory=list)

    # Response schema
    response: dict[str, Any] = Field(
        default_factory=dict,
        description="Response JSON Schema",
    )

    # Examples
    examples: list[dict[str, Any]] = Field(default_factory=list)


class ToolInterface(BaseModel):
    """Tool interface specification."""

    type: InterfaceType = InterfaceType.REST_API

    # For REST APIs
    base_url: str | None = None
    endpoints: list[Endpoint] = Field(default_factory=list)

    # For function calls
    function_name: str | None = None
    function_schema: dict[str, Any] = Field(
        default_factory=dict,
        description="JSON Schema for function parameters",
    )


class ToolAuthentication(BaseModel):
    """Tool authentication requirements."""

    type: AuthenticationType = AuthenticationType.NONE
    header: str | None = Field(None, description="Header name for API key")
    env_var: str | None = Field(None, description="Environment variable name")


class RateLimit(BaseModel):
    """Rate limiting configuration."""

    requests_per_minute: int | None = None
    requests_per_day: int | None = None
    tokens_per_minute: int | None = None


class ToolRequirements(BaseModel):
    """Tool usage requirements."""

    authentication: ToolAuthentication | None = None
    rate_limit: RateLimit | None = None
    permissions: list[str] = Field(default_factory=list)


class ToolPricing(BaseModel):
    """Tool pricing information."""

    model: PricingModel = PricingModel.FREE
    cost_per_call: float | None = None
    currency: str = "USD"
    free_tier: int | None = Field(None, description="Free calls per month")


class Provider(BaseModel):
    """Tool provider information."""

    name: str = Field(..., min_length=1)
    tier: str | None = Field(None, description="free, standard, enterprise")
    url: str | None = None


class Tool(BaseEntity):
    """Tool definition model.

    Represents an AI tool or API with complete interface specification,
    including endpoints, authentication, pricing, and usage requirements.
    """

    # Classification
    category: ToolCategory = Field(..., description="Tool category")
    name_en: str | None = None

    # Applicability
    applicable_industries: list[str] = Field(
        default_factory=list,
        description="Industry IDs where this tool applies",
    )
    applicable_scenarios: list[str] = Field(
        default_factory=list,
        description="Scenario IDs where this tool applies",
    )

    # Interface specification
    interface: ToolInterface = Field(
        default_factory=ToolInterface,
        description="Tool interface specification",
    )

    # Requirements
    requirements: ToolRequirements | None = None

    # Pricing
    pricing: ToolPricing | None = None

    # Providers
    providers: list[Provider] = Field(default_factory=list)

    # Related capabilities
    related_capabilities: list[str] = Field(
        default_factory=list,
        description="Capability IDs that this tool supports",
    )

    @field_validator("id")
    @classmethod
    def validate_tool_id(cls, v: str) -> str:
        """Validate tool ID format: tool-{name}."""
        if not v.startswith("tool-"):
            raise ValueError(f"Tool ID must start with 'tool-': {v}")
        return v

    @property
    def is_free(self) -> bool:
        """Check if tool is free to use."""
        if self.pricing is None:
            return True
        return self.pricing.model == PricingModel.FREE

    @property
    def requires_auth(self) -> bool:
        """Check if tool requires authentication."""
        if self.requirements is None or self.requirements.authentication is None:
            return False
        return self.requirements.authentication.type != AuthenticationType.NONE

    @property
    def endpoint_names(self) -> list[str]:
        """Get all endpoint names."""
        return [ep.name for ep in self.interface.endpoints]
