årskort = float(input('Hur mycket kostar ett årskort? '))
biljett = float(input('Hur mycket kostar en biljett? '))
besök = float(input('Hur mångar gånger har du tänkt att besöka gymmet under året? '))

biljett = biljett*besök
if årskort <= biljett:
  print(f'Årskort är mer värt än att köpa biljetter varje besök!')
else:
    print('Det är mer värt att köpa biljetter varje besöker istället för årskort')
