# Platform and network catalogue status

_Last reviewed: 23 November 2026._

## Microsoft Store registration and packaging status — 23 November 2026

The Windows application **MDM SystemCheck** is registered in Microsoft Partner Center with Store ID `9N9Z3PCL3MG1`. Its identity is `ivanbillyjean.MDMSystemCheck`, publisher `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A`, publisher display name `ivan_billyjean`, and package family name `ivanbillyjean.MDMSystemCheck_hgbzc83p2bnep`.

The [private source PR #27](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/27) prepares an unsigned **Store-submission MSIX** (`1.1.0.0`, Windows x64) and validates its manifest identity. Windows build CI passed, but full PR validation and merging were still outstanding at the last check. **No Store-certified package, direct Store link or published Microsoft Store listing is confirmed.** Do not sideload the unsigned Store package as if it were a signed installer. A separate portable ZIP is available only when a build artifact is successfully uploaded and verified.

Android source is **1.1.0 (build 35)** and the public `v1.1.0` Git tag exists. **The presence of a tag does not prove signed APK/AAB asset availability or Play Store rollout.** CSV manual import was merged in [PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25); automatic GitHub CSV synchronization remains planned. Mac APP/PKG packaging has not been released.

## Current public distribution

Android **1.1.0 (build 35)** is merged in source and a [public v1.1.0 tag](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) exists; verify signed assets before considering it downloadable. Publishing a GitHub APK does not itself complete Play Console review or Google Play rollout. There are **no released native Windows or macOS packages**.

| Platform | Current state | Intended delivery |
| --- | --- | --- |
| Android | Source 1.1.0 (build 35); signed artifact availability not independently verified | Google Play AAB; signed public APK |
| Windows | Partner Center product `9N9Z3PCL3MG1` registered; [MSIX PR #27](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/27) in review, no Store release | Microsoft Store MSIX plus portable Windows x64 ZIP |
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
