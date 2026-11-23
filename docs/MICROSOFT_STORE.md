# Windows distribution — Microsoft Store / MSIX discontinued

_Updated 23 November 2026. This legacy document path remains to preserve links._

**MDM SystemCheck has abandoned the Windows MSIX and Microsoft Store distribution path.** There is no planned Microsoft Store release, certification, sideloaded MSIX, or user installation through Partner Center. The formerly reserved Microsoft Store product identity is historical account metadata, **not** a current distribution endpoint.

## Supported Windows download

The only supported format is the official [Windows 1.1.1 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1):

- `MDM-SystemCheck-Windows-x64.zip` — extract all files, then run `mdm_system_check.exe`.
- `SHA256SUMS-windows.txt` — integrity comparison only; it does **not** authenticate the publisher.

See [Windows installation](WINDOWS_DOWNLOAD.md) and [Windows signature status](WINDOWS_SIGNING.md). The Windows executable is not Authenticode-signed and can be blocked by SmartScreen or corporate policies. Do not disable system protection globally.

## Technical changes

The private Flutter build no longer depends on the `msix` package, contains a Store `msix_config`, runs `dart run msix:create`, verifies an MSIX manifest, or generates MSIX checksums. Its Windows workflow now publishes **only** the portable ZIP and SHA-256 to the public GitHub support repository. Public stable tags use `windows-v<version>`; development uses `latest-windows-dev`.

## Legacy release records

Earlier private GitHub Windows releases have experimental unsigned MSIX files. They are historical artifacts only, **not supported downloads**; no new MSIX files will be generated. The historic files have not been deleted as part of this documentation change.

The Microsoft Store registration historically used product ID `9N9Z3PCL3MG1`, package identity `ivanbillyjean.MDMSystemCheck` and publisher `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A`. These values are preserved here solely for historical traceability and should not be used as current installation instructions.

Other platform distribution remains unchanged: Android signed APK / manually uploaded Google Play AAB, and an unnotarized universal macOS ZIP on GitHub.
