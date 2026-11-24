# Platform and signed catalogue status

_Last reviewed: 24 November 2026._

| Platform | Public stable | Distribution |
| --- | --- | --- |
| Android | [1.1.5 signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.5) | APK + SHA-256; AAB generated privately, Google Play rollout **not confirmed** |
| Windows | [1.1.5 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5) | ZIP + SHA-256; unsigned executable, **no MSIX or Microsoft Store** |
| macOS | [1.1.5 universal portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.5) | ZIP + SHA-256; not Developer ID signed or notarized |
| iOS | Not published | iOS/iPadOS network destinations are profile references, not a native iOS application |

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

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval and post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v9 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; public 1.1.6 binaries and Google Play rollout are not yet confirmed.


## Current catalogue and release status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval and post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v8 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; public 1.1.6 binaries and Google Play rollout are not yet confirmed.

## Linux x86-64 preview (1.1.6+42)

An isolated Linux build has been requested on the private `linux-build` branch. It does not change the Android, Windows or macOS release channels. Planned assets: AppImage, Debian package and portable tar.gz bundle with SHA-256 checksums. Packages are unsigned; GPG signing is not yet configured. Availability is pending successful CI publication and manual Linux validation. Check [public releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=linux-v) before downloading. Ubuntu 22.04+ and compatible Debian/Linux Mint x86-64 environments are initial test targets, not certified compatibility. Verify checksums using `sha256sum -c SHA256SUMS-linux.txt`; run AppImage after `chmod +x`, or install the DEB with `sudo apt install ./MDM-SystemCheck-Linux-x64.deb`. Google Play Integrity and embedded VirusTotal are Android-only. Linux CSV export, catalogue v9 retrieval and desktop functionality remain to be tested. No Linux-specific device catalogue changes are included.

## Platform release workflow split

The private main branch now contains a manual Release Manager (`.github/workflows/release-manager.yml`) with independent Android, Windows, macOS and Linux selections, all disabled by default. Android AAB selection builds both the APK and a private AAB; it is not AAB-only. Android, Windows and macOS no longer build on ordinary pushes. PR CI runs analysis and tests only. The signed catalogue workflow remains independent. Linux currently also triggers when its own workflow changes, to bootstrap the first x64 preview; its publication is fixed to 1.1.6+42 preview until general channel/version support is implemented. The release manager's development/stable selection currently applies to Android, Windows and macOS only. Do not treat Linux preview as stable or assume a successful build until release assets exist.

Verified public 1.1.6 downloads: [Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6), [Windows ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6), [macOS ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6). Signed Android AAB is available in the private CI artifact; Play Store rollout is separate. Linux preview publication remains pending. Existing stable releases and catalogue v9 are unchanged.
