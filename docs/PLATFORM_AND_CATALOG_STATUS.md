# Platform and catalogue status

_Last reviewed: 23 November 2026._

## Releases and distribution policy

- **Android:** [public stable APK releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/latest), signed using the project's production Android keystore and published with SHA-256. The latest verified stable before the v1.1.3 rollout is **1.1.2**. Uploading an AAB to Google Play and confirming a Play Store production rollout are separate maintainer actions.
- **Windows:** [portable Windows x64 ZIP releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=windows-v), latest verified stable before v1.1.3 **1.1.2**. No MSIX or Microsoft Store distribution. The executable is unsigned.
- **macOS:** [universal macOS ZIP releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=macos-v), latest verified stable before v1.1.3 **1.1.2**. The executable is neither Developer ID signed nor notarized; Gatekeeper and enterprise policies may restrict it.
- **v1.1.3 source:** OEM device profiles, common Android + manufacturer flow composition, and dual Ed25519 public keys. Public availability must be checked on release pages once the CI release jobs complete. No native iOS build is published.

## Network catalogue

| Catalogue | Contents | Signing | Status |
| --- | --- | --- | --- |
| [Canonical CSV](../data/network/network-flows.csv) | 434 records | Ed25519 v5, original public key | **Active** until client migration |
| [v6 candidate](../data/network/network-flows-v6.csv) | 480 records, 16 categories | Ed25519 v6, rotated public key | Signed, staged; **not yet active** |

The signed catalogue is checked automatically at most once every 24 hours by supported clients. They verify HTTPS source, SHA-256, Ed25519 signature, strict CSV schema and version rollback. Manual import is user-approved and untrusted; a verified cached catalogue remains usable when GitHub is unavailable.

v6 uses a newly generated key because the original private signing key was lost. v1.1.3 source trusts **both** keys, choosing the legacy key for v1–v5 and the rotated key for v6+. The canonical CSV and its manifest must be promoted together **only after** compatible v1.1.3 applications are available. Older clients will reject v6 and retain their last verified copy rather than trust an unfamiliar key.

Future Android Enterprise or OEM network changes should be made once in the canonical CSV after cutover: `device:android` for common Google/Android flows, `device:samsung`, `device:motorola`, `device:crosscall` for vendor-specific flows, and `mdm:knox-manage` for Samsung's standalone MDM platform. Server-originating, regional, wildcard and documentary flows must not be treated as terminal checks. Details: [catalogue maintenance](../data/network/README.md).

## Privacy and diagnostic scope

Network tests originate on the device running SystemCheck. HTTP(S) response or TCP connect success does not prove MDM enrollment, update availability, authentication or successful push delivery. Optional VoWiFi sends UDP datagrams but does not establish an IPsec tunnel. Sensitive diagnostic reports remain local unless users export them. Android Google Play Integrity may contact `https://api.mdm.ivanboi.fr/verify` on explicit request; VirusTotal handles separate user-selected uploads.

## Retention

Keep historic **stable** release tags and their checksums available for rollback. Do not publish insecure experimental MSIX packages or obsolete package instructions as supported downloads. Private CI development artifacts may be automatically pruned according to the documented retention policy; never delete customer data, stable releases, or signing key backups to tidy the project.
