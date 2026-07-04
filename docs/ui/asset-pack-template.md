# UI Asset Pack Template

Status: Draft  
Applies To: Velvet UI Packs  
Reference Pack: Velvet v0 Front Room  
Purpose: Define the recommended file structure, naming pattern, required metadata, and minimum documentation for a Velvet-compatible UI pack.

## Purpose

A Velvet UI pack is more than a collection of background images.

A valid UI pack must include artwork, scene definitions, hotspot maps, state overlays, safety paths, and documentation that explains how the skin behaves.

This template gives builders a standard structure so UI packs can be reviewed, tested, shared, and eventually implemented without becoming a glitter drawer full of mystery files.

## Related Documents

```text
docs/ui/README.md
docs/ui/official-ui-pack.md
docs/ui/scene-layer-model.md
docs/ui/velvet-v0-screen-inventory.md
docs/ui/front-room-hotspot-map.md
docs/ui/custom-ui-skin-guide.md
assets/ui/velvet-v0/README.md
```

## Reference Implementation

The official Velvet v0 reference pack lives here:

```text
assets/ui/velvet-v0/
```

Its current reference assets are:

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

Use `velvet-v0-screen-inventory.md` to see how the reference assets map to screens, states, and implementation targets.

## Core Principle

Artwork is not enough.

Every visual scene must have a usable map, a safety path, and a declared relationship to the Velvet layer model.

## Recommended Directory Structure

```text
skin-name/
  README.md
  skin.yaml
  CHANGELOG.md
  LICENSE

  docs/
    interaction-map.md
    safety-paths.md
    driving-mode.md
    guest-mode.md
    asset-sources.md
    known-limitations.md

  scenes/
    front.scene.yaml
    audio.scene.yaml
    climate.scene.yaml
    comfort.scene.yaml
    lighting.scene.yaml
    archive.scene.yaml
    backroom.scene.yaml
    emergency.scene.yaml

  hotspot_maps/
    front.hotspots.yaml
    audio.hotspots.yaml
    climate.hotspots.yaml
    comfort.hotspots.yaml
    lighting.hotspots.yaml
    archive.hotspots.yaml
    backroom.hotspots.yaml

  overlays/
    audio.overlay.yaml
    climate.overlay.yaml
    comfort.overlay.yaml
    vehicle.overlay.yaml
    archive.overlay.yaml
    emergency.overlay.yaml

  control_sheets/
    audio.sheet.yaml
    climate.sheet.yaml
    lighting.sheet.yaml
    comfort.sheet.yaml
    vehicle.sheet.yaml
    presets.sheet.yaml

  assets/
    backgrounds/
      front.png
      audio.png
      climate.png
      comfort.png
      lighting.png
      archive.png
      backroom.png

    state_overlays/
      idle.png
      listening.png
      speaking.png
      thinking.png
      guest_mode.png
      driving_mode.png
      warning.png
      emergency.png
      offline.png
      degraded.png
      sleep.png

    icons/
      emergency.svg
      mute.svg
      backroom.svg
      warning.svg
      offline.svg
      healthy.svg
      caution.svg

    panels/
      card_audio.png
      card_climate.png
      card_comfort.png
      card_vehicle.png

    animations/
      README.md

  previews/
    front-preview.png
    overlay-preview.png
    scene-layer-preview.png
    control-sheet-preview.png
    backroom-preview.png
```

A small pack does not need every optional file, but it must include the required safety and interaction files.

## Minimum Required Files

A minimally reviewable skin pack must include:

```text
skin-name/
  README.md
  skin.yaml
  docs/
    interaction-map.md
    safety-paths.md
  scenes/
    front.scene.yaml
    backroom.scene.yaml
  hotspot_maps/
    front.hotspots.yaml
  assets/
    backgrounds/
      front.png
    state_overlays/
      warning.png
      emergency.png
      offline.png
```

A pack without emergency, Backroom, warning, and offline handling is not complete.

## Naming Rules

Use predictable names.

Recommended patterns:

- Scene definitions: `name.scene.yaml`
- Hotspot maps: `name.hotspots.yaml`
- Overlay definitions: `name.overlay.yaml`
- Control sheets: `name.sheet.yaml`
- Backgrounds: `name.png`
- State overlays: `state_name.png`
- Preview images: `purpose-preview.png`

Avoid names such as:

- `final.png`
- `final_final.png`
- `newscreen2.png`
- `coolone.png`
- `test_ui_real_use_this_one.png`

Mystery names are how future builders get bitten.

## `skin.yaml` Manifest

Every pack should include a `skin.yaml` file at the root.

Example:

```yaml
skin:
  id: velvet-v0-front-room
  name: Velvet v0 Front Room
  version: 0.1.0
  status: draft
  author: Velvet AI Ecosystem
  description: Image-led gothic library/parlor UI pack for the Tiburon v0 build.

compatibility:
  velvet_ui_pack_version: 0.1
  target_surfaces:
    - car_dashboard
  target_aspect_ratios:
    - "16:9"
  base_resolution:
    width: 1920
    height: 1080
  minimum_resolution:
    width: 1280
    height: 720

required_paths:
  emergency_access: true
  backroom_access: true
  mute_access: true
  warning_overlay: true
  offline_indicator: true
  driving_mode: true
  guest_mode: true

entrypoints:
  front_scene: scenes/front.scene.yaml
  backroom_scene: scenes/backroom.scene.yaml
  emergency_panel: overlays/emergency.overlay.yaml

regions:
  emergency_region: emergency
  backroom_region: backroom
  mute_region: mute

permissions:
  dangerous_actions_require_confirmation: true
  hardware_actions_use_capabilities: true
  receipts_required_for_control_actions: true

assets:
  backgrounds: assets/backgrounds
  state_overlays: assets/state_overlays
  icons: assets/icons
  previews: previews
```

## Scene File Template

A scene file describes one image-backed scene and the assets it uses.

Example:

```yaml
scene:
  id: front
  name: Front Room
  layer: front_scene
  background: assets/backgrounds/front.png
  hotspot_map: hotspot_maps/front.hotspots.yaml
  base_resolution:
    width: 1920
    height: 1080

transitions:
  enter: fade
  exit: fade
  duration_ms: 250

status_overlays:
  idle: assets/state_overlays/idle.png
  listening: assets/state_overlays/listening.png
  speaking: assets/state_overlays/speaking.png
  warning: assets/state_overlays/warning.png
  emergency: assets/state_overlays/emergency.png
  offline: assets/state_overlays/offline.png

allowed_modes:
  parked: true
  driving: true
  guest: true
  maintenance: false

fallbacks:
  missing_background: solid_black
  missing_state_overlay: text_status
  failed_scene_load: backroom_scene
```

## Hotspot Map Template

Hotspots define where the user can touch and what each interaction requests.

Example:

```yaml
scene: front
base_resolution:
  width: 1920
  height: 1080

regions:
  - id: audio
    label: Audio
    description: Gramophone audio/media touch region.
    type: polygon
    priority: normal
    action:
      tap: overlay:audio_quick
      hold: scene:audio_full
    polygon:
      - [120, 610]
      - [360, 570]
      - [430, 760]
      - [150, 810]

  - id: climate
    label: Climate
    description: Hearth / cabin warmth touch region.
    type: polygon
    priority: normal
    action:
      tap: overlay:climate_quick
      hold: sheet:climate_controls
    polygon:
      - [780, 520]
      - [1120, 520]
      - [1150, 760]
      - [760, 760]

  - id: backroom
    label: Backroom
    description: Maintenance seam.
    type: edge
    priority: high
    action:
      tap: scene:backroom_dashboard
    edge: right

  - id: emergency
    label: Emergency
    description: Safety access region.
    type: rect
    priority: critical
    action:
      tap: panel:emergency
    rect:
      x: 1720
      y: 920
      width: 160
      height: 120
```

## Overlay Template

Overlays are quick interaction cards that appear above a scene.

Example:

```yaml
overlay:
  id: climate_quick
  name: Climate Quick Card
  layer: contextual_overlay
  anchor_region: climate
  style: black_glass
  close_behavior: tap_outside_or_back

controls:
  - id: target_temperature
    type: slider
    label: Target Temp
    min: 16
    max: 30
    unit: celsius
    action: request:climate.set_target_temperature

  - id: fan_speed
    type: segmented
    label: Fan
    options: [0, 1, 2, 3, 4, 5]
    action: request:climate.set_fan_speed

  - id: deeper_controls
    type: button
    label: More
    action: sheet:climate_controls

safety:
  hides_emergency_access: false
  dangerous_actions: false
```

## Control Sheet Template

Control sheets are practical panels for precise control.

Example:

```yaml
sheet:
  id: climate_controls
  name: Climate Controls
  layer: control_sheet
  background_behavior: dim_scene
  close_behavior: back_or_close_button

sections:
  - id: temperature
    title: Temperature
    controls:
      - id: target_temperature
        type: slider
        min: 16
        max: 30
        unit: celsius
        action: request:climate.set_target_temperature

  - id: fan
    title: Fan
    controls:
      - id: fan_speed
        type: segmented
        options: [0, 1, 2, 3, 4, 5]
        action: request:climate.set_fan_speed

  - id: presets
    title: Presets
    controls:
      - id: warm_cabin
        type: preset
        label: Warm Cabin
        action: request:preset.apply
        payload:
          preset_id: warm_cabin

safety:
  requires_parked_for_deep_settings: true
  emergency_access_visible: true
```

## Backroom Scene Template

The Backroom is allowed to be more direct and technical.

Example:

```yaml
scene:
  id: backroom_dashboard
  name: Backroom Dashboard
  layer: backroom
  background: assets/backgrounds/backroom.png
  base_resolution:
    width: 1920
    height: 1080

sections:
  - module_health
  - vehicle_status
  - climate_systems
  - audio_routing
  - storage_network
  - logs_receipts
  - override_tools

access:
  owner_only: true
  guest_allowed: false
  requires_auth_for_dangerous_actions: true

safety:
  emergency_access_visible: true
  dangerous_actions_confirmed: true
  receipts_required: true
```

## Required Documentation

### `README.md`

The pack README should explain:

- What the skin is
- Target device or environment
- Visual style
- Included scenes
- Required safety paths
- How to preview it
- Known limitations

### `docs/interaction-map.md`

This document should explain what each major object or region does.

It should include:

- Front scene region list
- Tap behavior
- Hold behavior
- Swipe behavior, if used
- Overlay targets
- Full scene targets
- Backroom path
- Emergency path

### `docs/safety-paths.md`

This document should explain:

- Where emergency access lives
- Where Backroom access lives
- How warnings appear
- How offline/degraded state appears
- What changes in driving mode
- What changes in guest mode
- Which actions require confirmation

### `docs/asset-sources.md`

This document should list:

- Original asset sources
- Licenses
- Generated assets
- Modified assets
- Font licenses, if applicable
- Attribution requirements

Do not include proprietary or unlicensed assets in a public skin pack.

## Required Visual States

Each skin should define how these states appear:

- Idle
- Listening
- Speaking
- Thinking/processing
- Offline/local
- Guest mode
- Driving mode
- Warning
- Emergency
- Degraded hardware
- Backroom active
- Sleep/shutdown

If a skin cannot provide a custom image for a state, it must provide a fallback text/status overlay.

## Safety Review Checklist

Before a pack is accepted, verify:

- Emergency access is visible or one direct gesture away.
- Backroom access exists from the front scene.
- Mute or silent-listening access exists.
- Warning state overrides the theme.
- Offline/degraded state is visible.
- Driving mode simplifies the UI.
- Guest mode does not expose private or technical areas.
- Dangerous actions require confirmation.
- Hardware actions go through approved capability/event paths.
- Logs or receipts are reachable where required.
- Touch targets are practical on the target display.
- Critical controls do not require precision tapping.
- Fonts and contrast are readable.
- Motion is not distracting while driving.

## Implementation Notes

A UI pack should never directly control hardware.

Scene actions should request behavior through approved system interfaces such as:

- Local API
- Event bus
- Capability system
- Permission gate
- Safety controller
- Receipt/log system

The pack is the face and hands of the interface.

The governed system remains the nervous system underneath.

## Final Rule

If a skin looks beautiful but loses emergency access, it fails.

If a skin looks clever but bypasses safety, it fails.

If a skin changes the costume while preserving the skeleton, it belongs in Velvet's workshop.
