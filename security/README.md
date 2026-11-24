# Linux release verification

The MDM SystemCheck release signing identity uses an Ed25519 certification primary key and a dedicated Ed25519 signing subkey.

- Identity: MDM SystemCheck Releases
- Primary fingerprint: `22DDA2AC2133E3A88761A375F4A9039C27F8CCEA`
- Signing subkey fingerprint: `E91CE726DB5445BF43F4203EA858D0BEF8883115`
- Public key: [MDM-SystemCheck-public.asc](MDM-SystemCheck-public.asc)
- Fingerprint: [fingerprint.txt](fingerprint.txt)

The signing workflow was successfully validated on private Linux 1.1.6 build artifacts on 24 November 2026. The existing public Linux 1.1.6 binaries have not been replaced or retroactively signed by this documentation change. Do not assume a release is signed unless its detached signature is present and valid.

For a signed release, download the public key above and the release's packages, SHA256SUMS-linux.txt and SHA256SUMS-linux.txt.asc. Compare the primary fingerprint with an independently trusted maintainer source before importing.

```sh
gpg --show-keys --with-fingerprint MDM-SystemCheck-public.asc
gpg --import MDM-SystemCheck-public.asc
gpg --verify SHA256SUMS-linux.txt.asc SHA256SUMS-linux.txt
sha256sum -c SHA256SUMS-linux.txt
```

Check that GPG identifies the expected primary key and signing subkey. Stop on any unexpected fingerprint, bad signature or failed checksum. The signature covers the checksum manifest, not an embedded DEB signature. Never import a secret key or recovery archive from a release. Native Linux installation and runtime acceptance remain pending.
