# Velvet v0 UI Assets

Status: Draft asset folder  
Applies To: Velvet v0 Official UI Pack

## Purpose

This folder holds the reference images and preview assets for the official Velvet v0 UI pack.

Git does not track empty folders, so this README exists to create the asset path before the final images are uploaded.

## Expected Images

Place the final images here using these exact filenames:

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

## Image Mapping

Recommended source-to-target mapping:

```text
gothic_parlor_with_cinematic_ui.png
→ front-room-main.png

gothic_parlor_with_interactive_touch_map.png
→ front-room-touch-map.png

velvet_library_with_gothic_ui_design.png
→ front-room-overlay-demo.png

gothic_velvet_themed_ui_concept_design.png
→ scene-layer-preview.png

gothic_velvet_control_room_interface.png
→ control-sheet-preview.png

velvet_v0_maintenance_dashboard_interface.png
→ backroom-preview.png
```

## Images Still Needed

These should be generated or designed later:

```text
front-room-driving-mode.png
front-room-warning-mode.png
```

## Notes

- `front-room-main.png` should be the clean production-style home scene.
- `front-room-touch-map.png` should be the annotated builder/reference image.
- `front-room-overlay-demo.png` should show contextual UI cards over the room.
- `scene-layer-preview.png` should show the deeper themed scene layer.
- `control-sheet-preview.png` should show practical controls and widgets.
- `backroom-preview.png` should show the technical/maintenance layer.

Final implementation assets may later move or duplicate into `velvet-interface`; this folder is for documentation and reference assets.
