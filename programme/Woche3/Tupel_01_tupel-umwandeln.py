# Funktion zur Umwandlung eines Tupels in eine Liste
def tuple_to_list(input_tuple):
    return list(input_tuple)

# Funktion zur Umwandlung einer Liste in ein Tupel
def list_to_tuple(input_list):
    return tuple(input_list)

# Beispielhafte Verwendung der Funktionen
sample_tuple = (1, 2, 3, 4, 5)
sample_list = [1, 2, 3, 4, 5]

converted_list = tuple_to_list(sample_tuple)
converted_tuple = list_to_tuple(sample_list)

print('\nUmwandling einer Liste in ein Tupel:')
print("Ursprüngliches Tupel:", sample_tuple)
print("In Liste umgewandelt:", converted_list)

print('\nUmwandling eines Tupel in eine Liste:')
print("Ursprüngliche Liste:", sample_list)
print("In Tupel umgewandelt:", converted_tuple)
print()
