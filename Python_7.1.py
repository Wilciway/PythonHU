def convert(celcius):
    "Zet Celcius om naar Fahrenheit."
    print(" F     C")
    fahrenheit=celcius*1.8+32
    return("{}   {}" .format(fahrenheit,celcius))

def table():
    "Celcius omgezet naar Fahrenheit in stappen van 10 graden."
    celcius=0
    print(" F       C")
    for celcius in range(-30,40,10):
        fahrenheit = celcius * 1.8 + 32
        print("{}   {}".format(fahrenheit, celcius))



print(convert(20))
print(table())

