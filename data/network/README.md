# Network flow catalogue — single source of truth

**Production (Ed25519 signed v6):** [network-flows.csv](network-flows.csv) and [network-flows.manifest.json](network-flows.manifest.json), with **480 rows in 16 categories**, published together after Android, Windows and macOS 1.1.3 releases passed their build and test workflows.

The previous signed v5 files (434 rows) and transitional Samsung/unified/v6 snapshot CSVs are preserved in Git history, **not** as parallel editable files. From this point forward, maintain only the canonical CSV + manifest pair.

## Stable CSV schema

The CSV must be UTF-8, at most 1 MiB and 5,000 rows, with this exact column order:

```csv
id,category,name,host,port,protocol,execution_point,region,testability,purpose,reference
```

Each ID must be unique and match `[a-z0-9-]+`. `host` must be a concrete hostname without scheme/path or wildcard. The `reference` must be an HTTPS source. Explain optional services, source authority and regions in `purpose`.

## Android, OEM and MDM categories

| Category | Purpose |
| --- | --- |
| `device:android` | Shared Android Enterprise, Google Play, enrollment, FCM, content and Google updates |
| `device:samsung` | Samsung Knox **device** services: KME, Knox Configure, E-FOTA, licensing, optional Asset Intelligence and Remote Support |
| `mdm:knox-manage` | **Independent Samsung Knox Manage MDM**, with client and separate server/provider flows |
| `device:motorola` | Motorola OEM-specific services (currently community-sourced CDS OTA DNS/TCP) |
| `device:crosscall` | Crosscall OEM-specific services; verified OTA service hostnames are not yet available |
| Other `device:*` | Apple, macOS, Windows, Android AOSP Teams Rooms, optional VoWiFi/ePDG |
| Other `mdm:*` | Intune, Omnissa Workspace ONE, Ivanti, Meraki, Citrix and BlackBerry |

Samsung, Motorola and Crosscall device profiles combine the shared `device:android` category **plus** their own OEM category. Do not duplicate Google services unless a distinct context requires it. Knox Manage is **never** automatically part of the general Samsung device profile.

### Client versus server and confidence

An active test requires **both** `execution_point=DEVICE` and `testability=testable`. Entries marked `MDM_SERVER`, `server-side flow`, `wildcard required`, `documentation only`, or another reference status must not generate device-side success claims.

- An admin web portal is not a handset connectivity dependency.
- Server-to-FCM/APNs or S3 management traffic is not an outgoing device flow.
- Region-specific, tenant-specific or optional products must not be treated as mandatory for every device.
- TCP/DNS connectivity does not prove enrollment, actual push delivery, software-update availability or a successful HTTP API transaction.
- Motorola `moto-cds.appspot.com:443` is documented by [a community GitHub project](https://github.com/FixeQD/motorola-update), **not by Motorola as a comprehensive firewall rule**. This app checks only network reachability: no OTA POST, IMEI, serial number or build GUID sent. Crosscall OEM OTA destinations remain unconfirmed.

## Diagnostic engine handling since app 1.1.4

The signed v6 CSV is an auditable **reference catalogue**, not a promise that every documented port will accept a generic TCP probe. App 1.1.4 does not execute the misleading `TCP/5228–5230` combinations on `android.apis.google.com` or `*.googleapis.com` REST API hosts. FCM device push transport checks against `mtalk.google.com` remain active. It also deduplicates Android common services when users select Android alongside Samsung, Motorola or Crosscall.

A TCP timeout is an **inconclusive WARN**, not proof of a carrier/firewall block; TLS handshake failures are warnings with the actual exception detail; HTTP 4xx after valid TLS confirms network reachability but **not** an application-level success. CSV diagnostic exports include the active catalogue source and verified remote catalogue version.

When preparing the next signed catalogue v7, review currently documented API/FCM-port pairings against authoritative endpoint/port requirements, and classify inapplicable combinations as documentation-only or remove them. **Do not modify the already signed canonical v6 file without an incremented, correctly signed manifest.**

## Procedure for every future flow update

1. Confirm manufacturer documentation or a credible reference, the source (device vs server), host, protocol, port, region, service applicability and confidence.
2. Edit **only** `data/network/network-flows.csv` on an approved branch, retaining the exact schema and unique IDs. Examples: `device-motorola-004`, `device-crosscall-003`. Do not invent OEM hosts.
3. Increment the `version` field (next **v7**), calculate SHA-256 of the **exact new CSV bytes**, and sign `<version>\\n<sha256>\\n` with the **existing encrypted v6+ Ed25519 private key** using `tool/sign_network_catalog.py` from the private repo. Never regenerate a key for ordinary CSV additions, publish the private key, or type its passphrase in CI logs.
4. Commit **both** canonical CSV and signed manifest **atomically** in one Git commit, and let [.github/workflows/validate-network-catalog.yml](../../.github/workflows/validate-network-catalog.yml) verify the schema and Ed25519 signature.
5. On a supported client, refresh the catalogue, verify the reported version, and test offline cache/fallback. Add a new app release only when schema, category support, security public key or probe logic changes.

Existing v1–v5 signatures use the legacy public key; v6 and newer use the rotated one. Current application release **1.1.3** trusts both. Apps 1.1.2 and earlier cannot use v6: upgrade them, rather than weakening verification. Local manual CSV imports remain user-approved and **unsigned**; importing a category replaces rather than merges its records.
