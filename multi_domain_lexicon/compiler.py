"""Master Multi-Disciplinary Reasoning Prompt Compiler and Giant Graph Token-Offset Calculator."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, Iterator, List, Optional, Sequence

from .taxonomy import DEFAULT_REGISTRY, DomainSpec, LexiconRegistry, LexiconToken
from .visual_grounding import DEFAULT_VISUAL_RESOLVER, VisualReference, VisualReferenceResolver

MASTER_REASONING_PROMPT: str = (
    "Act as an advanced multi-disciplinary reasoning engine specializing in the convergence of "
    "creative systems, architectural design thinking, computational frameworks, and physical "
    "fabrication pipelines. Analyze the provided domain queries by utilizing the established "
    "lexicographical taxonomy, integrating visual resource references, executing incremental "
    "GraphRAG synthesis across craft app subdomains, and employing graphic engineering loops "
    "and hardware fabrication logic to ensure precise execution for automated synthesis."
)


@dataclass(frozen=True)
class TokenOffsetEvaluation:
    """Result of the Giant Graph Recompilation Token-Offset Cost Equation."""

    node_count: int
    full_graph_tokens: int
    recompile_tokens: int
    tokens_saved: int
    savings_ratio: float
    query_value_usd: float
    token_cost_per_1k: float
    full_graph_cost_usd: float
    recompile_cost_usd: float
    cost_saved_usd: float
    net_value_usd: float
    offset_cost_ratio: float
    roi_multiplier: float
    is_viable: bool
    equation: str

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)

    def __getitem__(self, key: str) -> object:
        return self.to_dict()[key]

    def get(self, key: str, default: object = None) -> object:
        return self.to_dict().get(key, default)

    def keys(self) -> Iterator[str]:
        return iter(self.to_dict().keys())


def evaluate_token_offset(
    node_count: int = 10000,
    recompile_tokens: int = 1500,
    query_value_usd: float = 25.0,
    token_cost_per_1k: float = 0.003,
    *,
    tokens_per_node: int = 120,
) -> TokenOffsetEvaluation:
    """Evaluate the Giant Graph Recompilation Token-Offset Cost Equation.

    Verifies that incremental GraphRAG subgraph compilation offsets full-graph
    token costs and keeps recompilation cost minimal relative to query value.
    """
    if node_count < 0:
        raise ValueError("node_count must be non-negative")
    if recompile_tokens < 0:
        raise ValueError("recompile_tokens must be non-negative")
    if token_cost_per_1k < 0:
        raise ValueError("token_cost_per_1k must be non-negative")

    full_graph_tokens = max(node_count * tokens_per_node, recompile_tokens)
    tokens_saved = max(0, full_graph_tokens - recompile_tokens)
    savings_ratio = (tokens_saved / full_graph_tokens) if full_graph_tokens > 0 else 0.0

    full_graph_cost_usd = round((full_graph_tokens / 1000.0) * token_cost_per_1k, 6)
    recompile_cost_usd = round((recompile_tokens / 1000.0) * token_cost_per_1k, 6)
    cost_saved_usd = round(full_graph_cost_usd - recompile_cost_usd, 6)
    net_value_usd = round(query_value_usd - recompile_cost_usd, 6)

    if query_value_usd > 0:
        offset_cost_ratio = round(recompile_cost_usd / query_value_usd, 6)
    else:
        offset_cost_ratio = float("inf") if recompile_cost_usd > 0 else 0.0

    if recompile_cost_usd > 0:
        roi_multiplier = round(query_value_usd / recompile_cost_usd, 2)
    else:
        roi_multiplier = float("inf") if query_value_usd > 0 else 0.0

    # Economically viable when incremental recompilation cost is <= 10% of query value and net value > 0
    is_viable = bool(query_value_usd > 0 and recompile_cost_usd <= (query_value_usd * 0.10) and net_value_usd > 0)

    equation = (
        f"Delta_C_offset = C_full({full_graph_tokens} tok, ${full_graph_cost_usd:.4f}) "
        f"- C_inc({recompile_tokens} tok, ${recompile_cost_usd:.4f}) "
        f"= {tokens_saved} tok saved ({savings_ratio * 100:.2f}%), "
        f"Net_Value=${net_value_usd:.4f}, Viable={is_viable}"
    )

    return TokenOffsetEvaluation(
        node_count=node_count,
        full_graph_tokens=full_graph_tokens,
        recompile_tokens=recompile_tokens,
        tokens_saved=tokens_saved,
        savings_ratio=round(savings_ratio, 6),
        query_value_usd=query_value_usd,
        token_cost_per_1k=token_cost_per_1k,
        full_graph_cost_usd=full_graph_cost_usd,
        recompile_cost_usd=recompile_cost_usd,
        cost_saved_usd=cost_saved_usd,
        net_value_usd=net_value_usd,
        offset_cost_ratio=offset_cost_ratio,
        roi_multiplier=roi_multiplier,
        is_viable=is_viable,
        equation=equation,
    )


@dataclass(frozen=True)
class CompiledPromptPayload:
    """Deterministic compiled prompt payload combining taxonomy tokens, visual grounding, and graph economics."""

    master_prompt: str
    query: str
    resolved_domains: List[str]
    lexicon_tokens: List[Dict[str, object]]
    visual_references: List[Dict[str, object]]
    token_offset: TokenOffsetEvaluation
    compiled_prompt: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "master_prompt": self.master_prompt,
            "query": self.query,
            "resolved_domains": list(self.resolved_domains),
            "lexicon_tokens": list(self.lexicon_tokens),
            "visual_references": list(self.visual_references),
            "token_offset": self.token_offset.to_dict(),
            "compiled_prompt": self.compiled_prompt,
        }

    def __getitem__(self, key: str) -> object:
        return self.to_dict()[key]

    def get(self, key: str, default: object = None) -> object:
        return self.to_dict().get(key, default)

    def keys(self) -> Iterator[str]:
        return iter(self.to_dict().keys())


class PromptCompiler:
    """Compiles multi-domain user queries into deterministic prompts grounded in visual schemas and GraphRAG economics."""

    def __init__(
        self,
        registry: Optional[LexiconRegistry] = None,
        visual_resolver: Optional[VisualReferenceResolver] = None,
    ) -> None:
        self._registry = registry or DEFAULT_REGISTRY
        self._visual_resolver = visual_resolver or DEFAULT_VISUAL_RESOLVER

    def evaluate_token_offset(
        self,
        node_count: int = 10000,
        recompile_tokens: int = 1500,
        query_value_usd: float = 25.0,
        token_cost_per_1k: float = 0.003,
        *,
        tokens_per_node: int = 120,
    ) -> TokenOffsetEvaluation:
        """Delegate to the canonical Giant Graph Token-Offset Cost Equation."""
        return evaluate_token_offset(
            node_count=node_count,
            recompile_tokens=recompile_tokens,
            query_value_usd=query_value_usd,
            token_cost_per_1k=token_cost_per_1k,
            tokens_per_node=tokens_per_node,
        )

    def compile(
        self,
        query: str,
        domains: Optional[Sequence[str]] = None,
        *,
        node_count: int = 25000,
        recompile_tokens: Optional[int] = None,
        query_value_usd: float = 25.0,
        token_cost_per_1k: float = 0.003,
    ) -> CompiledPromptPayload:
        """Compile a user query and optional domain list into a deterministic multi-disciplinary prompt."""
        matched_specs: List[DomainSpec] = self._registry.classify_query(query, explicit_domains=domains)
        resolved_domain_ids: List[str] = [spec.domain_id for spec in matched_specs]

        collected_tokens: List[LexiconToken] = []
        for spec in matched_specs:
            collected_tokens.extend(spec.tokens)

        visual_refs: List[VisualReference] = self._visual_resolver.resolve_many(resolved_domain_ids)

        effective_recompile_tokens = (
            recompile_tokens
            if recompile_tokens is not None
            else max(600, len(collected_tokens) * 280)
        )
        offset_eval = self.evaluate_token_offset(
            node_count=node_count,
            recompile_tokens=effective_recompile_tokens,
            query_value_usd=query_value_usd,
            token_cost_per_1k=token_cost_per_1k,
        )

        token_lines = [
            f"- `{t.code}` ({t.domain}): {t.name} -> Artifact `{t.output_artifact}` | Params: {', '.join(t.parameters)}"
            for t in collected_tokens
        ]
        visual_lines = [
            f"- [{v.target_id}] Style: {v.style_guide} | Diagram: `{v.diagram_type}` | "
            f"Expected Schema: {v.expected_visual_schema} | URI: `{v.sample_uri}`"
            for v in visual_refs
        ]

        compiled_sections = [
            "# MASTER MULTI-DISCIPLINARY REASONING DIRECTIVE",
            MASTER_REASONING_PROMPT,
            "",
            "## TARGET QUERY",
            query.strip(),
            "",
            f"## ACTIVE DOMAINS ({len(resolved_domain_ids)})",
            ", ".join(resolved_domain_ids),
            "",
            "## DETERMINISTIC LEXICOGRAPHICAL TOKENS",
            "\n".join(token_lines),
            "",
            "## VISUAL REFERENCE GROUNDING",
            "\n".join(visual_lines),
            "",
            "## GIANT GRAPH TOKEN-OFFSET ECONOMICS",
            offset_eval.equation,
        ]
        compiled_text = "\n".join(compiled_sections)

        return CompiledPromptPayload(
            master_prompt=MASTER_REASONING_PROMPT,
            query=query.strip(),
            resolved_domains=resolved_domain_ids,
            lexicon_tokens=[t.to_dict() for t in collected_tokens],
            visual_references=[v.to_dict() for v in visual_refs],
            token_offset=offset_eval,
            compiled_prompt=compiled_text,
        )
