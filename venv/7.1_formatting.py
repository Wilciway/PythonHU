def table():
    celcius=0
    for celcius in range(-30,40,10):
        fahrenheit = celcius * 1.8 + 32
        print("{}   {}".format(fahrenheit, celcius))

print(table())