# Network Flow Catalogue — Maintainer Guide

The **single active canonical CSV** is [network-flows.csv](network-flows.csv), accompanied by the Ed25519-signed [network-flows.manifest.json](network-flows.manifest.json). MDM SystemCheck checks the manifest at launch (at most once per 24 hours) and on manual refresh; a verified local cache and bundled defaults remain available offline.

**Migration, 23 November 2026:** canonical v5 currently contains 434 rows. The 480-row signed v6 pair [network-flows-v6.csv](network-flows-v6.csv) + [v6 manifest](network-flows-v6.manifest.json) is staged until v1.1.3 clients containing both Ed25519 public keys are available. The separate `network-flows-unified.csv` and `network-flows-samsung-knox.csv` are transitional working/legacy exports, not alternative automatic-update sources; they will be removed after canonical v6 cutover.

## CSV format and semantics

**Keep this exact UTF-8 header and order (11 columns):**

```csv
id,category,name,host,port,protocol,execution_point,region,testability,purpose,reference
```

The CSV must remain at most **1 MiB / 5,000 data rows**. Each `id` must be unique and use lowercase letters, numbers and hyphens only. The `host` field must be a concrete DNS hostname (no scheme, path or wildcard). Put the authoritative public HTTPS source in `reference`. Make `purpose` explicit about optional services, regions and whether information came from an official vendor or community repository.

| Category | What belongs here |
| --- | --- |
| `device:android` | Shared Android Enterprise / Google Play, FCM, enrollment, updates and general Google services |
| `device:samsung` | Samsung Knox **device** services such as KME, Knox Configure, E-FOTA and manufacturer licensing |
| `mdm:knox-manage` | **Separate Samsung Knox Manage MDM** device communication and server-side flows |
| `device:motorola` | Verified Motorola-specific connectivity such as the community-sourced OTA CDS host |
| `device:crosscall` | Verified Crosscall-specific services; do not fabricate OTA endpoints |
| `device:apple`, `device:macos`, `device:windows`, `device:rooms`, `device:vowifi` | Other device-family or optional ePDG checks |
| `mdm:intune`, `mdm:workspace-one`, `mdm:ivanti`, `mdm:meraki`, `mdm:citrix`, `mdm:blackberry` | Independent MDM providers |

An Android OEM profile combines `device:android` plus its own `device:<oem>` category. Do **not** duplicate shared Google entries for every manufacturer. Knox Manage is an MDM selection and must not be silently included in Samsung device tests.

### Executable versus reference-only flows

Only `execution_point=DEVICE` **and** `testability=testable` entries may generate network probes. `MDM_SERVER` is for server-originated flows, administrative portals, provider APIs or license assignment; these are **never** a client result. Reference-only records include wildcards (`wildcard required`), regional or tenant-specific services and documentation-only entries. A reachable endpoint is not proof of successful enrollment, licensing, push delivery or an available OTA update. UDP transmission is not equivalent to a successful response or completed VPN/IPsec session.

For Motorola, `moto-cds.appspot.com:443` comes from an **unofficial** community project ([FixeQD/motorola-update](https://github.com/FixeQD/motorola-update)). MDM SystemCheck performs DNS/TCP connectivity only, **never** the device-specific POST required by Motorola's update service. Crosscall-specific OTA FQDNs remain unconfirmed.

## Adding or changing flows (future maintenance)

1. Research the official manufacturer or MDM documentation, confirm the **originating device or server**, region and exact port/protocol. Prefer concrete endpoints; do not invent hostnames.
2. Change **only** [network-flows.csv](network-flows.csv) once v6 cutover has completed; until then, edit the staged v6 candidate and keep its existing signed bytes unchanged until the next publication. Use stable IDs such as `device-motorola-004` or `device-crosscall-003`.
3. Use a PR or controlled commit, run [CSV and signature validation](../../scripts/validate_network_catalog.py), review the diff, and prevent server/wildcard rows from being classed `testable`.
4. Bump `version` in the manifest, calculate SHA-256 of the **exact CSV bytes**, and sign `<version>\\n<sha256>\\n` with the **existing encrypted offline Ed25519 private key** using the private source repo's `tool/sign_network_catalog.py`. Keep the private key and passphrase off GitHub and out of CI logs.
5. Publish the updated **CSV and signed manifest atomically** in the same Git commit. The app rejects changed bytes without a matching Ed25519 signature and rejects older versions. Never modify a signed CSV in place while leaving the manifest unchanged.
6. Confirm the public [GitHub Actions validation](../../.github/workflows/validate-network-catalog.yml) passes and verify a client can refresh, cache and work offline. App releases are needed only when the client schema/categories, verification key or probe implementation changes.

**Key rotation:** v1–v5 are signed with the legacy key and v6+ with a new rotated key because the prior private key was unavailable. The v1.1.3 client source recognizes both. Do not activate v6 for old app builds until compatible binaries have been released. For future updates, use the **same v6+ private key**; do not generate another key unnecessarily.

Manual CSV import is supported but remains **user-approved, local and cryptographically untrusted**. Replacing a category through manual import is not a merge. No diagnostic data is uploaded to GitHub by catalogue synchronization.
