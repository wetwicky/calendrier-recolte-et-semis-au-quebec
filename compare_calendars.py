#!/usr/bin/env python3
"""
Script pour comparer les statistiques entre les versions française et anglaise
du calendrier de semis et récoltes du Québec.
"""

import re
from collections import Counter

def parse_ics_file(filename):
    """Parse un fichier ICS et retourne les statistiques."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Compter les événements
    events = re.findall(r'BEGIN:VEVENT.*?END:VEVENT', content, re.DOTALL)
    
    stats = {
        'total_events': len(events),
        'categories': Counter(),
        'types': Counter(),
        'months': Counter()
    }
    
    for event in events:
        # Extraire les catégories
        cat_match = re.search(r'CATEGORIES:(.*)', event)
        if cat_match:
            categories = cat_match.group(1).split(',')
            for cat in categories:
                stats['categories'][cat.strip()] += 1
        
        # Extraire le type d'événement du summary
        summary_match = re.search(r'SUMMARY:(.*)', event)
        if summary_match:
            summary = summary_match.group(1)
            if 'Semis' in summary or 'Planting' in summary:
                stats['types']['PLANTING'] += 1
            elif 'récolte' in summary or 'Harvest' in summary:
                if 'Début' in summary or 'Start' in summary:
                    stats['types']['HARVEST_START'] += 1
                elif 'Fin' in summary or 'End' in summary:
                    stats['types']['HARVEST_END'] += 1
            elif 'Non cultivable' in summary or 'Not Cultivable' in summary or 'Very Limited' in summary or 'Complex' in summary:
                stats['types']['EXCLUSION'] += 1
        
        # Extraire le mois
        date_match = re.search(r'DTSTART;VALUE=DATE:(\d{8})', event)
        if date_match:
            date_str = date_match.group(1)
            month = int(date_str[4:6])
            stats['months'][month] += 1
    
    return stats

def print_comparison():
    """Affiche la comparaison entre les deux versions."""
    print("📊 COMPARAISON DES CALENDRIERS - FRANÇAIS vs ANGLAIS")
    print("=" * 60)
    
    try:
        stats_fr = parse_ics_file('semis-et-recoltes.ics')
        stats_en = parse_ics_file('planting-and-harvest-quebec.ics')
        
        print(f"\n📈 ÉVÉNEMENTS TOTAUX:")
        print(f"Français  : {stats_fr['total_events']:3d} événements")
        print(f"Anglais   : {stats_en['total_events']:3d} événements")
        print(f"Différence: {abs(stats_fr['total_events'] - stats_en['total_events']):3d}")
        
        print(f"\n🏷️  CATÉGORIES:")
        all_categories = set(stats_fr['categories'].keys()) | set(stats_en['categories'].keys())
        for cat in sorted(all_categories):
            fr_count = stats_fr['categories'].get(cat, 0)
            en_count = stats_en['categories'].get(cat, 0)
            print(f"{cat:12s}: FR={fr_count:3d} | EN={en_count:3d} | Diff={abs(fr_count-en_count):2d}")
        
        print(f"\n📅 TYPES D'ÉVÉNEMENTS:")
        all_types = set(stats_fr['types'].keys()) | set(stats_en['types'].keys())
        for event_type in sorted(all_types):
            fr_count = stats_fr['types'].get(event_type, 0)
            en_count = stats_en['types'].get(event_type, 0)
            print(f"{event_type:15s}: FR={fr_count:3d} | EN={en_count:3d} | Diff={abs(fr_count-en_count):2d}")
        
        print(f"\n📆 RÉPARTITION PAR MOIS:")
        month_names = ['', 'Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 
                      'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']
        for month in range(1, 13):
            if month in stats_fr['months'] or month in stats_en['months']:
                fr_count = stats_fr['months'].get(month, 0)
                en_count = stats_en['months'].get(month, 0)
                print(f"{month_names[month]:3s} ({month:2d}): FR={fr_count:3d} | EN={en_count:3d} | Diff={abs(fr_count-en_count):2d}")
        
        # Vérifier la cohérence
        print(f"\n✅ VÉRIFICATION DE COHÉRENCE:")
        coherent = True
        
        if stats_fr['total_events'] != stats_en['total_events']:
            print(f"❌ Nombre total d'événements différent!")
            coherent = False
        
        for cat in all_categories:
            if stats_fr['categories'].get(cat, 0) != stats_en['categories'].get(cat, 0):
                print(f"❌ Catégorie {cat}: différence détectée")
                coherent = False
        
        for event_type in all_types:
            if stats_fr['types'].get(event_type, 0) != stats_en['types'].get(event_type, 0):
                print(f"❌ Type {event_type}: différence détectée")
                coherent = False
        
        if coherent:
            print("✅ Les deux calendriers sont parfaitement cohérents!")
        else:
            print("⚠️  Des différences ont été détectées entre les calendriers.")
    
    except FileNotFoundError as e:
        print(f"❌ Erreur: Fichier non trouvé - {e}")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    print_comparison()
