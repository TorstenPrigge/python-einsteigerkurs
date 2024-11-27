# Beispiel: Python-Bibliothek mit einer PLZ-Datenbank als Dictionary
POSTAL_CODE_DB = {
    "Berlin": ["10115", "10117", "10119", "10178", "10179"],
    "München": ["80331", "80333", "80335", "80336", "80337"],
    "Hamburg": ["20095", "20097", "20099", "20144", "20249"],
    # ... weitere Städte und PLZs
}

# Funktion, um Postleitzahlen für eine Stadt zu suchen
def get_postal_codes(city):
    return POSTAL_CODE_DB.get(city, [])

# Hauptskript
if __name__ == "__main__":
    city = input("Geben Sie eine Stadt ein: ").strip()
    postal_codes = get_postal_codes(city)
    if postal_codes:
        print(f"Die Postleitzahlen für {city} sind: {', '.join(postal_codes)}")
    else:
        print(f"Keine Postleitzahlen für {city} gefunden.")
