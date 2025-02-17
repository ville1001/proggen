import random

random.seed(123456)

lower_limit = lowerFloor = int(input("Nedre gräns: "))
while lower_limit < 0:
    print('Felaktitg värde')
    lower_limit = lowerFloor = int(input("Nedre gräns: "))

upper_limit = upperFloor = int(input("Övre gräns: "))
while upper_limit <= lower_limit:
    print('Felaktitg värde')
    upper_limit = upperFloor = int(input("Övre gräns: "))


step = int(input("Steglängd: "))
while step > (upper_limit-lower_limit):
    print("För store steglängs för detta intervall. Försök igen")
    step = int(input("Steglängd: "))

MaxCount = int(input("Antal gissningar: "))
while MaxCount < 0:
    print("För få gissningar valda! Försök igen!")
    MaxCount = int(input("Antal gissningar: "))


secret = random.randrange(lower_limit, upper_limit, step)

print("########## GISSNINGSSPELET ##########")

for i in range(MaxCount):
    guess = int(input("Mata in din gissning: "))
    if guess == secret:
        print("Du vann! Grattis!")
        break

    elif guess < secret:
        if(guess > lowerFloor):
            lowerFloor = guess

        print("Du gissade för lågt! Gissa mellan: " + str(lowerFloor) + " och " + str(upperFloor))

    else:
        if(guess < upperFloor):
            upperFloor = guess

        print("Du gissade för högt! Gissa mellan: " + str(lowerFloor) + " och " + str(upperFloor))
        