#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script pour nettoyer les événements dupliqués dans le fichier ICS
basé sur les UID uniques
"""

import re

def clean_duplicates(filename):
    """Supprime les événements dupliqués basés sur les UID"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Séparer l'en-tête et les événements
    lines = content.split('\n')

    # Trouver la fin de l'en-tête
    header_lines = []
    event_content = []
    in_header = True

    for line in lines:
        if in_header and line.strip() and not line.startswith('BEGIN:VEVENT'):
            header_lines.append(line)
        elif line.startswith('BEGIN:VEVENT'):
            in_header = False
            event_content.append(line)
        elif line == 'END:VCALENDAR':
            # Ne pas l'ajouter maintenant, on l'ajoutera à la fin
            pass
        else:
            if not in_header:
                event_content.append(line)

    # Extraire les événements complets
    events = []
    current_event = []
    in_event = False

    for line in event_content:
        if line.startswith('BEGIN:VEVENT'):
            current_event = [line]
            in_event = True
        elif line.startswith('END:VEVENT'):
            current_event.append(line)
            events.append('\n'.join(current_event))
            current_event = []
            in_event = False
        elif in_event:
            current_event.append(line)

    # Extraire les UID et déduplicater
    unique_events = {}

    for event in events:
        uid_match = re.search(r'^UID:(.+)$', event, re.MULTILINE)
        if uid_match:
            uid = uid_match.group(1)
            if uid not in unique_events:
                unique_events[uid] = event
            else:
                # Garder l'événement avec la description la plus complète
                existing_event = unique_events[uid]
                if '💡 Conseils pratiques' in event and '💡 Conseils pratiques' not in existing_event:
                    unique_events[uid] = event
                elif len(event) > len(existing_event):
                    unique_events[uid] = event

    # Reconstruire le fichier
    new_content = '\n'.join(header_lines) + '\n\n'
    new_content += '\n\n'.join(unique_events.values()) + '\n\n'
    new_content += 'END:VCALENDAR'

    # Écrire le fichier nettoyé
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Nettoyage terminé!")
    print(f"📊 {len(events)} événements trouvés, {len(unique_events)} événements uniques conservés")
    print(f"🗑️ {len(events) - len(unique_events)} doublons supprimés")

if __name__ == "__main__":
    filename = "semis-et-recoltes.ics"
    clean_duplicates(filename)
