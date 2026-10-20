---
name: multi-domain-lexicon
description: Deterministic lexicographical taxonomy, visual reference grounding, incremental GraphRAG token-offset calculator, and multi-disciplinary prompt compiler spanning all 15 ArtCraft creative apps, off-brand craft subdomains, Graphic Engineering / Comic Production Loops, Architectural Design Thinking, Physical Fabrication (3D CAD, KiCad PCB, Electronics, 3D Printing), AI, and Quantum Computing.
---

# Multi-Domain Lexicon (`multi-domain-lexicon`)

Use this skill whenever constructing, parsing, grounding, or compiling cross-disciplinary technical queries across creative production suites, graphic engineering pipelines, architectural design thinking, hardware/physical fabrication, artificial intelligence, and quantum computing.

## 1. Master Multi-Disciplinary Reasoning Prompt

Embed or prepend the canonical Master Reasoning Prompt when orchestrating cross-domain synthesis:

> "Act as an advanced multi-disciplinary reasoning engine specializing in the convergence of creative systems, architectural design thinking, computational frameworks, and physical fabrication pipelines. Analyze the provided domain queries by utilizing the established lexicographical taxonomy, integrating visual resource references, executing incremental GraphRAG synthesis across craft app subdomains, and employing graphic engineering loops and hardware fabrication logic to ensure precise execution for automated synthesis."

## 2. Deterministic Lexicographical Taxonomy

### 2.1 ArtCraft Flagship Suite (15 Applications) & Off-Brand Craft Subdomains

| App ID | Domain Role | Canonical Tokens | Visual Grounding Schema |
| :--- | :--- | :--- | :--- |
| `artcraft` | Creative Suite Launcher & Asset Hub | `ARTCRAFT.HUB.ORCHESTRATE`, `ARTCRAFT.ASSET.BRIDGE` | Cross-app DAG dependency graph & color-managed asset manifest |
| `cadcraft` | 2D/3D Precision CAD & Drafting | `CADCRAFT.STEP.SOLID`, `CADCRAFT.DXF.TOLERANCE` | Orthographic 4-view technical blueprint with GD&T callouts |
| `deckcraft` | Presentation & Narrative Deck Engine | `DECKCRAFT.SLIDE.GRID`, `DECKCRAFT.STORY.ARC` | 16:9 modular slide master grid with typographic hierarchy |
| `designcraft` | Multi-Page Editorial & Layout Publishing | `DESIGNCRAFT.SPREAD.BASELINE`, `DESIGNCRAFT.PREFLIGHT.CMYK` | Facing-page spread layout with baseline grid, bleed, and slug |
| `effectcraft` | Motion Graphics, Compositing & VFX | `EFFECTCRAFT.COMP.KEYFRAME`, `EFFECTCRAFT.NODE.SHADER` | Timeline dope sheet + bezier velocity graph + render pass tree |
| `figcraft` | Collaborative UI/UX & Design Systems | `FIGCRAFT.TOKEN.AUTOLAYOUT`, `FIGCRAFT.COMPONENT.VARIANT` | Component state matrix with design token inspection overlays |
| `filmcraft` | Non-Linear Video Editing & Color Timeline | `FILMCRAFT.NLE.EDL`, `FILMCRAFT.TIMELINE.RIPPLE` | Multi-track NLE timeline with waveform/vectorscope telemetry |
| `gridcraft` | Tabular Modeling, Formulas & Data Grids | `GRIDCRAFT.MODEL.DAG`, `GRIDCRAFT.PIVOT.MATRIX` | Structured financial/engineering spreadsheet dependency matrix |
| `lightcraft` | RAW Photography Develop & Catalog Triage | `LIGHTCRAFT.RAW.TONECURVE`, `LIGHTCRAFT.MASK.LUMINANCE` | Histogram + parametric tone curve + split-view develop proof |
| `pdfcraft` | Portable Document Inspection & Preflight | `PDFCRAFT.XREF.PREFLIGHT`, `PDFCRAFT.BBOX.EXTRACT` | PDF/X-4 object bounding-box overlay & font table inspector |
| `photocraft` | Raster Imaging, Layer Stack & Retouching | `PHOTOCRAFT.LAYER.BLEND`, `PHOTOCRAFT.FREQ.SEPARATION` | Non-destructive PSD layer stack with alpha/channel masks |
| `scriptcraft` | Screenplay, Fountain & Storyboard Breakdown | `SCRIPTCRAFT.FOUNTAIN.BEAT`, `SCRIPTCRAFT.SHOT.BREAKDOWN` | Industry-standard screenplay page + scene beat sheet |
| `soundcraft` | Digital Audio Workstation (DAW) & Mastering | `SOUNDCRAFT.MIX.LUFS`, `SOUNDCRAFT.BUS.SIDECHAIN` | Spectral analyzer + LUFS loudness meter + signal routing graph |
| `vectorcraft` | Precision Bezier Vector Illustration | `VECTORCRAFT.BEZIER.PATHFINDER`, `VECTORCRAFT.SVG.OUTLINE` | Anchor/handle bezier topology view with boolean path operations |
| `wordcraft` | Long-Form Manuscript & Structured Typography | `WORDCRAFT.MANUSCRIPT.STYLE`, `WORDCRAFT.TOC.SEMANTIC` | Semantic document DOM tree with paragraph/character style cascade |
| `offbrand_craft` | Third-Party / Open-Source Craft Adapters | `CRAFT.ADAPTER.BLENDER`, `CRAFT.ADAPTER.KICAD`, `CRAFT.ADAPTER.OBSIDIAN` | Universal USD/glTF/Gerber/Markdown interchange bridge schema |

### 2.2 Graphic Engineering & Graph Engineering Loops (`graphic_engineering`)
- **Tokens**: `GRAPHENG.BLOCKOUT.PERSPECTIVE`, `GRAPHENG.INK.LINEART`, `GRAPHENG.COLOR.DIRTYGRADIENT`, `GRAPHENG.LOOP.CONTINUITY_LINT`, `GRAPHENG.PANEL.CPL`
- **Pipeline**: Hybrid 3D/Vector Perspective Underlay -> Brush Ink Pass -> Dirty-Gradient Color -> Continuity Lint & Artist Decision Loop.

### 2.3 Architectural Design Thinking (`architecture_design_thinking`)
- **Tokens**: `ARCH.DISCOVERY.DOUBLE_DIAMOND`, `ARCH.SPATIAL.PROGRAM_MASSING`, `ARCH.PDF.BIM_SECTION`, `ARCH.CONCEPT.MENTAL_MODEL`
- **Pipeline**: Problem framing -> Spatial hierarchy & circulation diagrams -> Conceptual mental models -> Architectural drawing set extraction.

### 2.4 Physical Fabrication (`physical_fabrication`)
- **Tokens**: `FAB.CAD.PARAMETRIC_SOLID`, `FAB.PCB.KICAD_SCHEMATIC`, `FAB.PCB.GERBER_DRC`, `FAB.PRINT.SLICER_GCODE`, `FAB.ELEC.EMBEDDED_BOM`
- **Pipeline**: Parametric 3D CAD -> KiCad schematic capture & multi-layer PCB routing -> Design Rule Check (DRC) & Gerber/Excellon export -> FDM/SLA slicing (G-code toolpaths) & BOM assembly.

### 2.5 AI & Quantum Computing (`ai_quantum`)
- **Tokens**: `AI.GRAPHRAG.INCREMENTAL_SUBGRAPH`, `AI.AGENT.SWARM_ORCHESTRATOR`, `QUANTUM.WAVEFUNCTION.CLASSIFIER`, `QUANTUM.ORCH_OR.MICROTUBULE`, `AI.CORPUS.PAPER_SYNTHESIS_36`
- **Pipeline**: Incremental GraphRAG community detection -> Multi-agent swarm verification -> Hilbert-space wave-function classification & Orch-OR coherence modeling.

## 3. Giant Graph Token-Offset Cost Equation

When updating or querying a giant multi-domain knowledge graph (such as a 15-app ArtCraft + fabrication + research corpus graph), full graph recompilation scales quadratically with node count, whereas **Incremental Subgraph Delta Compilation** bounds token consumption:

$$\Delta C_{\text{offset}} = C_{\text{full}}(N) - C_{\text{incremental}}(\Delta n, k) = \left(N \cdot \tau_{\text{node}}\right) - \left(\Delta n \cdot \tau_{\text{node}} + k \cdot \tau_{\text{hop}}\right)$$

$$\text{Viability Ratio } \eta = \frac{V_{\text{query}}}{\left(\Delta n \cdot \tau_{\text{node}} + k \cdot \tau_{\text{hop}}\right) \cdot \frac{P_{1k}}{1000}} \ge 10.0$$

Use `multi-domain-lexicon token-offset` to evaluate whether a graph recompilation is economically viable and verify the percentage saved via incremental GraphRAG delta updates.

## 4. CLI Usage

```bash
# List all registered domains and ArtCraft applications
multi-domain-lexicon domains

# Lookup a specific domain or token with visual reference grounding
multi-domain-lexicon lookup physical_fabrication
multi-domain-lexicon lookup FAB.PCB.KICAD_SCHEMATIC

# Compile a multi-domain prompt with visual grounding and token-offset verification
multi-domain-lexicon compile "Design a custom MIDI controller enclosure and PCB with comic-style manual" \
  --domains cadcraft physical_fabrication graphic_engineering soundcraft

# Evaluate the Giant Graph Token-Offset Cost Equation
multi-domain-lexicon token-offset --nodes 50000 --delta-nodes 120 --hops 3 --query-value 25.0

# Generate sample queries across all domains
multi-domain-lexicon sample-queries
```
