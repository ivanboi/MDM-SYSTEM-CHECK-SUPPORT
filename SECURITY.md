# Security Policy — MDM SystemCheck

## Supported versions

Security fixes target the [latest stable Android release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest). Fixes for older versions are not guaranteed.

## macOS desktop security

The macOS ZIP is **not** Apple Developer ID signed or notarized. Gatekeeper, XProtect and managed-device policies should remain enabled. The build sandbox requests only network-client/server functions for diagnostics and read/write access to files explicitly selected through the native picker. There is no Apple Store publication. See [macOS installation and security guidance](docs/MACOS_DOWNLOAD.md). The public macOS 1.1.5 ZIP and checksum have been verified in GitHub Releases.

## Windows portable ZIP distribution security

Windows 1.1.5 is **unsigned**. See [Windows signing and verification](docs/WINDOWS_SIGNING.md) for trusted signing options and current limitations.

The official Windows x64 release uses a portable ZIP available from this public repository's [Windows GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5). It is **not code signed** and has not passed Microsoft Store certification. Download only from this repository, validate the accompanying SHA-256 checksum and keep Windows SmartScreen, antivirus and enterprise protections enabled. SHA-256 is an integrity check, not proof of publisher identity. Windows may warn or block unsigned apps; enterprise-managed devices may prohibit running them entirely.

## Retired Windows MSIX packages

Microsoft Store/MSIX distribution is **discontinued**, and no new MSIX files are generated or published. Older unsigned MSIX files from historical private releases are **unsupported archives**; they are not trusted installers and should not be sideloaded. Download the Windows portable ZIP only from verified [public GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.5). SHA-256 is an integrity check, not publisher authentication. Keep SmartScreen and enterprise protections enabled.

## Network reference catalogue and offline local import

The [public CSV catalogue](data/network/network-flows.csv) contains vendor-referenced network destinations, **not** a fully verified firewall allowlist. GitHub Actions validates its CSV schema, not the trustworthiness of every destination. Version 1.1.5 authenticates and can automatically synchronize the signed v8 CSV catalogue from public GitHub on launch (at most once every 24 hours) or explicit refresh, and retains the last verified copy on failure. Manual CSV import remains user-approved and unsigned.

[Merged source PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25) implements user-selected CSV files originally in the Android 1.1.0 (build 35) APK and explicit confirmation before locally overriding selected device/MDM categories. A locally imported file is **not signed/authenticated**: importing untrusted destinations could trigger probes to an attacker-controlled host. Do not import CSVs from unknown sources. The released synchronizer verifies the manifest's Ed25519 signature, CSV SHA-256 and schema, and retains offline rollback. Clients 1.1.3–1.1.4 cannot parse the new v7 categories; version 1.1.5 is required.

OVH is reserved for the optional Android Play Integrity verifier. Diagnostic history and manually chosen network catalogues remain on the device; users should review destination and metadata disclosures before sharing exports.

## Reporting a vulnerability privately

**Never disclose a vulnerability, exploit, secret, or confidential configuration in a public issue.**

Use **Security → Report a vulnerability** in this repository **if private vulnerability reporting is enabled**. Otherwise, contact the maintainer through an established private channel. If no confidential channel is available, do not publish technical details in public issues.

Include the application and Android versions, reproduction scenario, impact, and prerequisites, with secrets and personal data redacted. No guaranteed response or remediation timeline is offered.

## Scope and privacy

The application performs outbound DNS, TCP, HTTP(S), NTP, and optional VoWiFi/ePDG diagnostics. UDP 500/4500 transmissions do not prove IKE/IPsec negotiation or functioning VoWiFi service. Successful TCP/HTTPS connections do not prove authentication, MDM enrollment, or push notification delivery.

Results, preferences, and configured MDM endpoints are stored **locally, without dedicated application-level encryption**. They are not automatically uploaded to support. CSV exports may reveal sensitive network information: redact them before sharing.

## Protections described in the code

- Android application storage sandboxing; application backups are disabled. Cleartext HTTP is denied by default, except for narrowly scoped connectivity-check domains used to diagnose captive portals (`connectivitycheck.gstatic.com`, `connectivitycheck.android.com`, `captive.apple.com`, and `www.msftconnecttest.com`).
- Production APKs and AABs use a persistent Android signing key stored securely outside Git; APK signatures are verified in CI. Signing keys and credentials must never be shared through public support channels.
- TLS certificate and hostname validation for HTTPS; 1.1.5 distinguishes platform-reported hostname mismatch, expired/not-yet-valid certificates, untrusted chains and generic handshake errors without disabling verification.
- Neutralization of CSV values that could be interpreted as spreadsheet formulas.
- Validation of the expected source IP address and port for UDP responses; sending a UDP datagram alone does not prove IPsec connectivity.
- Custom tests are restricted by policy to hosts and networks the administrator is authorized to test.

**Limitations:** a compromised or rooted device may expose history and preferences; exported CSV files are sensitive. Do not enter credentials or secrets in diagnostic fields.

## Controls still to be verified

Further review is needed for temporary CSV file retention, local encryption requirements, request rate limiting, and stronger UDP/NTP validation. Play Integrity is a user-initiated diagnostic. See the [privacy policy](PRIVACY.md) for the verification data flow. Existing installations signed with a different key may require reinstallation, which can erase locally stored data.

## Repository separation

This **public** repository contains documentation, support forms, and approved release assets; the Flutter/Android source code resides in a **private** repository. No secrets, signing files, internal configurations, or source code should be added to this repository.

For non-sensitive functional issues, use the [public issue forms](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose).

## VirusTotal WebView

File scanning is user initiated. The embedded page uses HTTPS on `www.virustotal.com`, with external HTTPS navigation delegated to the browser. Direct file URL access is disabled. The Android picker returns only an authorized document reference. SystemCheck does not persist the selected document in diagnostic history. VirusTotal handles submissions under its terms and privacy notice. Browser sign-in continues outside the WebView when required.

## Catalogue v8 operational status

Catalogue v8 (24 November 2026): 507 records in 18 categories, published automatically with the existing Ed25519 key. Android confirmed verified GitHub catalogue v8 with zero manual entries. Windows/macOS runtime refresh and new OEM reachability tests remain pending. Four maintainer-provided Crosscall FOTA records (two active, two historical) and six Motorola additions (five active, one staging reference) are included. Carrier applicability varies. These are connectivity checks, not OTA transactions or independently verified vendor allowlists.
