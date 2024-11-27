# Funktion zur Erstellung eines Dictionaries mit Zahlen und ihren Quadraten
def create_square_dict(n):
    return {i: i**2 for i in range(1, n+1)}

# Benutzer zur Eingabe von n auffordern
while True:
    try:
        n = int(input("Geben Sie eine Zahl (n) ein: "))
        break
    except ValueError:
        print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

# Erstellung des Dictionaries
square_dict = create_square_dict(n)

# Ausgabe des Dictionaries, jede Zahl und ihr Quadrat in einer neuen Zeile mit Überschrift
print("Zahl  Quadrat")
print("--------------")
for number, square in square_dict.items():
    print(f"{number:>4} {square:>8}")

