# Windows application signing status and verification

_Last reviewed: 23 November 2026._

## Current download

The official [Windows 1.1.1 portable ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) is **not Authenticode-signed**. The published `SHA256SUMS-windows.txt` lets you check that your downloaded archive matches the release, but SHA-256 alone does not prove who published or built the application.

Windows SmartScreen, antivirus, and corporate policies may block unsigned executables. Do **not** disable your security protections to run MDM SystemCheck. If you are using a managed device, ask your IT administrator before proceeding.

## Could the application be signed?

Yes. The maintainer can sign the compiled Windows executable with an Authenticode certificate issued by a trusted CA (or an eligible managed signing service) **before** building the ZIP. An accompanying trusted timestamp helps preserve signature validation after the signing certificate expires.

- **Self-signed certificates:** suitable for controlled internal testing only; not trusted automatically on public computers.
- **Azure Artifact Signing:** managed signing for qualifying organizations in the EU/USA/Canada/UK and qualifying individuals in the USA/Canada; Public Trust enrollment for individual applicants in France is not currently offered.
- **Traditional CA code-signing certificate:** an OV/individual-validation option may be appropriate for an individual developer in France, subject to issuer verification, cost and hardware/HSM key controls.
- **Microsoft Store signing:** only applies after successful Store certification; the Store route is deferred and is separate from the GitHub ZIP.

Signing does not guarantee an immediate absence of SmartScreen warnings; software/publisher reputation grows over time.

**No trusted signing certificate has been configured for the published Windows binaries.** Do not interpret the Microsoft Partner Center seller verification as certificate issuance.

## Checking signatures in future releases

When a future release is explicitly marked **signed**, Windows users can inspect the signature in File Explorer (**Properties → Digital Signatures**) or use Microsoft's SignTool on a trusted Windows system:

```powershell
signtool verify /pa /v .\mdm_system_check.exe
```

If the Digital Signatures tab is absent or verification fails, treat the binary as unsigned and follow your organization's security rules. The ZIP checksum must be recalculated **after** any executable signing.

## Official references

- [Microsoft Windows code-signing options](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/code-signing-options)
- [Microsoft SmartScreen reputation](https://learn.microsoft.com/en-us/windows/apps/package-and-deploy/smartscreen-reputation)
- [Download and install Windows](WINDOWS_DOWNLOAD.md)
- [Security policy](../SECURITY.md)
