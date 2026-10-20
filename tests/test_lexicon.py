"""Comprehensive test suite for multi-domain-lexicon."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from multi_domain_lexicon import (
    ARTCRAFT_APPS,
    DEFAULT_REGISTRY,
    DEFAULT_VISUAL_RESOLVER,
    MASTER_REASONING_PROMPT,
    PromptCompiler,
    TAXONOMY_DOMAINS,
    VisualReferenceResolver,
    evaluate_token_offset,
)
from multi_domain_lexicon.cli import main as cli_main

EXPECTED_15_ARTCRAFT_APPS = {
    "artcraft",
    "cadcraft",
    "deckcraft",
    "designcraft",
    "effectcraft",
    "figcraft",
    "filmcraft",
    "gridcraft",
    "lightcraft",
    "pdfcraft",
    "photocraft",
    "scriptcraft",
    "soundcraft",
    "vectorcraft",
    "wordcraft",
}


def test_all_15_artcraft_flagship_apps_present() -> None:
    """Verify all 15 ArtCraft flagship applications exist in the taxonomy with tokens."""
    assert set(ARTCRAFT_APPS) == EXPECTED_15_ARTCRAFT_APPS
    assert len(ARTCRAFT_APPS) == 15
    artcraft_specs = DEFAULT_REGISTRY.get_artcraft_apps()
    assert len(artcraft_specs) == 15
    for app_id in EXPECTED_15_ARTCRAFT_APPS:
        spec = DEFAULT_REGISTRY.get_domain(app_id)
        assert spec is not None, f"Missing ArtCraft app domain: {app_id}"
        assert spec.category == "artcraft_suite"
        assert len(spec.tokens) >= 2


def test_offbrand_craft_adapters_registered() -> None:
    """Verify off-brand craft subdomain adapters (Blender, KiCad, Obsidian) resolve."""
    offbrand = DEFAULT_REGISTRY.get_domain("offbrand_craft")
    assert offbrand is not None
    token_codes = {t.code for t in offbrand.tokens}
    assert "CRAFT.ADAPTER.BLENDER" in token_codes
    assert "CRAFT.ADAPTER.KICAD" in token_codes
    assert "CRAFT.ADAPTER.OBSIDIAN" in token_codes


def test_graphic_engineering_loop_domain_and_tokens() -> None:
    """Verify Graphic Engineering & Graph Engineering Loops (comic pipeline) tokens resolve."""
    spec = DEFAULT_REGISTRY.get_domain("graphic_engineering")
    assert spec is not None
    codes = {t.code for t in spec.tokens}
    assert {
        "GRAPHENG.BLOCKOUT.PERSPECTIVE",
        "GRAPHENG.INK.LINEART",
        "GRAPHENG.COLOR.DIRTYGRADIENT",
        "GRAPHENG.LOOP.CONTINUITY_LINT",
        "GRAPHENG.PANEL.CPL",
    }.issubset(codes)


def test_architecture_design_thinking_domain() -> None:
    """Verify Architectural Design Thinking domain and tokens resolve."""
    spec = DEFAULT_REGISTRY.get_domain("architecture_design_thinking")
    assert spec is not None
    codes = {t.code for t in spec.tokens}
    assert "ARCH.DISCOVERY.DOUBLE_DIAMOND" in codes
    assert "ARCH.SPATIAL.PROGRAM_MASSING" in codes
    assert "ARCH.PDF.BIM_SECTION" in codes
    assert "ARCH.CONCEPT.MENTAL_MODEL" in codes


def test_physical_fabrication_cad_pcb_3d_printing_domain() -> None:
    """Verify Physical Fabrication covers 3D CAD, KiCad PCB, Gerber DRC, 3D printing G-code, and BOM."""
    spec = DEFAULT_REGISTRY.get_domain("physical_fabrication")
    assert spec is not None
    codes = {t.code for t in spec.tokens}
    assert {
        "FAB.CAD.PARAMETRIC_SOLID",
        "FAB.PCB.KICAD_SCHEMATIC",
        "FAB.PCB.GERBER_DRC",
        "FAB.PRINT.SLICER_GCODE",
        "FAB.ELEC.EMBEDDED_BOM",
    }.issubset(codes)


def test_ai_and_quantum_computing_domain() -> None:
    """Verify AI & Quantum domain covers GraphRAG, 36 papers, wave-function classifiers, and Orch-OR."""
    spec = DEFAULT_REGISTRY.get_domain("ai_quantum")
    assert spec is not None
    codes = {t.code for t in spec.tokens}
    assert {
        "AI.GRAPHRAG.INCREMENTAL_SUBGRAPH",
        "AI.AGENT.SWARM_ORCHESTRATOR",
        "AI.CORPUS.PAPER_SYNTHESIS_36",
        "QUANTUM.WAVEFUNCTION.CLASSIFIER",
        "QUANTUM.ORCH_OR.MICROTUBULE",
    }.issubset(codes)


def test_visual_reference_grounding_for_all_domains_and_tokens() -> None:
    """Verify VisualReferenceResolver maps every domain and token to a concrete VisualReference."""
    resolver = VisualReferenceResolver()
    for domain_id, spec in TAXONOMY_DOMAINS.items():
        ref = resolver.resolve_domain(domain_id)
        assert ref is not None, f"Missing visual reference for domain {domain_id}"
        assert ref.style_guide
        assert ref.diagram_type
        assert ref.expected_visual_schema
        assert len(ref.verification_checklist) >= 3
        assert ref.sample_uri.startswith("ref://")

        for token in spec.tokens:
            t_ref = resolver.resolve_token(token.code)
            assert t_ref is not None
            assert token.code in t_ref.expected_visual_schema
            assert token.output_artifact in t_ref.expected_visual_schema


def test_master_reasoning_prompt_exact_text() -> None:
    """Verify MASTER_REASONING_PROMPT matches the canonical specification."""
    expected = (
        "Act as an advanced multi-disciplinary reasoning engine specializing in the convergence of "
        "creative systems, architectural design thinking, computational frameworks, and physical "
        "fabrication pipelines. Analyze the provided domain queries by utilizing the established "
        "lexicographical taxonomy, integrating visual resource references, executing incremental "
        "GraphRAG synthesis across craft app subdomains, and employing graphic engineering loops "
        "and hardware fabrication logic to ensure precise execution for automated synthesis."
    )
    assert MASTER_REASONING_PROMPT == expected


def test_token_offset_equation_viability_and_savings() -> None:
    """Verify Giant Graph Token-Offset Cost Equation evaluates savings and economic viability."""
    viable_eval = evaluate_token_offset(
        node_count=50000,
        recompile_tokens=2000,
        query_value_usd=30.0,
        token_cost_per_1k=0.003,
    )
    assert viable_eval.is_viable is True
    assert viable_eval.full_graph_tokens == 50000 * 120
    assert viable_eval.tokens_saved == (50000 * 120) - 2000
    assert viable_eval.savings_ratio > 0.99
    assert viable_eval.recompile_cost_usd < viable_eval.full_graph_cost_usd
    assert viable_eval.net_value_usd > 29.9

    non_viable_eval = evaluate_token_offset(
        node_count=50000,
        recompile_tokens=5_000_000,
        query_value_usd=1.0,
        token_cost_per_1k=0.01,
    )
    assert non_viable_eval.is_viable is False


def test_prompt_compiler_end_to_end() -> None:
    """Verify PromptCompiler resolves tokens, visual references, and token-offset equation."""
    compiler = PromptCompiler()
    payload = compiler.compile(
        "Design a KiCad PCB and 3D printed enclosure with a comic book instruction manual and PDF preflight",
        domains=["physical_fabrication", "graphic_engineering", "pdfcraft"],
        node_count=40000,
        query_value_usd=50.0,
    )
    assert payload.master_prompt == MASTER_REASONING_PROMPT
    assert "physical_fabrication" in payload.resolved_domains
    assert "graphic_engineering" in payload.resolved_domains
    assert "pdfcraft" in payload.resolved_domains
    assert len(payload.lexicon_tokens) >= 8
    assert len(payload.visual_references) >= 3
    assert payload.token_offset.is_viable is True
    assert MASTER_REASONING_PROMPT in payload.compiled_prompt
    assert "FAB.PCB.KICAD_SCHEMATIC" in payload.compiled_prompt
    assert "GRAPHENG.INK.LINEART" in payload.compiled_prompt


def test_cli_domains_and_lookup_subcommands(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify CLI `domains` and `lookup` subcommands produce valid JSON output."""
    rc = cli_main(["domains", "--json"])
    assert rc == 0
    out = json.loads(capsys.readouterr().out)
    assert out["total_domains"] == 20
    assert len(out["artcraft_apps"]) == 15

    rc2 = cli_main(["lookup", "FAB.PCB.KICAD_SCHEMATIC", "--json"])
    assert rc2 == 0
    out2 = json.loads(capsys.readouterr().out)
    assert out2["type"] == "token"
    assert out2["token"]["code"] == "FAB.PCB.KICAD_SCHEMATIC"
    assert "visual_reference" in out2


def test_cli_compile_token_offset_and_sample_queries(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify CLI `compile`, `token-offset`, and `sample-queries` subcommands."""
    rc_compile = cli_main(
        [
            "compile",
            "Create a VectorCraft logo and SoundCraft audio cue with Quantum wave-function classification",
            "--domains",
            "vectorcraft",
            "soundcraft",
            "ai_quantum",
            "--json",
        ]
    )
    assert rc_compile == 0
    compiled_data = json.loads(capsys.readouterr().out)
    assert "vectorcraft" in compiled_data["resolved_domains"]
    assert "soundcraft" in compiled_data["resolved_domains"]
    assert "ai_quantum" in compiled_data["resolved_domains"]

    rc_offset = cli_main(
        [
            "token-offset",
            "--nodes",
            "50000",
            "--delta-nodes",
            "100",
            "--hops",
            "2",
            "--query-value",
            "40.0",
            "--json",
        ]
    )
    assert rc_offset == 0
    offset_data = json.loads(capsys.readouterr().out)
    assert offset_data["is_viable"] is True

    rc_samples = cli_main(["sample-queries", "--json"])
    assert rc_samples == 0
    samples_data = json.loads(capsys.readouterr().out)
    assert samples_data["count"] >= 20


def test_skill_md_frontmatter_and_readme_exist() -> None:
    """Verify SKILL.md has valid YAML frontmatter and README.md documents npx skills add."""
    root = Path(__file__).resolve().parent.parent
    skill_md = (root / "SKILL.md").read_text(encoding="utf-8")
    assert skill_md.startswith("---\n")
    assert "name: multi-domain-lexicon" in skill_md
    assert "description:" in skill_md
    assert MASTER_REASONING_PROMPT in skill_md

    readme_md = (root / "README.md").read_text(encoding="utf-8")
    assert "npx skills add NoJuanNobody/multi-domain-lexicon -g" in readme_md
