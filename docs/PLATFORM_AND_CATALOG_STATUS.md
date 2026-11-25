# Platform and signed catalogue status

_Last reviewed: 25 November 2026._

| Platform | Current version | Distribution |
| --- | --- | --- |
| Android | 1.1.8+44 | Google Play submission in progress; availability not confirmed. [Historical public APK 1.1.6](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6). |
| Windows | [1.1.6 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6) | SHA-256; unsigned executable; no MSIX or Microsoft Store. |
| macOS | [1.1.6 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6) | SHA-256; not Developer ID signed or notarized. |
| Linux | [1.1.6 x64](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/linux-v1.1.6) | AppImage, DEB, TAR.GZ; OpenPGP-signed checksum manifest; runtime acceptance pending. |
| iOS | Not published | Network profile references only. |

Android 1.1.8 includes cumulative 1.1.7 security fixes and signed APK/AAB release-candidate MobSF scanning. Android 12 minimum; Android 17 runtime acceptance pending. The maintainer confirms Play submission is in progress on 25 November 2026. Detailed AAB findings review and automated regression gates remain pending.

## Active signed network catalogue

**Version 9, 522 flows across 18 categories** is active on [network-flows.csv](../data/network/network-flows.csv) with its [Ed25519 manifest](../data/network/network-flows.manifest.json). Production app v1.1.3 adds dual verification: old public key for catalogues v1–v5, rotated public key for v6+. App v1.1.5+41 adds parser support for two new categories (ChromeOS and Fairphone) introduced in v7. Previous v5 CSV and manifest are retained in Git history, not as alternate production filenames. App builds 1.1.2 and older will reject v6+. Apps 1.1.3 and 1.1.4 may verify v7–v9 signatures but cannot parse the categories introduced in v7 and will safely retain their last verified v6 cache or bundled defaults until upgrading to 1.1.5.

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

## Catalogue v9 operational status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval is maintainer-confirmed; post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v9 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; Android, Windows and macOS public 1.1.6 binaries are confirmed; Google Play rollout is separate.


## Current catalogue and release status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval is maintainer-confirmed; post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v8 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; Android, Windows and macOS public 1.1.6 binaries are confirmed; Google Play rollout is separate.

## Linux x86-64 stable (1.1.6+42)

The initial isolated Linux build was superseded by the successful build on private `main`. It does not change the Android, Windows or macOS release channels. Published assets: AppImage, Debian package and portable tar.gz bundle with SHA-256 checksums. The original packages are unchanged; the checksum manifest now has a published OpenPGP detached signature. See [verification instructions](../security/README.md). CI publication and stable promotion succeeded; manual Linux validation remains pending. Check [public releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=linux-v) before downloading. Ubuntu 22.04+ and compatible Debian/Linux Mint x86-64 environments are initial test targets, not certified compatibility. Verify checksums using `sha256sum -c SHA256SUMS-linux.txt`; run AppImage after `chmod +x`, or install the DEB with `sudo apt install ./MDM-SystemCheck-Linux-x64.deb`. Google Play Integrity and embedded VirusTotal are Android-only. Linux CSV export, catalogue v9 retrieval and desktop functionality remain to be tested. No Linux-specific device catalogue changes are included.

## Platform release workflow split

The private main branch contains a manual Release Manager (`.github/workflows/release-manager.yml`) with independent Android, Windows, macOS and Linux selections, all disabled by default. Android test APK and Google Play production AAB use separate private workflows. Android, Windows and macOS no longer build on ordinary pushes. PR CI runs analysis and tests only. The signed catalogue workflow remains independent. Linux is manual-only and accepts the expected version, development/stable channel and explicit publication selection. Linux 1.1.6 stable assets are published; manual runtime validation remains pending.

Verified public 1.1.6 downloads: [Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6), [Windows ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6), [macOS ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6). Signed Android AAB is available in the private CI artifact; Play Store rollout is separate. Linux stable publication succeeded; manual validation remains pending. Existing stable releases and catalogue v9 are unchanged.

## Historical release baseline — 1.1.6+42 (24 November 2026)

Android, Windows, macOS and Linux stable 1.1.6 releases are verified on GitHub. Linux x86-64 1.1.6 preview has passed analysis, tests, native build, packaging and publication; its AppImage, DEB, portable tar.gz and SHA-256 file are available. Stable promotion succeeded using the same verified binaries without rebuilding; the stable tag and all four assets are verified. The Linux checksum manifest is now OpenPGP signed; manual desktop compatibility, CSV export and catalogue retrieval remain unverified.

| Platform | Verified download |
| --- | --- |
| Android signed APK | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6) |
| Windows x64 ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6) |
| macOS ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6) |
| Linux x64 | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/linux-v1.1.6) |

Android AAB is signed and available privately from CI run 45411459034; Google Play rollout is separate. Catalogue v9 remains independent and unchanged. No other platform needs rebuilding for Linux promotion.


## Maintainer validation and CI status

The maintainer confirms Google Play publication of 1.1.6+42 and catalogue v9 retrieval on macOS (24 November 2026). Linux desktop acceptance remains pending. The release manager now supports independent APK and AAB inputs, dynamic Linux version and development/stable channels, and optional Linux publication (default false); no platform distribution builds are triggered by ordinary pushes. Linux validation-only and separate Android APK/AAB workflows passed. Future Linux publication remains to be tested. The public [release manifest](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/blob/main/releases.json) records verified stable public assets; it has a metadata-only refresh workflow, successfully executed, and existing clients are unchanged.


## Android distribution policy — 24 November 2026

The independent Android test APK and production AAB workflows both passed analysis, tests, signature verification and private artifact upload (run 45429919328). Future test APKs are private; production AABs are private and uploaded manually to Google Play. Existing historical public APK releases remain available, but are not the production update channel. Windows, macOS and Linux distribution is unchanged. The public releases.json manifest is refreshed by a metadata-only workflow; Android APK metadata describes historical public releases, not Google Play rollout. Linux runtime acceptance is pending.
