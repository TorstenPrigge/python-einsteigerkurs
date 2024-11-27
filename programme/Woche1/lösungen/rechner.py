# Das Programm berechnet Summe, Differenz, Produkt und Differenz zweier Zahlen, die eingegeben wurden



zahl1 = float(input('Bitte Zahl 1 eingeben: '))

while True:
    try:
        zahl2 = float(input('Bitte Zahl 2 eingeben: '))
        if zahl2 != 0:
            #print(f"Du hast die Zahl {zahl2} eingegeben.")
            break  # Schleife beenden, wenn Eingabe nicht 0 ist       
        else:
            print("Die Zahl darf nicht 0 sein. Bitte erneut versuchen.")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")


summe = zahl1 + zahl2
diff = zahl1 - zahl2
product = zahl1 * zahl2
quotient = zahl1 / zahl2

print(f'Summe: {summe}')
print(f'Differenz: {diff}')
print(f'Produkt: {product}')
print(f'Quotient: {quotient}')
