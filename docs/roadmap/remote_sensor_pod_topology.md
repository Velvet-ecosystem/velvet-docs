# Remote Sensor Pod Topology

Future remote pods combine a camera, local microcontroller, auxiliary sensors, timestamping, health reporting, and remotely requestable reset behind one rugged connection where practical.

A pod is a small organ, not a dumb firehose. It preprocesses health and timing locally, preserves auxiliary-sensor isolation, reports link and error counters, and emits disconnect and reconnect receipts.

The shared link may carry power, video, and sensor data only when electrical, thermal, bandwidth, grounding, and failure analysis prove the arrangement suitable. Cable length, connector, shielding, strain relief, service access, and fallback behavior remain installation-specific.

Loss of an auxiliary sensor must not automatically remove the camera. Loss of the camera must not erase the pod's health report when a lower-bandwidth control path survives.
