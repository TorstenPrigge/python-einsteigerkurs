# Das Programm zählt die Anzahl aller Vokale in einem eingegebenen String und gibt die Anzahl aus.
#eingabe = input("Geben Sie einen String ein: ")
eingabe = "Dies ist ein Text"

vokale = "aeiouäÖü"

vokal_count = 0

number_of_e = eingabe.count('e')
#print(number_of_e)

# Durchlaufen jedes Zeichens im String
for character in eingabe.lower():
    if character in vokale:
        vokal_count += 1

print(f"Die Anzahl der Vokale im String ist: {vokal_count}")