svar = input('Skriv in antalet sekunder: ') # Tar input från användaren 

sek = int(svar) # Konverterar inputen till ett heltal

week = sek // 604_800

sek = sek % 604_800

dag = sek // 86_400

sek = sek % 86_400

tim = sek // 3_600  

sek = sek % 3_600

min = sek // 60

sek = sek % 60

print(f'Veckor: {week} \nDagar: {dag} \nTimmar: {tim} \nMinuter {min} \nSekunder {sek}')