# Security Policy — MDM SystemCheck

## Supported versions

Security fixes target the [latest stable Android release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest). Fixes for older versions are not guaranteed.

## Windows portable ZIP distribution security

Windows 1.1.1 is **unsigned**. See [Windows signing and verification](docs/WINDOWS_SIGNING.md) for trusted signing options and current limitations.

The official Windows x64 release uses a portable ZIP available from this public repository's [Windows GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1). It is **not code signed** and has not passed Microsoft Store certification. Download only from this repository, validate the accompanying SHA-256 checksum and keep Windows SmartScreen, antivirus and enterprise protections enabled. SHA-256 is an integrity check, not proof of publisher identity. Windows may warn or block unsigned apps; enterprise-managed devices may prohibit running them entirely.

## Microsoft Store identity and Windows package trust

The Partner Center identity for the future Windows package is `ivanbillyjean.MDMSystemCheck`, with publisher `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A` and Store ID `9N9Z3PCL3MG1`. The private Windows build process creates an unsigned submission package for Microsoft's certification process. **It is not distributed as a signed sideload package, and there is no confirmed public Store release.** Download builds only from verified release channels.

## Network reference catalogue and offline local import

The [public CSV catalogue](data/network/network-flows.csv) contains vendor-referenced network destinations, **not** a fully verified firewall allowlist. GitHub Actions validates its CSV schema, not the trustworthiness of every destination. The Android application **does not automatically download or execute the public CSV**; Android 1.1.0 source contains an optional user-approved manual import.

[Merged source PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25) implements user-selected CSV files in the Android 1.1.0 (build 35) release candidate and explicit confirmation before locally overriding selected device/MDM categories. A locally imported file is **not signed/authenticated**: importing untrusted destinations could trigger probes to an attacker-controlled host. Do not import CSVs from unknown sources. The unreleased automatic GitHub synchronizer must authenticate a signed manifest, validate schema and endpoints, and retain offline rollback before enabling network updates.

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
- TLS certificate validation for HTTPS and differentiation between HTTP error responses and connectivity.
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
