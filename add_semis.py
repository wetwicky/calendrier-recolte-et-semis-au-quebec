#!/usr/bin/env python3
"""
Script pour ajouter les événements de semis au calendrier ICS
"""

import re
from datetime import datetime, timedelta

# Mapping des cultures avec leurs périodes de semis et suggestions
SEMIS_MAPPING = {
    # FRUITS (généralement plants/boutures)
    'fraises': {
        'jours_avant': 90,
        'type': 'plants',
        'emoji': '🌱',
        'suggestions': 'Privilégier les plants certifiés. Planter en sol bien drainé. Pailler pour protéger du gel.'
    },
    'framboises': {
        'jours_avant': 365,
        'type': 'plants',
        'emoji': '🌱',
        'suggestions': 'Choisir variétés adaptées au froid québécois. Planter au printemps ou automne.'
    },
    'cerises': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'cerises-terre': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semer en intérieur. Transplanter après les derniers gels. Tuteurage recommandé.'
    },
    'bleuets': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'mures': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'groseilles': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'cassis': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'pommes': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'poires': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'prunes': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'rhubarbe': {
        'jours_avant': 180,
        'type': 'plants',
        'emoji': '🌱',
        'suggestions': 'Diviser les plants existants au printemps. Sol riche et bien drainé requis.'
    },

    # LEGUMES
    'laitue': {
        'jours_avant': 45,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semis successifs aux 2 semaines. Préfère temps frais. Arroser régulièrement.'
    },
    'epinards': {
        'jours_avant': 50,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Résistant au froid. Semer tôt au printemps et en fin d\'été. Sol riche en azote.'
    },
    'radis': {
        'jours_avant': 30,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Croissance rapide (30 jours). Semer direct. Éviter période chaude d\'été.'
    },
    'carottes': {
        'jours_avant': 80,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Sol meuble et profond. Éclaircir les plants. Éviter fumier frais.'
    },
    'betteraves': {
        'jours_avant': 60,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Tremper graines 24h avant semis. Éclaircir pour plants de 10cm d\'espacement.'
    },
    'navets': {
        'jours_avant': 60,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Préfère temps frais. Semer direct au jardin. Récolter jeunes pour tendreté.'
    },
    'petits-pois': {
        'jours_avant': 60,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Résistant au gel léger. Tremper graines avant semis. Installer tuteurs tôt.'
    },
    'haricots-verts': {
        'jours_avant': 60,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Attendre sol réchauffé (15°C). Semer après risque de gel. Récolter régulièrement.'
    },
    'feves': {
        'jours_avant': 80,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Très résistant au froid. Fixer l\'azote dans le sol. Pincer sommets si pucerons.'
    },
    'courgettes': {
        'jours_avant': 90,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semer en intérieur, transplanter en sol chaud. Beaucoup d\'espace requis (1m²).'
    },
    'concombres': {
        'jours_avant': 90,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Chaleur et humidité nécessaires. Pailler le sol. Tuteurer variétés grimpantes.'
    },
    'tomates': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semer en intérieur sous éclairage. Transplanter après derniers gels. Tuteurer obligatoire.'
    },
    'tomates-cerises': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Plus tolérantes au froid que tomates standard. Production abondante. Tuteurer.'
    },
    'poivrons': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Exige chaleur constante. Semer en intérieur. Protéger du vent. Arroser régulièrement.'
    },
    'aubergines': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Culture délicate au Québec. Nécessite serre ou endroit très chaud et abrité.'
    },
    'brocoli': {
        'jours_avant': 80,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Préfère temps frais. Transplanter jeunes plants. Récolter avant floraison.'
    },
    'chou-fleur': {
        'jours_avant': 80,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Plus délicat que brocoli. Blanchir en attachant feuilles autour de la pomme.'
    },
    'choux': {
        'jours_avant': 80,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Résistant au froid. Protéger des altises avec filet. Butter les plants.'
    },
    'choux-bruxelles': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Saison longue requise. Pincer bourgeon terminal en fin été. Récolter après gel.'
    },
    'poireaux': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semer en intérieur. Butter régulièrement pour blanchir. Résistant au gel.'
    },
    'oignons': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Préférer bulbilles pour climat court. Semer très tôt en intérieur. Sol bien drainé.'
    },
    'ail': {
        'jours_avant': 240,
        'type': 'bulbes',
        'emoji': '🌱',
        'suggestions': 'Planter à l\'automne avant gel. Choisir variétés d\'ail d\'hiver. Pailler.'
    },
    'pommes-terre': {
        'jours_avant': 90,
        'type': 'tubercules',
        'emoji': '🌱',
        'suggestions': 'Préchauffer tubercules au soleil. Butter régulièrement. Éviter pommes de terre vertes.'
    },
    'courges': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Beaucoup d\'espace requis. Sol riche et chaud. Pollinisation manuelle si nécessaire.'
    },
    'citrouilles': {
        'jours_avant': 120,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Espace énorme requis (3m²). Pincer tiges secondaires. Protéger fruits du sol.'
    },
    'mais': {
        'jours_avant': 90,
        'type': 'graines',
        'emoji': '🌱',
        'suggestions': 'Semer en blocs pour pollinisation. Sol chaud requis. Butter les plants.'
    },
    'asperges': {
        'jours_avant': 0,
        'type': 'plants',
        'emoji': '🌱',
        'suggestions': 'Vivace - plantation une fois. Choisir emplacement permanent. Récolte dès 3e année.'
    },  # Vivace, pas de semis annuel
}

def calculate_semis_date(recolte_date_str, jours_avant):
    """Calcule la date de semis basée sur la date de récolte"""
    # Parser la date de récolte (format YYYYMMDD)
    year = int(recolte_date_str[:4])
    month = int(recolte_date_str[4:6])
    day = int(recolte_date_str[6:8])

    recolte_date = datetime(year, month, day)
    semis_date = recolte_date - timedelta(days=jours_avant)

    return semis_date.strftime('%Y%m%d')

def add_semis_events(filename):
    """Ajoute les événements de semis au fichier ICS"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Trouver tous les événements de début de récolte
    pattern = r'BEGIN:VEVENT\nUID:([^-]+)-debut-(\d{8})@semis-recoltes-quebec\nDTSTART;VALUE=DATE:(\d{8})\nRRULE:FREQ=YEARLY\nSUMMARY:([^\\n]+)\nDESCRIPTION:([^\\n]+)\nCATEGORIES:(FRUITS|LEGUMES),RECOLTE\nEND:VEVENT'

    matches = re.findall(pattern, content)
    semis_events = []

    for match in matches:
        culture, date_str, dtstart, summary, description, category = match

        if culture in SEMIS_MAPPING:
            semis_info = SEMIS_MAPPING[culture]

            # Skip si pas de semis annuel (arbres/arbustes)
            if semis_info['jours_avant'] == 0:
                continue

            # Calculer la date de semis
            semis_date = calculate_semis_date(dtstart, semis_info['jours_avant'])

            # Créer la description avec suggestions pratiques
            description_base = f"Période optimale pour le semis/plantation de {culture.replace('-', ' ')} au Québec."
            if 'suggestions' in semis_info:
                description_complete = f"{description_base}\\n\\n💡 Conseils pratiques: {semis_info['suggestions']}"
            else:
                description_complete = description_base

            # Créer l'événement de semis
            semis_event = f"""BEGIN:VEVENT
UID:{culture}-semis-{semis_date}@semis-recoltes-quebec
DTSTART;VALUE=DATE:{semis_date}
RRULE:FREQ=YEARLY
SUMMARY:{semis_info['emoji']} Semis {culture.replace('-', ' ').title()} ({semis_info['type']})
DESCRIPTION:{description_complete}
CATEGORIES:{category},SEMIS
END:VEVENT

"""
            semis_events.append(semis_event)

    # Insérer les événements de semis après l'en-tête du calendrier
    header_end = content.find('X-WR-CALDESC:Calendrier des périodes de récolte des fruits et légumes au Québec')
    if header_end != -1:
        header_end = content.find('\n', header_end) + 1
        new_content = (content[:header_end] +
                      '\n' + ''.join(semis_events) +
                      content[header_end:])
    else:
        new_content = content

    # Écrire le nouveau fichier
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ {len(semis_events)} événements de semis ajoutés avec succès!")
    print(f"📁 Fichier mis à jour: {filename}")

if __name__ == "__main__":
    filename = "semis-et-recoltes.ics"

    try:
        add_semis_events(filename)
    except FileNotFoundError:
        print(f"❌ Erreur: Fichier '{filename}' non trouvé")
    except Exception as e:
        print(f"❌ Erreur: {e}")
