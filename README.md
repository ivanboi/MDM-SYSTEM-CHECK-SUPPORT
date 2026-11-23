# MDM SystemCheck — Official Support

**MDM SystemCheck (EMM SystemCheck)** is a **Flutter application for Android, Windows and macOS** for network diagnostics aimed at EMM/MDM administrators. It checks connectivity from the device running the app without accessing MDM administration APIs or validating enrollment or authentication.

This **public** repository is the home for public downloads, documentation, and support. **Source code, build configurations, and secrets remain in a separate private repository.** Access to the private repository is not required to receive support.

**Verified releases (23 November 2026):** Android **1.1.0+35** (signed APK), Windows **1.1.1** (unsigned x64 portable ZIP), and macOS **1.1.1** (unsigned, unnotarized universal Intel/Apple Silicon ZIP). Current private Flutter source is **1.1.1+36**. A private signed Android **1.1.1+36 AAB** has been generated for Play Console, but upload/review/rollout is not verified. Check assets and SHA-256 at the release pages.

## Windows signatures and verified downloads

The [Windows 1.1.1 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) and [Android 1.1.0 APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) are the currently verified stable assets. Windows is **not Authenticode-signed**; see the [signing and security guide](docs/WINDOWS_SIGNING.md). All historical stable Android and Windows releases are retained for support; older private-source CI prereleases are managed separately.

## Windows 1.1.1 — updated icon and CSV export

The Windows 1.1.1 portable ZIP uses the MDM SystemCheck icon rather than the default Flutter icon. CSV exports open a native **Save As** dialog starting in Downloads, allowing users to choose a different location. The Windows executable version metadata uses `ivanboi` / `MDM SystemCheck` instead of `com.example`; previously created application-data files are not automatically migrated. See [Windows installation guide](docs/WINDOWS_DOWNLOAD.md).

## Download MDM SystemCheck

| Platform | Official downloads | Installation |
| --- | --- | --- |
| Android | [Stable Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) | Install the signed APK or use Google Play when available. |
| Windows x64 | [Windows portable ZIP v1.1.1](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) | Download and extract **the entire** `MDM-SystemCheck-Windows-x64.zip`; run `mdm_system_check.exe`. No Microsoft Store or MSIX installer exists in the current pipeline. |
| Windows development | [Latest Windows development build](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-windows-dev) | For testing only; not a stable release. |
| macOS (Intel / Apple Silicon) | [Universal macOS 1.1.1 ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.1) | Extract the complete .app; **not Developer ID signed or notarized**, so Gatekeeper or organization policy may block launch. [Guide](docs/MACOS_DOWNLOAD.md). |

The Windows ZIP is **not Authenticode signed**. Security software, Windows SmartScreen and organizational policies may block it; do not disable protection globally. Verify the ZIP with the attached `SHA256SUMS-windows.txt`. The checksum checks file integrity but is **not** a software signature. See the [Windows download and installation guide](docs/WINDOWS_DOWNLOAD.md).

## Windows distribution — GitHub ZIP only (23 November 2026)

**MSIX and Microsoft Store have been discontinued.** MDM SystemCheck for Windows is published **exclusively** as the [portable Windows x64 ZIP with SHA-256 checksum](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1). The private Windows CI no longer builds MSIX or performs Store submission. Earlier unsigned MSIX files found in private historical releases are **unsupported archives** and must not be sideloaded.

The public ZIP executable is not Authenticode-signed; Windows SmartScreen or organizational policy may block it. See [installation](docs/WINDOWS_DOWNLOAD.md) and [signing](docs/WINDOWS_SIGNING.md).

The [Android 1.1.0 public release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.0) has a signed APK and SHA-256 checksum. A Google Play rollout must be verified separately. CSV manual import was merged in [PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25); automatic GitHub CSV synchronization remains planned. The macOS 1.1.1 .app is available in a GitHub ZIP; no PKG or Mac App Store publication.

## Network flow catalogue and multiplatform availability

- The [public 225-entry reference CSV](data/network/network-flows.csv) is schema-validated by [GitHub Actions](.github/workflows/validate-network-catalog.yml). It is not a verified complete firewall allowlist.
- **Manual CSV import is implemented** in the signed public Android 1.1.0 APK, Windows 1.1.1 and macOS 1.1.1. Users select a local file, approve activation, retain the override locally and can restore bundled defaults. Manually supplied files are not cryptographically authenticated.
- Windows 1.1.1 is [published as a portable ZIP](docs/WINDOWS_DOWNLOAD.md), with no supported MSIX or Microsoft Store alternative.
- macOS 1.1.1 is [published as a universal app ZIP](docs/MACOS_DOWNLOAD.md), **without Developer ID signing or notarization**. No native iOS app is published.
- Automatic signed remote catalogue synchronization is **not implemented**. Future updates require a verified signed manifest, anti-rollback protection and local fallback.
- GitHub hosts public releases, reference data and support; **OVH is used only for user-initiated Android Google Play Integrity**. Diagnostic reports are not automatically uploaded to the developer.

The public Android APK is **1.1.0+35**. The newer Flutter source **1.1.1+36** has a privately generated signed AAB for possible Play Console upload, but no Android 1.1.1 public stable release or Play rollout has been confirmed.

See [platform and catalogue status](docs/PLATFORM_AND_CATALOG_STATUS.md).

## Features

- DNS, TCP, HTTP(S), and NTP tests (UDP/123 request with response validation).
- Diagnostics for destinations reachable from the device running SystemCheck; server-to-server flows, wildcard, tenant-specific, or region-specific destinations are **reference-only**.
- Selectable network profiles: **iOS/iPadOS, macOS, Android, Android AOSP for Microsoft Teams Rooms, Samsung Knox services, and Windows**. Selected profiles are tested **from the current device**, not from the remote operating system named by the profile.
- MDM platforms: **Microsoft Intune, Omnissa Workspace ONE UEM, Ivanti Neurons for MDM/EPMM, Cisco Meraki Systems Manager, Citrix Endpoint Management, BlackBerry UEM/Dynamics, and Samsung Knox Manage**. Only one MDM platform is tested at a time. Knox Manage is a separate MDM platform, distinct from Samsung Knox device services.
- Optional deployment-specific network components (e.g., AWCM/UAG/Tunnel, Sentry/Core, Intune Tunnel, Citrix Gateway, BlackBerry Proxy): an administrator must explicitly enable them and enter the hostname/IP address and port.
- Optional VoWiFi/ePDG checks: DNS resolution of the carrier's hostname and indicative UDP 500/4500 datagram transmission. **No IKE/IPsec negotiation is performed, and VoWiFi operation is not verified.**
- Android-side FCM checks against `mtalk.google.com` (TCP 443/5228/5229/5230). A successful TCP connection does not prove that push notifications are received; `fcm.googleapis.com` is a server-side API and is not tested as a phone push flow.
- Optional Google Play Integrity check for app recognition, Play licensing and device integrity. Versions 1.0.4 and later use the OVH verifier.
- **Scan with VirusTotal** in GitHub APKs (1.0.7+) and Google Play bundles (1.0.8+). The official upload page opens below a SystemCheck app bar. Use **Choose file** for the Android document picker or **Open in browser** if you need to sign in externally. Uploads are subject to VirusTotal's Terms of Service. See the [Privacy Policy](PRIVACY.md).
- History and preferences are stored locally. Android CSV exports include Android version, build identifier and security patch level; desktop CSV reports identify the local OS. Windows/macOS exports use native Save As dialogs.

## Interpreting results

Tests measure network connectivity **from the device running the app**. They do not prove MDM enrollment, authentication, remote service availability, or push notification delivery. Custom components must target only infrastructure you are authorized to test. Check vendor documentation for current destination and port lists before defining firewall rules.

## Android APK downloads

- [Stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) provides the signed Android APK for production use.
- [Development](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-dev) provides a replaceable prerelease from eligible CI builds.
- Each release includes the APK and its SHA-256 checksum in `SHA256SUMS.txt`.

See the [changelog](CHANGELOG.md) for version history and installation details. For Play licensing checks, install the app from Google Play with the account you want to test.

## Public support

- [Report a bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml)
- [View public issues](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues)

For a bug report, provide the application and operating-system versions, reproduction steps, actual behavior, and expected behavior **without sensitive information**.

**All issues are public.** Never publish passwords, tokens, IMEIs, serial numbers, personal data, confidential internal addresses, or unredacted CSV exports. For vulnerabilities, **do not open a public issue**: follow the [security policy](SECURITY.md).

## Privacy

See the [Privacy Policy](PRIVACY.md) for what network probes send, what stays on the device, and what happens when you share a report.

Diagnostics and settings remain in the application's local storage, without dedicated application-level encryption; they are not automatically sent to support. Android backups are disabled, and cleartext HTTP is blocked by default except for a small set of explicitly permitted captive-portal connectivity-check domains. CSV exports neutralize spreadsheet-formula prefixes but may still be confidential. A compromised device may expose locally stored data.

## Vendor references

[Apple](https://support.apple.com/en-us/101555) · [Android Enterprise](https://support.google.com/work/android/answer/10513641?hl=en) · [Samsung Knox](https://docs.samsungknox.com/admin/knox-admin-portal/before-you-begin/samsung-knox-firewall-exceptions/) · [Microsoft Intune](https://learn.microsoft.com/en-us/intune/fundamentals/endpoints) · [Omnissa](https://ports.omnissa.com/home/) · [Ivanti](https://help.ivanti.com/ht/help/en_US/CLOUD/vNow/platform-allowlist.htm) · [Firebase FCM](https://firebase.google.com/docs/cloud-messaging/network-configuration)

Network references change over time; always consult the latest versions.
