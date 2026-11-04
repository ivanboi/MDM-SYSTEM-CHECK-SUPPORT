# Security Policy — MDM SystemCheck

## Supported versions

Security fixes target the latest maintained Android release of the project (documented version: **1.0.0+23**). Fixes for older versions are not guaranteed.

## Reporting a vulnerability privately

**Never disclose a vulnerability, exploit, secret, or confidential configuration in a public issue.**

Use **Security → Report a vulnerability** in this repository **if private vulnerability reporting is enabled**. Otherwise, contact the maintainer through an established private channel. If no confidential channel is available, do not publish technical details in public issues.

Include the application and Android versions, reproduction scenario, impact, and prerequisites, with secrets and personal data redacted. No guaranteed response or remediation timeline is offered.

## Scope and privacy

The application performs outbound DNS, TCP, HTTP(S), NTP, and optional VoWiFi/ePDG diagnostics. UDP 500/4500 transmissions do not prove IKE/IPsec negotiation or functioning VoWiFi service. Successful TCP/HTTPS connections do not prove authentication, MDM enrollment, or push notification delivery.

Results, preferences, and configured MDM endpoints are stored **locally, without dedicated application-level encryption**. They are not automatically uploaded to support. CSV exports may reveal sensitive network information: redact them before sharing.

## Protections described in the code

- Android application storage sandboxing; application backups and cleartext HTTP traffic are disabled in the generated release manifest.
- TLS certificate validation for HTTPS and differentiation between HTTP error responses and connectivity.
- Neutralization of CSV values that could be interpreted as spreadsheet formulas.
- Validation of the expected source IP address and port for UDP responses; sending a UDP datagram alone does not prove IPsec connectivity.
- Custom tests are restricted by policy to hosts and networks the administrator is authorized to test.

**Limitations:** a compromised or rooted device may expose history and preferences; exported CSV files are sensitive. Do not enter credentials or secrets in diagnostic fields.

## Controls still to be verified

Before production distribution: temporary CSV file retention, local encryption requirements, request rate limiting, stronger UDP/NTP validation, artifact signing, and Play Integrity configuration. **These protections are not claimed to be implemented.**

## Repository separation

This **public** repository contains only documentation and support forms; the Flutter/Android source code resides in a **private** repository. No secrets, signing files, internal configurations, or source code should be added to this repository.

For non-sensitive functional issues, use the [public issue forms](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose).
