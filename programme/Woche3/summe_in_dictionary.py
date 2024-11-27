# Beispielhaftes Dictionary mit numerischen Werten
example_dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40
}

# Funktion zur Berechnung der Summe aller Werte in einem Dictionary
def sum_of_values(input_dict):
    return sum(input_dict.values())

# Berechnung der Summe
total_sum = sum_of_values(example_dict)

# Ausgabe des Ergebnisses
print("Das Dictionary:", example_dict)
print("Die Summe aller Werte im Dictionary:", total_sum)
