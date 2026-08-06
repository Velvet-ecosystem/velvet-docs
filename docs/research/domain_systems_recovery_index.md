# Domain Systems Recovery Index

Status: active archive reconstruction

Purpose: preserve the vehicle-OEM, home-automation, building, industrial, forge, and robotics systems that shaped Velvet outside the narrow AI-research trail.

This index is intentionally separate from the named-researcher index. A system may influence Velvet through practical engineering, user experience, safety behaviour, retrofit strategy, or domain architecture without being an AI research project.

## Evidence States

- `CONFIRMED_CHAT_REFERENCE`
- `CONFIRMED_ARCHIVE_REFERENCE`
- `NAME_MENTION_ONLY`
- `RECOVERY_CANDIDATE`
- `INTERNAL_DOMAIN_CONCEPT`
- `CONVERGENT_FAMILY`

Similarity does not establish historical influence. Unrecovered standards and products remain search candidates, not attributed sources.

# 1. Vehicle OEM and Retrofit Systems

## Driver Monitoring, Emergency Assist, and Minimal-Risk Stop Comparisons

The medical-mobility research trail explicitly compared or catalogued the following systems:

| OEM or system | Evidence state | Recovered Velvet use |
|---|---|---|
| **Volkswagen Emergency Assist** | `CONFIRMED_CHAT_REFERENCE` | Driver non-response, escalating intervention, slowing, stopping, and hazards |
| **Mercedes-Benz Active Emergency Stop Assist** | `CONFIRMED_CHAT_REFERENCE` | Driver incapacitation response and bounded minimum-risk stopping |
| **Mercedes-Benz Drive Pilot** | `CONFIRMED_CHAT_REFERENCE` | Operational-domain, driver-responsibility, and fallback comparison |
| **Mercedes DISTRONIC with Steering Assist** | `CONFIRMED_CHAT_REFERENCE` | Longitudinal and lateral assistance boundaries |
| **BMW Emergency Stop Assistant** | `CONFIRMED_CHAT_REFERENCE` | Emergency stop sequence and driver-state escalation |
| **BMW Highway Assistant / Driving Assistant Professional** | `CONFIRMED_CHAT_REFERENCE` | Highway-domain and supervision comparison |
| **GM Super Cruise** | `CONFIRMED_CHAT_REFERENCE` | Direct driver monitoring, mapped-road dependency, and hands-free operational domain |
| **Ford BlueCruise** | `CONFIRMED_CHAT_REFERENCE` | Driver monitoring and mapped-road operational domain |
| **Toyota / Lexus Teammate** | `CONFIRMED_CHAT_REFERENCE` | Driver-assistance handoff, supervision, and domain restrictions |
| **Nissan ProPILOT** | `CONFIRMED_CHAT_REFERENCE` | Lane and speed assistance with driver responsibility |
| **Subaru DriverFocus** | `CONFIRMED_CHAT_REFERENCE` | Camera-based attention and driver-state monitoring |
| **Volvo Pilot Assist** | `CONFIRMED_CHAT_REFERENCE` | Bounded steering and speed assistance |
| **Hyundai / Kia / Genesis Highway Driving Assist (HDA)** | `CONFIRMED_CHAT_REFERENCE` | OEM assistance relevant to the Tiburon-family ecosystem and modern Hyundai group behaviour |
| **Tesla Autopilot / FSD driver monitoring** | `CONFIRMED_CHAT_REFERENCE` | Driver-monitoring strengths, failure patterns, naming risk, and supervision expectations |
| **XPeng XNGP / P7+** | `CONFIRMED_CHAT_REFERENCE` | Broader advanced-driving-system comparison |
| **European eCall** | `CONFIRMED_CHAT_REFERENCE` | Emergency communications after a serious event |
| **comma.ai / openpilot** | `CONFIRMED_CHAT_REFERENCE` | Open-source retrofit precedent, user-installed hardware, supported-vehicle breadth, driver responsibility, and hacker-built vehicle augmentation |

## Recovered OEM Lessons

The archive identifies reusable OEM mechanisms:

- direct driver monitoring
- gaze and head-position monitoring
- hand-position or steering-engagement monitoring
- escalating alerts
- bounded steering and braking support
- automatic slowing and stopping after non-response
- hazard-light activation
- emergency communication
- mapped-road or operational-domain restrictions
- connected-service dependencies
- post-stop recovery and resumption rules

It also identifies gaps Velvet was designed to address:

- medical-event reasoning rather than generic attention scoring alone
- configurable medical profiles
- cross-sensor evidence
- voice, wearable, passenger, touch, and capacitive confirmation
- manual-transmission retrofit bodies
- older vehicles abandoned by OEM support
- local-first operation
- owner-held doctrine and receipts
- transparent uncertainty

## Vehicle Architecture and HMI Foundations

Confirmed archive references include:

- CAN
- OBD-II
- ECUs
- AUTOSAR
- Android Automotive OS
- Android Auto
- Apple CarPlay
- Qt
- PyQt5
- Kanzi
- SocketCAN
- python-can
- Linux
- AGL
- Yocto
- systemd
- MQTT
- Kafka

Early archive files already separate UI, CAN integration, voice, Decision, Court, Execution, Event Bus, and Execution Receipts. The current architecture should preserve that history rather than pretending Court appeared fully formed later.

## OEM-Control Archaeology

The older module archive contains state machines and intent for:

- remote start
- steering and steering control
- windows
- door locks
- trunk
- mirrors
- drive modes
- climate
- lighting
- seat heat
- steering heat
- audio and media
- OEM controls

These are evidence sources, not executable modules. Direct hardware paths remain quarantined until rebuilt behind Court and dedicated executors.

# 2. Home, Building, and Property Automation

## Internal Named Home Concepts

The following names are confirmed internal Velvet concepts from the home-automation design trail:

| Internal concept | Evidence state | Recovered role |
|---|---|---|
| **The Castle Wakes** | `INTERNAL_DOMAIN_CONCEPT` | Whole-home transition from rest into an inhabited, ready state |
| **The Living Floorplan** | `INTERNAL_DOMAIN_CONCEPT` | Spatially organized home state and interaction rather than a flat device list |
| **The Quiet Command** | `INTERNAL_DOMAIN_CONCEPT` | Low-friction, restrained control that avoids constant chatter |
| **The Threshold** | `INTERNAL_DOMAIN_CONCEPT` | Entry, identity, presence, greeting, security, and mode transition |
| **The Night Watch** | `INTERNAL_DOMAIN_CONCEPT` | Overnight security, perimeter awareness, quiet alerting, and protective presence |
| **The Conservatory of Quiet Things** | `INTERNAL_DOMAIN_CONCEPT` | Ambient, low-noise environmental awareness and gentle automation |
| **The Forge Connection** | `INTERNAL_DOMAIN_CONCEPT` | Shared home-to-workshop continuity, tools, environment, and safety |
| **The Master Surface** | `INTERNAL_DOMAIN_CONCEPT` | A unified owner-facing surface across home, vehicle, forge, and other bodies |

## Recovered Home Capabilities

The historical home concepts include:

- lighting and scene control
- fireplace state
- curtains and coverings
- doors and locks
- climate and air quality
- security and perimeter sensing
- energy awareness
- garage state
- vehicle arrival and departure
- owner and guest presence
- room-level context
- quiet overnight behaviour
- home, vehicle, and forge continuity

## Home Architecture Laws

- a room is not merely a collection of devices
- presence and identity evidence must remain separate from authority
- hidden interface locations are not authentication
- automation should be reversible and observable
- security events may interrupt ordinary silence but still require bounded authority
- fire, heating, locks, garage movement, and high-energy equipment require dedicated safety policy
- cloud integrations may be optional tools but cannot own the home body
- home scenes should share Event Protocol, Receipts, Riven, and World Logic with the vehicle body

## Named Home Platforms and Standards Still Needing Transcript Recovery

The current archive pass has not yet proven that any of the following were historically discussed:

- Home Assistant
- Matter
- Thread
- Zigbee
- Z-Wave
- Node-RED
- KNX
- BACnet
- Apple HomeKit
- Google Home
- Amazon Alexa smart-home APIs

These belong in the search queue only. They must not be listed as Velvet influences until the original transcript or file is recovered.

# 3. Industrial, Forge, and Building-Control Systems

## Confirmed Internal Industrial Scope

The interface archive explicitly includes:

- industrial HMI
- factory automation
- process control
- machine start and stop
- emergency stop
- status and diagnostics
- safety-critical interface notes
- multi-panel layouts
- fixed industrial control-station surfaces

This proves that Velvet's interface architecture was intended to travel beyond the car and home into machinery and industrial environments.

## Forge Scope

The forge body includes or anticipates:

- tool and machine presence
- power-state awareness
- environmental sensing
- ventilation and heat
- lighting
- security
- workpiece or project context
- hazardous-state warnings
- local cameras and microphones
- restricted machine-control requests
- owner-presence gates
- post-work shutdown and inspection

Forge automation should remain a body with explicit machine boundaries, not a generic smart-home extension.

## Industrial Safety Laws

- display state is not machine state
- emergency-stop UI is not a substitute for a physical safety circuit
- PLC or controller feedback must be distinguished from sensor-confirmed consequence
- machine commands require body, installation, session, route, and capability verification
- high-energy machinery should default to observation and proposal until dedicated executors and safety reviews exist
- network loss must not create unsafe motion
- local manual controls and hardwired safety systems remain authoritative where required
- receipts must preserve denied, interrupted, failed, and uncertain machine actions
- simulated process success does not prove safe physical control

## Industrial Standards and Platforms Still Needing Transcript Recovery

The current archive evidence does not yet prove historical discussion of:

- PLCs from a specific vendor
- SCADA products
- OPC UA
- Modbus
- EtherCAT
- PROFINET
- EtherNet/IP
- BACnet
- KNX
- IEC 61131-3
- IEC 61508
- ISA-95
- ROS-Industrial

These are high-priority search terms, not current attributions.

# 4. Robotics and Teleoperation

## Confirmed Archive Scope

The public interface work explicitly includes a robotics control surface with:

- movement pad
- arm control
- camera feeds
- emergency stop
- teleoperation
- drone-interface applicability

## Robotics Relationship to Unified-Organ AI

A robot body should use the same laws as vehicle, home, and forge bodies:

```text
observe
  -> model body and world state
  -> propose
  -> verify Runtime context
  -> authorize through Court
  -> execute through a bounded organ
  -> observe consequence
  -> receipt the result
```

## Robotics Systems Still Needing Transcript Recovery

The current archive pass has not yet proven historical discussion of:

- ROS or ROS 2
- MoveIt
- Gazebo / Ignition
- Webots
- Isaac Sim
- Open-RMF
- micro-ROS
- PX4
- ArduPilot

These are recovery candidates only.

# 5. Cross-Domain Architectural Result

Vehicle, home, industrial, forge, and robotics work are not side projects around an AI core.

They are the reason Velvet's architecture became:

- multi-body
- local-first
- event-driven
- capability-gated
- receipt-backed
- scene-based
- simulation-aware
- identity-conscious
- spatial and temporal
- gracefully degradable
- explicit about physical consequence

The same cognitive or memory mechanism may appear in every body, but each domain keeps its own installation identity, safety policy, executors, interfaces, and failure evidence.

# 6. Recovery Queue

## Vehicle OEM

1. Recover the original OEM comparison tables and scorecards.
2. Map each named system to direct source material.
3. Record what Velvet adopted, adapted, rejected, or found missing.
4. Link the findings to Temperance, Charlotte, driver monitoring, emergency communication, and retrofit-body doctrine.

## Home

1. Recover the original conversations for each named home concept.
2. Identify any named home platforms, standards, or commercial systems actually discussed.
3. Recover the home body registry, room model, energy, security, and garage paths.
4. Separate ambience, convenience, safety, and authority.

## Industrial and Forge

1. Recover machine and forge concepts from old chats and archive files.
2. Identify any named PLC, SCADA, protocol, safety-standard, or industrial-HMI references.
3. Recover resource, saturation, power, ventilation, and emergency-stop reasoning.
4. Preserve the difference between user-interface emergency controls and hardwired safety.

## Robotics

1. Recover any named robotics stacks, simulators, drones, or teleoperation systems.
2. Link robotics lessons to the Simulated Body and Cognitive Event Layer.
3. Record manipulator, mobility, perception, and emergency-stop boundaries separately.

# Current Correction

The provenance archive must cover the full Velvet ecosystem.

AI research is one shelf. Vehicle OEM engineering, retrofit culture, home automation, industrial control, forge safety, interface systems, and robotics are equally important shelves.