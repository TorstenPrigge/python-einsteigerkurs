# Beispielhaftes Dictionary
example_dict = {
    'Name': 'Alice',
    'Alter': 30,
    'Beruf': 'Ingenieurin',
    'Stadt': 'Berlin'
}

# Funktion zur Umwandlung eines Dictionaries in eine Liste von Tupeln
def dict_to_tuples(input_dict):
    return list(input_dict.items())

# Umwandlung des Dictionaries in eine Liste von Tupeln
tuples_list = dict_to_tuples(example_dict)

# Ausgabe der Liste von Tupeln
print("Das Dictionary als Liste von Tupeln:")
for item in tuples_list:
    print(item)
