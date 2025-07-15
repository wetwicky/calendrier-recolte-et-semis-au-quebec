#!/usr/bin/env python3
"""
Script pour créer les packages de release du calendrier Quebec.
Génère des archives ZIP avec les fichiers essentiels pour les utilisateurs.
"""

import os
import zipfile
import shutil
from datetime import datetime

def create_release_packages():
    """Crée les packages de release."""
    
    version = "v1.0.0"
    date_str = datetime.now().strftime("%Y%m%d")
    
    # Fichiers à inclure dans chaque package
    common_files = [
        "README.md",
        "LICENSE", 
        "CHANGELOG.md",
        "RELEASE_NOTES.md"
    ]
    
    french_files = common_files + ["semis-et-recoltes.ics"]
    english_files = common_files + ["planting-and-harvest-quebec.ics"]
    complete_files = common_files + [
        "semis-et-recoltes.ics",
        "planting-and-harvest-quebec.ics",
        "compare_calendars.py",
        "count_stats.py", 
        "verify_ics.py",
        "clean_duplicates.py",
        "add_rrule.py",
        "add_semis.py"
    ]
    
    # Créer le dossier releases s'il n'existe pas
    if not os.path.exists("releases"):
        os.makedirs("releases")
    
    def create_zip(filename, files, description):
        """Crée un fichier ZIP avec les fichiers spécifiés."""
        zip_path = f"releases/{filename}"
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                if os.path.exists(file):
                    zipf.write(file, file)
                    print(f"  ✅ Ajouté: {file}")
                else:
                    print(f"  ❌ Manquant: {file}")
        
        file_size = os.path.getsize(zip_path) / 1024  # KB
        print(f"📦 {description}: {zip_path} ({file_size:.1f} KB)")
        return zip_path
    
    print(f"🚀 CRÉATION DES PACKAGES DE RELEASE {version}")
    print("=" * 50)
    
    # Package français seulement
    french_zip = create_zip(
        f"quebec-calendrier-semis-recoltes-francais-{version}.zip",
        french_files,
        "Package Français"
    )
    
    # Package anglais seulement  
    english_zip = create_zip(
        f"quebec-planting-harvest-calendar-english-{version}.zip", 
        english_files,
        "Package English"
    )
    
    # Package complet avec scripts
    complete_zip = create_zip(
        f"quebec-calendrier-complet-bilingual-{version}.zip",
        complete_files, 
        "Package Complet Bilingue"
    )
    
    print(f"\n📋 RÉSUMÉ DES PACKAGES:")
    print(f"📁 Dossier: releases/")
    print(f"🇫🇷 Français: {os.path.basename(french_zip)}")
    print(f"🇬🇧 English: {os.path.basename(english_zip)}")
    print(f"🌍 Complet: {os.path.basename(complete_zip)}")
    
    # Créer un fichier de checksums
    checksum_file = f"releases/checksums-{version}.txt"
    with open(checksum_file, 'w') as f:
        f.write(f"# Checksums for Quebec Calendar Release {version}\n")
        f.write(f"# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for zip_file in [french_zip, english_zip, complete_zip]:
            size = os.path.getsize(zip_file)
            f.write(f"{os.path.basename(zip_file):60s} {size:8d} bytes\n")
    
    print(f"🔐 Checksums: {checksum_file}")
    
    # Instructions pour GitHub release
    print(f"\n📝 INSTRUCTIONS GITHUB RELEASE:")
    print(f"1. Aller sur: https://github.com/wetwicky/calendrier-recolte-et-semis-au-quebec/releases")
    print(f"2. Cliquer 'Create a new release'")
    print(f"3. Tag: {version}")
    print(f"4. Title: 'Quebec Planting & Harvest Calendar {version} - Complete Bilingual Release'")
    print(f"5. Uploader les 3 fichiers ZIP depuis le dossier releases/")
    print(f"6. Copier le contenu de RELEASE_NOTES.md dans la description")

if __name__ == "__main__":
    create_release_packages()
