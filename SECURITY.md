# Politique de sécurité — MDM SystemCheck

## Versions prises en charge

Les corrections visent la dernière version Android maintenue du projet (version documentée : **1.0.0+23**). Les versions antérieures ne bénéficient d'aucune garantie de correctif.

## Signaler une vulnérabilité de manière confidentielle

**Ne publiez jamais une vulnérabilité, un exploit, un secret ou une configuration confidentielle dans une issue publique.**

Utilisez **Security → Report a vulnerability** sur ce dépôt **si le signalement privé est activé**. Sinon, contactez le mainteneur par un canal privé déjà établi. Si aucun canal confidentiel n'est disponible, ne publiez pas les détails techniques dans les issues publiques.

Indiquez la version de l'application et d'Android, le scénario de reproduction, l'impact et les conditions préalables, en expurgeant les secrets et données personnelles. Aucun délai garanti de réponse ou de correction n'est annoncé.

## Périmètre et confidentialité

L'application réalise des diagnostics sortants DNS, TCP, HTTP(S), NTP et, sur demande, des tests VoWiFi/ePDG. Les envois UDP 500/4500 ne prouvent pas une négociation IKE/IPsec ou un service VoWiFi fonctionnel. Une connexion TCP/HTTPS réussie ne prouve ni authentification, ni inscription MDM, ni réception d'une notification push.

Les résultats, les préférences et les points de terminaison MDM configurés sont stockés **localement, sans chiffrement applicatif spécifique**. Ils ne sont pas téléversés automatiquement au support. Les exports CSV peuvent révéler des informations réseau sensibles : anonymisez-les avant partage.

## Protections décrites dans le code

- Isolation du stockage par Android ; sauvegarde applicative et trafic HTTP en clair désactivés dans le manifeste de release généré.
- Validation des certificats TLS pour HTTPS et distinction entre réponse HTTP en erreur et connectivité.
- Neutralisation des valeurs CSV pouvant être interprétées comme formules par un tableur.
- Validation de l'adresse IP et du port source attendus pour les réponses UDP ; un simple envoi UDP ne prouve aucune connectivité IPsec.
- Tests personnalisés uniquement vers les hôtes et réseaux pour lesquels l'administrateur est autorisé.

**Limites :** un appareil compromis/rooté peut exposer l'historique et les préférences ; les fichiers CSV exportés sont sensibles. Ne saisissez aucun identifiant ou secret dans les champs de diagnostic.

## Contrôles restant à vérifier

Avant distribution en production : rétention des fichiers CSV temporaires, besoin de chiffrement local, limitation du débit des requêtes, validation renforcée UDP/NTP, signature des livrables et configuration Play Integrity. **Ces protections ne sont pas déclarées implémentées.**

## Séparation des dépôts

Ce dépôt **public** contient seulement la documentation et les formulaires de support ; le code source Flutter/Android est dans un dépôt **privé**. Aucun secret, fichier de signature, configuration interne ou code source ne doit être ajouté à ce dépôt.

Pour les problèmes fonctionnels non sensibles, utilisez les [formulaires publics](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose).
