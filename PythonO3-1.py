print('=== Välkommen! Mata in ett av menyvalen. ===')



def IsGradeCorrect(Grade):
    if ':' not in Grade:
        return(False)
    
    if 3<=int(Grade[-1])<=5:
        return(True)
    else:
        return(False)
    


def RapporteraBetyg():
    Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))
    course = ()

    while Resultat != ' ' and Resultat != '':
        if IsGradeCorrect(Resultat):
            course = course + tuple(Resultat.split(':'))

        else:
            print("Felaktig inmatning, försök igen!")

        Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))
    #Archive(course)
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

