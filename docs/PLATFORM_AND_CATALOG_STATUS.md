# Platform and network catalogue status

_Last reviewed: 23 November 2026._

## Current public distribution

**Android 1.0.9 (build 34)** is the current packaged release: see [GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.0.9). Publishing a GitHub APK does not itself complete Play Console review or Google Play rollout. There are **no released native Windows or macOS packages**.

| Platform | Current state | Intended delivery |
| --- | --- | --- |
| Android | Released 1.0.9 (build 34) | Google Play AAB; signed public APK |
| Windows | [Merged private PR #22](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/22); desktop foundation built, no Store release | Microsoft Store MSIX plus portable Windows x64 ZIP |
| macOS | Proposed, not yet implemented | GitHub ZIP with a .app (Apple Silicon and Intel), optional user-scope PKG; no paid Apple Developer program |
| Remote network catalogue | Reference data on public GitHub, **not consumed automatically by released app** | Future signed manifests, verified downloads, offline cache/fallback |
| Manual network CSV import | [Merged private PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25), Android 1.1.0 build 35 source; public APK availability unverified | User-selected local CSV, validation, confirmation, persistence and rollback |

Windows/macOS/iOS **profile names inside Android** identify network services that can be tested *from the Android device*. They do not indicate native desktop/mobile binaries are already available.

**Source handoff:** Android **1.1.0 (build 35)** has been merged into the private repository with a stable Android release workflow marker. A new signed public APK and Google Play rollout are distinct steps and must be confirmed separately.

## CSV reference catalogue

The public [network-flows.csv](../data/network/network-flows.csv) contains **225 contextual records**. It is managed and schema-validated by GitHub Actions; it is **not** a complete vendor firewall allowlist.

- Use the full published header, unchanged field order and UTF-8 encoding.
- `execution_point=MDM_SERVER` destinations are not to be presented as originating from a managed device.
- `testability` and regional/vendor constraints apply; not every row is a probe.
- The upcoming manual importer does not authenticate a file's origin, even when its format is valid.
- Automatic updates require a signed manifest, client-pinned verification key, anti-rollback/version validation and a verified local/offline fallback; SHA-256 by itself does **not** authenticate origin.

## Privacy, permissions and hosting

Network checks run directly from the device. Diagnostic results, settings and the planned manually imported CSV are stored locally, without automatic diagnostic uploads. Outbound DNS/HTTP/TCP and UDP probes disclose normal connection metadata to selected network destinations.

**OVH is used solely for optional Android Google Play Integrity verification** at `https://api.mdm.ivanboi.fr/verify`. The main app does not depend on OVH for its catalogue, results, VirusTotal or user support.

The planned unsigned/unnotarized macOS ZIP/APP or PKG may be blocked by Gatekeeper or company security policy. Installation or execution without administrator privileges cannot be guaranteed for managed computers.

## Versioning and support

Application versions and GitHub network catalogue revisions are independent. Documentation changes do not constitute a new binary release. Report problems through [GitHub Issues](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose); do not post secrets or internal network exports publicly.
