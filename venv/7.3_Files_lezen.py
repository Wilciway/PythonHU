file = open("Kaartnummers.txt","r")
regels = 0
BiggestNumber=0
positie=1

for line in file:
    number, name = line.split(',')
    CardNumber = int(number)
    regels += 1 #Na elke regel voegt het 1 toe aan regels om het aantal regels te tellen
    if CardNumber > BiggestNumber:  #elke keer dat CardNumber groter is dan BiggestNumber gaat die naar het volgende nummer tot het grootste nummer gevonden is
        BiggestNumber = CardNumber
        positie +=1   #elke keer dat het opnieuw zoekt naar het hoogste nummer voegt het 1 toe aan positie

print("Deze file telt ",regels," regels")
print("Het grootste kaartnummer is: ",BiggestNumber," en dat staat op regel ",positie)
file.close
