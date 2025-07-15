# Guide de Release GitHub - Calendrier Québec

Ce guide explique comment créer une release complète sur GitHub pour le projet du calendrier de semis et récoltes du Québec.

## 🎯 Méthodes de Release

### Option 1: Manuelle (Recommandée pour débutants)

1. **Préparer les packages**
   ```bash
   python create_release.py
   ```

2. **Aller sur GitHub**
   - Visiter: https://github.com/wetwicky/calendrier-recolte-et-semis-au-quebec/releases
   - Cliquer "Create a new release"

3. **Configurer la release**
   - **Tag:** `v1.0.0` (doit correspondre au tag Git)
   - **Title:** `Quebec Planting & Harvest Calendar v1.0.0 - Complete Bilingual Release`
   - **Description:** Copier le contenu de `RELEASE_NOTES.md`

4. **Uploader les fichiers**
   Depuis le dossier `releases/`:
   - `quebec-calendrier-semis-recoltes-francais-v1.0.0.zip`
   - `quebec-planting-harvest-calendar-english-v1.0.0.zip`
   - `quebec-calendrier-complet-bilingual-v1.0.0.zip`
   - `checksums-v1.0.0.txt`

5. **Publier**
   - Vérifier que "Set as the latest release" est coché
   - Cliquer "Publish release"

### Option 2: Automatisée (PowerShell)

1. **Obtenir un token GitHub**
   - Aller dans Settings → Developer settings → Personal access tokens
   - Créer un token avec permissions `repo`

2. **Exécuter le script**
   ```powershell
   .\create_github_release.ps1 -GitHubToken "votre_token_ici"
   ```

3. **Vérification**
   - Le script créera automatiquement la release
   - Tous les fichiers seront uploadés
   - Un lien vers la release sera affiché

## 📋 Checklist Pre-Release

Avant de créer une release, vérifier que:

- [ ] Tous les commits sont poussés sur `main`
- [ ] Le tag Git est créé et poussé (`git tag v1.0.0 && git push origin v1.0.0`)
- [ ] `CHANGELOG.md` est à jour
- [ ] `RELEASE_NOTES.md` est rédigé
- [ ] Les calendriers ICS sont validés (run `python verify_ics.py`)
- [ ] Les deux langues sont synchronisées (run `python compare_calendars.py`)
- [ ] Les packages ZIP sont générés (run `python create_release.py`)

## 📦 Contenu des Packages

### Package Français (13 KB)
- `semis-et-recoltes.ics` - Calendrier français
- `README.md` - Documentation bilingue
- `LICENSE` - Licence MIT
- `CHANGELOG.md` - Historique des versions
- `RELEASE_NOTES.md` - Notes de cette release

### Package English (13 KB)
- `planting-and-harvest-quebec.ics` - English calendar
- Documentation complète (identique au français)

### Package Complet (26 KB)
- Les deux calendriers ICS
- Tous les scripts Python de maintenance
- Documentation complète
- Parfait pour les développeurs et mainteneurs

## 🔍 Vérifications Post-Release

Après création de la release:

1. **Tester les téléchargements**
   - Télécharger chaque package ZIP
   - Vérifier que les fichiers se décompressent correctement
   - Tester l'importation des fichiers ICS dans un calendrier

2. **Vérifier les liens**
   - README badges pointent vers la bonne release
   - Les liens de téléchargement fonctionnent
   - La documentation est accessible

3. **Validation communautaire**
   - Partager avec des testeurs
   - Vérifier dans différentes applications de calendrier
   - Collecter les retours utilisateurs

## 🚀 Futures Releases

Pour les versions futures:

1. **Incrémenter la version** selon [Semantic Versioning](https://semver.org/):
   - `v1.0.1` - Correction de bugs
   - `v1.1.0` - Nouvelles fonctionnalités
   - `v2.0.0` - Changements majeurs

2. **Mettre à jour la documentation**
   - Modifier le tag dans `create_release.py`
   - Mettre à jour `CHANGELOG.md`
   - Rédiger de nouvelles `RELEASE_NOTES.md`

3. **Tester les changements**
   - Exécuter tous les scripts de validation
   - Comparer les versions avec `compare_calendars.py`
   - Vérifier la cohérence des données

## 📞 Support

Pour questions sur le processus de release:
- Ouvrir une issue sur GitHub
- Consulter la documentation du projet
- Vérifier les logs d'erreur des scripts

---

**Happy Releasing! 🎉**
