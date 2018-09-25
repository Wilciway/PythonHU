

def kwadraten_som(grondgetallen):
    som = 0
    for x in grondgetallen:
        if x > 0:
            som=som+x*x
    return som

getallen = ([4, 5, 3, -81])
print(kwadraten_som(getallen))