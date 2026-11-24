# Network flow catalogue — single source of truth

**Production (Ed25519 signed v9):** [network-flows.csv](network-flows.csv) and [network-flows.manifest.json](network-flows.manifest.json), with **522 rows in 18 categories**, published atomically and retrieval confirmed on Android and Windows. Android app 1.1.5+41 is required to recognize the new ChromeOS and Fairphone categories.

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
| `device:crosscall` | Crosscall OEM-specific FOTA services; two active maintainer-provided endpoints and two historical references |
| `device:chromeos` | Google-documented ChromeOS enterprise enrollment, device attestation, update metadata and download hosts (15 testable targets) |
| `device:fairphone` | Fairphone Gen. 6-specific OTA host not verified; two documentation-only records, including a legacy FP2 warning; do not probe as Gen. 6 OTA |
| Other `device:*` | Apple, macOS, Windows, Android AOSP Teams Rooms, optional VoWiFi/ePDG |
| Other `mdm:*` | Intune, Omnissa Workspace ONE, Ivanti, Meraki, Citrix and BlackBerry |

Samsung combines shared `device:android` with its OEM category; Motorola and Crosscall require separate Android selection. Do not duplicate Google services unless a distinct context requires it. Knox Manage is **never** automatically part of the general Samsung device profile.

### Client versus server and confidence

An active test requires **both** `execution_point=DEVICE` and `testability=testable`. Entries marked `MDM_SERVER`, `server-side flow`, `wildcard required`, `documentation only`, or another reference status must not generate device-side success claims.

- An admin web portal is not a handset connectivity dependency.
- Server-to-FCM/APNs or S3 management traffic is not an outgoing device flow.
- Region-specific, tenant-specific or optional products must not be treated as mandatory for every device.
- TCP/DNS connectivity does not prove enrollment, actual push delivery, software-update availability or a successful HTTP API transaction.
- Motorola `moto-cds.appspot.com:443` is documented by [a community GitHub project](https://github.com/FixeQD/motorola-update), **not by Motorola as a comprehensive firewall rule**. This app checks only network reachability: no OTA POST, IMEI, serial number or build GUID sent. Additional Motorola and Crosscall destinations are maintainer-provided; independent vendor verification remains pending.

## Historical changes in signed catalogue v7 (superseded by v8)

- **497 rows in 18 categories**: 15 new testable Google-documented `device:chromeos` hosts; 2 documentation-only `device:fairphone` references. In v7, no proprietary Fairphone Gen. 6 or Crosscall OTA host was treated as an active destination; v8 subsequently added maintainer-provided Crosscall checks.
- Motorola OTA connectivity to `moto-cds.appspot.com:443` was actually exercised in the 1.1.4 network diagnostic export: DNS and TCP passed. This does not authenticate or execute the OTA update check.
- Motorola and Crosscall profiles are explicitly **specific servers**; select the `Android` device profile separately for shared Android Enterprise/Google dependencies. Samsung intentionally includes its shared Android Enterprise checks plus Knox manufacturer services.
- Thirty `device:android` rows for generic Google REST API endpoints on FCM-style ports 5228–5230 are now `documentation only`. Their active use produced false-positive timeouts; appropriate FCM device messaging remains under `mtalk.google.com`.
- The v7 manifest was signed offline using the existing rotated Ed25519 private key; the CSV and manifest were committed in one atomic Git tree update. At that time no private key or passphrase was stored in GitHub; v9 introduced private-repository Actions secrets.
- Keep all future platform endpoints supported by authoritative sources. Unknown/legacy manufacturer URLs should be documentation-only or omitted rather than tested as mandatory.

## Diagnostic engine handling since app 1.1.4

The signed v9 CSV is an auditable **reference catalogue**, not a promise that every documented port will accept a generic TCP probe. App 1.1.4 does not execute the misleading `TCP/5228–5230` combinations on `android.apis.google.com` or `*.googleapis.com` REST API hosts. FCM device push transport checks against `mtalk.google.com` remain active. It also deduplicates Android common services when profiles overlap. As of 1.1.5, Motorola and Crosscall do not automatically inherit Android, while Samsung retains common Android checks.

A TCP timeout is an **inconclusive WARN**, not proof of a carrier/firewall block; TLS handshake failures are warnings with the actual exception detail; HTTP 4xx after valid TLS confirms network reachability but **not** an application-level success. CSV diagnostic exports include the active catalogue source and verified remote catalogue version.

Do not edit the live signed CSV independently of its manifest.

## Procedure for every future flow update

1. Confirm manufacturer documentation or a credible reference, the source (device vs server), host, protocol, port, region, service applicability and confidence.
2. Submit reviewed ID-based CSV upserts in the private source repository `tool/catalog-changes/` directory. The publisher merges these with the canonical CSV; removing a patch row does not delete a live record.
3. The private Actions workflow automatically increments the version, signs using the existing Ed25519 key stored in repository secrets, and validates the result.
4. It publishes the CSV and manifest atomically to support main. Check the public validation workflow. Never commit or expose signing secrets.
5. On a supported client, refresh the catalogue, verify the reported version, and test offline cache/fallback. Add a new app release only when schema, category support, security public key or probe logic changes.

Existing v1–v5 signatures use the legacy public key; v6 and newer use the rotated one. Current application release **1.1.5** trusts both and recognizes all 18 catalogue categories. Apps 1.1.3–1.1.4 lack v7's new categories and preserve a last-good catalogue. Apps 1.1.2 and earlier cannot use v6+: upgrade them, rather than weakening verification. Local manual CSV imports remain user-approved and **unsigned**; importing a category replaces rather than merges its records.

## Signed catalogue v8 (historical)

Catalogue v8 (24 November 2026): 507 records in 18 categories, published automatically with the existing Ed25519 key. Android confirmed verified GitHub catalogue v8 with zero manual entries. Windows/macOS runtime refresh and new OEM reachability tests remain pending. Four maintainer-provided Crosscall FOTA records (two active, two historical) and six Motorola additions (five active, one staging reference) are included. Carrier applicability varies. These are connectivity checks, not OTA transactions or independently verified vendor allowlists.


## Current catalogue and release status

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval and post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v8 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; public 1.1.6 binaries and Google Play rollout are not yet confirmed.
