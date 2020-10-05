Minuter = float(input('Samtals minuter per månad: '))
kostnadMin = float(input('Kostnad i kr per samtals minut: '))
pris = Minuter*kostnadMin
if pris >= 300:
  pris = pris*0.9
  print(f'Pris per månad efter 10% rabatt: {pris}kr')
else:
    print(f'Pris per månad: {pris}kr')