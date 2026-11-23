# Central network flow catalogue

The current catalogue contains 434 contextual flow records extracted from the current private Flutter source models. Repeated hostnames are intentional when the MDM context or originating device differs.

Columns: `id, category, name, host, port, protocol, execution_point, region, testability, purpose, reference`.

Only `execution_point=DEVICE` and `testability=testable` may be considered for active probes, subject to operating system and region applicability. Server-side flows, wildcard destinations and documentation-only records are reference-only. These records are **not** a complete or authoritative firewall allowlist: review the cited vendor guidance and tenant-specific requirements.

## Manual offline import (Android 1.1.0 public APK, Windows/macOS 1.1.1)

[Merged private app PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25) introduces an offline CSV picker and strict validation using this **exact header and column order**. The user chooses a CSV from device storage and approves its activation. Only categories present in the imported file override their built-in endpoints; all other categories continue using embedded endpoints. A local copy is retained across restarts and a **Restore bundled catalogue** action clears the override. Imports are limited to 1 MiB and 5,000 rows in the implemented importer.

For a manual fallback after GitHub becomes inaccessible, first obtain a trusted copy of [network-flows.csv](network-flows.csv) by an authorized method, transfer it to the device, then use **Network Flow Catalogue → Import CSV from device** in a verified 1.1.0 build. This feature does **not** exist in Android 1.0.9; it is available in the verified signed public Android 1.1.0+35 APK and Windows/macOS 1.1.1 releases. Manually supplied CSVs are *not cryptographically authenticated*; verify the source and review unusual destinations before activation.

**Migration status:** The applications still use their embedded Dart lists. This CSV is published for review and CI schema checks; runtime download and automatic activation are NOT implemented. A future release must validate a signed publication manifest, enforce allowed protocols and ports, preserve a bundled offline catalogue, and fall back to the last verified cache. Do not treat plain SHA-256 alone as proof of authenticity.

Never publish tenant secrets or private hostnames here. Changes should be reviewed by pull request.

## Android Enterprise source refresh (23 November 2026)

The 433-record catalogue incorporates the Google [Android Enterprise Network Requirements](https://support.google.com/work/android/answer/10513641?hl=en) device destinations, including Play services, account authentication, certificate validation, FCM/GCM messaging, connectivity checks, OEM-dependent OTA updates and Play Protect. `android.clients.google.com` was removed from all records. Wildcard families such as `*.googleapis.com` are represented by reference-only base-domain records with the wildcard explicitly retained in the name and purpose; a base-domain probe is **not** proof that wildcard children are reachable. The signed catalogue manifest is version **4**, published with the updated CSV. Clients with verified catalogue synchronization check the signed manifest during application use and retain their last verified local copy if GitHub is unavailable. Manual imports are untrusted and remain user-approved.

## Apple enterprise network verification (23 November 2026)

The [Apple enterprise network reference](https://support.apple.com/fr-fr/101555) was compared with the existing Apple and macOS device profiles. The catalogue now includes additional device certificate-validation endpoints, Managed Apple Account directory lookup, Apple app attestation wildcard reference, APNs wildcard reference, Apple/iCloud/App Store wildcard reference families, indicative UDP 443 for documented iCloud connectivity endpoints, and selected macOS recovery, software update and content-cache paths.

Already present flows such as Apple NTP (UDP/123), `mesu.apple.com`, Apple Account sign-in, device enrollment, APNs gateway and App Store URLs were not duplicated. Wildcard base names are represented only with `testability=wildcard required`; they cannot be actively probed as an entire wildcard family. APNs TCP/2197 is explicitly `execution_point=MDM_SERVER` and `testability=server-side flow`, not a device-level check. UDP probes only indicate network-path behavior; a reachable port is not proof of iCloud, APNs, App Store purchase processing or MDM enrollment.

Signed manifest version **5** protects the 434-record CSV from tampering and rollback. The application can retrieve the updated reference catalogue through its existing signed synchronization feature, without creating a new binary release.

## Apple APNs and enrollment clarification (23 November 2026)

Apple's official [enterprise network matrix](https://support.apple.com/en-us/101555) lists `*.push.apple.com` TCP **443, 80, 5223, 2197**. All four ports are now represented in the Apple device profile. Wildcard rows are reference-only, and TCP/2197 is explicitly a provider/server-side APNs flow, **not** a device connectivity test. Concrete host probes for `gateway.push.apple.com` (443 and 5223) and `courier.push.apple.com` (5223) are retained; passing them does not prove APNs push delivery or a valid provider certificate.

Apple Device Enrollment (ADE), Apple Business enrollment, enrollment profile hosting, and account-driven enrollment were already listed. Their records now have explicit **MDM Enrollment** descriptions. Management-server-only operations — `mdmenrollment.apple.com`, APNs certificate portal `identity.apple.com`, `deviceservices-external.apple.com` Activation Lock operations, and `vpp.itunes.apple.com` license assignments — are marked `execution_point=MDM_SERVER` and `testability=server-side flow`. Endpoints used by an enrolling device, including `deviceenrollment.apple.com`, `iprofiles.apple.com`, and `axm-servicediscovery.apple.com`, remain testable device flows.

The **v5** Ed25519-signed catalogue contains **434** records. Active probing requires both `execution_point=DEVICE` and `testability=testable`; wildcard reference rows and server-only flows must not be presented as successful live checks. Apple recommends disabling HTTPS interception for these Apple services.

## Unified Android and OEM network catalogue (23 November 2026)

**Current consolidated working CSV:** [network-flows-unified.csv](network-flows-unified.csv). This **479-row complete catalogue** brings together the previously published 434 network records and the 41 additional Samsung Knox/Knox Manage entries, plus four reference-only records for Motorola and Crosscall without removing any non-Samsung provider or device profiles. The source has 149 generic Android records (`device:android`), 63 Samsung Knox device records (`device:samsung`), and 28 Samsung Knox Manage MDM records (`mdm:knox-manage`). The remainder covers Apple, Windows, macOS, Teams Rooms and other MDM providers.

**Long-term OEM model:** maintain common Android/Google services under `device:android`, vendor-specific destinations under `device:samsung`, and Knox Manage administration/device dependencies under `mdm:knox-manage`. The Flutter import parser and device selection now recognize `device:motorola` and `device:crosscall`; the consolidated CSV includes two documentation-only shared Android Enterprise references for each OEM. These are **not** unique Motorola or Crosscall servers, and do not generate active OEM-specific tests. Add independently confirmed manufacturer endpoints to their categories as they become available. Do not duplicate shared Google endpoints for every vendor unless their context differs. Keep the existing 11-column schema and unique IDs to preserve current import compatibility.

**Client versus management/server:** only records marked `execution_point=DEVICE` **and** `testability=testable` can be eligible for active connectivity probes. `MDM_SERVER`, portal, wildcard and documentation-only entries are context, not handset probe results. Knox Configure administrative portal, Knox remote-support desktop portal, server-side S3 asset retrieval and APNs provider endpoints are explicitly server/reference-only; Knox Asset Intelligence device S3 debug uploads remain device-originated. Tests of regional or optional services are meaningful only in their applicable tenant and enrollment configuration. TCP reachability is not proof of push, enrollment or valid licensing; UDP datagrams do not verify messaging or IPsec.

**Signed catalogue publication:** [network-flows.csv](network-flows.csv) remains the existing **434-row, Ed25519-signed v5 live** catalogue. Replacing it with the 475-row consolidated version before generating a valid v6 signature using the offline private key would break automatic updates. The consolidated file can be **manually imported only in builds that accept the new Motorola/Crosscall categories**, because it contains *all* profiles; manual import replaces categories rather than merging individual rows. It is not yet automatically synchronized and is not signed. Publish it to the canonical `network-flows.csv` path only together with a newly signed v6 manifest. The private source repository now provides [`tool/sign_network_catalog.py`](https://github.com/ivanboi/MDM-SYSTEM-CHECK/blob/main/tool/sign_network_catalog.py) for offline signing with the pre-existing Ed25519 private key; it verifies that the key matches the public key pinned in the app. Signing has **not** been completed until the authorized maintainer runs the script with the offline key and publishes both files. Do not commit the signing private key. The earlier [network-flows-samsung-knox.csv](network-flows-samsung-knox.csv) is superseded by this consolidated CSV and retained as a historical snapshot only.

## Manufacturer research status (23 November 2026)

- [Motorola Moto OEMConfig guide](https://en-emea.support.motorola.com/app/answers/detail/a_id/173986): enterprise configurations are distributed through managed Google Play, and the device is managed by an EMM/MDM. No comprehensive official Motorola-only firewall destination list was found. Moto Device Manager is an optional *separate MDM product*, not required for a generic Motorola handset.
- [Crosscall OEMConfig listing in Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/configuration/android-oem-configuration-overview): Crosscall OEMConfig is `com.hmct.crosscalloemconfig`, also distributed through managed Google Play. [Crosscall security updates](https://www.crosscall.com/en/pages/security-update) document update support by device model, but do not provide verified update FQDNs.
- [Google Android Enterprise network requirements](https://support.google.com/work/android/answer/10513641?hl=en): shared managed Play, provisioning, authentication, FCM and optional Google OTA paths belong in `device:android`; Google's OTA hosts must **not** be asserted as mandatory Motorola/Crosscall OEM endpoints without confirmation. No unverified vendor hostnames were added.

**Signing handoff** (on a trusted maintainer workstation, never in CI without controlled secret handling):

```bash
python -m pip install cryptography
python tool/sign_network_catalog.py --csv network-flows-unified.csv --private-key /secure/offline-ed25519-key.pem --version 6 --out-dir /secure/staged-catalog
```

The `--csv` argument refers to a locally downloaded copy of the consolidated CSV. Verify exact contents, sign offline, then publish the two staged files to `data/network/` **together**. Neither the signature nor the manifest can be generated legitimately from the pinned public key alone.
