vaken = input('Är du vaken? [ja/nej]').lower()
if vaken == 'ja':
    print('God morgon!')
    frukost = input('Vill du äta till frukost? \n\tMackor\n\tFil och flingor\n\tGröt\n ').lower()
elif vaken == 'Nej':
    print('Fortsätt sova')
else:
    print('Snooze 5 min')
#
if frukost == 'mackor': 
    pålägg = input('Vilka pålägg på mackan? \n\tSkinka\n\tOst\n\tGurka\n ').lower()
    if pålägg == 'skinka':
        print('Du gör en skinkmacka')
    elif pålägg == 'ost':
        print('Du gör en ostmacka')
    elif pålägg == 'gurka':
        print('Du gör en gurkmacka')
    else:
        print('Vad för pålägg ville du ha?')
elif frukost == 'fil och flingor':
    flingor = input('Vilka flingor vill du ha? \n\tCheerios\n\tAll-bran\n\tCornflakes\n ').lower()
    if flingor == 'cheerios':
        print('Du äter fil och cheerios')
    elif flingor == 'all-bran':
        print('Du äter fil och all-bran')
    elif flingor == 'cornflakes':
        print('Du äter fil och cornflakes')
    else:
        print('Vilka flingor ville du ha?')
elif frukost == 'gröt':
    gröt = input('Vilken gröt vill du ha? \n\tHavregrynsgröt\n\tMannagrynsgröt\n\tRisgrynsgröt\n ').lower()
    if gröt == 'havregrynsgröt':
        print('Du lagar havregrynsgröt')
    elif gröt == 'mannagrynsgröt':
        print('Du lagar mannagrynsgröt')
    elif gröt == 'risgrynsgröt':
        print('Du lagar risgrynsgröt')
    else:
        print('Vilken gröt vill du laga?')
else:
    print('Ät inget då')