# Platform and signed catalogue status

_Last reviewed: 24 November 2026._

| Platform | Public stable | Distribution |
| --- | --- | --- |
| Android | [1.1.5 signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.5) | APK + SHA-256; AAB generated privately, Google Play rollout **not confirmed** |
| Windows | [1.1.5 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5) | ZIP + SHA-256; unsigned executable, **no MSIX or Microsoft Store** |
| macOS | [1.1.5 universal portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.5) | ZIP + SHA-256; not Developer ID signed or notarized |
| iOS | Not published | iOS/iPadOS network destinations are profile references, not a native iOS application |

## Active signed network catalogue

**Version 8, 507 flows across 18 categories** is active on [network-flows.csv](../data/network/network-flows.csv) with its [Ed25519 manifest](../data/network/network-flows.manifest.json). Production app v1.1.3 adds dual verification: old public key for catalogues v1–v5, rotated public key for v6+. App v1.1.5+41 adds parser support for two new categories (ChromeOS and Fairphone) introduced in v7. Previous v5 CSV and manifest are retained in Git history, not as alternate production filenames. App builds 1.1.2 and older will reject v6+. Apps 1.1.3 and 1.1.4 may verify v7/v8 signatures but cannot parse the categories introduced in v7 and will safely retain their last verified v6 cache or bundled defaults until upgrading to 1.1.5.

For new Motorola, Crosscall, Samsung or other vendor flows, see [single-source CSV maintenance](../data/network/README.md). Shared Android Enterprise services belong to `device:android`, manufacturer destinations to `device:samsung`, `device:motorola` or `device:crosscall`; **Samsung Knox Manage** is an independent `mdm:knox-manage` platform. Server-side, portal, wildcard, regionally irrelevant and documentation-only records are not active client checks.

## Security and limits

Tests originate on the actual device running SystemCheck; a reachable TCP port does not validate OS compliance, MDM enrollment, push delivery or firmware availability. No OTA API POST or identifying payload is sent to the community-sourced Motorola CDS host. Optional Android Google Play Integrity uses the OVH verifier when initiated. The app does not automatically upload diagnostic results. User-selected local CSV imports are not cryptographically authenticated.

Maintain historical stable releases and checksums for rollback; do not revive deprecated MSIX or claim a Google Play rollout from GitHub publication.

## Diagnostic reliability release 1.1.4

Android, macOS and Windows 1.1.4 GitHub binaries have been verified on the public support releases. Android 1.1.4 was also published with signed APK and SHA-256 after passing CI validation; its AAB is available privately for Play Console submission. Google Play rollout remains unconfirmed. The release deduplicates shared Android/OEM probes, skips misapplied Google REST API push-port probes, treats TCP timeouts and TLS handshake failures as inconclusive warnings, recognizes TLS-verified HTTP 4xx as network-reachable and includes the verified network catalogue version in exported reports. The signed canonical v6 catalogue and its Ed25519 signature remain unchanged.

## ChromeOS, Fairphone, Motorola and Crosscall in v1.1.5

The Motorola and Crosscall profile labels explicitly say **specific servers**. The Motorola `moto-cds.appspot.com:443` DNS and TCP probes both passed in the Android 1.1.4 5G CSV (44 ms, 32 ms); this does not query OTA update availability. Crosscall v8 contains two active maintainer-provided FOTA endpoints and two historical references. ChromeOS has 15 Google-documented device/enterprise/update destinations tested from the phone as network paths, **not** as verified Chromebook enrollment. Fairphone has two historical/shared endpoint references marked **documentation only**; none establish a modern Fairphone Gen. 6 OEM-specific OTA server. Select Android separately for common Google/Android Enterprise network requirements.

TLS problems explicitly reported by the OS are classified in 1.1.5 as hostname mismatch, expired/not-yet-valid certificate, untrusted chain or generic handshake error. The app does not bypass certificate validation and will not infer a particular certificate cause when the OS returns only a generic handshake failure.

## Verified stable release 1.1.5 (24 November 2026)

All three GitHub Actions release workflows completed successfully for source commit `a6fe9a5421be531a52267cd9a9624c2c34c2b26c` and uploaded production release assets with SHA-256 files: [Android signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.5), [Windows x64 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5), and [macOS universal ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.5). The Android 1.1.5 APK was installed and confirmed working by the maintainer. An AAB is available in the [successful private Android build](https://github.com/ivanboi/MDM-SYSTEM-CHECK/actions/runs/45342707315) for manual Play Console upload. **Google Play 1.1.5 publication is not confirmed and is maintainer-managed.**

The standalone ChromeOS and Fairphone entries are network-profile checks/reference data, **not** native ChromeOS/iOS applications or app-store publications. Windows remains unsigned (no MSIX / Microsoft Store), and macOS is not Developer ID signed or notarized.

## Catalogue v8 operational status

Catalogue v8 (24 November 2026): 507 records in 18 categories, published automatically with the existing Ed25519 key. Android confirmed verified GitHub catalogue v8 with zero manual entries. Windows/macOS runtime refresh and new OEM reachability tests remain pending. Four maintainer-provided Crosscall FOTA records (two active, two historical) and six Motorola additions (five active, one staging reference) are included. Carrier applicability varies. These are connectivity checks, not OTA transactions or independently verified vendor allowlists.
