#!/usr/bin/env python3
"""
Script pour ajouter les événements de semis au calendrier ICS
"""

import re
from datetime import datetime, timedelta

# Mapping des cultures avec leurs périodes de semis (en jours avant la récolte)
SEMIS_MAPPING = {
    # FRUITS (généralement plants/boutures)
    'fraises': {'jours_avant': 90, 'type': 'plants', 'emoji': '🌱'},
    'framboises': {'jours_avant': 365, 'type': 'plants', 'emoji': '🌱'},
    'cerises': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'cerises-terre': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'bleuets': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'mures': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'groseilles': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'cassis': {'jours_avant': 0, 'type': 'arbuste', 'emoji': '🌳'},  # Pas de semis annuel
    'pommes': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'poires': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'prunes': {'jours_avant': 0, 'type': 'arbre', 'emoji': '🌳'},  # Pas de semis annuel
    'rhubarbe': {'jours_avant': 180, 'type': 'plants', 'emoji': '🌱'},
    
    # LEGUMES
    'laitue': {'jours_avant': 45, 'type': 'graines', 'emoji': '🌱'},
    'epinards': {'jours_avant': 50, 'type': 'graines', 'emoji': '🌱'},
    'radis': {'jours_avant': 30, 'type': 'graines', 'emoji': '🌱'},
    'carottes': {'jours_avant': 80, 'type': 'graines', 'emoji': '🌱'},
    'betteraves': {'jours_avant': 60, 'type': 'graines', 'emoji': '🌱'},
    'navets': {'jours_avant': 60, 'type': 'graines', 'emoji': '🌱'},
    'petits-pois': {'jours_avant': 60, 'type': 'graines', 'emoji': '🌱'},
    'haricots-verts': {'jours_avant': 60, 'type': 'graines', 'emoji': '🌱'},
    'feves': {'jours_avant': 80, 'type': 'graines', 'emoji': '🌱'},
    'courgettes': {'jours_avant': 90, 'type': 'graines', 'emoji': '🌱'},
    'concombres': {'jours_avant': 90, 'type': 'graines', 'emoji': '🌱'},
    'tomates': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'tomates-cerises': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'poivrons': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'aubergines': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'brocoli': {'jours_avant': 80, 'type': 'graines', 'emoji': '🌱'},
    'chou-fleur': {'jours_avant': 80, 'type': 'graines', 'emoji': '🌱'},
    'choux': {'jours_avant': 80, 'type': 'graines', 'emoji': '🌱'},
    'choux-bruxelles': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'poireaux': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'oignons': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'ail': {'jours_avant': 240, 'type': 'bulbes', 'emoji': '🌱'},  # Planté en automne
    'pommes-terre': {'jours_avant': 90, 'type': 'tubercules', 'emoji': '🌱'},
    'courges': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'citrouilles': {'jours_avant': 120, 'type': 'graines', 'emoji': '🌱'},
    'mais': {'jours_avant': 90, 'type': 'graines', 'emoji': '🌱'},
    'asperges': {'jours_avant': 0, 'type': 'plants', 'emoji': '🌱'},  # Vivace, pas de semis annuel
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
            
            # Créer l'événement de semis
            semis_event = f"""BEGIN:VEVENT
UID:{culture}-semis-{semis_date}@semis-recoltes-quebec
DTSTART;VALUE=DATE:{semis_date}
RRULE:FREQ=YEARLY
SUMMARY:{semis_info['emoji']} Semis {culture.replace('-', ' ').title()} ({semis_info['type']})
DESCRIPTION:Période optimale pour le semis/plantation de {culture.replace('-', ' ')} au Québec
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
