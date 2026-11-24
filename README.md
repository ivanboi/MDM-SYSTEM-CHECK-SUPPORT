# MDM SystemCheck — Official Downloads and Support

Network connectivity and EMM/MDM troubleshooting for Android, Windows and macOS. Checks run from the device running MDM SystemCheck. They **do not** prove MDM enrollment, server authentication, application updates or receipt of push notifications.

## Official downloads

| Platform | Download | Important |
| --- | --- | --- |
| Android | [1.1.5 signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.5) | SHA-256 provided; Google Play publication is managed separately. |
| Windows | [1.1.5 x64 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5) | Extract all files. Unsigned executable; **no MSIX / Microsoft Store**. |
| macOS | [1.1.5 universal ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.5) | Not Apple Developer ID signed or notarized. |
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

## Version 1.1.5 and catalogue v8

Version `1.1.5+41` interprets platform-reported certificate errors as hostname mismatch, expired/not-yet-valid certificate, untrusted chain or generic TLS handshake warning; unknown causes are not guessed, and certificate validation remains enabled. Error messages are no longer damaged by the old sanitizer.

The **Ed25519-signed v8** catalogue has **507 records across 18 categories**. It includes 15 Google-documented ChromeOS targets and two Fairphone documentation-only records, and reclassifies 30 invalid Google API push-port checks as documentation-only. Version 1.1.5 is required to parse the new categories; older apps safely retain their last verified catalogue. Motorola's `moto-cds.appspot.com:443` DNS/TCP check was verified as executed in the 1.1.4 export; no Motorola OTA POST or device identifier is sent.

## Diagnostic reliability improvements in version 1.1.4

Version 1.1.4 removes duplicated Android network probes when multiple OEM profiles are selected. It excludes non-applicable TCP 5228–5230 probes against Google REST API hosts while preserving device FCM transport checks for `mtalk.google.com`. A connection timeout is reported as an inconclusive **WARN**, not definitive evidence of a firewall block. A verified TLS connection followed by HTTP 400 or other 4xx responses confirms reachability (**PASS**) but **not** a successful management API request. TLS handshake warnings include the underlying exception instead of presuming SSL inspection.

Diagnostic CSV exports identify the signed remote catalogue version and whether the app used bundled, verified GitHub or manually imported data. The signed Ed25519 v6 network catalogue was unchanged during release 1.1.4; 1.1.5 now uses the separate signed v8 data release.

## Signed network flow catalogue

**Single active canonical source:** [network-flows.csv](data/network/network-flows.csv), authenticated by [network-flows.manifest.json](data/network/network-flows.manifest.json). The application validates an Ed25519 signature, SHA-256 and the strict 11-column CSV schema before accepting an automatic update. The signed catalogue version is independent of the application version.

The **507-record v8 catalogue is now active**, with 18 categories, at the canonical CSV and manifest paths. Ed25519 verification uses a rotated public key because the original private signing key was lost. **Application v1.1.5** trusts the legacy key for v1–v5 and the rotated key for v6+, and understands v7's ChromeOS/Fairphone categories. Builds 1.1.3 and 1.1.4 lack these categories and safely retain the last valid catalogue or bundled defaults; older 1.1.2 clients cannot verify v6+.

To add flows in the future, see [Network catalogue maintenance](data/network/README.md). Only `execution_point=DEVICE` **and** `testability=testable` rows are eligible for live checks. MDM server/administration, wildcard, tenant-specific and documentation-only entries cannot be used as terminal success indicators. Manual CSV import requires explicit approval and is not cryptographically authenticated.

## What the app does

- DNS, TCP, HTTP(S) and NTP probes; optional indicative VoWiFi/ePDG UDP 500/4500 transmission (not an IPsec handshake).
- Guided checks for the selected manufacturer or MDM; users can configure tenant-specific endpoints.
- Local diagnostic history and CSV export. Windows/macOS use a native Save As dialog.
- Android-only optional Google Play Integrity check through the OVH verifier, and VirusTotal WebView upload when explicitly requested. Network diagnostic reports are **not** automatically uploaded.

## Support, privacy and security

[Report a bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml) · [Privacy policy](PRIVACY.md) · [Security policy](SECURITY.md) · [Changelog](CHANGELOG.md)

Do not post credentials, private network destinations, serial numbers, IMEIs, tokens or unredacted diagnostic exports in public issues. The private Flutter source code, build/signing configurations and secrets are maintained separately from this public support repository.

## Catalogue v8 operational status

Catalogue v8 (24 November 2026): 507 records in 18 categories, published by GitHub Actions using the existing Ed25519 key. Android confirmed verified GitHub catalogue v8 with zero manual entries. Windows/macOS runtime refresh and new OEM reachability tests remain pending. Four maintainer-provided Crosscall FOTA records (two active, two historical) and six Motorola additions (five active, one staging reference) are included; carrier-specific applicability varies. These are connectivity checks, not OTA transactions or independently verified vendor allowlists.
