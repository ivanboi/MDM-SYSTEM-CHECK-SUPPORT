# Central network flow catalogue

This initial catalogue contains 225 contextual flow records extracted from the current private Flutter source models. Repeated hostnames are intentional when the MDM context or originating device differs.

Columns: `id, category, name, host, port, protocol, execution_point, region, testability, purpose, reference`.

Only `execution_point=DEVICE` and `testability=testable` may be considered for active probes, subject to operating system and region applicability. Server-side flows, wildcard destinations and documentation-only records are reference-only. These records are **not** a complete or authoritative firewall allowlist: review the cited vendor guidance and tenant-specific requirements.

**Migration status:** The applications still use their embedded Dart lists. This CSV is published for review and CI schema checks; runtime download and automatic activation are NOT implemented. A future release must validate a signed publication manifest, enforce allowed protocols and ports, preserve a bundled offline catalogue, and fall back to the last verified cache. Do not treat plain SHA-256 alone as proof of authenticity.

Never publish tenant secrets or private hostnames here. Changes should be reviewed by pull request.
