print('=== Välkommen! Mata in ett av menyvalen. ===')

def RapporteraBetyg():
    Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))

    while Resultat != ' ':
        rapport = tuple(Resultat.split(':'))
        print(rapport)
        
        Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))

    print("Klar med inmatningar")


while True:
    print('')
    print("1: Mata in kurser och  betyg")
    print("2: Gör en rapportering")
    print("0: Avsluta")
    choice = int(input("Mata in ett menyval: "))
    

    if(choice == 1):
        RapporteraBetyg()
    elif(choice == 2):
        print("spling")
    elif(choice == 0):
        print("Programmet avslutas")
        break
    else:
        print("Felaktigt val, försök igen")

