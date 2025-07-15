#!/usr/bin/env python3
"""
Script pour afficher les statistiques des suggestions pratiques
"""

def count_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Compter les événements de semis
    semis_count = content.count('Semis')

    # Compter les suggestions pratiques
    conseils_count = content.count('💡 Conseils pratiques')

    # Compter les événements de récolte
    recolte_count = content.count('RECOLTE')

    print(f"📊 Statistiques du calendrier:")
    print(f"   • {semis_count} événements mentionnant 'Semis'")
    print(f"   • {conseils_count} suggestions pratiques (💡)")
    print(f"   • {recolte_count} événements de récolte")

    # Trouver les événements de semis sans suggestions
    lines = content.split('\n')
    semis_events = []
    current_event = None

    for i, line in enumerate(lines):
        if 'Semis' in line and 'SUMMARY:' in line:
            current_event = {'summary': line, 'line': i+1}
        elif current_event and line.startswith('DESCRIPTION:'):
            current_event['description'] = line
            if '💡 Conseils pratiques' not in line:
                current_event['has_suggestions'] = False
            else:
                current_event['has_suggestions'] = True
            semis_events.append(current_event)
            current_event = None

    with_suggestions = sum(1 for event in semis_events if event['has_suggestions'])
    without_suggestions = sum(1 for event in semis_events if not event['has_suggestions'])

    print(f"   • {len(semis_events)} événements de semis au total")
    print(f"   • {with_suggestions} avec suggestions pratiques")
    print(f"   • {without_suggestions} sans suggestions")

    if without_suggestions > 0:
        print(f"\n🚨 Événements de semis sans suggestions:")
        for event in semis_events:
            if not event['has_suggestions']:
                culture = event['summary'].split('Semis ')[1].split(' (')[0]
                print(f"   - {culture}")

if __name__ == "__main__":
    count_stats("semis-et-recoltes.ics")
