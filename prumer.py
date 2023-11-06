def prumer (seznam : list)-> float:
    suma=0
    for i in seznam:
        suma=suma+i
    vysledek=suma/len(seznam)
    return vysledek 

print(prumer([1,2,3,6]))
