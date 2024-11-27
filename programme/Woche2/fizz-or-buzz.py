from colorama import Fore, Style


START=1
END=30
DIVIDER1=3
DIVIDER2=5
AUSGABE1="foo"
AUSGABE2="bar"
AUSGABE3=AUSGABE1+AUSGABE2

print()
print("\033[4mErklärung:\033[0m")
print(Fore.YELLOW + f'{AUSGABE1}      => Zahl ist durch {DIVIDER1} teilbar' + Style.RESET_ALL)
print(Fore.GREEN + f'{AUSGABE2}      => Zahl ist durch {DIVIDER2} teilbar' + Style.RESET_ALL)
print(Fore.BLUE + f'{AUSGABE3}   => Zahl ist durch {DIVIDER1} und {DIVIDER2} teilbar' + Style.RESET_ALL)
print(' alle anderen Zahlen sind weder durch 3 noch durch 5 teilbar')
print()

for number in range(START, END):
    if number % DIVIDER1 == 0 and number % DIVIDER2 == 0:
        print(Fore.YELLOW + f'{number} -> {AUSGABE3}' + Style.RESET_ALL)
    elif number % DIVIDER1 == 0:
        print(Fore.GREEN + f'{number} -> {AUSGABE1}'+ Style.RESET_ALL )
    elif number % DIVIDER2 == 0:
        print(Fore.BLUE + f'{number} -> {AUSGABE2}'+ Style.RESET_ALL )
    else:
        print(f'{number} ')