cont=True
while (cont):
    try:
        start = int(input ('Start: '))
        end = int(input ('End: '))
        step = int(input ('Schrittweite: '))

        if step < 0:
            print(f'Bitte geben sie eine positive Zahl für die Schrittweise ein.')
            continue

        out=''
        counter=start
        while counter <= end:
            print(counter)
            out += f'{counter}' 
            counter+= step
    
        weiter = input ('Programm Abbrechen? (j) ... sonst beliebige Taste drücken um es nochmal auszuführen:  ')
        if (weiter == 'j'):
            cont = False

    except Exception as e:
        print(f'falsche Eingabe, nochmal probieren: {e}' )
        again = input('nochmal j|n')
        if again == 'n':
            break