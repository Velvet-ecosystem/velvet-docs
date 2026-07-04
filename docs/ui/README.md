# Velvet UI Documentation

Status: Draft  
Applies To: Velvet UI Packs  
Primary Reference Pack: Velvet v0 Front Room

## Purpose

This folder documents Velvet's image-led UI system.

The UI is not intended to be a generic button grid or a simple wallpaper pack. Velvet's screen is built as a layered scene system: a living front room, contextual overlays, deeper themed scenes, practical control sheets, and a truthful technical Backroom.

The official Velvet v0 pack uses a gothic library / parlor / boudoir / graveyard visual language for the Tiburon build. Other builders may create their own skins, but they must preserve Velvet's safety paths, layer model, diagnostics access, and governed system boundaries.

## Start Here

Read these in order:

1. `official-ui-pack.md`  
   Defines the official Velvet v0 visual direction and interaction doctrine.

2. `scene-layer-model.md`  
   Explains the standard layer stack: Front Scene, Contextual Overlay, Full Themed Scene, Control Sheet, and Backroom.

3. `front-room-hotspot-map.md`  
   Maps the official Velvet v0 Front Room into touch regions, actions, and draft hotspot YAML.

4. `velvet-v0-screen-inventory.md`  
   Lists the official v0 screens, states, reference assets, and implementation targets.

5. `custom-ui-skin-guide.md`  
   Explains how other builders can create their own visual styles without breaking Velvet's bones.

6. `asset-pack-template.md`  
   Defines the recommended file structure, manifests, hotspot maps, overlays, control sheets, and review materials for UI packs.

## Official Velvet v0 Asset Folder

Reference images live here:

```text
assets/ui/velvet-v0/
```

Current official reference assets:

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

Use the asset folder README for image roles and upload rules:

```text
assets/ui/velvet-v0/README.md
```

## Velvet v0 Layer Preview Map

| Layer | Doc / Asset | Purpose |
|---|---|---|
| Front Room | `front-room-main.png` | Clean production-style home scene |
| Touch Map | `front-room-touch-map.png` | Annotated builder/reference map |
| Contextual Overlay | `front-room-overlay-demo.png` | Shows quick cards over the room |
| Scene Layer | `scene-layer-preview.png` | Shows deeper themed scene concept |
| Control Sheet | `control-sheet-preview.png` | Shows practical widgets and presets |
| Backroom | `backroom-preview.png` | Shows diagnostics and technical layer |
| Driving Mode | `front-room-driving-mode.png` | Shows simplified moving-state UI |
| Warning Mode | `front-room-warning-mode.png` | Shows safety override state |

## Build Inventory

The official v0 build checklist lives here:

```text
velvet-v0-screen-inventory.md
```

Use it to track which screens, states, overlays, control sheets, and implementation targets belong to the first Velvet v0 UI pack.

## Core UI Doctrine

The Front Room may be beautiful.

The Backroom must be truthful.

The emergency path must be immediate.

A skin may change the room. It may not change the exits, safety doors, or nervous system.

## Implementation Boundary

UI packs define visuals, scenes, overlays, touch regions, and requested actions.

UI packs must not directly control hardware.

Approved UI actions should pass through Velvet's governed interfaces, such as:

- local API
- event bus
- capability system
- permission gate
- safety controller
- receipt/log system

## Next Implementation Target

After these docs are accepted, matching implementation skeletons should be created in `velvet-interface`:

```text
ui/scenes/velvet_v0/
  skin.yaml
  scenes/
  hotspot_maps/
  overlays/
  control_sheets/
```

The first implementation slice should be:

```text
Front Room Home
  -> Hearth / Climate Quick Overlay
    -> Climate Control Sheet
      -> Backroom Climate Diagnostics
```

This proves the whole layer model without trying to build every room at once.
