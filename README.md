# Multi-Domain Lexicon (`multi-domain-lexicon`)

Deterministic lexicographical taxonomy, visual reference grounding, incremental GraphRAG token-offset cost calculator, and multi-disciplinary prompt compiler spanning all **15 ArtCraft applications**, off-brand craft subdomains, **Graphic Engineering / Graph Engineering Loops**, **Architectural Design Thinking**, **Physical Fabrication** (3D CAD, KiCad PCB design, electronics, 3D printing), **Artificial Intelligence**, and **Quantum Computing**.

## Install as an Agent Skill

```bash
npx skills add NoJuanNobody/multi-domain-lexicon -g
```

## Local Python Installation

```bash
pip install -e .
```

## Master Multi-Disciplinary Reasoning Prompt

> "Act as an advanced multi-disciplinary reasoning engine specializing in the convergence of creative systems, architectural design thinking, computational frameworks, and physical fabrication pipelines. Analyze the provided domain queries by utilizing the established lexicographical taxonomy, integrating visual resource references, executing incremental GraphRAG synthesis across craft app subdomains, and employing graphic engineering loops and hardware fabrication logic to ensure precise execution for automated synthesis."

## Taxonomy Overview

| Domain / App | Category | Core Lexicon Tokens | Visual Reference Grounding |
| :--- | :--- | :--- | :--- |
| `artcraft` | ArtCraft Suite | `ARTCRAFT.HUB.ORCHESTRATE`, `ARTCRAFT.ASSET.BRIDGE` | Cross-App Asset DAG & Color Manifest |
| `cadcraft` | ArtCraft Suite | `CADCRAFT.STEP.SOLID`, `CADCRAFT.DXF.TOLERANCE` | 4-View Orthographic Blueprint + GD&T |
| `deckcraft` | ArtCraft Suite | `DECKCRAFT.SLIDE.GRID`, `DECKCRAFT.STORY.ARC` | 16:9 Slide Master Typographic Grid |
| `designcraft` | ArtCraft Suite | `DESIGNCRAFT.SPREAD.BASELINE`, `DESIGNCRAFT.PREFLIGHT.CMYK` | Facing-Page Editorial Spread + Bleed/Slug |
| `effectcraft` | ArtCraft Suite | `EFFECTCRAFT.COMP.KEYFRAME`, `EFFECTCRAFT.NODE.SHADER` | Compositing Node Graph + Velocity Curve |
| `figcraft` | ArtCraft Suite | `FIGCRAFT.TOKEN.AUTOLAYOUT`, `FIGCRAFT.COMPONENT.VARIANT` | UI Component Variant Matrix + Token Specs |
| `filmcraft` | ArtCraft Suite | `FILMCRAFT.NLE.EDL`, `FILMCRAFT.TIMELINE.RIPPLE` | Multi-Track NLE Timeline + Scopes |
| `gridcraft` | ArtCraft Suite | `GRIDCRAFT.MODEL.DAG`, `GRIDCRAFT.PIVOT.MATRIX` | Formula Dependency Graph + Pivot Schema |
| `lightcraft` | ArtCraft Suite | `LIGHTCRAFT.RAW.TONECURVE`, `LIGHTCRAFT.MASK.LUMINANCE` | RAW Histogram + Parametric Tone Curve |
| `pdfcraft` | ArtCraft Suite | `PDFCRAFT.XREF.PREFLIGHT`, `PDFCRAFT.BBOX.EXTRACT` | PDF/X-4 Bounding Box & Font Audit |
| `photocraft` | ArtCraft Suite | `PHOTOCRAFT.LAYER.BLEND`, `PHOTOCRAFT.FREQ.SEPARATION` | Non-Destructive Layer Stack + Mask Channels |
| `scriptcraft` | ArtCraft Suite | `SCRIPTCRAFT.FOUNTAIN.BEAT`, `SCRIPTCRAFT.SHOT.BREAKDOWN` | Fountain Screenplay + Shot Breakdown Sheet |
| `soundcraft` | ArtCraft Suite | `SOUNDCRAFT.MIX.LUFS`, `SOUNDCRAFT.BUS.SIDECHAIN` | DAW Signal Routing + Spectral/LUFS Meter |
| `vectorcraft` | ArtCraft Suite | `VECTORCRAFT.BEZIER.PATHFINDER`, `VECTORCRAFT.SVG.OUTLINE` | Bezier Anchor/Handle Topology Diagram |
| `wordcraft` | ArtCraft Suite | `WORDCRAFT.MANUSCRIPT.STYLE`, `WORDCRAFT.TOC.SEMANTIC` | Semantic Manuscript Style Hierarchy |
| `offbrand_craft` | Craft Adapters | `CRAFT.ADAPTER.BLENDER`, `CRAFT.ADAPTER.KICAD`, `CRAFT.ADAPTER.OBSIDIAN` | Universal Interchange Schema (USD/Gerber/MD) |
| `graphic_engineering` | Engineering Loops | `GRAPHENG.BLOCKOUT.PERSPECTIVE`, `GRAPHENG.INK.LINEART`, `GRAPHENG.COLOR.DIRTYGRADIENT`, `GRAPHENG.LOOP.CONTINUITY_LINT` | 3-Pass Comic Panel Sheet (Blockout/Ink/Color) |
| `architecture_design_thinking` | Architecture & UX | `ARCH.DISCOVERY.DOUBLE_DIAMOND`, `ARCH.SPATIAL.PROGRAM_MASSING`, `ARCH.PDF.BIM_SECTION` | Axonometric Massing + Double-Diamond Map |
| `physical_fabrication` | Hardware & Fab | `FAB.CAD.PARAMETRIC_SOLID`, `FAB.PCB.KICAD_SCHEMATIC`, `FAB.PCB.GERBER_DRC`, `FAB.PRINT.SLICER_GCODE`, `FAB.ELEC.EMBEDDED_BOM` | KiCad Multi-Layer PCB Plot + Slicer Toolpath |
| `ai_quantum` | AI & Quantum | `AI.GRAPHRAG.INCREMENTAL_SUBGRAPH`, `QUANTUM.WAVEFUNCTION.CLASSIFIER`, `QUANTUM.ORCH_OR.MICROTUBULE`, `AI.CORPUS.PAPER_SYNTHESIS_36` | Hilbert State Bloch/Density Plot + GraphRAG DAG |

## CLI Reference

```bash
# List all domains
multi-domain-lexicon domains

# Lookup tokens and visual grounding for a domain or token code
multi-domain-lexicon lookup physical_fabrication

# Compile a deterministic prompt with visual grounding & token-offset metrics
multi-domain-lexicon compile "Synthesize a KiCad PCB and 3D printed enclosure with an architectural spec sheet" \
  --domains physical_fabrication cadcraft architecture_design_thinking pdfcraft

# Calculate Giant Graph Token-Offset Cost Equation
multi-domain-lexicon token-offset --nodes 50000 --delta-nodes 120 --hops 3 --query-value 25.0

# Emit curated multi-domain sample queries
multi-domain-lexicon sample-queries
```
