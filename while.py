import random
randomTal = random.randint(1,10)
gissa = 0
tries = 1
while gissa != randomTal :
    tries += 1
    gissa = float(input('Gissa på ett heltal mellan 1 och 10: '))
    if gissa < randomTal :
        print(f"{gissa} är för lite")
    elif gissa > randomTal :
        print(f"{gissa} är för mycket")
    else:
        print(f"{gissa} är rätt")
print(f"👌 Grattis! Du gissade rätt number på {tries} antal försök!👌 ")