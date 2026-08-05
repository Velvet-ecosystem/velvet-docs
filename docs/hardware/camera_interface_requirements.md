# Camera Interface Requirements

Every camera or remote vision pod declares:

- link-health and error counters
- supported cable length and transport limits
- local timestamp source and quality
- bounded reset or restart request
- behavior when auxiliary sensors fail
- optional raw stream and preferred fused output
- disconnect and reconnect receipt types
- power, thermal, mounting, grounding, and strain-relief notes
- privacy and retention policy

The default output to Queen is a fused observation plus health evidence. Raw video is optional and purpose-bound. A camera may degrade independently; one failed channel must not collapse the complete vision stack. Stale frames, reordered timestamps, frame drops, and silent-but-healthy reports are health failures.
