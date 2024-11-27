# Funktion zur Überprüfung, ob set1 eine Teilmenge von set3 ist
def is_subset(set1, set3):
    return set1.issubset(set3)

# Beispielhafte Mengen
set1 = {1, 2, 3}
set2 = {7, 8, 9}
set3 = {1, 2, 3, 4, 5}

RED = '\033[91m'
RESET = '\033[0m'

# Überprüfung, ob set1 eine Teilmenge von set2 ist
subset_result1 = is_subset(set1, set3)
subset_result2 = is_subset(set2, set3)

# Ausgabe des Ergebnisses
if subset_result1:
    print(f"Menge {set1} ist eine Teilmenge von Menge {set3}.")
else:
    print(f"Menge {set1} ist {RED}keine{RESET} Teilmenge von Menge {set3}.")

if subset_result2:
    print(f"Menge {set2} ist eine Teilmenge von Menge {set3}.")
else:
    print(f"Menge {set2} ist {RED}keine{RESET} Teilmenge von Menge {set3}.")
