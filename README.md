# 🌱 Calendrier Semis et Récoltes - Québec | Quebec Planting and Harvest Calendar

Un calendrier au format ICS contenant les périodes de semis et récolte des fruits et légumes adaptés au climat du Québec, ainsi que les exclusions avec explications pour les variétés non cultivables.

*An ICS format calendar containing planting and harvest periods for fruits and vegetables adapted to Quebec's climate, along with exclusions and explanations for varieties not suitable for cultivation.*

## 📅 Description | Description

Ce projet fournit un calendrier complet pour les jardiniers québécois avec :

- **Périodes de semis** pour les cultures annuelles
- **Périodes de récolte** pour 39 fruits et légumes
- **Événements d'exclusion** pour les variétés non adaptées au climat québécois
- **Format ICS standard** compatible avec la plupart des applications de calendrier
- **Emojis et descriptions détaillées** pour une meilleure lisibilité

*This project provides a complete calendar for Quebec gardeners with:*

- *Planting periods for annual crops*
- *Harvest periods for 39 fruits and vegetables*
- *Exclusion events for varieties not adapted to Quebec's climate*
- *Standard ICS format compatible with most calendar applications*
- *Emojis and detailed descriptions for better readability*

## 📁 Contenu | Files

### Français | French
- `semis-et-recoltes.ics` - Fichier calendrier principal avec récurrence annuelle
- `README.md` - Documentation du projet

### English
- `planting-and-harvest-quebec.ics` - Main calendar file with annual recurrence
- Documentation included in this README

### Scripts Python | Python Scripts
- `add_rrule.py` - Script Python pour ajouter les règles de récurrence
- `add_semis.py` - Script Python pour ajouter les événements de semis
- `verify_ics.py` - Script Python pour vérifier et nettoyer le fichier ICS
- `clean_duplicates.py` - Script pour nettoyer les doublons
- `count_stats.py` - Script pour afficher les statistiques du calendrier

## 🍎 Fruits inclus (13 variétés)

| Fruit | Période de récolte | Émoji |
|-------|-------------------|-------|
| Fraises | 15 juin → 31 juillet | 🍓 |
| Framboises | 1er juillet → 15 août | 🔴 |
| Cerises | 15 juin → 15 août | 🍒 |
| Cerises de terre | 15 août → 15 octobre | 🟡 |
| Bleuets | 20 juillet → 31 août | 🫐 |
| Mûres | 1er août → 15 septembre | 🫐 |
| Groseilles | 10 juillet → 20 août | 🍇 |
| Cassis | 15 juillet → 25 août | 🫐 |
| Pommes | 1er septembre → 31 octobre | 🍎 |
| Poires | 15 septembre → 15 octobre | 🍐 |
| Prunes | 20 août → 30 septembre | 🟣 |
| Rhubarbe | 1er juin → 31 juillet | 🌱 |

## 🥕 Légumes inclus (26 variétés)

| Légume | Période de récolte | Émoji |
|--------|-------------------|-------|
| Laitue | 1er juin → 30 septembre | 🥬 |
| Épinards | 15 mai → 15 octobre | 🌿 |
| Radis | 15 mai → 1er octobre | 🔴 |
| Carottes | 1er juillet → 31 octobre | 🥕 |
| Betteraves | 15 juillet → 31 octobre | 🟠 |
| Navets | 1er juillet → 31 octobre | ⚪ |
| Petits pois | 15 juin → 31 juillet | 🟢 |
| Haricots verts | 15 juillet → 15 septembre | 🫛 |
| Fèves | 20 juillet → 15 septembre | 🫘 |
| Courgettes | 15 juillet → 30 septembre | 🥒 |
| Concombres | 20 juillet → 30 septembre | 🥒 |
| Tomates | 15 juillet → 1er octobre | 🍅 |
| Tomates cerises | 15 juillet → 1er octobre | 🍅 |
| Poivrons | 1er août → 30 septembre | 🫑 |
| Aubergines | 1er août → 30 septembre | 🍆 |
| Brocoli | 1er juillet → 31 octobre | 🥦 |
| Chou-fleur | 15 juillet → 31 octobre | 🥬 |
| Choux | 1er juillet → 15 novembre | 🥬 |
| Choux de Bruxelles | 1er septembre → 30 novembre | 🥬 |
| Poireaux | 1er août → 15 novembre | 🥬 |
| Oignons | 1er août → 15 octobre | 🧅 |
| Ail | 15 juillet → 31 août | 🧄 |
| Pommes de terre | 15 juillet → 15 octobre | 🥔 |
| Courges | 1er septembre → 31 octobre | 🎃 |
| Citrouilles | 1er septembre → 31 octobre | 🎃 |
| Maïs | 15 août → 30 septembre | 🌽 |
| Asperges | 10 mai → 15 juin | 🌱 |

## 🚫 Exclusions documentées

Le calendrier inclut également des événements d'exclusion pour expliquer pourquoi certaines variétés ne sont pas cultivables au Québec :

### Fruits non adaptés
- **Agrumes** (oranges 🍊, citrons 🍋, pamplemousses) ❄️ - *Trop sensibles au gel*
- **Avocats** 🥑 🌡️ - *Température minimale trop élevée*
- **Figues** 🟤 ⏰ - *Saison trop courte*
- **Kiwis** 🥝 ⏰ - *Période de maturation trop longue*

### Légumes difficiles ou non adaptés
- **Artichauts** 🟢 ⏰ - *Saison trop courte pour plante vivace*
- **Okra** 🌶️ 🌡️ - *Nécessite plus de chaleur*
- **Melons/Pastèques** 🍈🍉 - *Conditions de chaleur insuffisantes*
- **Légumes techniques** (fenouil, endives) 🔧 - *Culture complexe*

### Légende des emojis d'exclusion
- **❄️** = Sensible au gel/climat froid
- **🌡️** = Nécessite plus de chaleur
- **⏰** = Saison de croissance trop courte
- **🔧** = Technique de culture complexe

## 🌱 Événements de semis

Le calendrier inclut également les périodes optimales de semis pour **17 cultures annuelles** :

### Types de semis inclus
- **🌱 Graines** : Semis direct ou en intérieur (laitue, radis, carottes, etc.)
- **🌱 Plants/Transplants** : Plantation de plants (tomates, poivrons, brocoli, etc.)
- **🌱 Bulbes/Tubercules** : Plantation d'ail, pommes de terre
- **🌳 Arbres/Arbustes** : Pas de semis annuel (plantation une fois)

### Cultures exclues des semis
Les **arbres fruitiers** et **arbustes** ne nécessitent pas de semis annuel :
- Pommes, poires, prunes, cerises (arbres)
- Bleuets, mûres, groseilles, cassis (arbustes)
- Asperges (vivace établie)

Les dates de semis sont calculées automatiquement en fonction des périodes de récolte optimales.

## 📲 Installation et utilisation | Installation and Usage

### 1. Télécharger le calendrier | Download the calendar
```bash
git clone https://github.com/wetwicky/calendrier-recolte-et-semis-au-quebec.git
cd calendrier-recolte-et-semis-au-quebec
```

### 2. Choisir la version | Choose your version

#### Français 🇫🇷
Utilisez le fichier `semis-et-recoltes.ics`

#### English 🇬🇧
Use the file `planting-and-harvest-quebec.ics`

### 3. Importer dans votre application de calendrier | Import into your calendar app

#### Google Calendar
1. Ouvrez Google Calendar | Open Google Calendar
2. Cliquez sur le `+` à côté de "Autres calendriers" | Click the `+` next to "Other calendars"
3. Sélectionnez "Créer un calendrier" ou "Importer" | Select "Create calendar" or "Import"
4. Importez le fichier ICS de votre choix | Import your chosen ICS file

#### Apple Calendar (macOS/iOS)
1. Double-cliquez sur le fichier ICS | Double-click the ICS file
2. Choisissez le calendrier de destination | Choose the destination calendar
3. Cliquez sur "Importer" | Click "Import"

#### Outlook
1. Ouvrez Outlook | Open Outlook
2. Allez dans Fichier > Ouvrir et exporter > Importer/Exporter | Go to File > Open & Export > Import/Export
3. Sélectionnez le fichier ICS | Select the ICS file

#### Applications mobiles | Mobile Apps
La plupart des applications de calendrier mobile supportent l'importation de fichiers ICS via le partage de fichiers.

*Most mobile calendar apps support ICS file import through file sharing.*

## 🌿 Catégories d'événements

Le calendrier utilise les catégories suivantes :
- `FRUITS,SEMIS` - Périodes de semis/plantation des fruits
- `LEGUMES,SEMIS` - Périodes de semis/plantation des légumes
- `FRUITS,RECOLTE` - Périodes de récolte des fruits
- `LEGUMES,RECOLTE` - Périodes de récolte des légumes
- `FRUITS,EXCLUSION` - Fruits non cultivables avec explications
- `LEGUMES,EXCLUSION` - Légumes non cultivables avec explications

## 🔄 Récurrence annuelle

Ce calendrier est configuré avec des **règles de récurrence annuelle automatique** :
- ✅ **Tous les événements se répètent chaque année** à la même date
- ✅ **Aucune intervention manuelle requise** pour les années suivantes
- ✅ **Compatible avec tous les clients de calendrier** supportant les règles RRULE
- ✅ **Mise à jour automatique** pour les prochaines décennies

### Format technique
Chaque événement inclut la règle : `RRULE:FREQ=YEARLY`

### Script de maintenance
Deux scripts Python sont fournis pour la maintenance du calendrier :

**Ajouter les règles de récurrence :**
```bash
python add_rrule.py
```

**Vérifier et nettoyer le fichier :**
```bash
python verify_ics.py
```

Le script de vérification affiche des statistiques utiles sur le calendrier.

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour proposer des modifications :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité
3. Committez vos changements (suivez les conventions de commit)
4. Poussez vers la branche
5. Ouvrez une Pull Request

### Format des commits
Ce projet utilise les [Conventional Commits](https://www.conventionalcommits.org/) avec gitmojis :
```
<type>[optional scope]: <gitmoji> <description>
```

Exemple :
```
feat(calendar): ✨ ajouter périodes de récolte pour les herbes aromatiques
```

## 📍 Zones climatiques | Climate Zones

Ce calendrier est optimisé pour : *This calendar is optimized for:*
- **Zone de rusticité** : 3a à 5b (selon Agriculture Canada) | **Hardiness zone**: 3a to 5b (Agriculture Canada)
- **Régions** : Sud du Québec, vallée du Saint-Laurent, Montréal, Québec | **Regions**: Southern Quebec, St. Lawrence Valley, Montreal, Quebec City
- **Climat** : Continental humide avec hivers froids | **Climate**: Humid continental with cold winters

## 📚 Références | References

- Agriculture et Agroalimentaire Canada | Agriculture and Agri-Food Canada
- Guide de jardinage du Québec | Quebec Gardening Guide
- Ministère de l'Agriculture du Québec (MAPAQ) | Quebec Ministry of Agriculture
- Sociétés horticoles locales | Local horticultural societies

## 📄 Licence | License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

*This project is under MIT license. See the `LICENSE` file for more details.*

## 📧 Contact

Pour questions ou suggestions | For questions or suggestions: [votre-email@exemple.com]

---

**Bon jardinage ! 🌱 | Happy gardening! 🌱**
