# Retrofit Body Registry

Velvet may inhabit vehicles, rooms, workshops, mobile devices, and other bodies assembled from mixed hardware. The body registry records what exists, how it is connected, and how much trust it has earned.

## Registry Entry

A body component should record:

- stable component identity
- physical location
- electrical or network path
- sensor, observer, or actuator role
- discovery source
- verification state
- trust state
- owning executor
- safety gate requirements
- maintenance history

## Discovery Is Not Trust

```text
detected
  -> identified
  -> verified
  -> mapped
  -> approved
  -> available to bounded executor
```

A newly discovered relay, CAN node, camera, sensor, or actuator is not automatically authorized hardware.

## Observation and Actuation

Observation components may be admitted under read-only rules when their isolation is proven.

Actuation components require:

- explicit registry approval
- approved executor ownership
- matching safety gate
- bounded operating limits
- receipts
- physical kill or cancel paths where appropriate

## Retrofit Principle

Velvet should learn the body without inventing authority over it.

The registry is evidence about the body. Runtime policy decides what may be done with that evidence.
