# Eingabe eines Strings vom Benutzer
#text = input("Geben Sie einen String ein: ")
text = "Dies ist ein Text."

# Überprüfen, ob der Text mit einem Punkt endet und den Punkt entfernen
if text.endswith(('.' , '!' , '?')):
    text = text[:-1]

# Umwandeln des Strings in eine Liste von Wörtern
wort_liste = text.split()

# Ausgabe der Liste von Wörtern
print("Die Liste von Wörtern ist:", wort_liste)

# Umwandeln der Liste von Wörtern zurück in einen String
neuer_string = " ".join(wort_liste)

# Ausgabe des neuen Strings
print("Der umgewandelte String ist:", neuer_string)
