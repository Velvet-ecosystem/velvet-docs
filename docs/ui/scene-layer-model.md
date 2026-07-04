# UI Scene Layer Model

Status: Draft  
Applies To: Velvet UI Packs  
Reference Pack: Velvet v0 Front Room

## Purpose

This document defines the standard Velvet UI layer model.

The layer model keeps the interface from collapsing into either a pretty but useless wallpaper or a plain technical dashboard. Each layer has a job. The front can be beautiful. The deeper layers become more practical. The safety path stays immediate.

The standard flow is:

```text
Front Scene
  -> Contextual Overlay
    -> Full Themed Scene
      -> Control Sheet
        -> Backroom / Technical Layer
```

A user does not always move through every layer. The model defines available depth, not a forced path.

## Related Documents

```text
docs/ui/README.md
docs/ui/official-ui-pack.md
docs/ui/front-room-hotspot-map.md
docs/ui/velvet-v0-screen-inventory.md
docs/ui/custom-ui-skin-guide.md
docs/ui/asset-pack-template.md
assets/ui/velvet-v0/README.md
```

## Reference Assets

The official Velvet v0 asset pack demonstrates each layer:

```text
assets/ui/velvet-v0/front-room-main.png
assets/ui/velvet-v0/front-room-overlay-demo.png
assets/ui/velvet-v0/scene-layer-preview.png
assets/ui/velvet-v0/control-sheet-preview.png
assets/ui/velvet-v0/backroom-preview.png
assets/ui/velvet-v0/front-room-driving-mode.png
assets/ui/velvet-v0/front-room-warning-mode.png
```

Use `velvet-v0-screen-inventory.md` for the full screen list and implementation targets.

## Layer Summary

| Layer | Name | Purpose | Visual Style | Velvet v0 Asset |
|---|---|---|---|---|
| 1 | Front Scene | Default home and presence | Image-led, atmospheric, minimal controls | `front-room-main.png` |
| 2 | Contextual Overlay | Quick interaction | Small cards over the scene | `front-room-overlay-demo.png` |
| 3 | Full Themed Scene | Dedicated image-led functional world | Immersive sub-scene | `scene-layer-preview.png` |
| 4 | Control Sheet | Precise controls and presets | Practical themed widgets | `control-sheet-preview.png` |
| 5 | Backroom | Diagnostics, maintenance, truth | Technical panels and buttons | `backroom-preview.png` |

## Layer 1: Front Scene

The Front Scene is the first thing the user sees.

It is not a button grid. It is an environment with meaning.

The Front Scene may represent:

- a room
- a cockpit
- a garage
- a workbench
- a medical cabin
- a cyberdeck
- a map table
- a home console

Required responsibilities:

- show system presence
- provide primary object-based touch regions
- show basic status
- expose emergency access
- expose Backroom access
- expose mute or silent-listening access
- indicate offline/degraded state
- respond to listening/speaking state

The Front Scene is allowed to be poetic. It is not allowed to hide safety.

## Layer 2: Contextual Overlay

Contextual Overlays are quick panels opened from the Front Scene.

They should appear above the scene without fully replacing it.

Common overlay uses:

- quick audio control
- quick climate control
- quick lighting control
- quick comfort presets
- vehicle summary
- archive preview
- security state

Overlay rules:

- Keep the background scene visible or dimmed.
- Use short readable text.
- Keep controls lightweight.
- Provide a clear close/back action.
- Do not hide emergency access unless duplicated.
- Do not trigger dangerous actions without confirmation.

A contextual overlay is a quick drawer, not a control room.

## Layer 3: Full Themed Scene

Full Themed Scenes are deeper image-led environments.

They are used when a major functional area deserves its own visual world.

Examples:

- Library Home
- Boudoir Comfort
- Graveyard Archive
- Audio Room
- Workshop / Foundry
- Medical Guardian
- Map Table
- Garage Wall
- Cyberdeck Terminal Room

Full scenes should still use object-based regions and atmospheric design, but they may carry more detail than the Front Scene.

Full scenes are useful when:

- the function has multiple related controls
- the scene has a strong metaphor
- the user needs to enter a dedicated mode
- the system wants to separate public, private, guest, archive, or maintenance areas

## Layer 4: Control Sheet

Control Sheets are practical panels for precision.

They may contain:

- sliders
- toggles
- segmented controls
- tabs
- lists
- preset chips
- simple graphs
- input fields
- small buttons

Control Sheets can still inherit the skin's palette and typography, but clarity takes priority.

Use Control Sheets for:

- detailed climate adjustment
- audio routing
- equalizer settings
- lighting color and brightness
- seat comfort levels
- vehicle summary settings
- presets and automations

Control Sheet rules:

- Text must be readable.
- Active state must be obvious.
- Controls must be finger-usable.
- Risky actions require confirmation.
- Driving mode may restrict or simplify the sheet.

This is where the velvet glove meets the actual wrench.

## Layer 5: Backroom / Technical Layer

The Backroom is the technical and maintenance layer.

It is allowed to look more like a dashboard because its job is truth, not atmosphere.

Backroom sections may include:

- module health
- vehicle/CAN status
- power status
- sensor status
- audio routing
- climate systems
- storage and network
- logs and receipts
- permissions
- update center
- override tools
- emergency tools

Backroom rules:

- Be honest.
- Be readable.
- Show real state.
- Do not hide faults behind theme language.
- Separate ordinary controls from dangerous controls.
- Require appropriate access for dangerous actions.
- Preserve logs and receipts where applicable.

The Backroom is where Velvet stops flirting with the wallpaper and shows the bolts.

## Driving and Warning States

Driving mode and warning mode are not separate decorative skins. They are state overlays and behavior rules that can affect any layer.

Reference assets:

```text
assets/ui/velvet-v0/front-room-driving-mode.png
assets/ui/velvet-v0/front-room-warning-mode.png
```

Driving mode reduces distraction, restricts risky navigation, and prioritizes voice, quick controls, and safety.

Warning and emergency mode override the beauty layer. Critical information must become clear, readable, and immediate.

## Transition Rules

Transitions should communicate depth.

Recommended patterns:

- Front Scene -> Overlay: soft rise, fade, or glass card appearance
- Overlay -> Full Scene: fade or slide into scene
- Full Scene -> Control Sheet: drawer, sheet rise, or panel unfold
- Any Layer -> Backroom: seam open, hatch open, hard cut, or authenticated transition
- Warning/Emergency: immediate override

Decorative transitions must not delay emergency or warning states.

## Input Rules

Recommended input pattern:

| Gesture | Meaning |
|---|---|
| Tap | quick action or overlay |
| Hold | deeper controls or full scene |
| Swipe from edge | Backroom, navigation, or drawer |
| Back | close overlay or return one layer |
| Emergency tap | immediate emergency panel |

Important functions must not depend only on hidden gestures.

## State Overlay Rules

Each layer should understand common system states:

- idle
- listening
- speaking
- processing
- offline/local
- guest mode
- driving mode
- warning
- emergency
- degraded
- sleep/shutdown

The Front Scene may show these states through atmosphere. The Backroom must show them directly.

Examples:

- Listening: microphone sigil pulses.
- Speaking: center aura or avatar state animates.
- Offline/local: status bar shows local/offline mode.
- Driving: animation reduces and controls simplify.
- Warning: high-contrast overlay appears.
- Emergency: emergency panel overrides all noncritical visuals.

## Safety Priority

Safety always outranks visual style.

Priority order:

1. Emergency state
2. Critical warning
3. Driving safety restrictions
4. Access/permission rules
5. Control accuracy
6. Visual theme
7. Decorative animation

If a visual effect conflicts with a safety path, the visual effect loses.

## Implementation Boundary

The layer model describes interface behavior. It does not grant hardware authority.

UI layers may request actions through approved Velvet paths:

- local API
- event bus
- capability system
- permission gate
- safety controller
- receipt/log system

UI layers must not directly perform unsafe hardware actions.

## Example: Hearth Interaction Path

A typical interaction might look like this:

```text
Front Scene: tap fireplace/hearth
  -> Contextual Overlay: climate quick card
      tap target temp
        -> request climate setpoint through approved API
      hold More
        -> Control Sheet: full climate controls
      open Backroom
        -> Backroom: climate diagnostics
```

The user can stay shallow for quick warmth or go deeper for diagnostics.

This is the first recommended vertical implementation slice for Velvet v0.

## Example: Gramophone Interaction Path

```text
Front Scene: tap gramophone
  -> Contextual Overlay: audio quick card
      tap play/pause
        -> request media control through approved API
      hold gramophone
        -> Full Themed Scene: Audio Room
      More
        -> Control Sheet: audio routing / EQ
      Backroom
        -> Backroom: audio DSP and amplifier diagnostics
```

## Example: Graveyard Archive Path

```text
Front Scene: tap moon/window/archive marker
  -> Full Themed Scene: Graveyard Archive
      tap monument
        -> archived memory or retired module record
      tap gate
        -> recovery or continuity path
      back
        -> Front Scene
```

The Graveyard Archive represents memory, rest, and old states. It is not a default danger scene.

## Minimum Compliance

A Velvet-compatible UI pack must provide at least:

- one Front Scene
- emergency access
- Backroom access
- mute or silent-listening access
- warning state
- offline/degraded state
- driving-mode behavior
- at least one practical Control Sheet or Backroom view

A pack can be visually simple and still compliant if these paths exist.

## Final Rule

The user may enter through beauty.

They must always be able to reach truth.

They must never have to hunt for safety.
