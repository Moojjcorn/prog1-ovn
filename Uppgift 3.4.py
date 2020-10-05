t = float(input('Vilken temperatur är det? '))
if t <= 18:
    print('Det är kallt \nSätt på värmen')
    if t <= 12:
        print('Sätt på en jacka!')
    if t <= 5:
        print('Det är svinkallt!')
else:
    print('Det är varmt')
    if t >= 22: 
        print('Stäng av värmen')
    if t >= 30:
        print('Det är ökenhett!')
