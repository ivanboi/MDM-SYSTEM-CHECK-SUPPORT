# Platform and network catalogue status

_Last reviewed: 23 November 2026._

## Microsoft Store registration and packaging status — 23 November 2026

The Windows application **MDM SystemCheck** is registered in Microsoft Partner Center with Store ID `9N9Z3PCL3MG1`. Its identity is `ivanbillyjean.MDMSystemCheck`, publisher `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A`, publisher display name `ivan_billyjean`, and package family name `ivanbillyjean.MDMSystemCheck_hgbzc83p2bnep`.

Windows is distributed primarily by [public GitHub portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1). Its checksum is published with the ZIP. The private MSIX is retained only for a possible Microsoft Store submission; no certified Store package or live listing is confirmed. The ZIP is not Authenticode signed; SmartScreen or corporate policies may block execution.

The **Android 1.1.0+35 signed APK and checksum are verified** in the public `v1.1.0` release. Flutter source is **1.1.1+36** and a private signed AAB from [CI run 45205709549](https://github.com/ivanboi/MDM-SYSTEM-CHECK/actions/runs/45205709549) is available for manual Google Play upload. No Android 1.1.1 public stable release or Play Console rollout has been confirmed. Windows and macOS 1.1.1 ZIPs are available publicly. Automatic GitHub CSV synchronization is not implemented.

## Verified current distribution and signing

[Windows 1.1.1](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) is publicly available as a portable ZIP and SHA-256, **without Authenticode signing**. [Android 1.1.0](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) contains the signed APK. The [signing guide](WINDOWS_SIGNING.md) documents trusted certificate choices and SmartScreen limitations. Historic stable binaries are retained.

## Current public distribution

Android **1.1.0 (build 35)** is merged in source and a [public v1.1.0 tag](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) exists; the signed APK and SHA-256 are now confirmed publicly available. Publishing a GitHub APK does not itself complete Play Console review or Google Play rollout. Windows ZIP distribution is configured independently of Android; A [public macOS 1.1.1 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.1) and its SHA-256 are **published and verified**. The app is **universal arm64 + x86_64**; Developer ID signing and notarization are not enabled.

| Platform | Current state | Intended delivery |
| --- | --- | --- |
| Android | Signed public APK 1.1.0 (build 35) and checksum verified; Play rollout separate | Google Play AAB; signed public APK |
| Windows | Public portable ZIP is the preferred GitHub release; Microsoft Store deferred | Microsoft Store MSIX plus portable Windows x64 ZIP |
| macOS | [Published universal 1.1.1 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.1), Intel and Apple Silicon, SHA-256 verified; not Developer ID signed/notarized | GitHub ZIP containing the .app; no Mac App Store or PKG publication |
| Remote network catalogue | Reference data on public GitHub, **not consumed automatically by released app** | Future signed manifests, verified downloads, offline cache/fallback |
| Manual network CSV import | [Merged private PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25), Android 1.1.0 signed public APK verified; available on Windows 1.1.1 and macOS 1.1.1 as well | User-selected local CSV, validation, confirmation, persistence and rollback |

Windows/macOS/iOS **profile names inside Android** identify network services that can be tested *from the Android device*. They identify remote target flows, not the platform executing the test. Native Windows and macOS desktop binaries are available; no native iOS app exists.

**Current handoff:** Android **1.1.0+35** has a verified signed public APK. The private signed **1.1.1+36 AAB** was generated separately, with no confirmed Play Console upload or rollout.

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

The released unsigned/unnotarized macOS ZIP containing the .app may be blocked by Gatekeeper or company security policy. Installation or execution without administrator privileges cannot be guaranteed for managed computers.

## Versioning and support

Application versions and GitHub network catalogue revisions are independent. Documentation changes do not constitute a new binary release. Report problems through [GitHub Issues](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose); do not post secrets or internal network exports publicly.
