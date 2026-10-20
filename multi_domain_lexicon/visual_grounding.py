"""Visual Reference Grounding pairing lexicon domains and tokens with deterministic visual schemas."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from .taxonomy import DEFAULT_REGISTRY, LexiconRegistry


@dataclass(frozen=True)
class VisualReference:
    """Concrete visual reference specification paired with a domain or lexicon token."""

    target_id: str
    style_guide: str
    diagram_type: str
    expected_visual_schema: str
    verification_checklist: Tuple[str, ...]
    sample_uri: str

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


_DOMAIN_VISUAL_SPECS: Dict[str, VisualReference] = {
    "artcraft": VisualReference(
        target_id="artcraft",
        style_guide="ArtCraft Unified ACEScg / Display-P3 Dark Studio System",
        diagram_type="directed_acyclic_asset_graph",
        expected_visual_schema="Cross-app DAG diagram showing upstream/downstream creative asset nodes and ICC/OCIO transforms.",
        verification_checklist=(
            "All linked application nodes resolve without circular dependencies",
            "Color space tags (ACEScg / sRGB / CMYK) explicitly annotated on edges",
            "Asset checksums and version locks visible in node metadata",
        ),
        sample_uri="ref://artcraft/schemas/asset-hub-dag.svg",
    ),
    "cadcraft": VisualReference(
        target_id="cadcraft",
        style_guide="ISO 128 / ASME Y14.5 Technical Blueprint Drafting Standard",
        diagram_type="orthographic_4_view_blueprint",
        expected_visual_schema="Third-angle orthographic projection (Front, Top, Right, Isometric) with GD&T feature control frames.",
        verification_checklist=(
            "Visible, hidden, and center lines follow ISO 128 line-weight hierarchy",
            "Primary/Secondary/Tertiary datum reference frames (A|B|C) anchored",
            "Title block specifies units (mm), scale ratio, and general tolerance class",
        ),
        sample_uri="ref://cadcraft/blueprints/iso128-orthographic-gdt.pdf",
    ),
    "deckcraft": VisualReference(
        target_id="deckcraft",
        style_guide="Swiss International 12-Column 16:9 Executive Presentation Grid",
        diagram_type="modular_slide_master_wireframe",
        expected_visual_schema="1920x1080 12-column slide layout with assertion headline bar, visual evidence zone, and source footer.",
        verification_checklist=(
            "80px safe margin around slide perimeter",
            "Single declarative assertion headline per slide (<= 14 words)",
            "Contrast ratio >= 7:1 between foreground typography and canvas",
        ),
        sample_uri="ref://deckcraft/masters/16x9-assertion-evidence.svg",
    ),
    "designcraft": VisualReference(
        target_id="designcraft",
        style_guide="Swiss/Muller-Brockmann Editorial Spread & Baseline Grid System",
        diagram_type="facing_page_editorial_spread",
        expected_visual_schema="Facing-page spread with 12pt baseline grid, inner/outer margins, 3mm bleed guide, and CMYK ink density overlay.",
        verification_checklist=(
            "Body copy baselines lock across adjacent columns",
            "Full-bleed imagery extends 3mm past trim box; live text stays inside safety margin",
            "Total Area Coverage (TAC) stays below 300% for offset press compliance",
        ),
        sample_uri="ref://designcraft/spreads/editorial-baseline-cmyk.pdf",
    ),
    "effectcraft": VisualReference(
        target_id="effectcraft",
        style_guide="32-Bit Linear Float Node Compositing & Motion Telemetry Spec",
        diagram_type="compositing_node_graph_and_velocity_curve",
        expected_visual_schema="Dual panel displaying AOV shader merge DAG alongside cubic-bezier temporal speed/value curves.",
        verification_checklist=(
            "Premultiplied alpha handling verified on all Over/Plus merge nodes",
            "Easing velocity curves show continuous tangents without abrupt frame spikes",
            "Cryptomatte and Z-depth passes normalized to camera clipping planes",
        ),
        sample_uri="ref://effectcraft/comps/aov-node-velocity-sheet.png",
    ),
    "figcraft": VisualReference(
        target_id="figcraft",
        style_guide="W3C Design Token & Auto-Layout Component Matrix Specification",
        diagram_type="component_variant_matrix_redline",
        expected_visual_schema="State-by-variant component grid (Default/Hover/Focus/Disabled x Light/Dark) with spacing redlines.",
        verification_checklist=(
            "Zero hardcoded hex colors; 100% bound to semantic token aliases",
            "Auto-layout hug/fill constraints survive 320px to 1440px viewport resize",
            "Focus ring and interactive targets meet 24x24px minimum hit area",
        ),
        sample_uri="ref://figcraft/systems/component-variant-redline.svg",
    ),
    "filmcraft": VisualReference(
        target_id="filmcraft",
        style_guide="SMPTE Timecode NLE Timeline & Broadcast Rec.709/ACES Scope Layout",
        diagram_type="multitrack_timeline_and_vectorscope",
        expected_visual_schema="Multi-track video/audio timeline paired with IRE waveform monitor, RGB parade, and skin-tone vectorscope.",
        verification_checklist=(
            "Luminance peaks bounded between 0 and 100 IRE (or target HDR nit ceiling)",
            "Skin-tone vectors align along the I-line on calibrated vectorscope",
            "2-pop and SMPTE leader frame accuracy verified against EDL cut list",
        ),
        sample_uri="ref://filmcraft/timelines/nle-scopes-sheet.png",
    ),
    "gridcraft": VisualReference(
        target_id="gridcraft",
        style_guide="FAST Standard Financial & Engineering Tabular Modeling Convention",
        diagram_type="formula_dependency_dag_and_sensitivity_heatmap",
        expected_visual_schema="Color-coded input/calculation/output grid paired with an acyclic formula dependency graph.",
        verification_checklist=(
            "Zero circular references or volatile hardcodes inside formula cells",
            "Balance check and row/column cross-foot assertions evaluate to 0.00",
            "2D sensitivity matrix highlights break-even frontier",
        ),
        sample_uri="ref://gridcraft/models/formula-dag-heatmap.svg",
    ),
    "lightcraft": VisualReference(
        target_id="lightcraft",
        style_guide="16-Bit ProPhoto RGB Parametric Develop & Zone System Proof",
        diagram_type="histogram_tonecurve_and_zone_mask",
        expected_visual_schema="Split before/after RAW proof with RGB histogram, spline tone curve, and luminance zone overlay.",
        verification_checklist=(
            "Highlight and shadow clipping indicators clear across target dynamic range",
            "White balance Kelvin/Tint anchored to neutral grey reference patch",
            "Luminance mask transitions feathered without halo artifacts",
        ),
        sample_uri="ref://lightcraft/proofs/raw-zone-tonecurve.png",
    ),
    "pdfcraft": VisualReference(
        target_id="pdfcraft",
        style_guide="ISO 15930 (PDF/X-4) & ISO 19005 (PDF/A-2b) Structural Inspection Map",
        diagram_type="page_bbox_and_xref_tree",
        expected_visual_schema="Page canvas overlaid with color-coded text/vector/table bounding boxes and MediaBox/TrimBox geometry.",
        verification_checklist=(
            "100% of glyphs backed by embedded Unicode ToUnicode CMaps",
            "MediaBox, CropBox, BleedBox, and TrimBox hierarchy strictly nested",
            "XRef table and digital signature byte ranges validated",
        ),
        sample_uri="ref://pdfcraft/preflight/bbox-xref-overlay.pdf",
    ),
    "photocraft": VisualReference(
        target_id="photocraft",
        style_guide="Non-Destructive 16-Bit Raster Stack & Frequency Separation Schema",
        diagram_type="layer_stack_and_alpha_channel_decomposition",
        expected_visual_schema="Exploded isometric layer tree showing low-frequency color base, high-frequency texture, and alpha masks.",
        verification_checklist=(
            "All retouching operations isolated on non-destructive smart/adjustment layers",
            "High/low frequency separation recombines to bit-exact original at neutral state",
            "Edge masks free of chromatic fringe or premultiplication halos",
        ),
        sample_uri="ref://photocraft/stacks/freq-sep-layer-tree.png",
    ),
    "scriptcraft": VisualReference(
        target_id="scriptcraft",
        style_guide="Hollywood Standard Courier 12pt Screenplay & 1st AD Stripboard Format",
        diagram_type="fountain_page_and_eighths_breakdown",
        expected_visual_schema="Annotated screenplay page marked in 1/8th page vertical increments with color-coded department breakdown tags.",
        verification_checklist=(
            "Scene headings strictly follow INT./EXT. LOCATION - DAY/NIGHT grammar",
            "Page eighths sum accurately for scheduling stripboard estimation",
            "Cast, prop, VFX, and camera tags resolve to unique breakdown IDs",
        ),
        sample_uri="ref://scriptcraft/breakdowns/annotated-eighths-page.pdf",
    ),
    "soundcraft": VisualReference(
        target_id="soundcraft",
        style_guide="ITU-R BS.1770-4 Loudness, Phase Correlation & DAW Signal Flow Standard",
        diagram_type="daw_bus_routing_and_lufs_spectrogram",
        expected_visual_schema="Signal routing block diagram paired with 20Hz-20kHz spectrogram, phase goniometer, and LUFS loudness history.",
        verification_checklist=(
            "Integrated loudness hits target LUFS (+/- 0.5 LU) with True Peak <= -1.0 dBTP",
            "Stereo phase correlation remains positive (+0.2 to +1.0) across low-end sub-bass",
            "Sidechain gain reduction recovery completes prior to subsequent transient",
        ),
        sample_uri="ref://soundcraft/meters/bus-routing-lufs-spec.svg",
    ),
    "vectorcraft": VisualReference(
        target_id="vectorcraft",
        style_guide="G2 Curvature-Continuous Bezier Topology & CNC/Plotter Cut Contour Spec",
        diagram_type="bezier_control_polygon_and_curvature_comb",
        expected_visual_schema="Outline view showing anchor points, tangent handles, curvature combs, and winding-rule orientation.",
        verification_checklist=(
            "Extrema anchor points placed at horizontal and vertical tangents",
            "No stray points, unclosed contours, or self-intersecting loops",
            "Cut paths separated onto dedicated spot-color layer with 0.01mm hairline stroke",
        ),
        sample_uri="ref://vectorcraft/topology/bezier-curvature-comb.svg",
    ),
    "wordcraft": VisualReference(
        target_id="wordcraft",
        style_guide="Semantic Document AST, Typographic Hierarchy & IEEE/Chicago Citation Spec",
        diagram_type="document_dom_and_style_cascade_tree",
        expected_visual_schema="Hierarchical H1-H4 structural outline paired with paragraph rhythm and cross-reference anchor map.",
        verification_checklist=(
            "Zero manual line-breaks or ad-hoc font overrides outside named styles",
            "Measure constrained to 60-75 characters per line for optimal readability",
            "All figure, table, and bibliographic citations resolve bidirectionally",
        ),
        sample_uri="ref://wordcraft/specs/semantic-style-cascade.svg",
    ),
    "offbrand_craft": VisualReference(
        target_id="offbrand_craft",
        style_guide="Open Ecosystem Interchange Spec (USD / glTF / KiCad STEP / Obsidian MD)",
        diagram_type="cross_tool_schema_translation_map",
        expected_visual_schema="Bidirectional protocol diagram mapping Blender USD scenes, KiCad PCBs, and Obsidian Markdown vaults into ArtCraft.",
        verification_checklist=(
            "Coordinate system handedness (Y-up vs Z-up) and unit scale (1.0 = 1m or 1mm) normalized",
            "Material PBR roughness/metallic channels preserved across glTF/USD export",
            "YAML frontmatter keys validated against target knowledge vault schema",
        ),
        sample_uri="ref://offbrand_craft/bridges/open-interchange-map.svg",
    ),
    "graphic_engineering": VisualReference(
        target_id="graphic_engineering",
        style_guide="Hybrid 3D/Vector Perspective Underlay + Brush Ink + SOOP Dirty-Gradient Pipeline",
        diagram_type="four_stage_comic_panel_progression_sheet",
        expected_visual_schema=(
            "4-up sequential contact sheet: (1) 3D/Vector horizon & vanishing-point perspective blockout, "
            "(2) tapered sumi/G-pen ink line-art + spot blacks, (3) SOOP dirty-gradient color flats, "
            "(4) 180-degree axis & eyeline continuity lint overlay."
        ),
        verification_checklist=(
            "Vanishing lines converge accurately to 1/2/3-point horizon geometry",
            "Spot-black ratio (30-45%) establishes clear foreground/midground/background silhouette separation",
            "Dirty-gradient ramps preserve flat-cut readability without muddy airbrushing",
            "180-degree camera axis and Z-pattern balloon reading order pass continuity lint",
        ),
        sample_uri="ref://graphic_engineering/pipeline/4stage-panel-progression.png",
    ),
    "architecture_design_thinking": VisualReference(
        target_id="architecture_design_thinking",
        style_guide="AIA / ISO 19650 Architectural Drawing Set & Double-Diamond Discovery Framework",
        diagram_type="axonometric_massing_and_bim_section_sheet",
        expected_visual_schema=(
            "Split architectural presentation board: left side shows Double-Diamond problem/affordance map and "
            "programmatic bubble diagram; right side shows scale-calibrated section cut with daylight vectors and CSI callouts."
        ),
        verification_checklist=(
            "Graphic bar scale, north arrow, and section cut markers (A-A') present on all plan/section views",
            "Public/semi-public/private spatial hierarchy color-coded with circulation flow arrows",
            "User mental model states mapped 1:1 to physical/digital spatial affordances",
        ),
        sample_uri="ref://architecture_design_thinking/boards/axon-section-discovery.pdf",
    ),
    "physical_fabrication": VisualReference(
        target_id="physical_fabrication",
        style_guide="IPC-2221 / KiCad EDA Multi-Layer PCB + ISO GPS Mechanical CAD + FDM/SLA G-Code Spec",
        diagram_type="kicad_pcb_gerber_and_slicer_toolpath_sheet",
        expected_visual_schema=(
            "3-panel hardware fabrication blueprint: (1) KiCad hierarchical schematic & 4-layer copper/solder-mask Gerber plot, "
            "(2) exploded mechanical CAD enclosure with PCB standoffs, (3) 3D printer slicer layer preview showing perimeters, "
            "gyroid infill, and support overhangs."
        ),
        verification_checklist=(
            "KiCad ERC and DRC report 0 unconnected nets, 0 trace clearance violations, and controlled impedance within +/- 10%",
            "Gerber RS-274X + Excellon drill files + pick-and-place CPL centroid orientation verified",
            "3D print slicer preview confirms overhang angles <= 45 deg (or supported) and manifold watertight mesh",
        ),
        sample_uri="ref://physical_fabrication/blueprints/kicad-cad-gcode-triptych.svg",
    ),
    "ai_quantum": VisualReference(
        target_id="ai_quantum",
        style_guide="Incremental GraphRAG Subgraph Topology & Hilbert-Space Bloch/Density Matrix Spec",
        diagram_type="graphrag_delta_and_quantum_state_tomography",
        expected_visual_schema=(
            "Dual scientific figure: (1) Leiden community knowledge graph highlighting k-hop incremental delta nodes vs frozen "
            "backbone, (2) Quantum circuit ansatz + Bloch sphere wave-function decision boundary + Orch-OR decoherence curve."
        ),
        verification_checklist=(
            "Incremental GraphRAG update touches only k-hop neighborhood (delta_n << N) with verified token-offset savings",
            "Wave-function density matrix rho is Hermitian, positive semi-definite, with Tr(rho) == 1.0",
            "36-paper corpus synthesis claims traced to specific paper IDs and theorem/table anchors",
        ),
        sample_uri="ref://ai_quantum/figures/graphrag-hilbert-tomography.svg",
    ),
}


class VisualReferenceResolver:
    """Resolves lexicon domains and tokens into concrete visual reference grounding specifications."""

    def __init__(self, registry: Optional[LexiconRegistry] = None) -> None:
        self._registry = registry or DEFAULT_REGISTRY

    def resolve_domain(self, domain_id: str) -> Optional[VisualReference]:
        """Return the VisualReference for a given domain_id."""
        key = domain_id.strip().lower().replace("-", "_")
        return _DOMAIN_VISUAL_SPECS.get(key)

    def resolve_token(self, token_code: str) -> Optional[VisualReference]:
        """Return a token-specialized VisualReference grounded in its parent domain's visual spec."""
        token = self._registry.get_token(token_code)
        if token is None:
            return None
        base = self.resolve_domain(token.domain)
        if base is None:
            return None
        return VisualReference(
            target_id=token.code,
            style_guide=base.style_guide,
            diagram_type=base.diagram_type,
            expected_visual_schema=(
                f"[{token.code} -> {token.output_artifact}] {token.name}: "
                f"{token.description} | Base Schema: {base.expected_visual_schema}"
            ),
            verification_checklist=base.verification_checklist
            + (f"Verify output artifact `{token.output_artifact}` parameters: {', '.join(token.parameters)}",),
            sample_uri=f"{base.sample_uri}#{token.code.lower()}",
        )

    def resolve(self, identifier: str) -> Optional[VisualReference]:
        """Resolve either a domain_id or a token_code to its VisualReference."""
        by_domain = self.resolve_domain(identifier)
        if by_domain is not None:
            return by_domain
        return self.resolve_token(identifier)

    def resolve_many(self, identifiers: Sequence[str]) -> List[VisualReference]:
        """Resolve a sequence of domain IDs or token codes without duplicates."""
        seen = set()
        resolved: List[VisualReference] = []
        for ident in identifiers:
            ref = self.resolve(ident)
            if ref is not None and ref.target_id not in seen:
                seen.add(ref.target_id)
                resolved.append(ref)
        return resolved


DEFAULT_VISUAL_RESOLVER = VisualReferenceResolver()
