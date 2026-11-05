# MDM SystemCheck Privacy Policy

Effective November 5, 2026

This policy describes how the MDM SystemCheck Android app handles data during network diagnostics, report export and support.

## What reaches a server

**MDM SystemCheck does not automatically upload diagnostic results, CSV reports, device information or app settings to the developer or to GitHub.** The app has no developer-operated diagnostic backend or user accounts and does not send analytics, advertising data or crash reports to the developer.

When you run diagnostics, the app sends network probes directly from your Android device. The destination depends on the selected network profiles, MDM platform and any custom endpoints you enable.

| Check | What leaves the device |
| --- | --- |
| DNS | The hostname being looked up may be sent to your device's configured DNS resolver. This can include a custom hostname you entered. |
| TCP and HTTP(S) | Connection attempts and, for HTTP(S) checks, standard GET requests reach the tested endpoint. These requests do not carry a diagnostic report or app settings. HTTPS is used where configured. A limited set of captive portal checks use unencrypted HTTP. |
| NTP and optional VoWiFi/ePDG | The app sends an NTP request to a time server or a small UDP probe to the selected ePDG endpoint. The probes do not include diagnostic reports or device identifiers. |

Resolvers, destination servers and network operators may see or log your network's source IP address, requested hostname, request metadata or connection timing, depending on the test and the network. Their data handling is governed by their own policies. Use custom probes only for infrastructure you are authorized to test.

## What stays on the device

- The app stores up to 50 diagnostic runs in its local history. A report can include test results, timestamps, endpoints and ports, your selected profiles and MDM platform, app version and build number, Android version and build identifier, and Android security patch level.
- The app stores selected profiles, the ePDG hostname, and enabled custom component settings locally so they can be restored when you reopen the app. The Android build identifier in a report identifies the operating system build.
- Android app backups are disabled. The app uses Android's app storage protections and does not add its own encryption to stored history or settings.

## When you save, share or submit information

- **Save to device** writes a CSV to the location you choose in the Android file picker. If you select a cloud-backed location, that provider may receive the file.
- **Share** creates a temporary CSV on the device and passes it to the app or service you select through Android's share sheet. The chosen service and recipients may retain copies.
- **Report an issue** opens GitHub in your browser. The app does not attach a diagnostic report. Information you submit to a public issue is visible to others and handled under [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Remove sensitive data and internal network details before posting or sharing.

## Retention and deletion

You can delete individual runs or clear the history in the app. To remove stored settings and other app data, clear the app's storage in Android Settings or uninstall the app. Delete any saved or shared copies separately.

## Contact

For general privacy questions, use the [public support page](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues) without posting personal or confidential information. For a private security report, follow the [security policy](SECURITY.md).
