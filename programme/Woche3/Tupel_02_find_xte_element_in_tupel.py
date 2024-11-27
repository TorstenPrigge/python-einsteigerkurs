def finde_n_tes_element(tupel, n):
    if n < 0 or n >= len(tupel):
        return "Index außerhalb des gültigen Bereichs."
    return tupel[n]

# Beispiel-Tupel
tupel = (10, 20, 30, 40, 50)

# Benutzerabfrage für den Index
n = int(input("Geben Sie den Index ein (beginnend bei 0): "))

element = finde_n_tes_element(tupel, n-1)
print(f"Das Element an der Position {n} ist: {element}")
3


