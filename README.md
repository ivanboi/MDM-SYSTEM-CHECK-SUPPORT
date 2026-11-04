# MDM SystemCheck — Support officiel

**MDM SystemCheck (EMM SystemCheck)** est une application **Android Flutter** de diagnostic réseau pour les administrateurs EMM/MDM. Elle vérifie la connectivité depuis le téléphone Android, sans accéder aux API d'administration MDM ni valider une inscription ou une authentification.

Ce dépôt **public** héberge exclusivement le support, la documentation et les formulaires de signalement. **Le code source, les configurations de compilation et les secrets restent dans un dépôt privé distinct.** Aucun accès au dépôt privé n'est nécessaire pour obtenir du support.

## Fonctionnalités

- Tests DNS, TCP, HTTP(S) et NTP (requête UDP/123 avec validation de la réponse).
- Diagnostics des destinations accessibles depuis le terminal Android ; flux serveur-à-serveur, destinations génériques (wildcards), propres au tenant ou à la région : **référence uniquement**.
- Profils réseau sélectionnables : **iOS/iPadOS, macOS, Android, Android AOSP pour Microsoft Teams Rooms, services Samsung Knox et Windows**. Les tests de tous les profils sélectionnés sont effectués depuis **le téléphone Android**, pas depuis les systèmes distants.
- Plateformes MDM : **Microsoft Intune, Omnissa Workspace ONE UEM, Ivanti Neurons for MDM/EPMM, Cisco Meraki Systems Manager, Citrix Endpoint Management, BlackBerry UEM/Dynamics et Samsung Knox Manage**. Une seule plateforme MDM est testée à la fois. Knox Manage est une plateforme MDM distincte des services de terminaux Samsung Knox.
- Composants réseau optionnels propres au déploiement (ex. AWCM/UAG/Tunnel, Sentry/Core, Intune Tunnel, Citrix Gateway, BlackBerry Proxy) : activation explicite et saisie du nom d'hôte/IP et du port par l'administrateur.
- Contrôle VoWiFi/ePDG optionnel : résolution DNS du nom d'hôte de l'opérateur et envoi indicatif de datagrammes UDP 500/4500. **Aucune négociation IKE/IPsec ni preuve de fonctionnement VoWiFi.**
- Contrôles FCM côté Android sur `mtalk.google.com` (TCP 443/5228/5229/5230). Une connexion TCP réussie ne prouve pas la réception d'une notification push ; `fcm.googleapis.com` est une API côté serveur et n'est pas testée comme flux push du téléphone.
- Historique et préférences conservés localement ; exports CSV comprenant notamment version Android, identifiant de build et niveau de correctif de sécurité Android.

## Interprétation des résultats

Les tests mesurent une connectivité réseau **depuis le téléphone Android**. Ils ne prouvent ni inscription MDM, ni authentification, ni disponibilité d'un service distant, ni réception des notifications push. Les composants personnalisés ne doivent cibler que des infrastructures pour lesquelles vous avez une autorisation. Vérifiez les listes de destinations et ports dans la documentation officielle des éditeurs avant de définir une règle de pare-feu.

## Version et distribution

Version documentée : **1.0.0+23** (Android versionCode 23). L'application est destinée à Android uniquement ; la présence de profils iOS/macOS/Windows ne signifie pas que l'application s'exécute sur ces plateformes. Les builds APK et AAB peuvent être produits par la CI du dépôt privé. **La publication Google Play, la signature de distribution et Play Integrity ne sont pas présentés comme déjà opérationnels.**

## Support public

- [Signaler un bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml)
- [Proposer une amélioration](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml)
- [Consulter les demandes publiques](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues)

Pour un bug, fournissez la version de l'application et d'Android, les étapes de reproduction, le résultat observé et le résultat attendu **sans données sensibles**.

**Toutes les issues sont publiques.** Ne publiez jamais mots de passe, jetons, IMEI, numéros de série, données personnelles, adresses internes confidentielles ou exports CSV non anonymisés. Pour une vulnérabilité, **n'ouvrez pas d'issue publique** : suivez la [politique de sécurité](SECURITY.md).

## Confidentialité

Les diagnostics et paramètres restent dans le stockage local de l'application, sans chiffrement applicatif spécifique ; ils ne sont pas envoyés automatiquement au support. Les sauvegardes Android et le trafic HTTP non chiffré sont désactivés dans le manifeste de release généré. Les exports CSV neutralisent les préfixes de formules de tableur, mais restent potentiellement confidentiels. Un appareil compromis peut exposer les données locales.

## Références éditeurs

[Apple](https://support.apple.com/en-us/101555) · [Android Enterprise](https://support.google.com/work/android/answer/10513641?hl=en) · [Samsung Knox](https://docs.samsungknox.com/admin/knox-admin-portal/before-you-begin/samsung-knox-firewall-exceptions/) · [Microsoft Intune](https://learn.microsoft.com/en-us/intune/fundamentals/endpoints) · [Omnissa](https://ports.omnissa.com/home/) · [Ivanti](https://help.ivanti.com/ht/help/en_US/CLOUD/vNow/platform-allowlist.htm) · [Firebase FCM](https://firebase.google.com/docs/cloud-messaging/network-configuration)

Les références réseau évoluent ; consultez toujours leur version actuelle.
