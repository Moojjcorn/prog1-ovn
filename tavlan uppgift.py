inmatning = int(input('Skriv ett heltal: '))
svar = inmatning % 2

if svar == 1:
    print(f'Talet {inmatning} är ojämnt')
else:
    print(f'Talet {inmatning} är jämnt')