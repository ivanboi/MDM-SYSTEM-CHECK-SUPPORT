# MDM SystemCheck — Support officiel

**MDM SystemCheck** est une application Android développée avec Flutter, destinée au diagnostic de connectivité réseau des terminaux et à la vérification indicative des flux nécessaires aux solutions EMM/MDM.

Ce dépôt est le **point d'entrée public pour le support**, les anomalies et les demandes d'évolution. Il ne contient **aucun code source de l'application**.

## Fonctionnalités

- Vérifications réseau **DNS, TCP, HTTP(S) et NTP** depuis le terminal Android.
- Diagnostics de connectivité des services EMM/MDM sélectionnés.
- Vérification indicative des flux **VoWiFi/ePDG**, avec saisie facultative du nom de domaine de l'opérateur.
- Sélection de plusieurs profils de terminaux pour consulter et tester les flux réseau applicables.
- Configuration facultative des composants réseau spécifiques à chaque déploiement MDM.
- Historique local des diagnostics et **export CSV** pour l'analyse par les équipes IT.

## Profils de terminaux

- Apple iOS / iPadOS
- Apple macOS
- Android
- Android AOSP pour Microsoft Teams Rooms
- Services Samsung Knox (hors Knox Manage, qui est une solution MDM distincte)
- Windows

**Important :** les tests sont exécutés **depuis le téléphone Android** qui héberge l'application. Ils ne prouvent pas le fonctionnement du système d'exploitation d'un autre appareil.

## Solutions MDM prises en charge

- Microsoft Intune
- Omnissa Workspace ONE UEM
- Ivanti Neurons for MDM / EPMM
- Cisco Meraki Systems Manager
- Citrix Endpoint Management
- BlackBerry UEM / Dynamics
- Samsung Knox Manage

L'application vérifie les destinations concrètes pouvant être testées depuis le terminal. Les flux serveur à serveur, adresses génériques et destinations dépendantes d'un tenant sont fournis à titre de référence et ne peuvent pas tous être testés automatiquement.

## Limites des diagnostics

- Une connexion TCP ou HTTPS réussie **ne prouve pas** l'inscription MDM, l'authentification ni la réception des notifications push.
- Les contrôles VoWiFi UDP 500/4500 sont **indicatifs** : ils ne réalisent pas de négociation IKE/IPsec.
- Les adresses et ports requis peuvent évoluer : vérifiez les exigences réseau actuelles de chaque éditeur.
- L'application ne se connecte pas aux API d'administration MDM et **n'envoie pas automatiquement les diagnostics** à un serveur de support.
- Les paramètres et l'historique sont stockés localement ; les exports CSV peuvent contenir des données techniques sensibles.

## Version et disponibilité

Version officielle du projet : **1.0.0** (Android, versionCode 23). La distribution via Google Play et l'intégration de Play Integrity sont des étapes distinctes ; leur disponibilité ne doit pas être présumée.

## Contacter le support

- 🐛 **[Signaler un bug](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=bug_report.yml)**
- 💡 **[Proposer une amélioration](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new?template=feature_request.yml)**
- 📋 **[Consulter les issues publiques](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues)**

Indiquez la version de l'application, la version d'Android, les étapes de reproduction et le résultat attendu. Ne joignez jamais de CSV non anonymisé.

**Toutes les issues de ce dépôt sont publiques.** Ne publiez pas de mots de passe, jetons, IMEI, numéros de série, données personnelles, adresses IP internes, noms d'hôtes confidentiels ou configurations réseau sensibles.

## Sécurité et divulgation responsable

**Ne signalez jamais une vulnérabilité dans une issue publique.** Consultez la [politique de sécurité](SECURITY.md) pour connaître le canal de signalement confidentiel et les informations à transmettre.

## Confidentialité du code

Le code source de MDM SystemCheck est conservé dans un dépôt GitHub privé distinct. Ce dépôt public est réservé au support et à la documentation destinée aux utilisateurs.
