#!/usr/bin/env python3
"""
Script pour ajouter la récurrence annuelle à tous les événements du calendrier ICS
"""

def add_rrule_to_ics(input_file, output_file):
    """Ajoute RRULE:FREQ=YEARLY à tous les événements du fichier ICS"""

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Diviser le contenu en lignes
    lines = content.split('\n')
    new_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Si on trouve une ligne DTSTART;VALUE=DATE, ajouter RRULE après
        if line.startswith('DTSTART;VALUE=DATE:'):
            new_lines.append('RRULE:FREQ=YEARLY')

        i += 1

    # Reconstituer le contenu
    new_content = '\n'.join(new_lines)

    # Écrire le nouveau fichier
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Règles de récurrence ajoutées avec succès!")
    print(f"📁 Fichier mis à jour: {output_file}")

if __name__ == "__main__":
    input_file = "semis-et-recoltes.ics"
    output_file = "semis-et-recoltes.ics"

    try:
        add_rrule_to_ics(input_file, output_file)
    except FileNotFoundError:
        print(f"❌ Erreur: Fichier '{input_file}' non trouvé")
    except Exception as e:
        print(f"❌ Erreur: {e}")
