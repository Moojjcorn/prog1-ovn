idag = float(input('Mätarinställningen idag? '))
förraÅret = float(input('Mätarinställningen för ett år sedan? '))
bensin = float(input('Hur mycket bensin har förbrukats under året? '))
kördaMil = idag - förraÅret 
print(f'Antal körda mil: {kördaMil:.2f}')
print(f'Antal liter bensin: {bensin:.2f}')
FörbrukningMil = bensin / kördaMil
print(f'Förbrukning per mil {FörbrukningMil:.2f}')