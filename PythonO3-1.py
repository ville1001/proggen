print('=== Välkommen! Mata in ett av menyvalen. ===')


def IsDateCorrect(Date):
    try:
        year, month, day = map(int, Date.split('-'))  # Omvandlar till int

        if year < 0 or year > 3000:
            print("Felaktigt år")
            return False #kontrolerar året
        elif month < 1 or month > 12:
            print("Felaktigt månad")
            return False #kontrollerar månaden
        elif day < 1 or day > 31:
            print("Felaktigt dag")
            return False #Kontrollerar dagen
        else:
            return(True)
    except:
        print("Value error exception")
        return(False)



def lagra(Grades):
    Date = input("Mata in ett rapporteringdatum: ")

    if(IsDateCorrect(Date)):
        for i in range(len(Grades)):
            Grades[i] = Grades[i] + (Date,)

    else:
        print("ojdå fel inmatning, försök igen")
        lagra(Grades)

    print(Grades)

def IsGradeCorrect(Grade):
    if ':' not in Grade:
        return(False)
    
    if 3<=int(Grade[-1])<=5:
        return(True)
    else:
        return(False)
    

def RapporteraBetyg():
    Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))
    Archive = []

    while Resultat != ' ' and Resultat != '':
        if IsGradeCorrect(Resultat):
            kurs_tuple = tuple(Resultat.split(':'))
            Archive.append(kurs_tuple)
        else:
            print("Felaktig inmatning, försök igen!")

        Resultat = input(str("Mata in en kurs och ett betyg på formen kurskod:betyg: "))
    print("Klar med inmatningar")
    return(Archive)


while True:
    
    print('')
    print("1: Mata in kurser och  betyg")
    print("2: Gör en rapportering")
    print("0: Avsluta")

    choice = int(input("Mata in ett menyval: "))

    if(choice == 1):
        Resultat = RapporteraBetyg()
        
    elif(choice == 2):
        lagra(Resultat)
        
    elif(choice == 0):
        print("Programmet avslutas")
        break
    else:
        print("Felaktigt val, försök igen")

