# Platform and signed catalogue status

_Last reviewed: 24 November 2026._

| Platform | Public stable | Distribution |
| --- | --- | --- |
| Android | [1.1.4 signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.4) | APK + SHA-256; AAB generated privately, Google Play rollout **not confirmed** |
| Windows | [1.1.4 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.4) | ZIP + SHA-256; unsigned executable, **no MSIX or Microsoft Store** |
| macOS | [1.1.4 universal portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.4) | ZIP + SHA-256; not Developer ID signed or notarized |
| iOS | Not published | iOS/iPadOS network destinations are profile references, not a native iOS application |

## Active signed network catalogue

**Version 6, 480 flows across 16 categories** is active on [network-flows.csv](../data/network/network-flows.csv) with its [Ed25519 manifest](../data/network/network-flows.manifest.json). Production app v1.1.3 adds dual verification: old public key for catalogues v1–v5, rotated public key for v6+. Previous v5 CSV and manifest are retained in Git history, not as alternate production filenames. App builds 1.1.2 and older will reject v6 and keep their last validated v5 cache/bundled defaults until upgraded.

For new Motorola, Crosscall, Samsung or other vendor flows, see [single-source CSV maintenance](../data/network/README.md). Shared Android Enterprise services belong to `device:android`, manufacturer destinations to `device:samsung`, `device:motorola` or `device:crosscall`; **Samsung Knox Manage** is an independent `mdm:knox-manage` platform. Server-side, portal, wildcard, regionally irrelevant and documentation-only records are not active client checks.

## Security and limits

Tests originate on the actual device running SystemCheck; a reachable TCP port does not validate OS compliance, MDM enrollment, push delivery or firmware availability. No OTA API POST or identifying payload is sent to the community-sourced Motorola CDS host. Optional Android Google Play Integrity uses the OVH verifier when initiated. The app does not automatically upload diagnostic results. User-selected local CSV imports are not cryptographically authenticated.

Maintain historical stable releases and checksums for rollback; do not revive deprecated MSIX or claim a Google Play rollout from GitHub publication.

## Diagnostic reliability release 1.1.4

Android, macOS and Windows 1.1.4 GitHub binaries have been verified on the public support releases. Android 1.1.4 was also published with signed APK and SHA-256 after passing CI validation; its AAB is available privately for Play Console submission. Google Play rollout remains unconfirmed. The release deduplicates shared Android/OEM probes, skips misapplied Google REST API push-port probes, treats TCP timeouts and TLS handshake failures as inconclusive warnings, recognizes TLS-verified HTTP 4xx as network-reachable and includes the verified network catalogue version in exported reports. The signed canonical v6 catalogue and its Ed25519 signature remain unchanged.
