# Funktion, die überprüft, ob ein gegebenes Element in einem Tupel vorhanden ist
def is_element_in_tuple(input_tuple, element):
    return element in input_tuple

# Beispielhafte Verwendung der Funktion
sample_tuple = (10, 20, 30, 40, 50)

# Benutzer zur Eingabe des zu suchenden Elements auffordern
element = int(input("Geben Sie das Element ein, das Sie im Tupel suchen möchten: "))





# Überprüfung, ob das Element im Tupel vorhanden ist
if is_element_in_tuple(sample_tuple, element):
    print(f"Das Element {element} ist im Tupel vorhanden.")
else:
    # ANSI-Escape-Sequenz für rote Schrift
    RED = '\033[91m'
    RESET = '\033[0m'
    print(f"Das Element {element} ist {RED}nicht{RESET} im Tupel vorhanden.")