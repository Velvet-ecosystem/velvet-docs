# Velvet v0 UI Assets

Status: Draft reference asset pack  
Applies To: Velvet v0 Official UI Pack

## Purpose

This folder holds the reference images and preview assets for the official Velvet v0 UI pack.

These images document the first Velvet v0 image-led interface direction: a gothic library / parlor / boudoir / graveyard UI language with layered interaction, object-based touch regions, practical control sheets, driving mode, warning mode, and a technical Backroom.

This folder is for documentation and reference assets. Final implementation assets may later move or duplicate into `velvet-interface`.

## Current Asset Set

The official reference set currently includes:

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

## Asset Roles

### `front-room-main.png`

Clean production-style Front Room home scene.

Use this to show the default image-led Velvet v0 home screen without large instructional labels.

### `front-room-touch-map.png`

Annotated builder/reference image showing major touch regions.

Use this for documentation, hotspot planning, and builder explanation. This is not intended as the production home screen.

### `front-room-overlay-demo.png`

Contextual overlay demonstration.

Use this to show how quick cards can appear over the Front Room while keeping the room visible behind the overlay.

### `scene-layer-preview.png`

Scene layer preview.

Use this to show the deeper themed scene concept, such as Library Home, Boudoir Comfort, Graveyard Archive, or related image-led sub-scenes.

### `control-sheet-preview.png`

Control Sheet Layer preview.

Use this to show practical widgets, sliders, presets, toggles, and readable controls while still preserving the Velvet visual language.

### `backroom-preview.png`

Backroom / technical layer preview.

Use this to show diagnostics, maintenance, modules, receipts, vehicle status, and technical truth.

### `front-room-driving-mode.png`

Driving-mode Front Room preview.

Use this to show how the Front Room simplifies while moving: fewer distractions, clearer voice state, quick climate/audio, read-only vehicle status, mute/silent listening, and visible emergency access.

### `front-room-warning-mode.png`

Warning/emergency Front Room preview.

Use this to show how safety overrides beauty: the room dims, warning hierarchy becomes dominant, emergency access is unmistakable, and the Backroom/emergency path remains clear.

## Related Documents

Primary docs:

```text
docs/ui/official-ui-pack.md
docs/ui/custom-ui-skin-guide.md
docs/ui/scene-layer-model.md
docs/ui/asset-pack-template.md
docs/ui/front-room-hotspot-map.md
```

The hotspot map document references several assets in this folder directly.

## Implementation Notes

- These images are documentation references, not direct hardware-control logic.
- UI scenes should request actions through approved Velvet interfaces.
- Safety, warning, emergency, and Backroom access must remain available regardless of visual style.
- The official Velvet v0 pack may be refined later, but this folder preserves the first complete visual direction.

## Upload Rules

When replacing or adding images, use exact lowercase filenames and avoid doubled extensions such as `.png.png`.

Windows users may need to disable hidden file extensions before renaming images.
