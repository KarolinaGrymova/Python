def prumer (seznam : list[int])-> float:
    suma=0
    for i in seznam:
        suma=suma+i
    vysledek=suma/len(seznam)
    return vysledek 

print(prumer([1,3,4,6]))
