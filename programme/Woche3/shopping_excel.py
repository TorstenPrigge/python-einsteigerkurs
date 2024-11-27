import os
import pandas as pd

def lese_datei(dateiname):
    try:
        # Lesen der Excel-Datei
        df = pd.read_excel(dateiname)
        # Annahme, dass die Einkaufsliste in der ersten Spalte steht
        inhalte = df.iloc[:, 0].tolist()
        return inhalte
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

def speichere_in_excel(gruppierte_daten, dateiname):
    try:
        # Erstellen eines DataFrame aus dem Dictionary
        df = pd.DataFrame(list(gruppierte_daten.items()), columns=['Ware', 'Anzahl'])
        # Schreiben des DataFrame in eine Excel-Datei
        df.to_excel(dateiname, index=False)
        print(f"Gruppierte Daten wurden in der Datei {dateiname} gespeichert.")
    except IOError:
        print(f"Ein Fehler ist beim Schreiben der Datei {dateiname} aufgetreten.")

# Verzeichnis und Dateinamen für die Eingabe- und Ausgabedateien
verzeichnis = "./programme/Woche3/"
dateiname_eingabe = os.path.join(verzeichnis, "raw_shopping_list.xlsx")
dateiname_ausgabe = os.path.join(verzeichnis, "Shopping.xlsx")

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

# Speichern der gruppierten Daten in einer Excel-Datei
speichere_in_excel(gruppierte_daten, dateiname_ausgabe)
