# MDM SystemCheck — Official Support

**MDM SystemCheck (EMM SystemCheck)** is a **Flutter application for Android and Windows** for network diagnostics aimed at EMM/MDM administrators. It checks connectivity from the device running the app without accessing MDM administration APIs or validating enrollment or authentication.

This **public** repository is the home for public downloads, documentation, and support. **Source code, build configurations, and secrets remain in a separate private repository.** Access to the private repository is not required to receive support.

Current source version: **Android 1.1.0 (build 35)**. The [v1.1.0 GitHub release tag](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) exists, but signed APK/AAB assets and Google Play rollout have not been independently verified here. Check the release's files and SHA-256 before download; Store review and rollout remain separate.

## Windows signatures and verified downloads

The [Windows 1.1.1 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) and [Android 1.1.0 APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) are the currently verified stable assets. Windows is **not Authenticode-signed**; see the [signing and security guide](docs/WINDOWS_SIGNING.md). All historical stable Android and Windows releases are retained for support; older private-source CI prereleases are managed separately.

## Windows 1.1.1 — updated icon and CSV export

The Windows 1.1.1 portable ZIP uses the MDM SystemCheck icon rather than the default Flutter icon. CSV exports open a native **Save As** dialog starting in Downloads, allowing users to choose a different location. The Windows executable version metadata uses `ivanboi` / `MDM SystemCheck` instead of `com.example`; previously created application-data files are not automatically migrated. See [Windows installation guide](docs/WINDOWS_DOWNLOAD.md).

## Download MDM SystemCheck

| Platform | Official downloads | Installation |
| --- | --- | --- |
| Android | [Stable Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) | Install the signed APK or use Google Play when available. |
| Windows x64 | [Windows portable ZIP v1.1.1](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) | Download and extract **the entire** `MDM-SystemCheck-Windows-x64.zip`; run `mdm_system_check.exe`. No MSIX or Microsoft Store required. |
| Windows development | [Latest Windows development build](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-windows-dev) | For testing only; not a stable release. |
| macOS | Not released | Future target. |

The Windows ZIP is **not Authenticode signed**. Security software, Windows SmartScreen and organizational policies may block it; do not disable protection globally. Verify the ZIP with the attached `SHA256SUMS-windows.txt`. The checksum checks file integrity but is **not** a software signature. See the [Windows download and installation guide](docs/WINDOWS_DOWNLOAD.md).

## Microsoft Store registration and packaging status — 23 November 2026

The Windows application **MDM SystemCheck** is registered in Microsoft Partner Center with Store ID `9N9Z3PCL3MG1`. Its identity is `ivanbillyjean.MDMSystemCheck`, publisher `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A`, publisher display name `ivan_billyjean`, and package family name `ivanbillyjean.MDMSystemCheck_hgbzc83p2bnep`.

The Windows MSIX packaging is built in the **private source repository only**, reserved for a possible future Microsoft Store submission. The **preferred Windows download is the public portable ZIP**, which requires no Store submission. There is no confirmed Store-certified listing. Do not sideload the unsigned private MSIX.

Android source is **1.1.0 (build 35)** and the public `v1.1.0` Git tag exists. **The presence of a tag does not prove signed APK/AAB asset availability or Play Store rollout.** CSV manual import was merged in [PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25); automatic GitHub CSV synchronization remains planned. Mac APP/PKG packaging has not been released.

## Shared network flow catalogue and desktop roadmap (23 November 2026)

- The [public network reference catalogue](data/network/README.md) contains **225 contextual CSV entries** extracted from the current application models, validated by [GitHub Actions](.github/workflows/validate-network-catalog.yml). [Download the CSV](data/network/network-flows.csv).
- **Android 1.1.0 (build 35) source includes manual CSV import; confirm a matching installed binary before using it.** The application does not automatically download this CSV.
- [Manual CSV import PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25) is **merged into the private source** and part of the Android 1.1.0 build 35 release candidate. Planned behaviour: select a local UTF-8 CSV, validate all records, explicitly approve activation, persist locally, and restore bundled defaults. Verify a signed 1.1.0 APK and its availability before describing the feature as released.
- [Windows PR #22](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/22) is **merged into the private source**, with a proposed Windows x64 portable build. Microsoft Store MSIX submission requires additional packaging and Partner Center details.
- macOS Apple Silicon/Intel builds are **planned, not released**. Proposed GitHub ZIP/APP distribution and optional user-scope PKG avoid Apple subscription fees, but unsigned and unnotarized downloads may be blocked by Gatekeeper/enterprise controls.
- Automatically fetching GitHub catalogues is **not implemented**. Secure publication must use signed manifests and offline fallback before activation.
- GitHub hosts source, public catalogue, approved releases and support; **OVH is used only for the optional Android Google Play Integrity verifier**. Diagnostic results remain local unless the user chooses to export or share them.

See [platform and catalogue status](docs/PLATFORM_AND_CATALOG_STATUS.md) for the delivery and threat-model distinctions.

**Release handoff:** source version **1.1.0 (build 35)** has been merged and the stable Android release workflow requested. Do not assume a public APK exists until it appears under [Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases) or that Google Play has completed its separate review.

## Features

- DNS, TCP, HTTP(S), and NTP tests (UDP/123 request with response validation).
- Diagnostics for destinations reachable from the Android device; server-to-server flows, wildcard, tenant-specific, or region-specific destinations are **reference-only**.
- Selectable network profiles: **iOS/iPadOS, macOS, Android, Android AOSP for Microsoft Teams Rooms, Samsung Knox services, and Windows**. All selected profile tests run **from the Android phone**, not from the remote operating systems.
- MDM platforms: **Microsoft Intune, Omnissa Workspace ONE UEM, Ivanti Neurons for MDM/EPMM, Cisco Meraki Systems Manager, Citrix Endpoint Management, BlackBerry UEM/Dynamics, and Samsung Knox Manage**. Only one MDM platform is tested at a time. Knox Manage is a separate MDM platform, distinct from Samsung Knox device services.
- Optional deployment-specific network components (e.g., AWCM/UAG/Tunnel, Sentry/Core, Intune Tunnel, Citrix Gateway, BlackBerry Proxy): an administrator must explicitly enable them and enter the hostname/IP address and port.
- Optional VoWiFi/ePDG checks: DNS resolution of the carrier's hostname and indicative UDP 500/4500 datagram transmission. **No IKE/IPsec negotiation is performed, and VoWiFi operation is not verified.**
- Android-side FCM checks against `mtalk.google.com` (TCP 443/5228/5229/5230). A successful TCP connection does not prove that push notifications are received; `fcm.googleapis.com` is a server-side API and is not tested as a phone push flow.
- Optional Google Play Integrity check for app recognition, Play licensing and device integrity. Versions 1.0.4 and later use the OVH verifier.
- **Scan with VirusTotal** in GitHub APKs (1.0.7+) and Google Play bundles (1.0.8+). The official upload page opens below a SystemCheck app bar. Use **Choose file** for the Android document picker or **Open in browser** if you need to sign in externally. Uploads are subject to VirusTotal's Terms of Service. See the [Privacy Policy](PRIVACY.md).
- History and preferences are stored locally; CSV exports include Android version, build identifier, and Android Security Patch Level.

## Interpreting results

Tests measure network connectivity **from the Android phone**. They do not prove MDM enrollment, authentication, remote service availability, or push notification delivery. Custom components must target only infrastructure you are authorized to test. Check vendor documentation for current destination and port lists before defining firewall rules.

## Android APK downloads

- [Stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) provides the signed Android APK for production use.
- [Development](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-dev) provides a replaceable prerelease from eligible CI builds.
- Each release includes the APK and its SHA-256 checksum in `SHA256SUMS.txt`.

See the [changelog](CHANGELOG.md) for version history and installation details. For Play licensing checks, install the app from Google Play with the account you want to test.

## Public support

- [Report a bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml)
- [View public issues](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues)

For a bug report, provide the application and Android versions, reproduction steps, actual behavior, and expected behavior **without sensitive information**.

**All issues are public.** Never publish passwords, tokens, IMEIs, serial numbers, personal data, confidential internal addresses, or unredacted CSV exports. For vulnerabilities, **do not open a public issue**: follow the [security policy](SECURITY.md).

## Privacy

See the [Privacy Policy](PRIVACY.md) for what network probes send, what stays on the device, and what happens when you share a report.

Diagnostics and settings remain in the application's local storage, without dedicated application-level encryption; they are not automatically sent to support. Android backups are disabled, and cleartext HTTP is blocked by default except for a small set of explicitly permitted captive-portal connectivity-check domains. CSV exports neutralize spreadsheet-formula prefixes but may still be confidential. A compromised device may expose locally stored data.

## Vendor references

[Apple](https://support.apple.com/en-us/101555) · [Android Enterprise](https://support.google.com/work/android/answer/10513641?hl=en) · [Samsung Knox](https://docs.samsungknox.com/admin/knox-admin-portal/before-you-begin/samsung-knox-firewall-exceptions/) · [Microsoft Intune](https://learn.microsoft.com/en-us/intune/fundamentals/endpoints) · [Omnissa](https://ports.omnissa.com/home/) · [Ivanti](https://help.ivanti.com/ht/help/en_US/CLOUD/vNow/platform-allowlist.htm) · [Firebase FCM](https://firebase.google.com/docs/cloud-messaging/network-configuration)

Network references change over time; always consult the latest versions.
