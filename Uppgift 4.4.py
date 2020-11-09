
meter = int(input('Ange meter i heltal: '))
cm = meter * 100
antal = 0
while cm > 1:
    antal = antal + 1
    cm = cm*0.7
print(f'Bollen stutsar {antal} gånger')