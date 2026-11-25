# VR climbing experiment

A VR climbing study connecting architectural enclosure, controller interaction
and route-following decisions, with original Unreal Engine prototype assets and
documented experimental logic.

**Unreal Engine 5.4 · Blueprints · VR interaction · Experiment control · Rhino**

[Implementation](docs/IMPLEMENTATION.md) · [Open in UE](docs/OPEN_IN_UNREAL.md) · [Scenes](docs/SCENES.md) · [Citation](CITATION.cff)

## Research question and system

How can a virtual climbing task connect spatial enclosure with route-following
decisions? The system combines architectural scenes, controller input, hand–hold
interaction and a grip-error measure.

The archive preserves **ten original prototype assets** from 12–13 April 2025.
The later study is documented by the thesis and final presentation. Its complete
executable project has not been recovered or tested here.

| Competition-space example | Training-space example |
| --- | --- |
| ![Competition-space VR environment](assets/scene-competition-a.jpg) | ![Enclosed training-space VR environment](assets/scene-training.jpg) |

*Final presentation board 4, 25 May 2025. [Four experimental scenes and reference route](docs/SCENES.md).*

## Computational workflow

`Scene and route → controller input → hand–hold interaction → route comparison → error count → trial completion`

| Function | Implementation or evidence | Verification available |
| --- | --- | --- |
| Controller mapping and input setup | [Input assets](unreal/Content/Project_0412/Input/) and [BP_VRController](unreal/Content/Project_0412/Blueprint/player/BP_VRController.uasset) | File hashes, literal references and package symbols |
| Locomotion and grip/drop integration | [BP_VRCharacter](unreal/Content/Project_0412/Blueprint/Character/BP_VRCharacter.uasset) | Static character/interface symbol inspection |
| Grippable objects and application wiring | [Blueprint classes](unreal/Content/Project_0412/Blueprint/) and [test map](unreal/Content/Project_0412/MAPS/) | Static package integrity and references |
| Route-index rule, error counter and 30-grip completion | [Thesis Blueprint figure and specification](docs/IMPLEMENTATION.md#later-experiment-documented-scoring-workflow) | Documentary evidence; final editable scoring graph not recovered |

The thesis describes a 20 cm hand-contact sphere, vibration on successful contact,
a route-index tolerance of three and a 30-grip trial limit. The experimenter
recorded the displayed result. [Implementation and evidence](docs/IMPLEMENTATION.md).

[![Thesis Figure 10: overlap and scoring logic](assets/grip-blueprint.png)](assets/grip-blueprint.png)

## Quick start

With Python 3.9 or later, inspect the archive using the standard library:

```sh
python inspect_assets.py
```

Expected output: `"status": "PASS"`, ten checked files and no unresolved literal
project references. This is a static archive check. To inspect the visual programs
in the editor, follow the [UE 5.4 setup instructions](docs/OPEN_IN_UNREAL.md).
The original `python tools/inspect_assets.py` entry remains supported.

## Repository guide

| Location | Responsibility |
| --- | --- |
| [inspect_assets.py](inspect_assets.py) | Root entry for static archive checks |
| [tools/](tools/) | Archive-inspection implementation |
| [unreal/Content/Project_0412/](unreal/Content/Project_0412/) | Original Blueprint, input and map assets with unchanged internal paths |
| [assets/](assets/) | Thesis Blueprint figure, final scenes and architectural drawings |
| [docs/](docs/) | Implementation, engine setup, scenes and final design |
| [PROVENANCE.md](PROVENANCE.md) · [source_manifest.json](source_manifest.json) | Source versions, asset sizes and SHA-256 hashes |

## Validation and scope

Static checks verify all ten original assets and literal `/Game/` references.
Both inspection entry points passed in the 25 November 2026 organization review.
The [CI configuration](.github/workflows/checks.yml) runs the same static check.
They do not compile Blueprints, establish active graph connections or test
headset behaviour. The prototype's relationship to the later scoring system
is documented in [PROVENANCE.md](PROVENANCE.md).

Engine binaries and third-party plugin source are external dependencies.
[Dependencies and rights](THIRD_PARTY_NOTICES.md). This archive has no Python
analysis dataset or reconstructed participant-level results.

## Research record

**Zihao Lin · Undergraduate thesis and graduation design · Tsinghua University, 2025**

**Thesis:** 建筑空间垂直围合度对攀岩决策表现的影响研究  
**Design:** 岩双阙 / *Twin Cliff*  
**Supervisor:** Zhang Li, School of Architecture, Tsinghua University

The study used three competition-space conditions labelled 10%, 40% and 70%
visible sky, plus a training-space condition. The thesis reports 20 recruits;
its displayed result table contains 16 participant records per condition.
This repository documents the system and study design without adopting disputed
inferential results from the archived draft.

[Final exterior, section, site plan and interiors](docs/ARCHITECTURE.md) · [Repository citation](CITATION.cff).
