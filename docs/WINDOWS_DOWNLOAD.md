# Windows portable download and installation

MDM SystemCheck is distributed for Windows as a portable **x64 ZIP**. It is the only supported Windows package; MSIX and Microsoft Store publication are discontinued.

## Download

- [Stable Windows releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.3), version 1.1.3.
- [Development Windows release](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/latest-windows-dev), for testing only.
- Choose **`MDM-SystemCheck-Windows-x64.zip`** and **`SHA256SUMS-windows.txt`** under Assets. Android APK downloads remain on the separate Android release pages.

## Install and run

1. Download the ZIP and its SHA-256 checksum from this public GitHub repository.
2. On Windows, right-click the ZIP and select **Extract All**. Keep all DLLs and the `data` directory alongside the executable; do not run the program inside the ZIP archive.
3. Open the extracted directory and run `mdm_system_check.exe`. Administrator access is not required by the application, but organizational security policies may restrict execution.
4. The application stores its diagnostic history, settings, and internal state locally. You can export CSV reports intentionally and choose a local network-flow CSV for manual import.

## Exporting CSV reports

Select **Save to device** after a diagnostic. Windows opens a native **Save As** dialog starting in Downloads; save there or choose another directory. This replaces the previous behavior of saving files inside AppData. Report filenames follow `mdm_diagnostic_YYYYMMDD_HHMMSS.csv` by default.

## Windows application identity

Starting with Windows 1.1.1, the official SystemCheck icon appears on the executable and taskbar. Application metadata identifies `ivanboi` and `MDM SystemCheck`, replacing Flutter's generated `com.example`. Existing diagnostic history or settings in the previous AppData path are not automatically migrated or deleted.

## Integrity and Windows security

The ZIP's executable is **not Authenticode-signed**. See the [Windows signing guide](WINDOWS_SIGNING.md) for future signature verification and certificate limitations.


The Windows ZIP is **not digitally signed**. GitHub SHA-256 checksums check integrity only; they do not authenticate the publisher or replace code signing.

You can verify the download in PowerShell:

```powershell
(Get-FileHash .\MDM-SystemCheck-Windows-x64.zip -Algorithm SHA256).Hash
Get-Content .\SHA256SUMS-windows.txt
```

The hashes should match (case-insensitive). If SmartScreen or antivirus blocks the program, check the source and contact your IT/security administrator. **Do not disable system protections to run the app.**

## Updating

Check [Windows GitHub Releases](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases?q=windows-v) for a newer stable version. Download and extract the new ZIP into a new folder; close the previous application before replacing files. In-app automatic updates are not implemented yet. The [Windows v1.1.1 public ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.3) remains unsigned; a release SHA-256 is an integrity check, not an Authenticode signature.

## Known limits

- Windows download is x64 only. A separate [universal macOS 1.1.1 ZIP](MACOS_DOWNLOAD.md) is also published.
- Existing DNS/TCP/HTTP(S)/NTP tests run on the Windows computer, not on a remote phone.
- Manual network-flow CSV import is available, but automatic GitHub catalogue synchronization is not.
- Windows-specific BitLocker, Defender, Entra ID, Intune enrollment, TPM and Secure Boot checks are not yet implemented.
- Google Play Integrity and the integrated VirusTotal WebView remain Android-only.

## No MSIX / Microsoft Store distribution

The Windows MSIX and Microsoft Store publication paths were **abandoned** on 23 November 2026. The public GitHub portable ZIP above is the **only supported Windows download**. The current workflow generates no MSIX. Older unsigned MSIX files retained in private historical releases are legacy archives, not installation options. There are no planned Microsoft Store links or Store updates.
