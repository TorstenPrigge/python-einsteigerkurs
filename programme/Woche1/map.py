def quadrat(x):
    return x * x

zahlen = [1, 2, 3, 4]
ergebnisse = map(quadrat, zahlen)

print(list(ergebnisse))  # Ausgabe: [1, 4, 9, 16]

