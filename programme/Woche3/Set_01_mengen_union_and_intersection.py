# Funktion zur Berechnung der Vereinigung zweier Mengen
def union_of_sets(set1, set2):
    return set1.union(set2)

# Funktion zur Berechnung der Überschneidung zweier Mengen
def intersection_of_sets(set1, set2):
    return set1.intersection(set2)

# Beispielhafte Mengen
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Berechnung der Vereinigung und der Überschneidung
union_result = union_of_sets(set1, set2)
intersection_result = intersection_of_sets(set1, set2)

# Ausgabe der Ergebnisse
print("Menge 1:", set1)
print("Menge 2:", set2)
print("Vereinigung:", union_result)
print("Überschneidung:", intersection_result)
