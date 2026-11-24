# macOS portable download and installation

The macOS edition of MDM SystemCheck is distributed through GitHub as a ZIP containing the complete **MDM SystemCheck.app** bundle. It does **not** use the Mac App Store.

**Release status:** **macOS 1.1.4 is published and verified**. GitHub Actions successfully compiled a universal app and verified the stable ZIP and its SHA-256.

## Downloads

- [macOS stable v1.1.4](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/releases/tag/macos-v1.1.4), **published**.
- Development builds use the `latest-macos-dev` tag when one is published; no public development assets were verified in this audit.
- Assets: `MDM-SystemCheck-macOS.zip` and `SHA256SUMS-macos.txt`.

## Installation

1. Download the ZIP and checksum from this repository's official GitHub Releases page.
2. Unzip the archive: it contains **MDM SystemCheck.app**.
3. Move the complete application bundle into a user-writable location (such as your Applications folder, if permissions allow).
4. Launch the application only if macOS security policy permits it. Administrator rights are not required by the application's own code, but macOS protection or enterprise policy may prevent launch.

### Important Apple security limitation

**This macOS distribution is not Apple Developer ID signed and not notarized.** Gatekeeper and managed-security policies can refuse to open it. Never disable Gatekeeper, SIP, XProtect, or company-wide protections globally to run it. A ZIP SHA-256 checksum establishes file integrity only, **not the publisher's identity**. A publicly trusted macOS installation experience will require Developer ID signing and Apple notarization in a later release.

## Download integrity

Run in Terminal from the directory containing the downloaded files:

```sh
shasum -a 256 MDM-SystemCheck-macOS.zip
cat SHA256SUMS-macos.txt
```

The computed hex digest must match the release checksum.

## Features and limitations

- Diagnostics run **on this Mac**, checking local DNS, TCP, HTTP(S), NTP, and selected network endpoints.
- A local network-flow CSV can be imported through the system file picker, explicitly approved by the user.
- **Save to device** opens the macOS **Save As** dialog initially in Downloads, where the user can choose another destination.
- The official SystemCheck icon and `com.ivanboi.mdmsystemcheck` app identity are applied during the macOS build.
- Google Play Integrity and the embedded VirusTotal WebView are Android-only; neither is available in the macOS app.
- No macOS MDM enrollment audit, FileVault, Secure Enclave, or local endpoint security compliance assessment is implemented.
- In-app automatic updates and notarization are not yet implemented.
- The initial CI build was verified with `lipo -archs` and contains **x86_64 and arm64**, i.e. a universal application for Intel and Apple Silicon Macs.

[Public support](../README.md) · [Security](../SECURITY.md) · [Privacy](../PRIVACY.md)
