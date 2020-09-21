pris = float(input('Skriv priset på varan: '))
moms = float(input('Skriv in varans moms i procent: '))

emoms = pris / (moms / 100 + 1)

print(f'Priset exclusivt moms : {emoms}kr ')
print(f'Momsen är: {pris - emoms}kr ')