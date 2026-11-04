# Security Policy — MDM SystemCheck

## Versions prises en charge

Les correctifs de sécurité visent la version Android la plus récente de MDM SystemCheck, actuellement **1.0.0**. Les versions plus anciennes ne bénéficient pas nécessairement de correctifs.

## Signaler une vulnérabilité

**Ne créez pas d'issue publique pour une vulnérabilité, un secret exposé ou un problème de confidentialité.** Les issues de ce dépôt sont publiques.

Utilisez **Security → Report a vulnerability** sur ce dépôt **uniquement si l'option de signalement privé est activée**. Sinon, contactez le mainteneur par un canal privé déjà établi. En l'absence d'un canal confidentiel confirmé, ne publiez pas de détails d'exploitation dans une issue publique.

Un rapport utile comprend :
- la version de l'application et d'Android ;
- une description du risque et de son impact ;
- des étapes de reproduction sans données sensibles ;
- les conditions nécessaires à la reproduction.

Aucun délai de réponse ou de correction garanti n'est annoncé.

## Confidentialité des diagnostics

MDM SystemCheck effectue des tests réseau DNS, TCP, HTTP(S), NTP et, sur demande, des contrôles indicatifs VoWiFi/ePDG. Ces tests ne constituent pas une validation d'inscription MDM, d'authentification ou de tunnel IPsec.

Les résultats de diagnostic et les paramètres de connectivité sont stockés localement. L'application ne transmet pas automatiquement ces données au dépôt GitHub ni au support. **Les exports CSV peuvent contenir des informations sensibles sur l'environnement réseau.** Ne publiez pas d'exports non anonymisés.

N'indiquez jamais de mots de passe, jetons, identifiants personnels, IMEI, numéros de série ou adresses internes confidentielles dans une issue.

## Mesures et limites de sécurité

L'application s'appuie sur l'isolation Android, désactive la sauvegarde de l'application et le trafic HTTP non chiffré dans son manifeste généré, et vérifie les certificats TLS pour les tests HTTPS. Les exports CSV appliquent une protection contre l'interprétation de champs comme des formules de tableur.

**Limites connues :** l'historique et les préférences locales ne disposent pas de chiffrement applicatif spécifique ; un appareil compromis peut exposer ces informations. Les fichiers CSV exportés doivent être traités comme des documents potentiellement confidentiels. Les tests réseau personnalisés ne doivent viser que des infrastructures pour lesquelles vous disposez d'une autorisation.

La gestion des fichiers temporaires, le renforcement de certains contrôles réseau, la signature de distribution et Play Integrity font partie des points à vérifier ou à finaliser avant une distribution de production. Aucune protection non implémentée n'est présentée comme active.

## Périmètre de ce dépôt

Ce dépôt public héberge uniquement la documentation de support et les formulaires d'issues. Le code source et les éléments de compilation sont conservés dans un dépôt privé distinct.

Les signalements fonctionnels ordinaires peuvent être soumis via les [formulaires publics](https://github.com/ivanboi/MDM-SYSTEM-CHECK-SUPPORT/issues/new/choose), après suppression de toute donnée confidentielle.
