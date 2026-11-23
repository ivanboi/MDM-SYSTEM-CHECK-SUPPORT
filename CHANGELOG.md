# Changelog

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
