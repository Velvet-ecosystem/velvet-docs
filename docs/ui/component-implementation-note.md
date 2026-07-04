# UI Component Implementation Note

Status: Draft  
Applies To: Velvet v0 UI Pack  
Purpose: Explain how Velvet's reference images become working interface components.

## Purpose

The Velvet v0 UI images are design references, not the final working interface by themselves.

A reference image proves visual direction. A working UI needs live components, touch regions, state binding, safety rules, and calls through Velvet's governed system paths.

This note explains the split between:

- reference images
- reusable sliced assets
- live coded widgets
- configuration files
- local API / event requests

## Core Rule

Do not turn the whole UI into one flat picture.

Velvet may use image-led scenes, but the parts that change, respond, animate, or control real systems should be live interface elements.

A beautiful dead screen is not enough.

## Three Kinds of UI Assets

### 1. Reference Images

Reference images show the target look.

They are used for design review, documentation, and implementation guidance.

Examples:

```text
assets/ui/velvet-v0/front-room-main.png
assets/ui/velvet-v0/front-room-overlay-demo.png
assets/ui/velvet-v0/control-sheet-preview.png
assets/ui/velvet-v0/backroom-preview.png
```

New component/reference boards may include:

```text
overlay-card-climate-reference.png
overlay-card-audio-reference.png
overlay-card-comfort-reference.png
component-language-sheet.png
```

These should not be treated as the whole working UI.

### 2. Reusable Visual Assets

Reusable visual assets are small pieces that may be exported as PNG or SVG and drawn by the UI system.

Examples:

```text
glow-idle.png
glow-active.png
glow-warning.png
glow-private.png
listening-pulse.png
backroom-seam.png
emergency-marker.png
ornament-divider.svg
icon-close.svg
icon-back.svg
icon-warning.svg
```

These can be layered over live scenes and reused across overlays.

### 3. Live Coded Widgets

Live widgets are real UI components that display current state and accept input.

Examples:

```text
VelvetCard
VelvetButton
VelvetSlider
VelvetToggle
VelvetChip
VelvetTabs
VelvetStatusPill
VelvetWarningBadge
VelvetGlowPoint
```

These should be built in code or declarative UI definitions so they can react to system state.

## Why Controls Should Be Live

A flat image can show a temperature of `22°C`, but it cannot know the actual cabin target temperature.

A flat image can show a fan speed of `5`, but it cannot change fan speed.

A flat image can show a song title, but it cannot update when the track changes.

A flat image can show a warning, but it cannot respond to a real safety event.

Live widgets solve this.

## Example: Climate Overlay

The reference board may show:

```text
Climate
22°C
Fan 0 1 2 3 4 5
Warm Cabin
Quiet
Defog
```

The working overlay should bind those elements to real values:

```text
target_temperature -> climate.current_target_temperature
fan_speed          -> climate.current_fan_speed
mode               -> climate.airflow_mode
presets            -> preset.apply requests
```

Actions should request behavior through approved Velvet interfaces:

```text
request:climate.set_target_temperature
request:climate.set_fan_speed
request:climate.set_airflow_mode
request:preset.apply
```

The overlay does not directly control relays, fans, heaters, or hardware pins.

## Example Working Path

```text
Front Room: tap fireplace/hearth
  -> open climate_quick overlay
    -> user taps fan speed 3
      -> UI sends request:climate.set_fan_speed
        -> permission/capability check
          -> climate module handles action
            -> receipt/log is written
              -> overlay updates state
```

This proves the full chain without overbuilding the whole interface.

## Reference vs Working UI

| Thing | Reference Image | Working UI |
|---|---|---|
| Front room | `front-room-main.png` | image-backed scene with live hotspots |
| Touch map | `front-room-touch-map.png` | YAML/geometry regions with actions |
| Climate card | concept/reference image | live overlay with bound values |
| Slider | shown on design sheet | coded widget with value and callback |
| Glow point | shown on design sheet | reusable asset or animated component |
| Emergency marker | shown visually | always reachable safety panel trigger |
| Backroom | preview image | real diagnostics screen with actual state |

## Recommended Folder Split

For documentation/reference assets:

```text
assets/ui/velvet-v0/references/
  overlay-card-climate-reference.png
  overlay-card-audio-reference.png
  overlay-card-comfort-reference.png
  component-language-sheet.png
```

For reusable visual assets:

```text
assets/ui/velvet-v0/components/
  glow-idle.png
  glow-active.png
  glow-warning.png
  glow-private.png
  listening-pulse.png
  backroom-seam.png
  emergency-marker.png
  ornament-divider.svg
  icon-close.svg
  icon-back.svg
```

For implementation in `velvet-interface`:

```text
ui/scenes/velvet_v0/
  skin.yaml
  component_tokens.yaml
  scenes/
    front_room.scene.yaml
  hotspot_maps/
    front_room.hotspots.yaml
  overlays/
    climate_quick.overlay.yaml
    audio_quick.overlay.yaml
    comfort_quick.overlay.yaml
  control_sheets/
    climate.sheet.yaml
  components/
    velvet_card.py
    velvet_button.py
    velvet_slider.py
    velvet_chip.py
    velvet_toggle.py
    velvet_glow_point.py
```

## Component Tokens

Shared style values should live in one place so the UI stays consistent.

Example:

```yaml
colors:
  glass_black: "#090706"
  warm_gold: "#C49A5A"
  amber_glow: "#F0A23A"
  deep_burgundy: "#4A0F0B"
  warning_red: "#A3261D"
  ivory_text: "#E8D6B3"

radii:
  card: 22
  chip: 10
  button_circle: 44

borders:
  card_width: 1
  active_width: 1

effects:
  card_opacity: 0.86
  card_blur: true
  glow_soft: true
```

These values should shape cards, chips, buttons, sliders, glow points, and warning panels.

## First Implementation Slice

Start with one path:

```text
Front Room Home
  -> Hearth / Climate Quick Overlay
    -> Climate Control Sheet
      -> Backroom Climate Diagnostics
```

This proves:

- scene background
- hotspot mapping
- overlay opening
- live widget values
- approved API/event request
- safety boundary
- receipt/log path
- Backroom diagnostic depth

## Safety Requirements

Reference art may be atmospheric.

Working UI must preserve:

- emergency access
- Backroom access
- mute / silent listening access
- warning override
- driving-mode simplification
- permission gates
- logs / receipts
- readable state display

If a visual effect conflicts with safety, the visual effect loses.

## Final Rule

Use reference images to teach the style.

Use reusable assets to carry the style.

Use live widgets to make the system work.

Velvet's face may be painted, but her controls must breathe.
