# Beispielhaftes Dictionary
example_dict = {
    'Name': 'Torsten',
    'Alter': 62,
    'Beruf': 'IT Ingenieur',
    'PLZ': '14612',
    'Stadt': 'Falkensee'
}

# Funktion zur Ausgabe aller Schlüssel eines Dictionaries
def print_keys(input_dict):
    for key in input_dict.keys():
        print(key)

# Ausgabe der Schlüssel
print("Die Schlüssel des Dictionaries sind:")
print_keys(example_dict)
