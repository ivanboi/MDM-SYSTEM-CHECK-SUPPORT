# MDM SystemCheck Privacy Policy

Updated November 23, 2026

This policy describes how the MDM SystemCheck Android app handles data during network diagnostics, file reputation checks, report export and support.

## Public network catalogue and future offline import

A [reference-only network catalogue](data/network/README.md) is published on GitHub. **The current Android 1.0.9 build does not automatically fetch that catalogue**, so its publication does not change the network data sent by the installed application.

A **future, not yet released** manual CSV import ([PR #23](https://github.com/ivanboi/MDM-SYSTEM-CHECK/pull/23)) is designed to select a file from device storage, validate the fields, explicitly confirm activation, and retain the active copy locally. Importing a file itself would not upload its contents to GitHub, OVH, or another server. Running diagnostics against imported destinations would send the usual DNS/TCP/HTTP(S)/UDP network requests to those destinations, potentially revealing source IP and connection metadata.

A separately planned automatic GitHub catalogue downloader is **not implemented**. If later released, fetching it will involve normal HTTPS requests visible to GitHub and intermediaries (for example source IP and timing), and the privacy documentation will be revisited before release.

Windows and macOS applications are also **not currently distributed**. This policy's current behaviour describes the released Android application.

## What reaches a server

**MDM SystemCheck does not automatically upload diagnostic results, CSV reports, device information or app settings to the developer or to GitHub.** Network reports are stored on the device. The app has no user accounts and does not send analytics, advertising data or crash reports to the developer. App versions with the optional Google Play Integrity module use a dedicated verification service when you run that check, as described below.

When you run diagnostics, the app sends network probes directly from your Android device. The destination depends on the selected network profiles, MDM platform and any custom endpoints you enable.

| Check | What leaves the device |
| --- | --- |
| DNS | The hostname being looked up may be sent to your device's configured DNS resolver. This can include a custom hostname you entered. |
| TCP and HTTP(S) | Connection attempts and, for HTTP(S) checks, standard GET requests reach the tested endpoint. These requests do not carry a diagnostic report or app settings. HTTPS is used where configured. A limited set of captive portal checks use unencrypted HTTP. |
| NTP and optional VoWiFi/ePDG | The app sends an NTP request to a time server or a small UDP probe to the selected ePDG endpoint. The probes do not include diagnostic reports or device identifiers. |

Resolvers, destination servers and network operators may see or log your network's source IP address, requested hostname, request metadata or connection timing, depending on the test and the network. Their data handling is governed by their own policies. Use custom probes only for infrastructure you are authorized to test.

## Optional Google Play Integrity check

In versions that include the Google Play Integrity module, selecting **Run Play Integrity check** starts a separate, user-requested verification.

- Google processes app metadata, the Google Play license status, device attestation information and a hash binding the check to a fresh random request ID. Additional environment signals depend on the Play Console configuration. Google describes this processing in its [Play Integrity data safety documentation](https://developer.android.com/google/play/integrity/terms#data-safety).
- The app sends the encrypted integrity token and random request ID over HTTPS to the developer's verification service. App versions 1.0.4 and later use `api.mdm.ivanboi.fr`, hosted by OVHcloud. Version 1.0.3 uses the service hosted on Google Cloud Run. That service asks Google to decode the token, validates the request binding and returns app recognition, licensing and device integrity labels to the app.
- The verification service processes tokens and decoded verdicts in memory. It does not write their contents to its application logs or a database. Network diagnostic results, CSV reports, MDM endpoints and saved settings are not included in integrity requests.
- Hosting access logs can contain your source IP address, user agent, requested path, timestamps, HTTP status or request timing. Log retention depends on the hosting and logging settings. Google's processing of integrity data follows its applicable terms.

The app displays the integrity result on the check screen. This flow is used for integrity diagnostics, not advertising or user tracking.

## Optional file scanning with VirusTotal

The current packaged release is 1.0.9 (build 34). The GitHub APK (version 1.0.7 and later) and the Google Play build (version 1.0.8 and later) include **Scan with VirusTotal**, which opens the official VirusTotal website in an embedded Android WebView. When that page requests a file, MDM SystemCheck opens the Android document picker and hands the page a temporary read reference to the file you select. The app does not copy the file or save the selection in its diagnostic history. The VirusTotal page handles any submission, account sign-in and report. Browser and WebView sessions are separate. **Open in browser** opens the site in your browser if sign-in or a browser fallback is needed. The app does not request a VirusTotal API key or send file data to the developer, OVH verifier, or GitHub.

### Version 1.0.6

In version 1.0.6 of the GitHub APK, **Scan with VirusTotal** opens the official VirusTotal website in your browser, normally in an Android Custom Tab. Your browser may reuse its existing VirusTotal session. The website handles file selection, sign-in, any upload confirmation, and the report. MDM SystemCheck does not request an API key or access the file, fingerprint, credentials, or report. The app does not send those items to the developer, OVH verifier, or GitHub.

### VirusTotal submissions

Files you submit may be retained or shared by VirusTotal. Use only files you are authorized to share and that contain no personal or confidential information. See the [VirusTotal Terms of Service](https://www.virustotal.com/gui/terms-of-service) and [Privacy Policy](https://www.virustotal.com/gui/privacy-policy).

### Version 1.0.5

Version 1.0.5 of the GitHub APK includes **File Reputation**. It uses the API key you enter to communicate directly with VirusTotal over HTTPS. MDM SystemCheck keeps the key in memory while this screen is open and does not send the key, file, hash, or result to the developer, OVH verifier, or GitHub.

- **Check SHA-256** computes the file's fingerprint on your device and sends the fingerprint to VirusTotal to retrieve an existing report. This action does not send the file or its name.
- **Submit file to VirusTotal** sends the complete file and its name only after you confirm permission to share it and accept the [VirusTotal Terms of Service](https://www.virustotal.com/gui/terms-of-service) for that submission. VirusTotal may retain or share submissions. Use only files you are authorized to share and that contain no personal or confidential information. VirusTotal handles submissions under its [Privacy Policy](https://www.virustotal.com/gui/privacy-policy).
- The app does not add files or results to the diagnostic history. Android's file picker may make a temporary local copy to make the selected file available to the app. Clearing app storage cannot remove a copy already sent to VirusTotal.

## What stays on the device

- The app stores up to 50 diagnostic runs in its local history. A report can include test results, timestamps, endpoints and ports, your selected profiles and MDM platform, app version and build number, Android version and build identifier, and Android security patch level.
- The app stores selected profiles, the ePDG hostname, and enabled custom component settings locally so they can be restored when you reopen the app. The Android build identifier in a report identifies the operating system build.
- Android app backups are disabled. The app uses Android's app storage protections and does not add its own encryption to stored history or settings.

## When you save, share or submit information

- **Save to device** writes a CSV to the location you choose in the Android file picker. If you select a cloud-backed location, that provider may receive the file.
- **Share** creates a temporary CSV on the device and passes it to the app or service you select through Android's share sheet. The chosen service and recipients may retain copies.
- **Report an issue** opens GitHub in your browser. The app does not attach a diagnostic report. Information you submit to a public issue is visible to others and handled under [GitHub's privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). Remove sensitive data and internal network details before posting or sharing.

## Retention and deletion

VirusTotal's embedded page can store its session data in Android WebView storage. Clearing the app's storage removes this local WebView data. The external browser maintains its own session and site data. Copies already submitted to VirusTotal remain subject to its policies.

You can delete individual runs or clear the history in the app. To remove stored settings and other app data, clear the app's storage in Android Settings or uninstall the app. Delete any saved or shared copies separately.

## Contact

For general privacy questions, use the [public support page](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues) without posting personal or confidential information. For a private security report, follow the [security policy](SECURITY.md).
