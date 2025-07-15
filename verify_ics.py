#!/usr/bin/env python3
"""
Script pour vérifier et nettoyer le fichier ICS
"""

def clean_and_verify_ics(filename):
    """Nettoie les duplications et vérifie le fichier ICS"""

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    events_count = 0
    rrule_count = 0

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Éviter les duplications de RRULE
        if line == 'RRULE:FREQ=YEARLY':
            # Vérifier si la ligne précédente est déjà une RRULE
            if cleaned_lines and cleaned_lines[-1].strip() == 'RRULE:FREQ=YEARLY':
                i += 1  # Ignorer cette duplication
                continue
            rrule_count += 1

        if line == 'BEGIN:VEVENT':
            events_count += 1

        cleaned_lines.append(lines[i])
        i += 1

    # Écrire le fichier nettoyé
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(cleaned_lines)

    print(f"✅ Fichier nettoyé avec succès!")
    print(f"📊 Statistiques:")
    print(f"   • {events_count} événements trouvés")
    print(f"   • {rrule_count} règles de récurrence")
    print(f"   • Ratio: {rrule_count/events_count:.1%} des événements ont une récurrence")

if __name__ == "__main__":
    filename = "semis-et-recoltes.ics"

    try:
        clean_and_verify_ics(filename)
    except FileNotFoundError:
        print(f"❌ Erreur: Fichier '{filename}' non trouvé")
    except Exception as e:
        print(f"❌ Erreur: {e}")
