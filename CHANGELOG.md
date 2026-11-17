# Changelog

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
