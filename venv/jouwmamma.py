file = open("Kaartnummers.txt","r")
BiggestNumber = 0
for line in file:
    number, name = line.split(',')
    CardNumber = int(number)
    if CardNumber > BiggestNumber:
        BiggestNumber = CardNumber





print(BiggestNumber)
file.close()

