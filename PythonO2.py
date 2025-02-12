x = int(input('Mata in ett heltal mellan 1-26: '))
print('')


def NumberToLetter(Number):
    return(chr(Number+96))        

def Factorial(Number):
    result = 1
    for i in range(1, Number+1):
        result = result*i
    return(result)

def Fibb(x):
    if x == 1 or x == 2:
        return(1)
    else:
        x = (Fibb(x-1)+Fibb(x-2))
    return(x)

def Table(Rows):

    print('N' + '      ' + 'Bokstav N' +'      ' + 'N-Fakultet' +'      ' + 'Fibonacci')

    for i in range(1, Rows+1):
        print(str(i) +'      '+ str(NumberToLetter(i)) + '      ' + str(Factorial(i)) + '      ' + str(Fibb(i)))

Table(x)