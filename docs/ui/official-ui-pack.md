# Velvet v0 Official UI Pack

Status: Draft  
Pack Name: Velvet v0 Front Room  
Primary Target: 2008 Hyundai Tiburon  
Interface Mode: Image-led scene UI  
Owner: Velvet AI Ecosystem

## Purpose

The Velvet v0 Official UI Pack defines the first complete visual language for Velvet's in-car screen.

This pack is not a generic dashboard skin. It is the reference implementation for an image-led, scene-based automotive interface where the visible screen feels like a living environment rather than an app grid.

The official v0 interface uses a gothic library, parlor, boudoir, and graveyard visual language to represent Velvet's front-facing presence, memory, comfort, safety, and maintenance layers.

## Design Principle

Velvet's main screen is a place, not a menu.

The user should feel they have entered Velvet's room. Controls are discovered through objects in the environment, subtle touch points, contextual overlays, and deeper backroom layers.

Large button grids are avoided on the front scene. Button-style controls are allowed deeper in the interface where clarity, safety, diagnostics, or precision matter.

## Layer Model

The official UI pack follows five layers:

1. Front Room / Main Living Scene
2. Contextual Overlay Layer
3. Full Themed Scene Layer
4. Control Sheet Layer
5. Backroom / Technical Layer

Each layer has a different purpose and a different level of visual abstraction.

## Layer 1: Front Room / Main Living Scene

The Front Room is Velvet's default home screen.

It is image-led and nearly buttonless. It contains the main visual scene, subtle touch targets, status hints, emergency access, voice/listening state, and the backroom seam.

Primary visual elements:

- Gothic library / parlor
- Fireplace / hearth
- Gramophone
- Bookshelves and ladder
- Armchair or chaise
- Moonlit window
- Graveyard or night exterior
- Boudoir/private alcove
- Subtle microphone sigil
- Backroom seam or keyhole
- Emergency mark

Primary interaction zones:

- Gramophone: audio and media
- Fireplace / hearth: climate and cabin warmth
- Bookshelf / ladder: archive, memory, recall
- Window / moon: lighting, night mode, exterior ambience
- Armchair / comfort point: seat comfort and mood presets
- Boudoir threshold: private owner comfort scene
- Vehicle point: system status, diagnostics, drive information
- Microphone sigil: conversation and listening state
- Backroom seam: maintenance and advanced controls
- Emergency point: safety access
- Mute point: silent listening or microphone mute

## Layer 2: Contextual Overlay Layer

Contextual overlays appear above the Front Room without fully leaving the scene.

They are used for quick interaction and lightweight adjustments.

Examples:

- Audio card near the gramophone
- Climate card near the hearth
- Comfort card near the armchair or boudoir threshold
- Vehicle status card near the vehicle point
- Archive preview card near the bookshelf

Overlay rules:

- The room remains visible behind the overlay.
- Panels should look like black glass, smoked glass, framed cards, or candlelit plates.
- Text must remain readable.
- Controls may include small sliders, selectors, and quick buttons.
- Overlays should not become full dashboards.

## Layer 3: Full Themed Scene Layer

Full themed scenes are deeper image-led environments opened from the Front Room.

Official v0 themed scenes:

### Library Home

The main return point and default identity scene.

Purpose:

- Home state
- System presence
- Listening
- Primary navigation

### Boudoir Comfort

A private comfort and owner-mode scene.

Purpose:

- Seat comfort
- Cabin mood
- Warmer/private state
- Owner-only interaction zones
- Deeper comfort presets

### Graveyard Archive

A memory, sleep, shutdown, and archive scene.

Purpose:

- Archived memories
- Retired modules
- Continuity history
- Shutdown/sleep atmosphere
- Recovery paths
- Fault isolation metaphor

The graveyard scene should not imply danger by default. It represents memory, rest, and old states.

## Layer 4: Control Sheet Layer

Control sheets are practical UI panels used for precise adjustments.

They may include:

- Sliders
- Toggles
- Segmented controls
- Preset chips
- Tabs
- Small buttons
- Status labels
- Simple graphs

Control sheets are still visually themed, but function takes priority over atmosphere.

Official first control sheets:

- Audio
- Climate
- Lighting
- Comfort
- Vehicle summary
- Presets
- Automations

The Control Sheet Layer may dim the background scene to improve readability.

## Layer 5: Backroom / Technical Layer

The Backroom is the technical and maintenance area.

This layer is allowed to use clearer button-style layouts because the user is no longer in the cinematic front room. The goal is clarity, safety, and maintenance.

Backroom sections:

- Dashboard
- Module health
- Vehicle / CAN status
- Climate systems
- Audio routing
- Storage / network
- Logs / receipts
- Tools / overrides
- Update center
- Settings
- Emergency / override tools

Backroom rules:

- Must be readable.
- Must be honest.
- Must prioritize system state over visual drama.
- Must expose logs and receipts where appropriate.
- Must separate emergency actions from ordinary controls.
- Must require appropriate access for dangerous actions.

## Visual Identity

Official v0 palette:

- Black glass
- Deep burgundy
- Warm amber
- Muted gold
- Candlelight ivory
- Dark wood brown
- Moonlit blue-gray
- Emergency red
- Healthy system green
- Caution amber

Style references:

- Gothic library
- Victorian parlor
- Private boudoir
- Moonlit graveyard
- Antique gramophone
- Fireplace and candlelight
- Heavy red curtains
- Gold filigree
- Dark polished wood

## Typography

Recommended typography categories:

- Display title: gothic serif or blackletter-inspired
- Section labels: elegant serif
- System text: clean readable sans or restrained serif
- Warning text: high-contrast and direct

Typography rules:

- The front scene may use decorative type sparingly.
- Control sheets and backroom screens must prioritize readability.
- Critical warnings must not use overly decorative fonts.

## Motion and State

The official pack may use subtle motion cues:

- Candle flicker
- Fireplace glow
- Starlight shimmer
- Listening pulse
- Soft highlight on touch zones
- Curtain movement
- Breathing glow around active objects
- Slight room dimming during overlays

Motion rules:

- No distracting motion while driving.
- Emergency and warning states override ambient animation.
- Motion must never hide critical information.
- Touch feedback should be clear but not arcade-like.

## Required Safety Elements

Every official and custom UI pack must preserve:

- Emergency access
- Backroom access
- Mute or silent-listening control
- Warning overlay path
- Degraded/offline state indication
- Driver-safe simplified mode
- Technical diagnostics path
- Receipt/log access where applicable

Emergency access must never be hidden behind decorative discovery.

## Driving Mode

When the vehicle is moving, the UI should simplify.

Driving mode may:

- Reduce animation
- Hide nonessential controls
- Enlarge critical quick actions
- Restrict deep menu entry
- Prioritize voice interaction
- Prioritize safety overlays
- Reduce reading-heavy content

The image-led front scene may remain visible, but interaction should become safer and simpler.

## Guest Mode

When guest mode is active, the UI may remain visually similar but restrict private or owner-only areas.

Guest mode rules:

- Private boudoir access may be hidden, locked, or replaced.
- Owner-specific memory may be restricted.
- Technical backroom access may be restricted.
- Personality and spoken behavior may become more reserved.
- Safety and emergency access remain available.

## Asset Requirements

Each scene pack should provide:

- Clean background image
- Hotspot map
- Overlay definitions
- State overlays
- Warning state assets
- Driving-mode simplification rules
- Backroom entry point
- Emergency entry point

Recommended base resolution:

- 16:9 landscape
- 1280x720 minimum
- 1920x1080 preferred for source assets
- Export down to target screen as needed

## Implementation Direction

The official UI pack should be implemented through the Velvet scene system:

- Image-backed scenes
- Polygon touch regions
- Automatic scaling
- Scene transitions
- Contextual overlays
- Control sheets
- Technical backroom screens

The UI pack should remain separate from core system logic.

Visual scenes should call actions through approved events or local APIs rather than controlling hardware directly.

## Non-Goals

The official v0 UI pack is not:

- A generic Android head unit skin
- An app icon grid
- A cloud dashboard
- A button-first interface
- A replacement for safety controls
- A direct hardware-control layer

It is the visual and interaction layer above Velvet's governed system.

## Core Rule

The front room may be beautiful.

The backroom must be truthful.

The emergency path must be immediate.
