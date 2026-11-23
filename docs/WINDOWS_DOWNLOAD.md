# Windows portable download and installation

MDM SystemCheck is distributed for Windows as a portable **x64 ZIP**. It does not need Microsoft Store, a Microsoft user account, or an MSIX package.

## Download

- [Stable Windows releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.0), version 1.1.0.
- [Development Windows release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-windows-dev), for testing only.
- Choose **`MDM-SystemCheck-Windows-x64.zip`** and **`SHA256SUMS-windows.txt`** under Assets. Android APK downloads remain on the separate Android release pages.

## Install and run

1. Download the ZIP and its SHA-256 checksum from this public GitHub repository.
2. On Windows, right-click the ZIP and select **Extract All**. Keep all DLLs and the `data` directory alongside the executable; do not run the program inside the ZIP archive.
3. Open the extracted directory and run `mdm_system_check.exe`. Administrator access is not required by the application, but organizational security policies may restrict execution.
4. The application stores its diagnostic results and settings locally. You can export CSV reports intentionally and choose a local network-flow CSV for manual import.

## Integrity and Windows security

The Windows ZIP is **not digitally signed**. GitHub SHA-256 checksums check integrity only; they do not authenticate the publisher or replace code signing.

You can verify the download in PowerShell:

```powershell
(Get-FileHash .\MDM-SystemCheck-Windows-x64.zip -Algorithm SHA256).Hash
Get-Content .\SHA256SUMS-windows.txt
```

The hashes should match (case-insensitive). If SmartScreen or antivirus blocks the program, check the source and contact your IT/security administrator. **Do not disable system protections to run the app.**

## Updating

Check [Windows GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=windows-v) for a newer stable version. Download and extract the new ZIP into a new folder; close the previous application before replacing files. In-app automatic updates are not implemented yet.

## Known limits

- Windows x64 only. macOS desktop builds are planned.
- Existing DNS/TCP/HTTP(S)/NTP tests run on the Windows computer, not on a remote phone.
- Manual network-flow CSV import is available, but automatic GitHub catalogue synchronization is not.
- Windows-specific BitLocker, Defender, Entra ID, Intune enrollment, TPM and Secure Boot checks are not yet implemented.
- Google Play Integrity and the integrated VirusTotal WebView remain Android-only.

## Microsoft Store

The product has been registered in Microsoft Partner Center, but the Store publication is deferred. The unsigned MSIX build is kept private and is **not offered for public installation**.

[Support](../README.md) · [Privacy](../PRIVACY.md) · [Security](../SECURITY.md)
