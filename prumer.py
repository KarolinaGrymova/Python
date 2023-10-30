def prumer (seznam : list)-> float:
    soucet=0
    for i in seznam:
        soucet=soucet+i
    vysledek=soucet/len(seznam)
    return vysledek 

print(prumer([1,2,3]))
