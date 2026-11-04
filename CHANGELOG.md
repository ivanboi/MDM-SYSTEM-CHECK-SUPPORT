# Changelog

## v1.0.1 — Android production signing (build 26)

Release date: November 4, 2026.

- Introduced persistent production signing for Android APKs and AABs.
- Secured the signing keystore and credentials using GitHub Actions secrets in the private source repository.
- Added automatic APK signature verification to the continuous integration pipeline.
- Validated the signed Android update process without changing application functionality.

**Installation:** Download the signed APK from the [v1.0.1 GitHub Release](https://github.com/ivanboi/MDM-SYSTEM-CHECK/releases/tag/v1.0.1). In-place updates require the installed app to use the same signing key. If an older installation was signed with a different key, reinstalling may be required and may erase locally stored application data.

**Distribution:** Official release artifacts are hosted in the private source repository. Users without access should obtain the APK through an authorized distribution channel; the support repository does not expose private binaries or signing credentials.

## Previous releases

See the [project release history](https://github.com/ivanboi/MDM-SYSTEM-CHECK/releases) if you have repository access.
