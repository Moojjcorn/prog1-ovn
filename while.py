import random
randomTal = random.randint(0,10)
gissa = 0
tries = 1
while gissa != randomTal :
    gissa = float(input('Gissa på ett heltal mellan 0 och 10: '))
    if gissa < randomTal :
        print(f"{gissa} är för lite")
        tries += 1
    elif gissa > randomTal :
        print(f"{gissa} är för mycket")
        tries += 1
    else:
        print(f"{gissa} är rätt")
print(f"👌 Grattis! Du gissade rätt number på {tries} antal försök!👌 ")