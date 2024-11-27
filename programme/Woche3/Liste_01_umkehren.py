#Programm, das die Elemente einer gegebenen Liste in umgekehrter Reihenfolge ausgibt.

# Eingabe einer Liste von Elementen
#elementlist = input("Geben Sie eine Liste von Elementen ein (durch Kommas getrennt): ")
elementlist = "Apfel, Birne, Orange, Banane"

# Umwandeln der Eingabe in eine Liste, indem die Eingabe an den Kommas getrennt wird
elementlist = elementlist.split(", ")

# Umkehren der Liste
revers = elementlist[::-1]

# ANSI Escape-Sequenz für rote Farbe
rot = "\033[31m"
reset = "\033[0m"  # Zurücksetzen der Farbe auf die Standardfarbe

# Ausgabe der umgekehrten Liste in Rot
print(elementlist)
print(f"Die umgekehrte Liste ist: {rot}{' '.join(revers)}{reset}")


