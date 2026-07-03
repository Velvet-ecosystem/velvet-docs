# Custom UI Skin Guide

Status: Draft  
Applies To: Velvet UI Packs  
Companion To: Velvet v0 Official UI Pack  
Purpose: Help builders create their own visual styles without breaking Velvet's interface structure, safety paths, or system doctrine.

## Purpose

The Custom UI Skin Guide explains how builders can create alternative visual styles for Velvet-based systems.

The official Velvet v0 UI Pack uses a gothic library, boudoir, and graveyard visual language. That style belongs to Velvet's Tiburon build.

Other builders may want different visual identities:

- Cyberdeck
- Classic car
- Off-road expedition
- Work truck
- Medical mobility
- Home console
- Forge or workshop
- Industrial control room
- Minimal OEM-style retrofit

Custom skins are allowed and encouraged, but they must preserve Velvet's core interaction architecture.

A skin may change the room.

It may not change the exits, safety doors, or nervous system.

## Core Rule

Custom UI skins may change:

- Visual style
- Theme
- Scene artwork
- Icons
- Typography
- Ambient motion
- Object metaphors
- Color palette
- Scene names

Custom UI skins must preserve:

- Emergency access
- Backroom access
- Warning overlays
- Driving-mode simplification
- Offline/degraded state indication
- Touch-target usability
- System diagnostics path
- Receipt/log access where required
- Separation between pretty UI and governed system actions

The visual layer is not allowed to bypass safety, permissions, receipts, or local authority rules.

## Required Layer Model

Every custom skin must follow the Velvet layer model:

1. Front Scene
2. Contextual Overlay
3. Full Themed Scene
4. Control Sheet
5. Backroom / Technical Layer

The visual theme may change, but the structure must remain recognizable.

## Layer 1: Front Scene

The Front Scene is the default home screen.

It should be image-led and atmospheric. It may be beautiful, practical, playful, industrial, minimal, rugged, or clinical, depending on the builder's project.

The Front Scene should not become a cluttered app grid.

Required front-scene elements:

- Main background image or rendered scene
- Primary touch regions
- Voice/listening state
- Small status area
- Emergency access
- Backroom access
- Offline/degraded indicator
- Mute or silent-listening control

Recommended front-scene interaction style:

- Object-based touch regions
- Subtle glow points
- Hidden seams
- Framed cards
- Scene objects that represent system functions

Examples:

- Gramophone opens audio.
- Gauge cluster opens vehicle status.
- Tool wall opens workshop controls.
- Map table opens navigation.
- Medical monitor opens health/safety status.
- Server rack opens diagnostics.
- Window opens lighting or exterior mode.

## Layer 2: Contextual Overlay

Contextual overlays are small, temporary panels that appear above the Front Scene.

They are used for quick actions.

Examples:

- Audio quick card
- Climate quick card
- Lighting quick card
- Comfort quick card
- Vehicle summary card
- Security status card
- Recent memory/log card

Overlay requirements:

- Must remain readable.
- Must not hide emergency access unless emergency access is duplicated elsewhere.
- Must clearly show how to close or back out.
- Must not perform dangerous actions without confirmation.
- Must remain visually compatible with the skin.

## Layer 3: Full Themed Scene

Full Themed Scenes are deeper image-led spaces reached from the Front Scene.

Each full scene should represent a major functional area.

Examples by skin:

### Cyberdeck Skin

- Terminal room: system status
- Signal wall: communications
- Vault: logs and secrets
- Engine room: power and modules

### Classic Car Skin

- Analog dashboard: vehicle status
- Radio bench: audio
- Garage wall: maintenance
- Glovebox: settings and documents

### Off-Road Skin

- Map table: navigation
- Tool roll: recovery gear
- Campfire: comfort
- Convoy board: communications

### Medical Mobility Skin

- Calm cabin: home
- Guardian panel: medical status
- Route safety board: emergency pull-over state
- Care log: events and reports

### Forge / Workshop Skin

- Workbench: main scene
- CAD table: design files
- Printer bay: 3D printers
- Tool wall: machine controls
- Materials rack: inventory

Full scenes should still avoid becoming generic app pages unless the user intentionally enters a control or backroom layer.

## Layer 4: Control Sheet

Control Sheets provide precise controls.

They are allowed to use more obvious UI elements:

- Sliders
- Toggles
- Tabs
- Presets
- Lists
- Simple graphs
- Small buttons
- Input fields

Control sheets are where function starts to outrank atmosphere.

Required control-sheet qualities:

- Readable text
- Clear hierarchy
- Large enough touch targets
- Obvious active/inactive states
- Clear back/close behavior
- Safe confirmation for risky actions

Control sheets should still visually belong to the skin, but they should never sacrifice clarity for decoration.

## Layer 5: Backroom / Technical Layer

The Backroom is the technical layer.

This layer may use traditional dashboard layouts, diagnostic cards, tables, buttons, and logs.

Required backroom sections, where applicable:

- System dashboard
- Module health
- Vehicle/CAN status
- Power status
- Climate systems
- Audio routing
- Sensor status
- Network status
- Storage status
- Logs/receipts
- Permissions
- Update center
- Override tools
- Emergency tools

Backroom rules:

- Be direct.
- Be readable.
- Be honest.
- Show real system state.
- Separate ordinary controls from dangerous controls.
- Require confirmation or authentication where needed.
- Do not hide faults behind theme language.

The backroom is allowed to be less magical.

It must be more truthful.

## Required Safety Paths

Every custom UI skin must provide:

### Emergency Access

Emergency access must be visible or one direct gesture away.

It must not rely on solving a hidden visual puzzle.

### Backroom Access

Backroom access must exist from the Front Scene.

It may be styled as:

- Seam
- Keyhole
- Gear
- Tool mark
- Hidden edge tab
- Maintenance hatch
- Console switch

But it must be discoverable by the owner or documented clearly.

### Warning Overlay

Critical warnings must override the theme.

Warning overlays must be clear, high contrast, and direct.

### Driving Mode

When the vehicle is moving, the UI must simplify.

Driving mode may:

- Reduce animation
- Hide decorative controls
- Increase size of critical touch targets
- Restrict deep menus
- Prefer voice interaction
- Lock risky actions
- Prioritize alerts and safety state

### Guest Mode

Guest mode may restrict private scenes, owner memory, and technical controls.

Guest mode must not restrict safety access.

## Touch Target Rules

Touch regions must be practical on the target screen.

Guidelines:

- Primary touch regions should be large enough for finger use.
- Avoid tiny decorative targets for important functions.
- Critical functions must not depend on precision tapping.
- Hidden regions may exist, but safety functions must not be hidden-only.
- Overlapping touch regions must have clear priority.
- Hold actions should not trigger accidentally.
- Swipe gestures should have backup access where possible.

## Visual State Requirements

Each skin should define visual states for:

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

State changes should be visible but not distracting.

## Asset Requirements

A custom skin should provide:

```text
skin-name/
  README.md
  skin.yaml
  scenes/
    front_scene.yaml
    audio_scene.yaml
    climate_scene.yaml
    backroom_scene.yaml
  assets/
    backgrounds/
    overlays/
    icons/
    state_overlays/
  hotspot_maps/
    front_scene_hotspots.yaml
  docs/
    interaction_map.md
    safety_paths.md
```

Required asset types:

- Background images
- Hotspot maps
- Overlay definitions
- State overlays
- Icons or markers
- Backroom layouts
- Safety-state assets
- Optional animation assets

Recommended source resolution:

- 1920x1080 for 16:9 scenes
- 1280x720 minimum
- Export to target screen resolution as needed

## Skin Manifest

Each skin should include a `skin.yaml` manifest.

Example:

```yaml
skin:
  id: classic-garage
  name: Classic Garage
  version: 0.1.0
  author: Example Builder
  target_surfaces:
    - car_dashboard
  base_resolution:
    width: 1920
    height: 1080

requirements:
  emergency_access: true
  backroom_access: true
  driving_mode: true
  guest_mode: true
  warning_overlay: true

scenes:
  front:
    file: scenes/front_scene.yaml
  backroom:
    file: scenes/backroom_scene.yaml

safety:
  emergency_region: emergency
  backroom_region: maintenance_hatch
  mute_region: mute
```

## Hotspot Map

Hotspots should be declared separately from the artwork.

Example:

```yaml
scene: front_scene
base_resolution:
  width: 1920
  height: 1080

regions:
  - id: audio
    label: Audio
    type: polygon
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
    type: polygon
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
    type: edge
    action:
      tap: scene:backroom_dashboard
    edge: right

  - id: emergency
    label: Emergency
    type: rect
    action:
      tap: panel:emergency
    rect:
      x: 1720
      y: 920
      width: 160
      height: 120
```

## Accessibility and Readability

Custom skins must consider:

- Daylight readability
- Night readability
- Glare
- Color contrast
- Font size
- Touch size
- Driver distraction
- Motion sensitivity
- Color-only warnings

Warnings must not rely on color alone.

## Separation from System Authority

A skin does not control hardware directly.

A skin requests actions through approved Velvet interfaces:

- Local API
- Event bus
- Capability system
- Permission gate
- Receipt/log system
- Safety controller

The visual layer should never bypass:

- Owner permissions
- Safety checks
- Emergency rules
- Hardware arbitration
- Logging/receipts

## Submission Requirements

A builder skin should include:

- Skin manifest
- Scene list
- Hotspot map
- Safety path documentation
- Screenshots or preview images
- Driving-mode behavior
- Guest-mode behavior
- Known limitations
- License information
- Asset source notes

For community or lab submission, the skin should also include:

- No secrets
- No copyrighted assets without permission
- No unsafe control shortcuts
- No hidden emergency blockers
- No direct hardware calls from visual scenes

## Review Checklist

Before a skin is accepted, review:

- Does emergency access work?
- Does backroom access work?
- Are warnings readable?
- Is driving mode simplified?
- Are touch regions usable?
- Are dangerous actions gated?
- Are receipts/logs reachable?
- Is the UI separated from hardware control?
- Does the skin provide required assets?
- Does the theme stay consistent?
- Does it avoid clutter on the front scene?

## Examples of Valid Skin Directions

### Velvet v0 Front Room

Gothic library, boudoir, graveyard, warm amber, burgundy, gold, image-led objects.

### Cyberdeck

Dark terminal room, glowing cables, signal maps, rack equipment, command panels.

### Classic Garage

Analog gauges, wooden workbench, chrome radio, parts shelf, old service manual.

### Overland Camp

Map table, lantern, tool roll, recovery board, tire pressure panel, route wall.

### Medical Guardian

Calm clinical cabin, soft blue-green status lights, clear warning hierarchy, medical log panel.

### Foundry / Workshop

CAD bench, printer bay, material rack, tool wall, job queue, machine status.

### Home Console

House parlor, security wall, media room, kitchen status, workshop door, family-safe mode.

## Non-Goals

A custom skin is not:

- A shortcut around safety
- A direct hardware controller
- A random wallpaper pack
- A pile of buttons with a background image
- A replacement for the backroom
- A way to hide warnings or emergency access

## Final Rule

The skin may wear any costume.

The skeleton must remain Velvet.
