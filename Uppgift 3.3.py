poäng = int(input('Hur många poäng fick du på matteprovet? '))

if poäng >= 51:
    print('Hur fick du mer än vad som var max på provet?!?!')
elif poäng >= 45: 
    print('Betyg: A')
elif poäng >= 40:
    print('Betyg: B')
elif poäng >= 35:
    print('Betyg: C')
elif poäng >= 30:
    print('Betyg: D')
elif poäng >= 25:
    print('Betyg: E')
elif poäng <= 24:
    print('Betyg: F')