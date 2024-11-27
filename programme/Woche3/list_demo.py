seasons1 = ['winter', 'spring', 'summer', 'autumn']
seasons2 = list(['winter', 'spring', 'summer', 'autumn'])
seasons3 = list(('winter', 'spring', 'summer', 'autumn'))


print()
print(seasons1[1])
print(seasons2[1])
print(seasons3[1])
print()
print(len(seasons1))
print(len(seasons2))
print(len(seasons3))
print()

for season in seasons1:
    print(season)

print()
for season in seasons2:
    print(season)

print()
for season in seasons3:
    print(season)