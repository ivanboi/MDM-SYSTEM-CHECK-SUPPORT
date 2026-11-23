# MDM SystemCheck — Windows / Microsoft Store

_Last reviewed: 23 November 2026._

## Registration

The developer's Microsoft Partner Center profile is verified, and the Windows app product has been created. The **public Windows distribution is the GitHub portable ZIP 1.1.1**, not the Microsoft Store. The unsigned Store MSIX is held privately for possible later submission.

| Field | Product identity |
| --- | --- |
| Public product name | MDM SystemCheck |
| Store ID | `9N9Z3PCL3MG1` |
| Package/Identity/Name | `ivanbillyjean.MDMSystemCheck` |
| Package/Identity/Publisher | `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A` |
| PublisherDisplayName | `ivan_billyjean` |
| Package Family Name | `ivanbillyjean.MDMSystemCheck_hgbzc83p2bnep` |

A Store deep link and web listing are **not available until the application is published**. The Package SID is unnecessary for users or package configuration.

## Preferred Windows delivery

No certificate or signing credentials are available for public Authenticode signing. The public GitHub ZIP remains unsigned. See [Windows signing status](WINDOWS_SIGNING.md).

The **portable ZIP on GitHub** is the default Windows distribution, not a Microsoft Store MSIX. Download the [Windows ZIP](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/windows-v1.1.1) and follow the [installation instructions](WINDOWS_DOWNLOAD.md). GitHub also hosts a separate `latest-windows-dev` prerelease. Windows binaries are not Authenticode signed; Windows SmartScreen or company policy may prevent their execution.

The MSIX is retained in the private source repository solely for a possible future Partner Center submission. It is unsigned and must not be distributed as a public installer.

## Status of software releases

- Windows Flutter foundation is merged in [private source PR #22](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/22).
- The private source Windows workflow builds an unsigned Store-submission MSIX (`1.1.1.0`, x64) matching the product identity; Store publication is optional and deferred.
- The MSIX is kept privately; no Microsoft Store certification, accepted submission or live listing is confirmed.
- The portable Windows ZIP is the **primary public download**, separate from MSIX and Store certification.
- The public Android 1.1.0 signed APK and SHA-256 are verified. A private signed Android 1.1.1+36 AAB exists for manual Play Console submission; no Google Play rollout is confirmed.
- The macOS 1.1.1 universal .app ZIP and SHA-256 are publicly released; there is no PKG or Mac App Store release.

## Next steps to publish

1. If Microsoft Store publication is resumed, use the existing private Windows MSIX packaging workflow; the packaging changes are already merged.
2. Download a successful `mdm-systemcheck-msix-store-x64` Windows workflow artifact. A completed build may not produce a downloadable artifact when GitHub's storage quota is exceeded.
3. Check SHA-256 and package manifest identity. The MSIX must use the exact publisher and package identity above.
4. Test on Windows 11 and run relevant Windows App Certification Kit checks.
5. Upload the **unsigned Store submission MSIX** in the product's Microsoft Partner Center submission; complete description, artwork, age rating, privacy/support links, capabilities and market availability.
6. Await Microsoft certification and publication. Microsoft signs approved packages for Microsoft Store distribution.

Do not sideload the unsigned Store MSIX or claim the Microsoft Store app is available before certification.

## Product functions and data

Windows network tests originate from the user's computer and use the same Flutter diagnostic logic. The shared code includes optional local CSV import, but automatic signed GitHub catalogue synchronization is not yet implemented. Results remain local unless explicitly exported/shared. **OVH is reserved for Android's optional Google Play Integrity verifier.**

[Support and downloads](../README.md) · [Privacy](../PRIVACY.md) · [Security](../SECURITY.md) · [Network catalogue](../data/network/README.md)
