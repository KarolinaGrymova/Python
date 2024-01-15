from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class Karta:
    id: str
    jmeno: str
    prijmeni: str


class Kustos(ABC):

    @abstractmethod
    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        ...

    @abstractmethod
    def odeber_kartu(self, id_karty: str) -> Optional[Karta]:
        ...

    @abstractmethod
    def muze_vstoupit(self, id_karty: str) -> bool:
        ...


mapa : dict[str,str] = {
     "car": "auto",
     "flower" : "kvetina"
}

class MujKustos(Kustos):
    def __init__(self) -> None:
        ...

    def pridej_kartu(self, id_karty: str, jmeno: str, prijmeni: str) -> Optional[Karta]:
        ...











flower_cesky = mapa["flower"]
print("flower je ceska: " + flower_cesky)
mapa["bike"] = "motorka"
print("bike je ceska: " + str(mapa["bike"]))

ff = mapa["flowera"]
#ff = mapa.get("flowera")
print(ff)
# print("flower je ceska: " + str(mapa["flower"]))
