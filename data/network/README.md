# Central network flow catalogue

The current catalogue contains 396 contextual flow records extracted from the current private Flutter source models. Repeated hostnames are intentional when the MDM context or originating device differs.

Columns: `id, category, name, host, port, protocol, execution_point, region, testability, purpose, reference`.

Only `execution_point=DEVICE` and `testability=testable` may be considered for active probes, subject to operating system and region applicability. Server-side flows, wildcard destinations and documentation-only records are reference-only. These records are **not** a complete or authoritative firewall allowlist: review the cited vendor guidance and tenant-specific requirements.

## Manual offline import (Android 1.1.0 public APK, Windows/macOS 1.1.1)

[Merged private app PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25) introduces an offline CSV picker and strict validation using this **exact header and column order**. The user chooses a CSV from device storage and approves its activation. Only categories present in the imported file override their built-in endpoints; all other categories continue using embedded endpoints. A local copy is retained across restarts and a **Restore bundled catalogue** action clears the override. Imports are limited to 1 MiB and 5,000 rows in the implemented importer.

For a manual fallback after GitHub becomes inaccessible, first obtain a trusted copy of [network-flows.csv](network-flows.csv) by an authorized method, transfer it to the device, then use **Network Flow Catalogue → Import CSV from device** in a verified 1.1.0 build. This feature does **not** exist in Android 1.0.9; it is available in the verified signed public Android 1.1.0+35 APK and Windows/macOS 1.1.1 releases. Manually supplied CSVs are *not cryptographically authenticated*; verify the source and review unusual destinations before activation.

**Migration status:** The applications still use their embedded Dart lists. This CSV is published for review and CI schema checks; runtime download and automatic activation are NOT implemented. A future release must validate a signed publication manifest, enforce allowed protocols and ports, preserve a bundled offline catalogue, and fall back to the last verified cache. Do not treat plain SHA-256 alone as proof of authenticity.

Never publish tenant secrets or private hostnames here. Changes should be reviewed by pull request.

## Android Enterprise source refresh (23 November 2026)

The 396-record catalogue incorporates the Google [Android Enterprise Network Requirements](https://support.google.com/work/android/answer/10513641?hl=en) device destinations, including Play services, account authentication, certificate validation, FCM/GCM messaging, connectivity checks, OEM-dependent OTA updates and Play Protect. `android.clients.google.com` was removed from all records. Wildcard families such as `*.googleapis.com` are represented by reference-only base-domain records with the wildcard explicitly retained in the name and purpose; a base-domain probe is **not** proof that wildcard children are reachable. The signed catalogue manifest is version **3**, published with the updated CSV. Clients with verified catalogue synchronization check the signed manifest during application use and retain their last verified local copy if GitHub is unavailable. Manual imports are untrusted and remain user-approved.
