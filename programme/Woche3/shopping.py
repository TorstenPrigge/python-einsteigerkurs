import os

def lese_datei(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            # Inhalt der Datei zeilenweise einlesen
            inhalte = datei.readlines()
            return [eintrag.strip() for eintrag in inhalte]
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden.")
        return []
    except IOError:
        print(f"Ein Fehler ist beim Lesen der Datei {dateiname} aufgetreten.")
        return []

def gruppiere_inhalte(inhalte):
    gruppierte_daten = {}
    for eintrag in inhalte:
        if eintrag in gruppierte_daten:
            gruppierte_daten[eintrag] += 1
        else:
            gruppierte_daten[eintrag] = 1
    return gruppierte_daten

def drucke_gruppierte_daten(gruppierte_daten):
    for artikel, anzahl in gruppierte_daten.items():
        print(f"{artikel}: {anzahl}")

def speichere_in_datei(gruppierte_daten, dateiname):
    try:
        with open(dateiname, 'w', encoding='utf-8') as datei:
            datei.write(f"{'Ware':<20} {'Anzahl':>10}\n")
            datei.write("="*31 + "\n")
            for artikel, anzahl in gruppierte_daten.items():
                datei.write(f"{artikel:<20} {anzahl:>8}\n")
        print(f"Gruppierte Daten wurden in der Datei {dateiname} gespeichert.")
    except IOError:
        print(f"Ein Fehler ist beim Schreiben der Datei {dateiname} aufgetreten.")

# Verzeichnis und Dateinamen für die Eingabe- und Ausgabedateien
verzeichnis = "./programme/Woche3/"
dateiname_eingabe = os.path.join(verzeichnis, "raw_shopping_list.txt")
dateiname_ausgabe = os.path.join(verzeichnis, "Shopping-Liste.txt")

# Einlesen der Datei
inhalte = lese_datei(dateiname_eingabe)

# Ausgabe des ursprünglichen Inhalts
print("Ursprünglicher Inhalt der Datei:")
for eintrag in inhalte:
    print(eintrag)

# Gruppierung der Inhalte
gruppierte_daten = gruppiere_inhalte(inhalte)

# Ausgabe der gruppierten Daten
print("\nGruppierte Daten:")
drucke_gruppierte_daten(gruppierte_daten)

# Speichern der gruppierten Daten in einer Datei als Tabelle
speichere_in_datei(gruppierte_daten, dateiname_ausgabe)
