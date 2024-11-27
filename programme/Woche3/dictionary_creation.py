# Funktion zur Erstellung eines Dictionaries aus einer Liste von Schlüsseln und Werten
def create_dict_from_lists(keys, values):
    return dict(zip(keys, values))

# Beispielhafte Listen von Schlüsseln und Werten
keys = ['Name', 'Alter', 'Beruf', 'PLZ', 'Stadt']
values = ['Torsten', 62, 'DevOpsEngineer', '14612', 'Falkensee']

# Erstellung des Dictionaries
result_dict = create_dict_from_lists(keys, values)

# Ausgabe des erstellten Dictionaries, jedes Schlüssel-Wert-Paar in einer neuen Zeile
print("Das erstellte Dictionary:")
for key, value in result_dict.items():
    print(f"{key}: {value}")

