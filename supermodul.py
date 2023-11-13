ans=0
posledni_vysledek=0
def plus(cislo1,cislo2: float)->float:
    global posledni_vysledek
    posledni_vysledek=cislo1+cislo2
    return posledni_vysledek
     

def multi(cislo1,cislo2: float)->float:
    global posledni_vysledek
    posledni_vysledek=cislo1*cislo2
    return posledni_vysledek

def uloz_vysledek():
    global ans
    ans=posledni_vysledek

def vrat_pamet():
    global posledni_vysledek
    return posledni_vysledek

def pricti_k_pameti(op: float)->float:
    global ans
    vysledek=op+ans
    return vysledek