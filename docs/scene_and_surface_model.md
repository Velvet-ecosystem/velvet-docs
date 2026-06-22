# Scene and Surface Model

Velvet's interface is organized as scenes inhabiting surfaces, not as one generic dashboard stretched across every body.

## Scenes

A scene is a contextual room of interaction. It may be expressive, hidden, body-aware, passenger-aware, or purpose-specific.

Examples include:

- primary dashboard scenes
- lighting and comfort scenes
- maintenance scenes
- home-room scenes
- mobile companion scenes
- maker and foundry scenes

Scenes may display state and route structured intent. They do not directly actuate hardware.

## Surfaces

A surface is the concrete body where a scene appears, such as:

- vehicle display
- desktop window
- mobile screen
- home panel
- workshop terminal
- small auxiliary display

Rendering details belong to the surface implementation. Scene meaning should remain portable.

## Widgets

Widgets are bounded reusable elements embedded within scenes.

Observation widgets accept sanitized state and remain display-only. Interactive widgets may propose intent through approved routes, but they may not select executors or invoke hardware directly.

## Passenger and Context Awareness

The same scene may present differently according to verified context:

- owner present
- guest present
- no passenger
- parked
- driving
- maintenance ceremony active
- emergency state

Context may change tone, visibility, privacy, and available requests. It does not bypass authority.

## Hidden Paths

Hidden maintenance scenes are permitted, but obscurity is not security.

Deep identity, authority, naming, wake-phrase, and protected administration controls must still require the appropriate physical ceremony, policy checks, and receipts.

## Canonical Boundary

```text
scene or widget
  -> structured request
  -> Runtime route
  -> Court and safety checks
  -> approved executor
```

A scene may feel alive without becoming an unbounded hardware controller.
