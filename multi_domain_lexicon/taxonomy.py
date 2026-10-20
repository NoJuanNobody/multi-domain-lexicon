"""Deterministic Lexicographical Taxonomy across ArtCraft apps and multi-disciplinary domains."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Dict, List, Optional, Sequence, Tuple

ARTCRAFT_APPS: Tuple[str, ...] = (
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
)


@dataclass(frozen=True)
class LexiconToken:
    """A single deterministic lexicographical token within a domain."""

    code: str
    domain: str
    name: str
    description: str
    parameters: Tuple[str, ...] = field(default_factory=tuple)
    keywords: Tuple[str, ...] = field(default_factory=tuple)
    output_artifact: str = ""

    def to_dict(self) -> Dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class DomainSpec:
    """Structured definition of a creative, engineering, architectural, fabrication, or AI/Quantum domain."""

    domain_id: str
    title: str
    category: str
    description: str
    tokens: Tuple[LexiconToken, ...]
    keywords: Tuple[str, ...]
    sample_queries: Tuple[str, ...]

    def to_dict(self) -> Dict[str, object]:
        return {
            "domain_id": self.domain_id,
            "title": self.title,
            "category": self.category,
            "description": self.description,
            "tokens": [t.to_dict() for t in self.tokens],
            "keywords": list(self.keywords),
            "sample_queries": list(self.sample_queries),
        }


def _build_domains() -> Dict[str, DomainSpec]:
    specs: List[DomainSpec] = [
        # 1. artcraft
        DomainSpec(
            domain_id="artcraft",
            title="ArtCraft Suite Launcher & Cross-App Asset Hub",
            category="artcraft_suite",
            description=(
                "Central orchestration hub for the 15-application ArtCraft creative suite, "
                "managing cross-application asset DAGs, ACEScg/ICC color pipelines, and MCP tool routing."
            ),
            tokens=(
                LexiconToken(
                    code="ARTCRAFT.HUB.ORCHESTRATE",
                    domain="artcraft",
                    name="Cross-App Pipeline Orchestration",
                    description="Dispatch multi-stage creative pipelines across ArtCraft applications with shared state.",
                    parameters=("pipeline_dag", "color_profile", "target_apps"),
                    keywords=("artcraft", "launcher", "orchestrate", "suite", "hub"),
                    output_artifact="manifest.artcraft.json",
                ),
                LexiconToken(
                    code="ARTCRAFT.ASSET.BRIDGE",
                    domain="artcraft",
                    name="Unified Asset Bridge",
                    description="Synchronize linked assets, fonts, LUTs, and geometry across craft tools.",
                    parameters=("asset_uri", "checksum", "consumers"),
                    keywords=("asset", "bridge", "sync", "lut", "color"),
                    output_artifact="asset_bridge_graph.json",
                ),
            ),
            keywords=("artcraft", "launcher", "suite", "hub", "cross-app", "asset bridge"),
            sample_queries=(
                "Orchestrate an ArtCraft pipeline linking VectorCraft logos into DesignCraft spreads and FilmCraft titles.",
            ),
        ),
        # 2. cadcraft
        DomainSpec(
            domain_id="cadcraft",
            title="CADCraft Precision 2D/3D Drafting & Parametric Solids",
            category="artcraft_suite",
            description="Parametric solid modeling, NURBS surfacing, DXF/STEP drafting, and GD&T tolerance analysis.",
            tokens=(
                LexiconToken(
                    code="CADCRAFT.STEP.SOLID",
                    domain="cadcraft",
                    name="Parametric Solid & B-Rep Assembly",
                    description="Construct watertight B-Rep solids with constraint-driven sketches and STEP export.",
                    parameters=("units_mm", "tolerance_grade", "material_density"),
                    keywords=("cad", "cadcraft", "step", "solid", "brep", "parametric"),
                    output_artifact="assembly.step",
                ),
                LexiconToken(
                    code="CADCRAFT.DXF.TOLERANCE",
                    domain="cadcraft",
                    name="Orthographic Projection & GD&T Callout",
                    description="Generate 4-view orthographic drawings with ASME Y14.5 datum targets and tolerances.",
                    parameters=("projection_angle", "datum_reference_frame", "linear_tol_mm"),
                    keywords=("dxf", "orthographic", "gdt", "datum", "tolerance", "blueprint"),
                    output_artifact="drawing_sheet.dxf",
                ),
            ),
            keywords=("cadcraft", "cad", "dxf", "step", "orthographic", "gdt", "drafting"),
            sample_queries=(
                "Generate a CADCraft parametric enclosure with ASME Y14.5 GD&T callouts and STEP/DXF exports.",
            ),
        ),
        # 3. deckcraft
        DomainSpec(
            domain_id="deckcraft",
            title="DeckCraft Narrative Presentation & Slide Systems",
            category="artcraft_suite",
            description="Keynote/deck architecture, master slide grids, executive data storytelling, and speaker pacing.",
            tokens=(
                LexiconToken(
                    code="DECKCRAFT.SLIDE.GRID",
                    domain="deckcraft",
                    name="Master Slide Modular Grid",
                    description="Enforce 12-column 16:9 slide master geometry with typographic scale tokens.",
                    parameters=("aspect_ratio", "column_count", "margin_pt"),
                    keywords=("deckcraft", "slide", "presentation", "deck", "master grid"),
                    output_artifact="presentation.deck",
                ),
                LexiconToken(
                    code="DECKCRAFT.STORY.ARC",
                    domain="deckcraft",
                    name="Executive Narrative Beat Progression",
                    description="Structure problem-thesis-proof-action narrative beats across slide sequences.",
                    parameters=("beat_count", "headline_assertion", "evidence_chart"),
                    keywords=("narrative", "pitch", "story arc", "slides", "keynote"),
                    output_artifact="story_arc_manifest.json",
                ),
            ),
            keywords=("deckcraft", "deck", "slides", "presentation", "keynote", "pitch"),
            sample_queries=(
                "Compile a 12-slide DeckCraft architecture review deck using assertion-evidence slide masters.",
            ),
        ),
        # 4. designcraft
        DomainSpec(
            domain_id="designcraft",
            title="DesignCraft Editorial Layout & Multi-Page Publishing",
            category="artcraft_suite",
            description="Facing-page editorial spreads, baseline grids, optical kerning, and CMYK print preflight.",
            tokens=(
                LexiconToken(
                    code="DESIGNCRAFT.SPREAD.BASELINE",
                    domain="designcraft",
                    name="Editorial Spread & Baseline Grid",
                    description="Align multi-column text frames and pull-quotes to an exact leading baseline grid.",
                    parameters=("page_size", "baseline_increment_pt", "bleed_mm"),
                    keywords=("designcraft", "editorial", "spread", "baseline", "indesign", "layout"),
                    output_artifact="publication.idml",
                ),
                LexiconToken(
                    code="DESIGNCRAFT.PREFLIGHT.CMYK",
                    domain="designcraft",
                    name="Press-Ready CMYK & Ink Limit Preflight",
                    description="Verify total area coverage (TAC <= 300%), spot pantone plates, and bleed marks.",
                    parameters=("icc_profile", "max_tac_percent", "crop_marks"),
                    keywords=("cmyk", "preflight", "bleed", "slug", "pantone", "print"),
                    output_artifact="press_ready_spread.pdf",
                ),
            ),
            keywords=("designcraft", "editorial", "spread", "cmyk", "baseline", "publishing"),
            sample_queries=(
                "Lay out a 24-page DesignCraft monograph with a 12pt baseline grid, 3mm bleed, and FOGRA39 CMYK preflight.",
            ),
        ),
        # 5. effectcraft
        DomainSpec(
            domain_id="effectcraft",
            title="EffectCraft Motion Graphics, Compositing & Shader VFX",
            category="artcraft_suite",
            description="Node-based EXR compositing, bezier keyframe velocity curves, procedural shaders, and motion tracking.",
            tokens=(
                LexiconToken(
                    code="EFFECTCRAFT.COMP.KEYFRAME",
                    domain="effectcraft",
                    name="Bezier Velocity Keyframe Rig",
                    description="Animate transform and procedural properties using cubic-bezier temporal interpolation.",
                    parameters=("fps", "cubic_bezier", "motion_blur_shutter_deg"),
                    keywords=("effectcraft", "keyframe", "motion graphics", "after effects", "velocity"),
                    output_artifact="comp_timeline.aec",
                ),
                LexiconToken(
                    code="EFFECTCRAFT.NODE.SHADER",
                    domain="effectcraft",
                    name="Multi-Pass AOV Shader Composite",
                    description="Merge beauty, depth, cryptomatte, and emission AOV passes in 32-bit float linear space.",
                    parameters=("color_space", "aov_channels", "shader_graph"),
                    keywords=("compositing", "shader", "aov", "cryptomatte", "exr", "vfx"),
                    output_artifact="composite_render.exr",
                ),
            ),
            keywords=("effectcraft", "vfx", "compositing", "motion", "shader", "keyframe", "exr"),
            sample_queries=(
                "Build an EffectCraft 32-bit float EXR composite combining cryptomatte isolation with eased HUD telemetry.",
            ),
        ),
        # 6. figcraft
        DomainSpec(
            domain_id="figcraft",
            title="FigCraft Collaborative UI/UX, Auto-Layout & Design Tokens",
            category="artcraft_suite",
            description="W3C design token trees, responsive auto-layout frames, interactive component variants, and WCAG audits.",
            tokens=(
                LexiconToken(
                    code="FIGCRAFT.TOKEN.AUTOLAYOUT",
                    domain="figcraft",
                    name="Auto-Layout & Semantic Design Token Binding",
                    description="Bind spacing, radius, color, and typography tokens to flexbox-like auto-layout containers.",
                    parameters=("direction", "gap_px", "token_namespace"),
                    keywords=("figcraft", "figma", "autolayout", "design tokens", "ui", "ux"),
                    output_artifact="design_tokens.json",
                ),
                LexiconToken(
                    code="FIGCRAFT.COMPONENT.VARIANT",
                    domain="figcraft",
                    name="Interactive State & Variant Matrix",
                    description="Specify default, hover, focus, active, disabled, and dark-mode component variants.",
                    parameters=("states", "wcag_contrast_min", "responsive_breakpoints"),
                    keywords=("component", "variant", "prototype", "state matrix", "wcag"),
                    output_artifact="component_matrix.fig",
                ),
            ),
            keywords=("figcraft", "ui", "ux", "autolayout", "design tokens", "variants", "figma"),
            sample_queries=(
                "Create a FigCraft responsive dashboard component system with W3C design tokens and WCAG AAA dark mode variants.",
            ),
        ),
        # 7. filmcraft
        DomainSpec(
            domain_id="filmcraft",
            title="FilmCraft Non-Linear Video Editing & DI Color Grading",
            category="artcraft_suite",
            description="Multi-track NLE ripple editing, EDL/XML conformation, waveform/vectorscope telemetry, and LUT grading.",
            tokens=(
                LexiconToken(
                    code="FILMCRAFT.NLE.EDL",
                    domain="filmcraft",
                    name="Timecode Conformation & EDL Assembly",
                    description="Assemble frame-accurate SMPTE timecode cuts with J/L split audio edits and XML/EDL export.",
                    parameters=("timecode_fps", "codec_profile", "handle_frames"),
                    keywords=("filmcraft", "nle", "edl", "timecode", "video editing", "premiere"),
                    output_artifact="sequence.edl",
                ),
                LexiconToken(
                    code="FILMCRAFT.TIMELINE.RIPPLE",
                    domain="filmcraft",
                    name="Multi-Track Ripple & Rec.709/ACES Grade",
                    description="Synchronize A/B roll cuts with secondary power-window color wheels and vectorscope bounds.",
                    parameters=("working_gamut", "target_nits", "audio_sync_tc"),
                    keywords=("timeline", "ripple", "color grade", "vectorscope", "rec709", "aces"),
                    output_artifact="master_timeline.fcpxml",
                ),
            ),
            keywords=("filmcraft", "video", "nle", "edl", "timecode", "grading", "timeline"),
            sample_queries=(
                "Conform a 24fps FilmCraft documentary timeline with SMPTE timecode EDL export and ACEScct color pipeline.",
            ),
        ),
        # 8. gridcraft
        DomainSpec(
            domain_id="gridcraft",
            title="GridCraft Reactive Spreadsheets, DAG Models & Pivot Matrices",
            category="artcraft_suite",
            description="Deterministic formula DAG evaluation, Monte Carlo financial modeling, and multidimensional pivot tables.",
            tokens=(
                LexiconToken(
                    code="GRIDCRAFT.MODEL.DAG",
                    domain="gridcraft",
                    name="Formula Dependency DAG & Sensitivity Table",
                    description="Construct acyclic formula graphs with zero circularity and 2D sensitivity sweeps.",
                    parameters=("sheet_schema", "sensitivity_axes", "precision_digits"),
                    keywords=("gridcraft", "spreadsheet", "excel", "formula", "financial model", "dag"),
                    output_artifact="model_workbook.xlsx",
                ),
                LexiconToken(
                    code="GRIDCRAFT.PIVOT.MATRIX",
                    domain="gridcraft",
                    name="Multi-Dimensional Pivot & Cohort Aggregation",
                    description="Aggregate tabular records across hierarchical dimensions with variance decomposition.",
                    parameters=("row_dims", "col_dims", "aggregation_fn"),
                    keywords=("pivot", "matrix", "cohort", "variance", "table"),
                    output_artifact="pivot_summary.csv",
                ),
            ),
            keywords=("gridcraft", "spreadsheet", "pivot", "formula", "model", "tabular"),
            sample_queries=(
                "Build a GridCraft unit-economics and BOM cost sensitivity model with automated cohort pivot tables.",
            ),
        ),
        # 9. lightcraft
        DomainSpec(
            domain_id="lightcraft",
            title="LightCraft RAW Photo Develop, Tone Curves & Catalog Triage",
            category="artcraft_suite",
            description="16-bit RAW demosaicing, parametric tone curves, luminance/depth masking, and XMP catalog sidecars.",
            tokens=(
                LexiconToken(
                    code="LIGHTCRAFT.RAW.TONECURVE",
                    domain="lightcraft",
                    name="Parametric RAW Exposure & Tone Curve",
                    description="Calibrate white balance, highlight recovery, shadow lift, and per-channel spline curves.",
                    parameters=("kelvin_temp", "tint", "exposure_ev", "curve_points"),
                    keywords=("lightcraft", "lightroom", "raw", "tone curve", "exposure", "develop"),
                    output_artifact="develop_recipe.xmp",
                ),
                LexiconToken(
                    code="LIGHTCRAFT.MASK.LUMINANCE",
                    domain="lightcraft",
                    name="AI Subject & Luminance Range Masking",
                    description="Isolate tonal zones or subjects for localized clarity, color grading, and grain.",
                    parameters=("luminance_range", "feather_pct", "local_ev"),
                    keywords=("mask", "luminance", "culling", "catalog", "xmp", "dng"),
                    output_artifact="graded_proof.dng",
                ),
            ),
            keywords=("lightcraft", "raw", "photo", "lightroom", "tone curve", "luminance", "xmp"),
            sample_queries=(
                "Develop a batch of 14-bit DNG architectural exteriors in LightCraft using luminance range masks and XMP presets.",
            ),
        ),
        # 10. pdfcraft
        DomainSpec(
            domain_id="pdfcraft",
            title="PDFCraft Document DOM Inspection, Redaction & Archival PDF/A",
            category="artcraft_suite",
            description="Low-level PDF xref inspection, vector/bbox extraction, cryptographic signing, OCR, and PDF/A-2b validation.",
            tokens=(
                LexiconToken(
                    code="PDFCRAFT.XREF.PREFLIGHT",
                    domain="pdfcraft",
                    name="PDF/A & PDF/X Structural XRef Audit",
                    description="Validate embedded font subsets, transparency flattening, and ISO compliance.",
                    parameters=("pdf_standard", "embed_fonts", "flatten_transparency"),
                    keywords=("pdfcraft", "pdf", "xref", "pdfa", "pdfx", "preflight", "acrobat"),
                    output_artifact="preflight_report.json",
                ),
                LexiconToken(
                    code="PDFCRAFT.BBOX.EXTRACT",
                    domain="pdfcraft",
                    name="Coordinate Bounding-Box Vector & Table Extraction",
                    description="Extract text runs, vector paths, and tables with exact page-space bounding coordinates.",
                    parameters=("page_range", "coordinate_origin", "ocr_fallback"),
                    keywords=("bbox", "extract", "ocr", "redaction", "table extraction", "coordinates"),
                    output_artifact="extracted_layout.json",
                ),
            ),
            keywords=("pdfcraft", "pdf", "bbox", "preflight", "ocr", "pdfa", "xref"),
            sample_queries=(
                "Run PDFCraft bounding-box extraction and PDF/X-4 font compliance audit on a 60-page architectural drawing set.",
            ),
        ),
        # 11. photocraft
        DomainSpec(
            domain_id="photocraft",
            title="PhotoCraft Non-Destructive Raster Layer Stack & Retouching",
            category="artcraft_suite",
            description="Multi-layer raster compositing, frequency separation, alpha channel calculations, and smart objects.",
            tokens=(
                LexiconToken(
                    code="PHOTOCRAFT.LAYER.BLEND",
                    domain="photocraft",
                    name="Non-Destructive Smart Layer & Blend Stack",
                    description="Compose raster layers with blend modes, clipping masks, and 16-bit adjustment layers.",
                    parameters=("bit_depth", "blend_mode", "mask_feather_px"),
                    keywords=("photocraft", "photoshop", "raster", "layer stack", "blend mode", "mask"),
                    output_artifact="composite.psd",
                ),
                LexiconToken(
                    code="PHOTOCRAFT.FREQ.SEPARATION",
                    domain="photocraft",
                    name="High/Low Spatial Frequency Separation",
                    description="Decompose image texture (high frequency) from tonal/color gradients (low frequency).",
                    parameters=("gaussian_radius_px", "linear_light_blend", "dodge_burn_curve"),
                    keywords=("retouching", "frequency separation", "channels", "alpha", "psd"),
                    output_artifact="retouched_master.tiff",
                ),
            ),
            keywords=("photocraft", "raster", "psd", "layers", "retouching", "frequency separation"),
            sample_queries=(
                "Construct a 16-bit PhotoCraft PSD stack using frequency separation and luminosity masks for product key art.",
            ),
        ),
        # 12. scriptcraft
        DomainSpec(
            domain_id="scriptcraft",
            title="ScriptCraft Fountain Screenwriting, Beat Sheets & Production Breakdown",
            category="artcraft_suite",
            description="Fountain screenplay syntax, scene-by-scene dramatic beat tracking, and 1st AD production breakdowns.",
            tokens=(
                LexiconToken(
                    code="SCRIPTCRAFT.FOUNTAIN.BEAT",
                    domain="scriptcraft",
                    name="Fountain Screenplay & Dramatic Beat Structure",
                    description="Format sluglines, action, parentheticals, and dual dialogue with timed page-per-minute metrics.",
                    parameters=("act_structure", "target_pages", "scene_numbering"),
                    keywords=("scriptcraft", "screenplay", "fountain", "slugline", "dialogue", "beat sheet"),
                    output_artifact="screenplay.fountain",
                ),
                LexiconToken(
                    code="SCRIPTCRAFT.SHOT.BREAKDOWN",
                    domain="scriptcraft",
                    name="1st AD Scene & Prop/VFX Breakdown",
                    description="Tag cast, props, wardrobe, stunts, and camera setups in eighths-of-a-page increments.",
                    parameters=("page_eighths", "department_tags", "day_night_int_ext"),
                    keywords=("breakdown", "stripboard", "shot list", "props", "production"),
                    output_artifact="production_breakdown.json",
                ),
            ),
            keywords=("scriptcraft", "fountain", "screenplay", "script", "shot breakdown", "beat sheet"),
            sample_queries=(
                "Write a ScriptCraft Fountain sequence and extract a 1st AD prop, VFX, and camera lens breakdown in page eighths.",
            ),
        ),
        # 13. soundcraft
        DomainSpec(
            domain_id="soundcraft",
            title="SoundCraft Digital Audio Workstation, DSP Mixing & Mastering",
            category="artcraft_suite",
            description="Multi-bus DAW signal routing, sidechain dynamics, mid/side EQ, stem separation, and ITU-R BS.1770 LUFS mastering.",
            tokens=(
                LexiconToken(
                    code="SOUNDCRAFT.MIX.LUFS",
                    domain="soundcraft",
                    name="Integrated LUFS Mastering & True-Peak Limiter",
                    description="Calibrate master bus loudness to target integrated LUFS and true-peak ceiling (dBTP).",
                    parameters=("target_lufs", "true_peak_dbtp", "sample_rate_hz"),
                    keywords=("soundcraft", "daw", "lufs", "mastering", "true peak", "audio"),
                    output_artifact="master_24bit.wav",
                ),
                LexiconToken(
                    code="SOUNDCRAFT.BUS.SIDECHAIN",
                    domain="soundcraft",
                    name="Subgroup Bus Routing & Spectral Sidechain",
                    description="Configure parallel compression, dynamic EQ ducking, and stem bus summing.",
                    parameters=("threshold_db", "ratio", "attack_ms", "release_ms"),
                    keywords=("sidechain", "bus", "stem", "compression", "eq", "mix"),
                    output_artifact="session_routing.soundcraft",
                ),
            ),
            keywords=("soundcraft", "audio", "daw", "lufs", "mastering", "sidechain", "mixing"),
            sample_queries=(
                "Master a 48kHz/24-bit SoundCraft session to -14 LUFS integrated / -1.0 dBTP with dynamic mid-side sidechain ducking.",
            ),
        ),
        # 14. vectorcraft
        DomainSpec(
            domain_id="vectorcraft",
            title="VectorCraft Precision Bezier Geometry, SVG & Plotter Paths",
            category="artcraft_suite",
            description="Cubic bezier spline topology, boolean pathfinder operations, variable-width strokes, and clean SVG/EPS output.",
            tokens=(
                LexiconToken(
                    code="VECTORCRAFT.BEZIER.PATHFINDER",
                    domain="vectorcraft",
                    name="Boolean Pathfinder & Curvature-Continuous Spline",
                    description="Construct G2 curvature-continuous bezier paths with non-destructive boolean compounds.",
                    parameters=("winding_rule", "boolean_op", "anchor_Snap_tol"),
                    keywords=("vectorcraft", "illustrator", "bezier", "pathfinder", "vector", "spline"),
                    output_artifact="artwork.svg",
                ),
                LexiconToken(
                    code="VECTORCRAFT.SVG.OUTLINE",
                    domain="vectorcraft",
                    name="Expanded Stroke Outline & CNC/Plotter Cut Path",
                    description="Expand strokes to closed contour loops free of self-intersections for vinyl/laser plotting.",
                    parameters=("stroke_miter_limit", "min_feature_mm", "spot_cut_swatch"),
                    keywords=("svg", "outline", "plotter", "laser cut", "eps", "contour"),
                    output_artifact="cut_contour.eps",
                ),
            ),
            keywords=("vectorcraft", "vector", "svg", "bezier", "pathfinder", "illustrator", "plotter"),
            sample_queries=(
                "Construct a geometric identity mark in VectorCraft using G2 continuous bezier splines and laser-ready SVG cut contours.",
            ),
        ),
        # 15. wordcraft
        DomainSpec(
            domain_id="wordcraft",
            title="WordCraft Semantic Manuscripts, Style Cascades & Technical Docs",
            category="artcraft_suite",
            description="Hierarchical paragraph/character style cascades, cross-references, citations, and structured DOCX/Markdown ASTs.",
            tokens=(
                LexiconToken(
                    code="WORDCRAFT.MANUSCRIPT.STYLE",
                    domain="wordcraft",
                    name="Hierarchical Paragraph & Character Style Cascade",
                    description="Enforce semantic heading levels, widow/orphan control, and OpenType ligature rules.",
                    parameters=("heading_depth", "font_family", "line_spacing"),
                    keywords=("wordcraft", "manuscript", "styles", "typography", "docx", "document"),
                    output_artifact="manuscript.docx",
                ),
                LexiconToken(
                    code="WORDCRAFT.TOC.SEMANTIC",
                    domain="wordcraft",
                    name="Automated TOC, Index & Citation Cross-Reference",
                    description="Compile dynamic tables of contents, figure captions, and BibTeX/CSL bibliography anchors.",
                    parameters=("citation_style", "toc_levels", "index_terms"),
                    keywords=("toc", "bibliography", "citations", "cross-reference", "technical writing"),
                    output_artifact="structured_doc.xml",
                ),
            ),
            keywords=("wordcraft", "manuscript", "docx", "typography", "citations", "toc"),
            sample_queries=(
                "Format a 150-page technical specification in WordCraft with IEEE citation anchors and semantic style cascades.",
            ),
        ),
        # 16. offbrand_craft (Off-Brand Craft Subdomains & Open Ecosystem Adapters)
        DomainSpec(
            domain_id="offbrand_craft",
            title="Off-Brand Craft Subdomain Adapters & Open Interchange",
            category="craft_adapters",
            description=(
                "Deterministic interchange adapters bridging ArtCraft tokens to third-party and open-source craft tools "
                "(Blender USD/glTF, KiCad EDA, FreeCAD, Inkscape, Obsidian PKM, Audacity/Reaper)."
            ),
            tokens=(
                LexiconToken(
                    code="CRAFT.ADAPTER.BLENDER",
                    domain="offbrand_craft",
                    name="Blender 3D / Grease Pencil / Freestyle Line-Art Bridge",
                    description="Exchange camera blockouts, rigged armatures, and Freestyle/LineArt SVG passes via USD/glTF.",
                    parameters=("scene_collection", "camera_focal_mm", "freestyle_svg_export"),
                    keywords=("blender", "usd", "gltf", "grease pencil", "freestyle", "offbrand"),
                    output_artifact="scene_bridge.usd",
                ),
                LexiconToken(
                    code="CRAFT.ADAPTER.KICAD",
                    domain="offbrand_craft",
                    name="KiCad EDA & CADCraft Mechanical IDF/STEP Sync",
                    description="Bidirectional board outline, mounting hole, and 3D package sync between KiCad and CADCraft.",
                    parameters=("board_thickness_mm", "step_3d_models", "netlist_format"),
                    keywords=("kicad", "freecad", "eda", "step sync", "offbrand"),
                    output_artifact="board_assembly.kicad_pcb",
                ),
                LexiconToken(
                    code="CRAFT.ADAPTER.OBSIDIAN",
                    domain="offbrand_craft",
                    name="Obsidian / Markdown Knowledge Graph Vault Adapter",
                    description="Export WordCraft/ScriptCraft lore and citations as wikilinked Markdown nodes with YAML frontmatter.",
                    parameters=("vault_root", "frontmatter_schema", "backlink_index"),
                    keywords=("obsidian", "markdown", "wikilink", "pkm", "vault"),
                    output_artifact="vault_index.md",
                ),
            ),
            keywords=("offbrand", "adapter", "blender", "obsidian", "freecad", "inkscape", "interchange"),
            sample_queries=(
                "Bridge a Blender 3D camera blockout and KiCad PCB STEP assembly into CADCraft and VectorCraft via off-brand craft adapters.",
            ),
        ),
        # 17. graphic_engineering (Graphic Engineering & Graph Engineering Loops)
        DomainSpec(
            domain_id="graphic_engineering",
            title="Graphic Engineering & Graph Engineering Loops (Comic Production Pipeline)",
            category="graphic_engineering",
            description=(
                "End-to-end comic book and sequential art production loop combining 3D/Vector perspective blockouts, "
                "Cinematic Prompt Language (CPL), brush ink line-art passes, SOOP dirty-gradient color, and continuity linting."
            ),
            tokens=(
                LexiconToken(
                    code="GRAPHENG.BLOCKOUT.PERSPECTIVE",
                    domain="graphic_engineering",
                    name="Hybrid 3D/Vector Perspective Underlay Blockout",
                    description="Stage characters and architecture in true 1/2/3-point or curvilinear perspective camera rigs.",
                    parameters=("focal_length_mm", "horizon_ratio", "camera_tilt_deg"),
                    keywords=("blockout", "perspective", "underlay", "comic", "panel", "staging"),
                    output_artifact="panel_blockout_underlay.png",
                ),
                LexiconToken(
                    code="GRAPHENG.INK.LINEART",
                    domain="graphic_engineering",
                    name="Tapered Brush Ink & Spot-Black Pass",
                    description="Render high-contrast sumi/G-pen line weights, feathering, and graphic chiaroscuro spot blacks.",
                    parameters=("line_weight_mm", "spot_black_threshold", "halftone_lpi"),
                    keywords=("ink", "lineart", "ink_look", "spot black", "chiaroscuro", "brush"),
                    output_artifact="panel_ink_pass.png",
                ),
                LexiconToken(
                    code="GRAPHENG.COLOR.DIRTYGRADIENT",
                    domain="graphic_engineering",
                    name="SOOP Dirty-Gradient & Flat-Cut Color Pass",
                    description="Apply flats with textured dirty-gradient ramps, atmospheric rim light, and paper grain multiply.",
                    parameters=("palette_key", "gradient_grit", "color_hold_lines"),
                    keywords=("dirty gradient", "flats", "color pass", "soop", "comic color"),
                    output_artifact="panel_color_final.tiff",
                ),
                LexiconToken(
                    code="GRAPHENG.LOOP.CONTINUITY_LINT",
                    domain="graphic_engineering",
                    name="Graph Engineering Continuity & 180-Degree Rule Linter",
                    description="Validate character costume state, spatial eyelines, 180-degree camera axis, and lettering balloon flow.",
                    parameters=("scene_graph_id", "check_180_axis", "reading_order_z"),
                    keywords=("continuity", "lint", "soop-loop", "graph engineering", "180 rule", "balloon"),
                    output_artifact="continuity_lint_report.json",
                ),
                LexiconToken(
                    code="GRAPHENG.PANEL.CPL",
                    domain="graphic_engineering",
                    name="Cinematic Prompt Language (CPL) Panel Specification",
                    description="Encode shot scale, lens focal length, key/fill ratio, and panel aspect ratio deterministically.",
                    parameters=("shot_scale", "lens_mm", "lighting_ratio", "panel_aspect"),
                    keywords=("cpl", "cinematic prompt", "shot scale", "lens", "framing"),
                    output_artifact="panel_cpl_spec.yaml",
                ),
            ),
            keywords=(
                "graphic engineering",
                "graph engineering",
                "comic",
                "ink",
                "blockout",
                "dirty gradient",
                "continuity lint",
                "cpl",
                "soop",
            ),
            sample_queries=(
                "Execute a Graphic Engineering loop for a 5-panel comic page: 24mm low-angle 3D perspective blockout, brush ink pass, dirty-gradient color, and continuity lint.",
            ),
        ),
        # 18. architecture_design_thinking
        DomainSpec(
            domain_id="architecture_design_thinking",
            title="Architectural Design Thinking, Spatial Hierarchy & Product Discovery",
            category="architecture_design_thinking",
            description=(
                "Convergence of architectural spatial programming, BIM section/plan PDF documentation, conceptual mental models, "
                "and Double-Diamond product discovery workflows."
            ),
            tokens=(
                LexiconToken(
                    code="ARCH.DISCOVERY.DOUBLE_DIAMOND",
                    domain="architecture_design_thinking",
                    name="Double-Diamond Problem Framing & Design Discovery",
                    description="Map divergent/convergent discovery phases: Discover, Define, Develop, Deliver with jobs-to-be-done.",
                    parameters=("problem_statement", "persona_constraints", "success_metrics"),
                    keywords=("design thinking", "double diamond", "discovery", "jtbd", "framing"),
                    output_artifact="discovery_brief.md",
                ),
                LexiconToken(
                    code="ARCH.SPATIAL.PROGRAM_MASSING",
                    domain="architecture_design_thinking",
                    name="Spatial Hierarchy, Circulation & Programmatic Massing",
                    description="Define public-to-private spatial gradients, daylighting envelopes, and circulation adjacency graphs.",
                    parameters=("floor_area_ratio", "adjacency_matrix", "solar_azimuth_deg"),
                    keywords=("architecture", "spatial", "massing", "circulation", "program", "axonometric"),
                    output_artifact="program_massing.ifc",
                ),
                LexiconToken(
                    code="ARCH.PDF.BIM_SECTION",
                    domain="architecture_design_thinking",
                    name="Architectural Construction Section & Detail Callout Sheet",
                    description="Generate scale-calibrated plans, building sections, wall assemblies, and CSI MasterFormat callouts.",
                    parameters=("scale_ratio", "cut_plane_z_m", "csi_division"),
                    keywords=("bim", "section", "elevation", "architectural pdf", "floor plan", "detail"),
                    output_artifact="arch_drawing_set.pdf",
                ),
                LexiconToken(
                    code="ARCH.CONCEPT.MENTAL_MODEL",
                    domain="architecture_design_thinking",
                    name="Conceptual Model & Affordance Mapping",
                    description="Align system state transitions with user mental models, spatial affordances, and wayfinding cues.",
                    parameters=("system_objects", "user_affordances", "feedback_latency_ms"),
                    keywords=("conceptual model", "affordance", "mental model", "wayfinding", "ux architecture"),
                    output_artifact="conceptual_model_diagram.svg",
                ),
            ),
            keywords=(
                "architecture",
                "design thinking",
                "double diamond",
                "spatial hierarchy",
                "bim",
                "massing",
                "floor plan",
                "conceptual model",
            ),
            sample_queries=(
                "Apply Architectural Design Thinking to frame a civic maker-space using Double-Diamond discovery, programmatic massing, and a 1:50 BIM section PDF.",
            ),
        ),
        # 19. physical_fabrication
        DomainSpec(
            domain_id="physical_fabrication",
            title="Physical Fabrication: 3D CAD, KiCad PCB Design, Electronics & 3D Printing",
            category="physical_fabrication",
            description=(
                "Complete hardware realization pipeline spanning parametric 3D mechanical modeling, KiCad schematic capture "
                "and multi-layer PCB layout, Gerber/Excellon DRC verification, embedded BOM sourcing, and FDM/SLA 3D printing G-code slicing."
            ),
            tokens=(
                LexiconToken(
                    code="FAB.CAD.PARAMETRIC_SOLID",
                    domain="physical_fabrication",
                    name="Parametric Mechanical Enclosure & Snap-Fit Bosses",
                    description="Model injection/print-ready enclosures with heat-set insert bosses, lip-and-groove seams, and draft angles.",
                    parameters=("wall_thickness_mm", "clearance_tol_mm", "fastener_spec"),
                    keywords=("3d modeling", "enclosure", "snap fit", "heat set insert", "mechanical cad"),
                    output_artifact="enclosure_body.step",
                ),
                LexiconToken(
                    code="FAB.PCB.KICAD_SCHEMATIC",
                    domain="physical_fabrication",
                    name="KiCad Schematic Capture, Netlist & Power Tree",
                    description="Design hierarchical electronic schematics with decoupling capacitors, ESD protection, and ERC verification.",
                    parameters=("mcu_part", "supply_rails_v", "bus_interfaces"),
                    keywords=("kicad", "schematic", "pcb", "electronics", "netlist", "erc", "mcu"),
                    output_artifact="hardware.kicad_sch",
                ),
                LexiconToken(
                    code="FAB.PCB.GERBER_DRC",
                    domain="physical_fabrication",
                    name="Multi-Layer PCB Impedance Routing & Gerber DRC",
                    description="Route controlled-impedance differential pairs (90-ohm USB / 50-ohm RF), ground planes, and run fab DRC.",
                    parameters=("layer_count", "min_trace_mil", "differential_impedance_ohm"),
                    keywords=("gerber", "drc", "pcb layout", "impedance", "kicad_pcb", "excellon"),
                    output_artifact="gerber_fab_pack.zip",
                ),
                LexiconToken(
                    code="FAB.PRINT.SLICER_GCODE",
                    domain="physical_fabrication",
                    name="FDM/SLA 3D Print Orientation, Support & G-Code Slicing",
                    description="Optimize build plate orientation, gyroid infill density, layer height, and volumetric flow rate into G-code.",
                    parameters=("process_type", "layer_height_mm", "infill_pct", "material_filament"),
                    keywords=("3d printing", "slicer", "gcode", "fdm", "sla", "gyroid", "infill", "stl", "3mf"),
                    output_artifact="print_job.gcode",
                ),
                LexiconToken(
                    code="FAB.ELEC.EMBEDDED_BOM",
                    domain="physical_fabrication",
                    name="Costed Pick-and-Place Centroid & LCSC/DigiKey BOM",
                    description="Generate SMT pick-and-place CPL coordinates and lifecycle-verified component bills of materials.",
                    parameters=("target_qty", "smt_assembly_side", "rohs_compliant"),
                    keywords=("bom", "pick and place", "smt", "pcba", "embedded", "digikey", "lcsc"),
                    output_artifact="pcba_bom_cpl.csv",
                ),
            ),
            keywords=(
                "physical fabrication",
                "3d printing",
                "kicad",
                "pcb",
                "electronics",
                "gerber",
                "gcode",
                "slicer",
                "3d modeling",
                "bom",
            ),
            sample_queries=(
                "Design a 4-layer ESP32-S3 KiCad PCB with 90-ohm USB-C routing, pass Gerber DRC, and slice a mating PETG snap-fit enclosure to G-code.",
            ),
        ),
        # 20. ai_quantum
        DomainSpec(
            domain_id="ai_quantum",
            title="Artificial Intelligence, Incremental GraphRAG & Quantum Computing",
            category="ai_quantum",
            description=(
                "Advanced computational intelligence spanning incremental GraphRAG knowledge graphs, autonomous multi-agent swarms, "
                "36-paper research corpus synthesis, Hilbert-space wave-function classifiers, and Orch-OR microtubule coherence models."
            ),
            tokens=(
                LexiconToken(
                    code="AI.GRAPHRAG.INCREMENTAL_SUBGRAPH",
                    domain="ai_quantum",
                    name="Incremental GraphRAG Community Delta Compilation",
                    description="Update localized k-hop knowledge graph neighborhoods without full O(N^2) corpus token recompilation.",
                    parameters=("total_nodes", "delta_nodes", "k_hops", "leiden_resolution"),
                    keywords=("graphrag", "incremental", "knowledge graph", "token offset", "leiden"),
                    output_artifact="subgraph_delta.json",
                ),
                LexiconToken(
                    code="AI.AGENT.SWARM_ORCHESTRATOR",
                    domain="ai_quantum",
                    name="Isolated Worktree Multi-Agent Swarm Protocol",
                    description="Coordinate parallel autonomous coding and research subagents with deterministic contract verification.",
                    parameters=("agent_count", "isolation_mode", "verification_gate"),
                    keywords=("agent", "swarm", "autonomous", "worktree", "orchestrator"),
                    output_artifact="swarm_trajectory.jsonl",
                ),
                LexiconToken(
                    code="AI.CORPUS.PAPER_SYNTHESIS_36",
                    domain="ai_quantum",
                    name="36-Paper Cross-Domain Research Corpus Synthesis",
                    description="Synthesize citations, empirical benchmarks, and theorem dependencies across a 36-paper frontier corpus.",
                    parameters=("corpus_size", "citation_graph", "synthesis_axis"),
                    keywords=("36 papers", "research corpus", "literature synthesis", "benchmarks"),
                    output_artifact="corpus_synthesis_matrix.md",
                ),
                LexiconToken(
                    code="QUANTUM.WAVEFUNCTION.CLASSIFIER",
                    domain="ai_quantum",
                    name="Variational Quantum Wave-Function State Classifier",
                    description="Encode feature manifolds into Hilbert-space amplitude/phase states and evaluate Born-rule measurement probabilities.",
                    parameters=("qubit_count", "ansatz_depth", "observable_pauli"),
                    keywords=("quantum", "wavefunction", "wave-function", "hilbert", "qubit", "classifier", "vqc"),
                    output_artifact="quantum_circuit.qasm",
                ),
                LexiconToken(
                    code="QUANTUM.ORCH_OR.MICROTUBULE",
                    domain="ai_quantum",
                    name="Orch-OR Dipolar Quantum Coherence & Objective Reduction Model",
                    description="Simulate Penrose-Hameroff gravitational self-energy E_G and decoherence timescales tau = hbar / E_G in tubulin lattices.",
                    parameters=("tubulin_dimers", "gravitational_self_energy_j", "decoherence_tau_ms"),
                    keywords=("orch-or", "consciousness", "microtubule", "penrose", "hameroff", "coherence"),
                    output_artifact="orch_or_simulation.json",
                ),
            ),
            keywords=(
                "ai",
                "quantum",
                "graphrag",
                "wave-function",
                "wavefunction",
                "orch-or",
                "consciousness",
                "36 papers",
                "autonomous agents",
            ),
            sample_queries=(
                "Synthesize the 36-paper AI & Quantum corpus using incremental GraphRAG and benchmark a variational wave-function classifier alongside Orch-OR coherence timescales.",
            ),
        ),
    ]
    return {spec.domain_id: spec for spec in specs}


TAXONOMY_DOMAINS: Dict[str, DomainSpec] = _build_domains()


class LexiconRegistry:
    """Registry providing deterministic lookup, search, and classification across all domains."""

    def __init__(self, domains: Optional[Dict[str, DomainSpec]] = None) -> None:
        self._domains: Dict[str, DomainSpec] = dict(domains or TAXONOMY_DOMAINS)
        self._tokens: Dict[str, LexiconToken] = {}
        for spec in self._domains.values():
            for token in spec.tokens:
                self._tokens[token.code.upper()] = token

    def list_domains(self) -> List[DomainSpec]:
        """Return all registered DomainSpec entries in deterministic order."""
        return list(self._domains.values())

    def get_artcraft_apps(self) -> List[DomainSpec]:
        """Return the 15 flagship ArtCraft application DomainSpecs."""
        return [self._domains[app_id] for app_id in ARTCRAFT_APPS if app_id in self._domains]

    def get_domain(self, domain_id: str) -> Optional[DomainSpec]:
        """Retrieve a DomainSpec by its identifier (case-insensitive)."""
        key = domain_id.strip().lower().replace("-", "_")
        return self._domains.get(key)

    def get_token(self, token_code: str) -> Optional[LexiconToken]:
        """Retrieve a LexiconToken by its canonical code (case-insensitive)."""
        return self._tokens.get(token_code.strip().upper())

    def lookup(self, identifier: str) -> Optional[Dict[str, object]]:
        """Lookup either a domain_id or a token code and return a structured dictionary."""
        domain = self.get_domain(identifier)
        if domain is not None:
            return {"type": "domain", "domain": domain.to_dict()}
        token = self.get_token(identifier)
        if token is not None:
            parent = self.get_domain(token.domain)
            return {
                "type": "token",
                "token": token.to_dict(),
                "domain_title": parent.title if parent else token.domain,
            }
        # Fallback to keyword search if exact match not found
        matches = self.search(identifier)
        if matches:
            return {"type": "search_results", "query": identifier, "matches": matches}
        return None

    def search(self, query: str) -> List[Dict[str, object]]:
        """Search domains and tokens matching any terms in the query string."""
        q = query.strip().lower()
        if not q:
            return []
        terms = [t for t in q.replace(",", " ").split() if t]
        results: List[Tuple[int, Dict[str, object]]] = []

        for spec in self._domains.values():
            haystack = " ".join(
                [
                    spec.domain_id,
                    spec.title.lower(),
                    spec.description.lower(),
                    " ".join(spec.keywords).lower(),
                ]
            )
            score = sum(2 if term in spec.keywords else (1 if term in haystack else 0) for term in terms)
            if q in haystack:
                score += 3
            if score > 0:
                results.append(
                    (
                        score,
                        {
                            "kind": "domain",
                            "id": spec.domain_id,
                            "title": spec.title,
                            "category": spec.category,
                            "score": score,
                        },
                    )
                )

            for token in spec.tokens:
                thaystack = " ".join(
                    [
                        token.code.lower(),
                        token.name.lower(),
                        token.description.lower(),
                        " ".join(token.keywords).lower(),
                    ]
                )
                tscore = sum(2 if term in token.keywords else (1 if term in thaystack else 0) for term in terms)
                if q in thaystack:
                    tscore += 4
                if tscore > 0:
                    results.append(
                        (
                            tscore,
                            {
                                "kind": "token",
                                "code": token.code,
                                "domain": token.domain,
                                "name": token.name,
                                "output_artifact": token.output_artifact,
                                "score": tscore,
                            },
                        )
                    )

        results.sort(key=lambda item: (-item[0], str(item[1].get("id") or item[1].get("code"))))
        return [item[1] for item in results]

    def classify_query(self, query: str, explicit_domains: Optional[Sequence[str]] = None) -> List[DomainSpec]:
        """Resolve explicit domain IDs and infer relevant domains from natural-language query text."""
        selected: Dict[str, DomainSpec] = {}
        if explicit_domains:
            for d_id in explicit_domains:
                spec = self.get_domain(d_id)
                if spec is not None:
                    selected[spec.domain_id] = spec

        q_lower = query.lower()
        scored: List[Tuple[int, DomainSpec]] = []
        for spec in self._domains.values():
            score = 0
            if spec.domain_id in q_lower:
                score += 5
            for kw in spec.keywords:
                if kw.lower() in q_lower:
                    score += 3
            for token in spec.tokens:
                if token.code.lower() in q_lower:
                    score += 6
                for tkw in token.keywords:
                    if tkw.lower() in q_lower:
                        score += 2
            if score > 0:
                scored.append((score, spec))

        scored.sort(key=lambda pair: (-pair[0], pair[1].domain_id))
        for _, spec in scored:
            if spec.domain_id not in selected:
                selected[spec.domain_id] = spec

        if not selected:
            # Default fallback to artcraft + ai_quantum if nothing matched
            selected["artcraft"] = self._domains["artcraft"]
            selected["ai_quantum"] = self._domains["ai_quantum"]

        return list(selected.values())

    def generate_sample_queries(self, domain_id: Optional[str] = None) -> List[Dict[str, object]]:
        """Return curated multi-domain and per-domain sample queries."""
        if domain_id:
            spec = self.get_domain(domain_id)
            if not spec:
                return []
            return [
                {
                    "domain_id": spec.domain_id,
                    "title": spec.title,
                    "tokens": [t.code for t in spec.tokens],
                    "query": q,
                }
                for q in spec.sample_queries
            ]

        samples: List[Dict[str, object]] = []
        for spec in self._domains.values():
            for q in spec.sample_queries:
                samples.append(
                    {
                        "domain_id": spec.domain_id,
                        "title": spec.title,
                        "tokens": [t.code for t in spec.tokens],
                        "query": q,
                    }
                )
        return samples


DEFAULT_REGISTRY = LexiconRegistry()
