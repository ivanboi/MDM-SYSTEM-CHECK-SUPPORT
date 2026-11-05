# MDM SystemCheck — Official Support

**MDM SystemCheck (EMM SystemCheck)** is an **Android Flutter application** for network diagnostics aimed at EMM/MDM administrators. It checks connectivity from an Android phone without accessing MDM administration APIs or validating enrollment or authentication.

This **public** repository is the home for public downloads, documentation, and support. **Source code, build configurations, and secrets remain in a separate private repository.** Access to the private repository is not required to receive support.

## Features

- DNS, TCP, HTTP(S), and NTP tests (UDP/123 request with response validation).
- Diagnostics for destinations reachable from the Android device; server-to-server flows, wildcard, tenant-specific, or region-specific destinations are **reference-only**.
- Selectable network profiles: **iOS/iPadOS, macOS, Android, Android AOSP for Microsoft Teams Rooms, Samsung Knox services, and Windows**. All selected profile tests run **from the Android phone**, not from the remote operating systems.
- MDM platforms: **Microsoft Intune, Omnissa Workspace ONE UEM, Ivanti Neurons for MDM/EPMM, Cisco Meraki Systems Manager, Citrix Endpoint Management, BlackBerry UEM/Dynamics, and Samsung Knox Manage**. Only one MDM platform is tested at a time. Knox Manage is a separate MDM platform, distinct from Samsung Knox device services.
- Optional deployment-specific network components (e.g., AWCM/UAG/Tunnel, Sentry/Core, Intune Tunnel, Citrix Gateway, BlackBerry Proxy): an administrator must explicitly enable them and enter the hostname/IP address and port.
- Optional VoWiFi/ePDG checks: DNS resolution of the carrier's hostname and indicative UDP 500/4500 datagram transmission. **No IKE/IPsec negotiation is performed, and VoWiFi operation is not verified.**
- Android-side FCM checks against `mtalk.google.com` (TCP 443/5228/5229/5230). A successful TCP connection does not prove that push notifications are received; `fcm.googleapis.com` is a server-side API and is not tested as a phone push flow.
- History and preferences are stored locally; CSV exports include Android version, build identifier, and Android Security Patch Level.

## Interpreting results

Tests measure network connectivity **from the Android phone**. They do not prove MDM enrollment, authentication, remote service availability, or push notification delivery. Custom components must target only infrastructure you are authorized to test. Check vendor documentation for current destination and port lists before defining firewall rules.

## Android APK downloads

- [Stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest) provides the signed Android APK for production use.
- [Development](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-dev) provides a replaceable prerelease from eligible CI builds.
- Each release includes the APK and its SHA-256 checksum in `SHA256SUMS.txt`.

See the [changelog](CHANGELOG.md) for version history and installation details. Google Play publication and Play Integrity are pending.

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
