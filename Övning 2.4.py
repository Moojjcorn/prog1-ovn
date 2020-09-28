miles = float(input('Skriv i miles '))
gallon = float(input('Skriv i gallons '))

mil = (miles * 1.609344) / 10
liter = gallon * 3.785 

print(f'Miles to Mil: {mil:.2f} \nGallons to liter: {liter:.2f}')