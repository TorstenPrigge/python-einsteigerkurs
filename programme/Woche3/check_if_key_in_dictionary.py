# Beispielhaftes Dictionary
example_dict = {
    'Name': 'Alice',
    'Alter': 30,
    'Beruf': 'Ingenieurin',
    'Stadt': 'Berlin'
}

# Funktion zur Überprüfung, ob ein Schlüssel im Dictionary vorhanden ist
def is_key_in_dict(input_dict, key):
    return key in input_dict

# Benutzer zur Eingabe des zu überprüfenden Schlüssels auffordern
key_to_check = input("Geben Sie den Schlüssel ein, den Sie überprüfen möchten: ")

# Überprüfung, ob der Schlüssel im Dictionary vorhanden ist
result = is_key_in_dict(example_dict, key_to_check)

RED = '\033[91m'
RESET = '\033[0m'

# Ausgabe des Ergebnisses
if result:
    print(f"Der Schlüssel '{key_to_check}' ist im Dictionary vorhanden.")
else:
    print(f"Der Schlüssel '{key_to_check}' ist {RED}nicht{RESET} im Dictionary vorhanden.")
