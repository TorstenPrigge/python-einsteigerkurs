# Eingabe einer Liste von Elementen
#liste = input("Geben Sie eine Liste von Elementen ein (durch Kommas getrennt): ")
liste = "apfel, banane, gurke, Gurke, Apfel, Kartoffel, apfel, Kartoffel"

# Umwandeln in lower case:
liste = liste.lower()

# Umwandeln der Eingabe in eine Liste
liste = liste.split(", ")

# Entfernen der Duplikate, indem die Liste in ein Set umgewandelt wird
liste_ohne_duplikate = list(set(liste))

# Alphabetisch sortieren
liste_ohne_duplikate.sort()

# ANSI Escape-Sequenz für rote Farbe
rot = "\033[31m"
reset = "\033[0m"  # Zurücksetzen der Farbe auf die Standardfarbe

# Ausgabe der alphabetisch sortierten Liste ohne Duplikate und in roter Schrift
print(f"Die alphabetisch sortierte Liste ohne Duplikate ist: {rot}{reset}")

# Ausgabe der Liste untereinander, Zeilenumbruch außerhalb des f-Strings
for item in liste_ohne_duplikate:
    print(f"{rot}{item}{reset}")





