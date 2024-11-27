
while True:
    try:
        
        MAX_ALTER=150
        ERW_ALTER=18
        RENTEN_ALTER=67
        
        # Benutzer nach seinem Namen und seinem Alter fragen
        name = input('Bitte gib deinen Namen ein: ')
        name = str(name)
        alter = input('Bitte gib dein Alter ein: ')
        alter = int(alter)

        # Altersgruppe bestimmen
        if alter < 0:
            print("Negatives Alter ist nicht realistisch. Gib bitte ein korrektes Alter ein!")
        elif alter >= MAX_ALTER:
            print(f"Wow ... {name}, du bist ein biologisches Wunder oder ein Alien. So alt wird doch kein normaler Mensch!")
        elif alter < ERW_ALTER:
            print(f"{name}, Du bist jugendlich.")
        elif alter <= RENTEN_ALTER:
            print(f"{name}, Du bist erwachsen.")
        else:
            print(f"{name}, Du bist im Rentenalter.")

        cancel = input("Zum Abbruch 'y' eingeben oder beliebige Taste drürcken um neu einzugeben: ")
        if cancel == 'y':
            break

    except Exception as e:
        print (f'*** Fehler bei der Alterskategorisierung: {e}')
        again = input('nochmal eingeben? j|n ')
        if again == 'n':
            break

