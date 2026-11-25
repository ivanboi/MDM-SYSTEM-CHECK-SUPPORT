# MDM SystemCheck — Official Downloads and Support

## Android security validation — 1.1.7 and later

Source version 1.1.7+43 is under security validation; public downloads remain 1.1.6 until new assets are verified. Android 12 is the new minimum; Android 17 runtime compatibility is not yet confirmed. Future signed APK/AAB builds require local MobSF static analysis before artifact distribution. Analysis results are reviewed privately; static analysis is not a security certification. Windows, macOS and Linux retain platform-specific checks; no iOS IPA is published.

Network connectivity and EMM/MDM troubleshooting for Android, Windows, macOS and Linux. Checks run from the device running MDM SystemCheck. They **do not** prove MDM enrollment, server authentication, application updates or receipt of push notifications.

## Official downloads

| Platform | Download | Important |
| --- | --- | --- |
| Android | [1.1.6 signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6) | SHA-256 provided; Google Play publication is managed separately. |
| Windows | [1.1.6 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6) | Extract all files. Unsigned executable; **no MSIX / Microsoft Store**. |
| macOS | [1.1.6 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6) | Not Apple Developer ID signed or notarized. |
| Linux | [1.1.6 x64 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/linux-v1.1.6) | AppImage, DEB and TAR.GZ; OpenPGP-signed checksum manifest; manual validation pending. |
| Development | [All releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases) | Prereleases may be unstable. |

Only a published release with its downloadable assets is an installable version. GitHub source commits and successful CI tests alone do not confirm an app-store rollout. Check the [platform status](docs/PLATFORM_AND_CATALOG_STATUS.md).

## Device profiles and supported MDM platforms

- **Android**: common Google/Android Enterprise network dependencies, maintained under `device:android`.
- **Samsung**: common Android dependencies plus Samsung Knox manufacturer services (`device:samsung`).
- **Motorola (specific servers)**: community-documented Motorola OTA CDS DNS/TCP 443 test (`device:motorola`); select Android separately for common Google requirements.
- **Crosscall (specific servers)**: two active maintainer-provided FOTA endpoints and two historical references (`device:crosscall`). Select Android separately for shared services.
- **ChromeOS (specific servers)**: Google-documented enterprise management, attestation, Omaha update and download hosts (`device:chromeos`), tested as remote network paths from the active device.
- **Fairphone (specific servers)**: current Gen. 6 OTA hostnames are not verified, so no unsubstantiated OEM-only test is executed (`device:fairphone`, documentation-only).
- **Other profiles**: Apple iOS/iPadOS, macOS, Android AOSP Teams Rooms and Windows.

**Samsung Knox Manage** is an independent MDM product (`mdm:knox-manage`), **not** part of the standard Samsung device services. Other supported MDM profiles: Microsoft Intune, Omnissa Workspace ONE, Ivanti, Cisco Meraki Systems Manager, Citrix Endpoint Management and BlackBerry UEM.

The Motorola OTA endpoint `moto-cds.appspot.com` (TCP 443) is documented by a third-party community project, **not** an official Motorola firewall policy. Only the network path is checked: no firmware update check POST or identifying payload is sent. Optional OEM or region-specific services should not be treated as mandatory connectivity requirements.

## Version 1.1.5 and catalogue v9

Version `1.1.5+41` interprets platform-reported certificate errors as hostname mismatch, expired/not-yet-valid certificate, untrusted chain or generic TLS handshake warning; unknown causes are not guessed, and certificate validation remains enabled. Error messages are no longer damaged by the old sanitizer.

The **Ed25519-signed v9** catalogue has **522 records across 18 categories**. It includes 15 Google-documented ChromeOS targets and two Fairphone documentation-only records, and reclassifies 30 invalid Google API push-port checks as documentation-only. Version 1.1.5 is required to parse the new categories; older apps safely retain their last verified catalogue. Motorola's `moto-cds.appspot.com:443` DNS/TCP check was verified as executed in the 1.1.4 export; no Motorola OTA POST or device identifier is sent.

## Diagnostic reliability improvements in version 1.1.4

Version 1.1.4 removes duplicated Android network probes when multiple OEM profiles are selected. It excludes non-applicable TCP 5228–5230 probes against Google REST API hosts while preserving device FCM transport checks for `mtalk.google.com`. A connection timeout is reported as an inconclusive **WARN**, not definitive evidence of a firewall block. A verified TLS connection followed by HTTP 400 or other 4xx responses confirms reachability (**PASS**) but **not** a successful management API request. TLS handshake warnings include the underlying exception instead of presuming SSL inspection.

Diagnostic CSV exports identify the signed remote catalogue version and whether the app used bundled, verified GitHub or manually imported data. The signed Ed25519 v6 network catalogue was unchanged during release 1.1.4; 1.1.5 now uses the separate signed v9 data release.

## Signed network flow catalogue

**Single active canonical source:** [network-flows.csv](data/network/network-flows.csv), authenticated by [network-flows.manifest.json](data/network/network-flows.manifest.json). The application validates an Ed25519 signature, SHA-256 and the strict 11-column CSV schema before accepting an automatic update. The signed catalogue version is independent of the application version.

The **522-record v9 catalogue is now active**, with 18 categories, at the canonical CSV and manifest paths. Ed25519 verification uses a rotated public key because the original private signing key was lost. **Application v1.1.5** trusts the legacy key for v1–v5 and the rotated key for v6+, and understands v7's ChromeOS/Fairphone categories. Builds 1.1.3 and 1.1.4 lack these categories and safely retain the last valid catalogue or bundled defaults; older 1.1.2 clients cannot verify v6+.

To add flows in the future, see [Network catalogue maintenance](data/network/README.md). Only `execution_point=DEVICE` **and** `testability=testable` rows are eligible for live checks. MDM server/administration, wildcard, tenant-specific and documentation-only entries cannot be used as terminal success indicators. Manual CSV import requires explicit approval and is not cryptographically authenticated.

## What the app does

- DNS, TCP, HTTP(S) and NTP probes; optional indicative VoWiFi/ePDG UDP 500/4500 transmission (not an IPsec handshake).
- Guided checks for the selected manufacturer or MDM; users can configure tenant-specific endpoints.
- Local diagnostic history and CSV export. Windows/macOS use a native Save As dialog.
- Android-only optional Google Play Integrity check through the OVH verifier, and VirusTotal WebView upload when explicitly requested. Network diagnostic reports are **not** automatically uploaded.

## Support, privacy and security

[Report a bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml) · [Privacy policy](PRIVACY.md) · [Security policy](SECURITY.md) · [Changelog](CHANGELOG.md)

Do not post credentials, private network destinations, serial numbers, IMEIs, tokens or unredacted diagnostic exports in public issues. The private Flutter source code, build/signing configurations and secrets are maintained separately from this public support repository.

## Catalogue v9 operational status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval is maintainer-confirmed; post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v9 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; Android, Windows and macOS public 1.1.6 binaries are confirmed; Google Play rollout is separate.


## Current catalogue and release status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval is maintainer-confirmed; post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v8 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; Android, Windows and macOS public 1.1.6 binaries are confirmed; Google Play rollout is separate.

## Linux x86-64 stable (1.1.6+42)

The initial isolated Linux build was superseded by the successful build on private `main`. It does not change the Android, Windows or macOS release channels. Published assets: AppImage, Debian package and portable tar.gz bundle with SHA-256 checksums. The checksum manifest is OpenPGP-signed; packages do not carry embedded signatures. CI publication and stable promotion succeeded; manual Linux validation remains pending. Check [public releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=linux-v) before downloading. Ubuntu 22.04+ and compatible Debian/Linux Mint x86-64 environments are initial test targets, not certified compatibility. Verify checksums using `sha256sum -c SHA256SUMS-linux.txt`; run AppImage after `chmod +x`, or install the DEB with `sudo apt install ./MDM-SystemCheck-Linux-x64.deb`. Google Play Integrity and embedded VirusTotal are Android-only. Linux CSV export, catalogue v9 retrieval and desktop functionality remain to be tested. No Linux-specific device catalogue changes are included.

## Platform release workflow split

The private main branch contains a manual Release Manager (`.github/workflows/release-manager.yml`) with independent Android, Windows, macOS and Linux selections, all disabled by default. Android test APK and Google Play production AAB use separate private workflows. Android, Windows and macOS no longer build on ordinary pushes. PR CI runs analysis and tests only. The signed catalogue workflow remains independent. Linux is manual-only and accepts the expected version, development/stable channel and explicit publication selection. Linux 1.1.6 stable assets are published; manual runtime validation remains pending.

Verified public 1.1.6 downloads: [Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6), [Windows ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6), [macOS ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6). Signed Android AAB is available in the private CI artifact; Play Store rollout is separate. Linux stable publication succeeded; manual validation remains pending. Existing stable releases and catalogue v9 are unchanged.

## Current release status — 1.1.6+42 (24 November 2026)

Android, Windows, macOS and Linux stable 1.1.6 releases are verified on GitHub. Linux x86-64 1.1.6 preview has passed analysis, tests, native build, packaging and publication; its AppImage, DEB, portable tar.gz and SHA-256 file are available. Stable promotion succeeded using the same verified binaries without rebuilding; the stable tag and all four assets are verified. The Linux checksum manifest is OpenPGP-signed; manual desktop compatibility, CSV export and catalogue retrieval remain unverified.

| Platform | Verified download |
| --- | --- |
| Android signed APK | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6) |
| Windows x64 ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6) |
| macOS ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6) |
| Linux x64 | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/linux-v1.1.6) |

Android AAB is signed and available privately from CI run 45411459034; Google Play rollout is separate. Catalogue v9 remains independent and unchanged. No other platform needs rebuilding for Linux promotion.


## Maintainer validation and CI status

The maintainer confirms Google Play publication of 1.1.6+42 and catalogue v9 retrieval on macOS (24 November 2026). Linux desktop acceptance remains pending. The release manager now supports independent APK and AAB inputs, dynamic Linux version and development/stable channels, and optional Linux publication (default false); no platform distribution builds are triggered by ordinary pushes. Linux validation-only and separate Android APK/AAB workflows passed. Detached signing and publication of the existing Linux release succeeded. The public [release manifest](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/blob/main/releases.json) records verified stable public assets; it has a metadata-only refresh workflow, first execution succeeded, and existing clients are unchanged.


## Android distribution policy — 24 November 2026

The independent Android test APK and production AAB workflows both passed analysis, tests, signature verification and private artifact upload (run 45429919328). Future test APKs are private; production AABs are private and uploaded manually to Google Play. Existing historical public APK releases remain available, but are not the production update channel. Windows, macOS and Linux distribution is unchanged. The public releases.json manifest is refreshed by a metadata-only workflow; Android APK metadata describes historical public releases, not Google Play rollout. Linux runtime acceptance is pending.

## Linux OpenPGP release signing

The dedicated Ed25519 public release key and its primary fingerprint (`22DDA2AC2133E3A88761A375F4A9039C27F8CCEA`) are available in [security/](security/README.md). The Linux signing pipeline has passed private validation. The original public Linux 1.1.6 packages remain byte-for-byte unchanged. The detached checksum signature and public key are published and verified. See the [verification instructions](security/README.md).
