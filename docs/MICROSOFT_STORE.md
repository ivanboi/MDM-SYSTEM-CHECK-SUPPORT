# MDM SystemCheck — Windows / Microsoft Store

_Last reviewed: 23 November 2026._

## Registration

The developer's Microsoft Partner Center profile is verified, and the Windows app product has been created.

| Field | Product identity |
| --- | --- |
| Public product name | MDM SystemCheck |
| Store ID | `9N9Z3PCL3MG1` |
| Package/Identity/Name | `ivanbillyjean.MDMSystemCheck` |
| Package/Identity/Publisher | `CN=E87ADF9C-1FB7-4617-B741-0F0E1BE2C80A` |
| PublisherDisplayName | `ivan_billyjean` |
| Package Family Name | `ivanbillyjean.MDMSystemCheck_hgbzc83p2bnep` |

A Store deep link and web listing are **not available until the application is published**. The Package SID is unnecessary for users or package configuration.

## Status of software releases

- Windows Flutter foundation is merged in [private source PR #22](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/22).
- [Private source PR #27](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/27) prepares an unsigned Store MSIX (`1.1.0.0`, x64) matching the product identity. The Windows CI job passed, but full PR validation/merge remained pending at the last check.
- **No downloadable MSIX, Microsoft Store certification, accepted submission, or live listing is confirmed.**
- A portable Windows ZIP is a separate test distribution, **not** an MSIX or certified Microsoft Store build.
- Android source version `1.1.0+35` and public tag `v1.1.0` exist. Android APK artifacts and Google Play rollout must be verified separately.
- macOS ZIP/APP and PKG packages are planned, not released.

## Next steps to publish

1. Wait for the full PR #27 CI suite to pass and merge the validated packaging changes.
2. Download a successful `mdm-systemcheck-msix-store-x64` Windows workflow artifact. A completed build may not produce a downloadable artifact when GitHub's storage quota is exceeded.
3. Check SHA-256 and package manifest identity. The MSIX must use the exact publisher and package identity above.
4. Test on Windows 11 and run relevant Windows App Certification Kit checks.
5. Upload the **unsigned Store submission MSIX** in the product's Microsoft Partner Center submission; complete description, artwork, age rating, privacy/support links, capabilities and market availability.
6. Await Microsoft certification and publication. Microsoft signs approved packages for Microsoft Store distribution.

Do not sideload the unsigned Store MSIX or claim the Microsoft Store app is available before certification.

## Product functions and data

Windows network tests originate from the user's computer and use the same Flutter diagnostic logic. The shared code includes optional local CSV import, but automatic signed GitHub catalogue synchronization is not yet implemented. Results remain local unless explicitly exported/shared. **OVH is reserved for Android's optional Google Play Integrity verifier.**

[Support and downloads](../README.md) · [Privacy](../PRIVACY.md) · [Security](../SECURITY.md) · [Network catalogue](../data/network/README.md)
