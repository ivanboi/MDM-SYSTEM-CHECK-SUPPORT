# Changelog

## Network catalogue v9 — 24 November 2026 (data-only)

Catalogue v9 (24 November 2026): 522 records in 18 categories, automatically signed and published using the existing Ed25519 key. Retrieval confirmed by the maintainer on Android APK and Windows Win32. Native macOS retrieval is maintainer-confirmed; post-update APNs/enrollment connectivity tests remain pending. Six legacy APNs gateway records are documentation-only and 15 records were added, including fallback, provider-only references and macOS enrollment paths. The v8 Motorola and Crosscall additions remain available. Network reachability does not prove enrollment, OTA availability or push delivery. Source version 1.1.6+42 includes cache bypass, one checksum-mismatch retry and detailed sync errors; Android, Windows and macOS public 1.1.6 binaries are confirmed; Google Play rollout is separate.

## Application 1.1.6+42 — source update (build publication pending verification)

- Bypass stale HTTP cache entries, retry the manifest/CSV pair once on checksum mismatch and expose specific error reasons.
- Preserve Ed25519 signature, SHA-256, schema and rollback checks and the last verified catalogue.
- Android APK, Windows portable ZIP and macOS universal ZIP release builds have been requested; Google Play AAB submission remains separate.

## Network catalogue v8 — 24 November 2026 (data-only)

Catalogue v8 (24 November 2026): 507 records in 18 categories, published automatically with the existing Ed25519 key. Android confirmed verified GitHub catalogue v8 with zero manual entries. Windows/macOS runtime refresh and new OEM reachability tests remain pending. Four maintainer-provided Crosscall FOTA records (two active, two historical) and six Motorola additions (five active, one staging reference) are included. Carrier applicability varies. These are connectivity checks, not OTA transactions or independently verified vendor allowlists.


## Android / Windows / macOS 1.1.5 — TLS diagnostics and manufacturer-specific profiles

- Distinguish TLS errors that **explicitly report** certificate hostname mismatch, expiry/not-yet-valid, untrusted certificate chain and other handshake failures. The OS error is preserved verbatim except for control-character sanitization; no TLS verification bypass is introduced.
- Restore the letters lost by an overly broad regex in the 1.1.4 TLS error reporting. Unknown handshake causes remain generic instead of asserting that a Microsoft server has a bad certificate.
- Rename the Motorola and Crosscall platform labels to `Motorola (specific servers)` and `Crosscall (specific servers)`.
- Add `ChromeOS (specific servers)` with official Google-documented enrollment, attestation and update checks; add `Fairphone (specific servers)` but do **not** perform unsupported Fairphone Gen. 6 OTA probes.
- Manufacturer-only profiles do not repeat the shared Android profile automatically. Select Android explicitly if shared Google/Android Enterprise requirements are relevant.
- Motorola OTA CDS `moto-cds.appspot.com:443` actually returned DNS PASS and TCP PASS in the 1.1.4 diagnostic export; this is connectivity only, not an OTA upgrade check.
- Catalogue **v7 signed Ed25519**: 497 rows in 18 categories. Adds 15 ChromeOS checks, two Fairphone documentation-only references and reclassifies 30 non-applicable Google API FCM-port combinations.
- The Android 1.1.5 signed APK can update a production-signed 1.1.4 APK; Google Play distribution of AAB remains a separate manual action.

## Android / Windows / macOS 1.1.4 — network diagnostic reliability

- Deduplicate shared Android Enterprise checks across multiple selected device profiles; Android and Motorola no longer repeat identical network-path probes.
- Stop treating Google API hosts on TCP/5228–5230 as standalone FCM-device socket destinations. Preserve valid `mtalk.google.com` push transport checks.
- Report non-conclusive TCP connection timeouts as **WARN**; they are not sufficient evidence of blocked firewall ports.
- Treat HTTP 4xx after a verified TLS session as proof of endpoint connectivity (**PASS**, but not proof of service/application availability); HTTP 5xx stays **WARN**.
- Display TLS handshake errors with their underlying diagnostic detail and without asserting that SSL interception has occurred.
- Add the verified network catalogue version and the active catalogue source to exported diagnostics.
- Keep the Ed25519-signed 480-row v6 catalogue and Android release keystore unchanged; no new key or CSV re-signing required.

## Android / Windows / macOS 1.1.3 — OEM profiles and signed catalogue migration

- Extend manufacturer diagnostics to Samsung, Motorola and Crosscall while preserving shared Android Enterprise paths.
- Keep Samsung Knox Manage separate from Samsung device service tests.
- Add community-documented Motorola OTA CDS host `moto-cds.appspot.com:443` as a **connectivity indicator only**, not an API-based OTA version query.
- Activate the 480-entry, 16-category signed CSV catalogue v6 at the canonical public CSV and manifest paths after successful release of 1.1.3 binaries.
- Rotate the signing key for v6+ and preserve the legacy public key for v1–v5 validation in the updated Flutter binaries.
- Preserve the historical signed v5 bytes in Git history. Old apps (1.1.2 and earlier) reject v6 and retain a validated v5 cache or bundled defaults until upgraded.
- Published Android signed APK, Windows portable ZIP and macOS ZIP 1.1.3 via successful independent CI workflows; Google Play rollout is not automatic.

## Windows ZIP-only distribution — 23 November 2026

- Discontinue Windows MSIX generation and Microsoft Store publication; remove MSIX package/dependency, manifest checks and duplicate private Windows release publication from the private source workflow.
- Continue Windows x64 releases **only** as portable ZIP and SHA-256 in public GitHub Releases, independent from Android APK and macOS universal ZIP.
- Older experimental private MSIX assets are **unsupported legacy archives** and have not been deleted; historical release notes are retained.
- Windows executable signing is still not configured; SmartScreen and enterprise policies may block execution.


## macOS v1.1.1 — universal GitHub ZIP published

- Add the native Flutter macOS desktop build pipeline and a ZIP containing the full application bundle with a separate SHA-256 checksum.
- Apply the official SystemCheck icon, macOS app identity and narrow file/network sandbox entitlements.
- Export CSV using native macOS Save As, starting in Downloads; perform local device-originating network diagnostics.
- Keep the macOS stable/development GitHub release tags independent from Android/Windows. macOS is not Developer ID signed or Apple notarized and may be blocked by Gatekeeper.
- The macOS stable ZIP and checksum have been verified in public GitHub Releases.


## Documentation verification — 23 November 2026

- Verified public Android 1.1.0 signed APK and SHA-256; Android Flutter source 1.1.1+36 does not indicate a newer Google Play release.
- Verified Windows 1.1.1 portable ZIP and SHA-256 as the public Windows distribution. The ZIP remains unsigned; MSIX is retained privately for optional Store submission.
- Aligned version labels, platform availability and maintenance guidance across both repositories without deleting historical stable documentation.


## Documentation maintenance and signing clarification — 23 November 2026

- Confirm current public stable binaries: Android 1.1.0 and portable Windows 1.1.1, with SHA-256 checksums.
- Clarify that the Windows executable is unsigned and that seller verification in Partner Center is not an Authenticode code-signing certificate.
- Correct stale release/PR references, keep historical stable release notes and direct maintenance cleanup only at redundant private CI prereleases.

## Windows v1.1.1 — official icon and accessible CSV reports

- Replace Flutter's default Windows taskbar and executable icon with the SystemCheck logo.
- Use a native Windows **Save As** dialog, initially in Downloads, for diagnostic CSV exports; users can choose the destination and filename.
- Update the Windows app's CompanyName / ProductName from generated `com.example` branding to `ivanboi` / `MDM SystemCheck`. Older AppData remains untouched.
- Publish a new portable Windows ZIP and checksum under `windows-v1.1.1`. The Microsoft Store MSIX remains private, Android release tags remain separate.


## Windows portable distribution — v1.1.0

- Publish the Flutter Windows x64 portable ZIP with SHA-256 checksums in **public support GitHub Releases**, independently from the Android APK release.
- Separate stable `windows-v1.1.0` and development `latest-windows-dev` release channels. Windows releases do not overwrite Android's `v1.1.0` release.
- Retain the unsigned Microsoft Store MSIX privately for future Store submission; it is not a Windows installer or public download.
- Document ZIP extraction, Windows SmartScreen and enterprise security policy limitations, and manual update checks via GitHub Releases.


## Microsoft Store identity registration — 23 November 2026 (no Store release)

- Verified Microsoft Partner Center product `9N9Z3PCL3MG1` and exact Windows package identity `ivanbillyjean.MDMSystemCheck`.
- [PR #27](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/27) adds a Store submission MSIX (`1.1.0.0`) and manifest verification in Windows CI. No Microsoft Store listing or approved MSIX exists yet.
- Public Git tag `v1.1.0` exists; signed APK assets and Google Play rollout require separate checks.

## Android 1.1.0 (build 35) — source merged; artifact publication requires verification

- Offline import of network-flow CSV files from local device storage, including schema validation, activation confirmation, category-specific overrides, persistence and restoring the built-in catalogue.
- Initial Flutter Windows desktop foundation and CI compilation, **not** Microsoft Store distribution.
- Preserve existing Android Play Integrity and VirusTotal flows.
- The GitHub public CSV reference remains **manual only**: automatic remote downloads and signed-manifest synchronization are not implemented.
- The signed Android release pipeline was requested from the source repository; availability of a public APK and AAB must be verified independently before distribution.

## Documentation and catalogue updates — 23 November 2026 (no new app release)

- Published the [225-record network reference CSV](data/network/network-flows.csv) and GitHub Actions schema validation in the public support repository.
- Documented the manual local CSV import ([merged private PR #25](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/25)), Windows desktop build ([merged private PR #22](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/22)), macOS plans, and future signed GitHub catalogue synchronization.
- No new Android APK/AAB, Microsoft Store package, or macOS installer is represented by this documentation update.

## v1.0.9 — Signed release with streamlined delivery (build 34)

November 17, 2026 · [Release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.0.9)

- Package the validated Android app with the VirusTotal WebView for Google Play.
- Publish the matching signed APK and checksum through the combined build and publication workflow.
- Refresh the English documentation, privacy notice and security guidance.
- The maintainer uploads the signed AAB to Google Play and manages its production review and rollout.

## v1.0.8 — VirusTotal file scanning on Google Play build (build 33)

- Enable the existing **Scan with VirusTotal** screen in the Google Play build.
- Open the Android document picker from the embedded VirusTotal page and offer **Open in browser** when sign-in is required.

## v1.0.7 — VirusTotal in SystemCheck (build 32)

- Display the official VirusTotal page below a SystemCheck app bar.
- Open the Android document picker from **Choose file**.
- Keep **Open in browser** available for external sign-in and recovery.

## v1.0.6 — VirusTotal browser integration (build 31)

- Open the official VirusTotal upload page from **Scan with VirusTotal** below **Google Play Integrity**.
- Use an Android Custom Tab when available, with the external browser as a fallback.
- Remove the in-app API key field and direct file submission. VirusTotal handles sign-in, uploads, terms, and reports on its website.

## v1.0.5 — VirusTotal File Reputation (build 30)

- Add **File Reputation** below **Google Play Integrity** in the signed GitHub APK.
- Look up existing VirusTotal reports by SHA-256 or submit a file up to 32 MB with per-upload confirmation and acceptance of VirusTotal's Terms of Service.
- Publish the signed APK and checksum on the stable GitHub channel.

## v1.0.4 — Play Integrity server migration (build 29)

- Send Play Integrity verification requests to the MDM SystemCheck server hosted on OVH.
- Keep network diagnostic reports and CSV exports on the device unless you choose to share them. See the [privacy policy](PRIVACY.md) for the integrity data flow.

## v1.0.3 — Google Play Integrity diagnostics (build 28)

November 7, 2026 · [Public release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.0.3)

- Added a user-initiated Google Play Integrity check for app recognition, licensing and device integrity signals.
- Connected the Android app to the verification service. See the [privacy policy](PRIVACY.md) for this data flow.
- Published the signed APK and checksum from the same verified build as the AAB.
- End-to-end Play Integrity validation requires installation through the Google Play test track.

## v1.0.2 — Stable public distribution (build 27)

November 4, 2026 · [Public release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.0.2)

- Published the signed Android APK in the public support repository, with a SHA-256 checksum in `SHA256SUMS.txt`.
- Established separate Stable and Development release channels.
- Kept the existing production signing key and application behavior.

For an in-place update, install the stable APK over an installation signed with the same key. Uninstalling an app signed with a different key can erase local data.

## v1.0.1 — Android production signing (build 26)

Release date: November 4, 2026.

- Introduced persistent production signing for Android APKs and AABs.
- Secured the signing keystore and credentials using GitHub Actions secrets in the private source repository.
- Added automatic APK signature verification to the continuous integration pipeline.
- Validated the signed Android update process without changing application functionality.

This release was distributed through the private source repository.

See [public releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases) for current downloads.

## Linux x86-64 stable (1.1.6+42)

The initial isolated Linux build was superseded by the successful build on private `main`. It does not change the Android, Windows or macOS release channels. Published assets: AppImage, Debian package and portable tar.gz bundle with SHA-256 checksums. Packages are unsigned; GPG signing is not yet configured. CI publication and stable promotion succeeded; manual Linux validation remains pending. Check [public releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=linux-v) before downloading. Ubuntu 22.04+ and compatible Debian/Linux Mint x86-64 environments are initial test targets, not certified compatibility. Verify checksums using `sha256sum -c SHA256SUMS-linux.txt`; run AppImage after `chmod +x`, or install the DEB with `sudo apt install ./MDM-SystemCheck-Linux-x64.deb`. Google Play Integrity and embedded VirusTotal are Android-only. Linux CSV export, catalogue v9 retrieval and desktop functionality remain to be tested. No Linux-specific device catalogue changes are included.

## Platform release workflow split

The private main branch contains a manual Release Manager (`.github/workflows/release-manager.yml`) with independent Android, Windows, macOS and Linux selections, all disabled by default. Android test APK and Google Play production AAB use separate private workflows. Android, Windows and macOS no longer build on ordinary pushes. PR CI runs analysis and tests only. The signed catalogue workflow remains independent. Linux is manual-only and accepts the expected version, development/stable channel and explicit publication selection. Linux 1.1.6 stable assets are published; manual runtime validation remains pending.

Verified public 1.1.6 downloads: [Android APK](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6), [Windows ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6), [macOS ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6). Signed Android AAB is available in the private CI artifact; Play Store rollout is separate. Linux stable publication succeeded; manual validation remains pending. Existing stable releases and catalogue v9 are unchanged.

## Current release status — 1.1.6+42 (24 November 2026)

Android, Windows, macOS and Linux stable 1.1.6 releases are verified on GitHub. Linux x86-64 1.1.6 preview has passed analysis, tests, native build, packaging and publication; its AppImage, DEB, portable tar.gz and SHA-256 file are available. Stable promotion succeeded using the same verified binaries without rebuilding; the stable tag and all four assets are verified. Linux packages are unsigned and manual desktop compatibility, CSV export and catalogue retrieval remain unverified.

| Platform | Verified download |
| --- | --- |
| Android signed APK | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/v1.1.6) |
| Windows x64 ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.6) |
| macOS ZIP | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.6) |
| Linux x64 | [1.1.6 stable](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/linux-v1.1.6) |

Android AAB is signed and available privately from CI run 45411459034; Google Play rollout is separate. Catalogue v9 remains independent and unchanged. No other platform needs rebuilding for Linux promotion.


## Maintainer validation and CI status

The maintainer confirms Google Play publication of 1.1.6+42 and catalogue v9 retrieval on macOS (24 November 2026). Linux desktop acceptance remains pending. The release manager now supports independent APK and AAB inputs, dynamic Linux version and development/stable channels, and optional Linux publication (default false); no platform distribution builds are triggered by ordinary pushes. Linux validation-only and separate Android APK/AAB workflows passed. Future Linux publication remains to be tested. The public [release manifest](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/blob/main/releases.json) records verified stable public assets; it has a metadata-only refresh workflow, pending first execution, and existing clients are unchanged.


## Android distribution policy — 24 November 2026

The independent Android test APK and production AAB workflows both passed analysis, tests, signature verification and private artifact upload (run 45429919328). Future test APKs are private; production AABs are private and uploaded manually to Google Play. Existing historical public APK releases remain available, but are not the production update channel. Windows, macOS and Linux distribution is unchanged. The public releases.json manifest is refreshed by a metadata-only workflow; Android APK metadata describes historical public releases, not Google Play rollout. Linux runtime acceptance is pending.
