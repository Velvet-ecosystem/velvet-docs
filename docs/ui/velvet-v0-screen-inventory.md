# Velvet v0 Screen Inventory

Status: Draft  
Applies To: Velvet v0 Official UI Pack  
Primary Target: 2008 Hyundai Tiburon  
Reference Assets: `assets/ui/velvet-v0/`

## Purpose

This document lists the official Velvet v0 UI screens, layers, reference images, and first implementation targets.

The goal is to keep the UI pack buildable. The images define the look. The docs define the rules. This inventory defines what must exist.

## Reference Asset Folder

All official Velvet v0 reference images live here:

```text
assets/ui/velvet-v0/
```

Current assets:

```text
front-room-main.png
front-room-touch-map.png
front-room-overlay-demo.png
scene-layer-preview.png
control-sheet-preview.png
backroom-preview.png
front-room-driving-mode.png
front-room-warning-mode.png
```

## Layer Inventory

| Layer | Screen / State | Reference Asset | Purpose | Implementation Status |
|---|---|---|---|---|
| Front Scene | Front Room Home | `front-room-main.png` | Default home scene and main presence layer | Documented |
| Front Scene | Front Room Touch Map | `front-room-touch-map.png` | Builder hotspot reference | Documented |
| Context Overlay | Overlay Demo | `front-room-overlay-demo.png` | Shows quick cards over the room | Reference image ready |
| Full Scene | Scene Layer Preview | `scene-layer-preview.png` | Shows deeper themed scenes | Reference image ready |
| Control Sheet | Control Sheet Preview | `control-sheet-preview.png` | Shows practical widgets and presets | Reference image ready |
| Backroom | Backroom Preview | `backroom-preview.png` | Shows diagnostics and technical layer | Reference image ready |
| Driving Mode | Driving Front Room | `front-room-driving-mode.png` | Simplified moving-state UI | Reference image ready |
| Warning Mode | Warning / Emergency Front Room | `front-room-warning-mode.png` | Safety override state | Reference image ready |

## Required v0 Screens

### 1. Front Room Home

Layer: Front Scene  
Reference Asset: `front-room-main.png`  
Primary Doc: `front-room-hotspot-map.md`

Purpose:

- default home screen
- Velvet presence
- image-led navigation
- object-based touch regions
- listening/speaking status
- emergency access
- Backroom access
- mute/silent-listening access

Required regions:

- audio / gramophone
- climate / hearth
- archive / bookshelf or ladder
- lighting / moon or window
- comfort / chair or chaise
- private / boudoir threshold
- vehicle / Tiburon point
- conversation / microphone sigil
- backroom / seam or keyhole
- emergency / safety mark
- mute / silent-listening mark

Implementation target:

```text
ui/scenes/velvet_v0/scenes/front_room.scene.yaml
ui/scenes/velvet_v0/hotspot_maps/front_room.hotspots.yaml
```

### 2. Audio Quick Overlay

Layer: Contextual Overlay  
Reference Asset: `front-room-overlay-demo.png`

Purpose:

- now playing
- basic transport controls
- source or mood preset
- volume preview
- deeper audio scene entry

Allowed while driving:

- yes, simplified only

Implementation target:

```text
ui/scenes/velvet_v0/overlays/audio_quick.overlay.yaml
```

### 3. Climate Quick Overlay

Layer: Contextual Overlay  
Reference Asset: `front-room-overlay-demo.png`

Purpose:

- current target temperature
- quick warmer/cooler
- fan quick access
- preset access
- entry to climate control sheet

Allowed while driving:

- yes, simplified only

Implementation target:

```text
ui/scenes/velvet_v0/overlays/climate_quick.overlay.yaml
```

### 4. Comfort Quick Overlay

Layer: Contextual Overlay  
Reference Asset: `front-room-overlay-demo.png`

Purpose:

- seat comfort presets
- warmth/massage preview where installed
- mood preset
- entry to comfort sheet

Allowed while driving:

- limited

Implementation target:

```text
ui/scenes/velvet_v0/overlays/comfort_quick.overlay.yaml
```

### 5. Vehicle Summary Overlay

Layer: Contextual Overlay  
Reference Assets: `front-room-driving-mode.png`, `front-room-overlay-demo.png`

Purpose:

- status
- speed/fuel/range where available
- module health summary
- read-only vehicle glance
- entry to vehicle status sheet or Backroom

Allowed while driving:

- read-only only

Implementation target:

```text
ui/scenes/velvet_v0/overlays/vehicle_summary.overlay.yaml
```

### 6. Scene Layer / Full Themed Scenes

Layer: Full Themed Scene  
Reference Asset: `scene-layer-preview.png`

Purpose:

- show deeper image-led spaces
- separate main home, private comfort, and archive worlds
- preserve atmosphere while offering depth

Initial v0 full scenes:

```text
library_home
boudoir_comfort
graveyard_archive
```

Implementation targets:

```text
ui/scenes/velvet_v0/scenes/library_home.scene.yaml
ui/scenes/velvet_v0/scenes/boudoir_comfort.scene.yaml
ui/scenes/velvet_v0/scenes/graveyard_archive.scene.yaml
```

### 7. Climate Control Sheet

Layer: Control Sheet  
Reference Asset: `control-sheet-preview.png`

Purpose:

- target temperature
- fan speed
- mode
- presets
- practical climate controls

First vertical slice target:

```text
Front Room Home
  -> Climate Quick Overlay
    -> Climate Control Sheet
      -> Backroom Climate Diagnostics
```

Implementation target:

```text
ui/scenes/velvet_v0/control_sheets/climate.sheet.yaml
```

### 8. Audio Control Sheet

Layer: Control Sheet  
Reference Asset: `control-sheet-preview.png`

Purpose:

- media routing
- volume
- presets
- equalizer / later DSP
- source selection

Implementation target:

```text
ui/scenes/velvet_v0/control_sheets/audio.sheet.yaml
```

### 9. Lighting Control Sheet

Layer: Control Sheet  
Reference Asset: `control-sheet-preview.png`

Purpose:

- starlight
- cabin accents
- brightness
- night mode
- scene presets

Implementation target:

```text
ui/scenes/velvet_v0/control_sheets/lighting.sheet.yaml
```

### 10. Comfort Control Sheet

Layer: Control Sheet  
Reference Asset: `control-sheet-preview.png`

Purpose:

- seat heat levels
- comfort presets
- ambient mode
- future massage controls

Implementation target:

```text
ui/scenes/velvet_v0/control_sheets/comfort.sheet.yaml
```

### 11. Backroom Dashboard

Layer: Backroom / Technical Layer  
Reference Asset: `backroom-preview.png`

Purpose:

- module health
- system truth
- diagnostics
- receipts/logs
- vehicle/CAN status
- network/storage status
- safe restart/update tools
- emergency and override tools

Implementation target:

```text
ui/scenes/velvet_v0/scenes/backroom_dashboard.scene.yaml
```

Rules:

- readable first
- truthful first
- dangerous actions gated
- receipts/logs reachable
- guest mode restricted

### 12. Driving Mode Front Room

Layer: Front State / Driving Mode  
Reference Asset: `front-room-driving-mode.png`

Purpose:

- simplified moving-state interface
- fewer distractions
- obvious voice state
- visible emergency access
- visible mute/silent-listening control
- compact quick audio/climate
- read-only vehicle status

Allowed while driving:

- audio quick overlay
- climate quick overlay
- voice focus
- mute/silent listening
- emergency panel
- read-only vehicle summary

Restricted while driving:

- Backroom tools
- deep archive
- private/boudoir scene
- risky control sheets
- dangerous vehicle actions

Implementation target:

```text
ui/scenes/velvet_v0/states/driving.state.yaml
```

### 13. Warning / Emergency Front Room

Layer: Warning / Emergency State  
Reference Asset: `front-room-warning-mode.png`

Purpose:

- high-priority warning overlay
- emergency action path
- Backroom/emergency access
- clear acknowledge path
- safety hierarchy over visual beauty

Rules:

- warning/emergency overrides decoration
- emergency access must be unmistakable
- critical text must be readable
- dangerous actions require confirmation when appropriate
- alert remains visible until resolved or acknowledged according to safety policy

Implementation target:

```text
ui/scenes/velvet_v0/states/warning.state.yaml
ui/scenes/velvet_v0/panels/emergency.panel.yaml
```

## First Implementation Slice

Do not build every screen first.

Build one complete vertical path:

```text
Front Room Home
  -> Hearth / Climate Quick Overlay
    -> Climate Control Sheet
      -> Backroom Climate Diagnostics
```

This proves:

- image-backed front scene
- hotspot interaction
- contextual overlay
- control sheet
- Backroom entry
- state preservation
- safety path retention

## Implementation Boundary

The screen inventory describes visuals and UI structure.

It does not grant hardware authority.

UI actions must request work through approved Velvet interfaces:

- local API
- event bus
- capability system
- permission gate
- safety controller
- receipt/log system

Visual files must not directly control hardware.

## Completion Criteria

The Velvet v0 UI pack is ready for first implementation when:

- all reference assets exist
- Front Room hotspot map is reviewed
- first vertical slice is approved
- scene/hotspot/control-sheet YAML skeletons exist in `velvet-interface`
- emergency and Backroom paths are preserved
- driving mode restrictions are documented

## Final Rule

A screen can be beautiful.

A system must be reachable.

Safety must never be decorative.
