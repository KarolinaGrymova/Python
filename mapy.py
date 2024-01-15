from dataclasses import dataclass



@dataclass
class Klic:
    klic: int

    def __eq__(self, __o: object) -> bool:
        return True

class Hodnota:
    def __init__(self, hodnota: str) -> None:
        self.hodnota=hodnota

mapa: dict[Klic, Hodnota] = {}
map[Klic(1)]=Hodnota("text")

