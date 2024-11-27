# Funktion zur Umwandlung einer Liste in eine Menge und Entfernung von Duplikaten
def remove_duplicates(input_list):
    return set(input_list)

# Beispielhafte Liste mit Duplikaten
sample_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]

# Umwandlung der Liste in eine Menge und Entfernung von Duplikaten
unique_set = remove_duplicates(sample_list)

# Ausgabe der Ergebnisse
print("Ursprüngliche Liste:", sample_list)
print("Liste ohne Duplikate (als Menge):", unique_set)
