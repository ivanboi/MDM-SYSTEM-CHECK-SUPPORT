# Changelog

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
