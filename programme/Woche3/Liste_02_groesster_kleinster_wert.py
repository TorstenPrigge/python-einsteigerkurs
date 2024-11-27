# Eingabe einer Liste von Strings
#liste = input("Geben Sie eine Liste von Strings ein (durch Kommas getrennt): ")
liste = "ach, du, meine, Güte, kompliziert "

# Umwandeln der Eingabe in eine Liste von Strings
liste = liste.split(", ")

# Finden des längsten und kürzesten Strings in der Liste
laengster_string = max(liste, key=len)
kuerzester_string = min(liste, key=len)

# Ausgabe des längsten und kürzesten Strings
print(f"Der längste String in der Liste ist: {laengster_string}")
print(f"Der kürzeste String in der Liste ist: {kuerzester_string}")
