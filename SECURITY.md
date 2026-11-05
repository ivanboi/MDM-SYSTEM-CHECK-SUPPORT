# Security Policy — MDM SystemCheck

## Supported versions

Security fixes target the [latest stable Android release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest). Fixes for older versions are not guaranteed.

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

Further review is needed for temporary CSV file retention, local encryption requirements, request rate limiting, stronger UDP/NTP validation, and Play Integrity integration. **Production Android signing is implemented; Play Integrity and Google Play publication are not.** Existing installations signed with a different key may require reinstallation, which can erase locally stored data.

## Repository separation

This **public** repository contains documentation, support forms, and approved release assets; the Flutter/Android source code resides in a **private** repository. No secrets, signing files, internal configurations, or source code should be added to this repository.

For non-sensitive functional issues, use the [public issue forms](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose).
