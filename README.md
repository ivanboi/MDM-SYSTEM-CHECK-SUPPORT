# MDM SystemCheck — Official Downloads and Support

Network connectivity and EMM/MDM troubleshooting for Android, Windows and macOS. Checks run from the device running MDM SystemCheck. They **do not** prove MDM enrollment, server authentication, application updates or receipt of push notifications.

## Official downloads

| Platform | Download | Important |
| --- | --- | --- |
| Android | [Latest signed APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) | SHA-256 provided; Google Play publication is managed separately. |
| Windows | [Windows stable portable ZIP releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=windows-v) | Extract all files. Unsigned executable; **no MSIX / Microsoft Store**. |
| macOS | [macOS stable ZIP releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=macos-v) | Not Apple Developer ID signed or notarized. |
| Development | [All releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases) | Prereleases may be unstable. |

Only a published release with its downloadable assets is an installable version. GitHub source commits and successful CI tests alone do not confirm an app-store rollout. Check the [platform status](docs/PLATFORM_AND_CATALOG_STATUS.md).

## Device profiles and supported MDM platforms

- **Android**: common Google/Android Enterprise network dependencies, maintained under `device:android`.
- **Samsung**: common Android dependencies plus Samsung Knox manufacturer services (`device:samsung`).
- **Motorola**: common Android dependencies plus a limited, community-documented Motorola OTA CDS DNS/TCP connectivity test (`device:motorola`).
- **Crosscall**: common Android dependencies. Crosscall-specific OTA hosts are **not yet confirmed** (`device:crosscall`).
- **Other profiles**: Apple iOS/iPadOS, macOS, Android AOSP Teams Rooms and Windows.

**Samsung Knox Manage** is an independent MDM product (`mdm:knox-manage`), **not** part of the standard Samsung device services. Other supported MDM profiles: Microsoft Intune, Omnissa Workspace ONE, Ivanti, Cisco Meraki Systems Manager, Citrix Endpoint Management and BlackBerry UEM.

The Motorola OTA endpoint `moto-cds.appspot.com` (TCP 443) is documented by a third-party community project, **not** an official Motorola firewall policy. Only the network path is checked: no firmware update check POST or identifying payload is sent. Optional OEM or region-specific services should not be treated as mandatory connectivity requirements.

## Signed network flow catalogue

**Single active canonical source:** [network-flows.csv](data/network/network-flows.csv), authenticated by [network-flows.manifest.json](data/network/network-flows.manifest.json). The application validates an Ed25519 signature, SHA-256 and the strict 11-column CSV schema before accepting an automatic update. The signed catalogue version is independent of the application version.

The **480-record v6 candidate** is [staged here](data/network/network-flows-v6.csv) together with its [signed manifest](data/network/network-flows-v6.manifest.json). v6 rotates the Ed25519 public key because the previous private signing key was lost. **The v5 canonical catalogue stays active until updated application binaries containing both trusted public keys have been distributed.** Older applications cannot verify v6.

To add flows in the future, see [Network catalogue maintenance](data/network/README.md). Only `execution_point=DEVICE` **and** `testability=testable` rows are eligible for live checks. MDM server/administration, wildcard, tenant-specific and documentation-only entries cannot be used as terminal success indicators. Manual CSV import requires explicit approval and is not cryptographically authenticated.

## What the app does

- DNS, TCP, HTTP(S) and NTP probes; optional indicative VoWiFi/ePDG UDP 500/4500 transmission (not an IPsec handshake).
- Guided checks for the selected manufacturer or MDM; users can configure tenant-specific endpoints.
- Local diagnostic history and CSV export. Windows/macOS use a native Save As dialog.
- Android-only optional Google Play Integrity check through the OVH verifier, and VirusTotal WebView upload when explicitly requested. Network diagnostic reports are **not** automatically uploaded.

## Support, privacy and security

[Report a bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml) · [Request a feature](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml) · [Privacy policy](PRIVACY.md) · [Security policy](SECURITY.md) · [Changelog](CHANGELOG.md)

Do not post credentials, private network destinations, serial numbers, IMEIs, tokens or unredacted diagnostic exports in public issues. The private Flutter source code, build/signing configurations and secrets are maintained separately from this public support repository.
