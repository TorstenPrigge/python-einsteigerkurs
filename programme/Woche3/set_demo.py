liste = ('winter', 'spring', 'summer', 'autumn', 'spring', 'summer')
seasons = {'winter', 'spring', 'summer', 'autumn', 'spring', 'summer'}
seasonsset = set(['winter', 'spring', 'summer', 'autumn', 'spring', 'summer'])

#print(seasons[1]) # funktioniert nicht mit sets

print(liste)
print('Länge der Liste: ',len(liste))
print('Länge des Sets: ',len(seasonsset))
print()
print('Liste:')
for season in liste:
    print(season)
print()
print('Set:')
for season in seasonsset:
    print(season)