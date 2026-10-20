"""Command-line interface for multi-domain-lexicon."""

from __future__ import annotations

import argparse
import json
import sys
from typing import List, Optional, Sequence

from .compiler import PromptCompiler, evaluate_token_offset
from .taxonomy import ARTCRAFT_APPS, DEFAULT_REGISTRY
from .visual_grounding import DEFAULT_VISUAL_RESOLVER


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="multi-domain-lexicon",
        description=(
            "Deterministic lexicographical taxonomy, visual reference grounding, "
            "Giant Graph token-offset calculator, and prompt compiler."
        ),
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    # 1. domains
    p_domains = subparsers.add_parser("domains", help="List all registered domains and ArtCraft applications")
    p_domains.add_argument("--category", help="Filter by domain category", default=None)
    p_domains.add_argument("--json", action="store_true", help="Output as JSON")

    # 2. lookup
    p_lookup = subparsers.add_parser("lookup", help="Lookup a domain, token code, or keyword with visual grounding")
    p_lookup.add_argument("identifier", help="Domain ID, token code, or search term")
    p_lookup.add_argument("--json", action="store_true", help="Output as JSON")

    # 3. compile
    p_compile = subparsers.add_parser("compile", help="Compile a user query with taxonomy tokens and visual grounding")
    p_compile.add_argument("query", help="User query to compile")
    p_compile.add_argument(
        "-d",
        "--domains",
        nargs="*",
        default=None,
        help="Explicit domain IDs to include",
    )
    p_compile.add_argument("--nodes", "--node-count", dest="node_count", type=int, default=25000)
    p_compile.add_argument("--recompile-tokens", dest="recompile_tokens", type=int, default=None)
    p_compile.add_argument("--query-value", dest="query_value_usd", type=float, default=25.0)
    p_compile.add_argument("--token-cost", dest="token_cost_per_1k", type=float, default=0.003)
    p_compile.add_argument("--json", action="store_true", help="Output full payload as JSON")

    # 4. token-offset
    p_offset = subparsers.add_parser(
        "token-offset",
        help="Evaluate the Giant Graph Recompilation Token-Offset Cost Equation",
    )
    p_offset.add_argument("--nodes", "--node-count", dest="node_count", type=int, default=50000)
    p_offset.add_argument("--recompile-tokens", dest="recompile_tokens", type=int, default=1500)
    p_offset.add_argument("--delta-nodes", dest="delta_nodes", type=int, default=None)
    p_offset.add_argument("--hops", dest="hops", type=int, default=2)
    p_offset.add_argument("--query-value", dest="query_value_usd", type=float, default=25.0)
    p_offset.add_argument("--token-cost", dest="token_cost_per_1k", type=float, default=0.003)
    p_offset.add_argument("--json", action="store_true", help="Output evaluation as JSON")

    # 5. sample-queries
    p_samples = subparsers.add_parser(
        "sample-queries",
        help="Generate sample multi-disciplinary queries across all domains",
    )
    p_samples.add_argument("-d", "--domain", default=None, help="Filter sample queries by domain_id")
    p_samples.add_argument("--json", action="store_true", help="Output sample queries as JSON")

    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.subcommand == "domains":
        specs = DEFAULT_REGISTRY.list_domains()
        if args.category:
            specs = [s for s in specs if s.category == args.category]
        if args.json:
            payload = {
                "total_domains": len(specs),
                "artcraft_apps": list(ARTCRAFT_APPS),
                "domains": [s.to_dict() for s in specs],
            }
            print(json.dumps(payload, indent=2))
        else:
            print(f"Registered Domains ({len(specs)}) | ArtCraft Flagship Apps ({len(ARTCRAFT_APPS)}):")
            for spec in specs:
                token_codes = ", ".join(t.code for t in spec.tokens)
                print(f"  - {spec.domain_id} [{spec.category}]: {spec.title} (Tokens: {token_codes})")
        return 0

    if args.subcommand == "lookup":
        result = DEFAULT_REGISTRY.lookup(args.identifier)
        if result is None:
            print(f"No domain or token found for '{args.identifier}'", file=sys.stderr)
            return 1
        vis = DEFAULT_VISUAL_RESOLVER.resolve(args.identifier)
        if vis is not None:
            result["visual_reference"] = vis.to_dict()
        print(json.dumps(result, indent=2))
        return 0

    if args.subcommand == "compile":
        compiler = PromptCompiler()
        payload = compiler.compile(
            query=args.query,
            domains=args.domains,
            node_count=args.node_count,
            recompile_tokens=args.recompile_tokens,
            query_value_usd=args.query_value_usd,
            token_cost_per_1k=args.token_cost_per_1k,
        )
        if args.json:
            print(json.dumps(payload.to_dict(), indent=2))
        else:
            print(payload.compiled_prompt)
        return 0

    if args.subcommand == "token-offset":
        recompile_tokens = args.recompile_tokens
        if args.delta_nodes is not None:
            recompile_tokens = (args.delta_nodes * 120) + (args.hops * 250)
        evaluation = evaluate_token_offset(
            node_count=args.node_count,
            recompile_tokens=recompile_tokens,
            query_value_usd=args.query_value_usd,
            token_cost_per_1k=args.token_cost_per_1k,
        )
        if args.json:
            print(json.dumps(evaluation.to_dict(), indent=2))
        else:
            print(evaluation.equation)
            print(json.dumps(evaluation.to_dict(), indent=2))
        return 0

    if args.subcommand == "sample-queries":
        samples: List[dict] = DEFAULT_REGISTRY.generate_sample_queries(domain_id=args.domain)
        if args.json:
            print(json.dumps({"count": len(samples), "samples": samples}, indent=2))
        else:
            for item in samples:
                print(f"[{item['domain_id']}] ({', '.join(item['tokens'])})")
                print(f"  Query: {item['query']}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
