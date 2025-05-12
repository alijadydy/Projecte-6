# Autor: Ali
# Data: {data}
# Exercici 4 - Herència: Figura geomètrica

import math

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)

q = Quadrat(4)
print("Àrea del quadrat:", q.area())

c = Cercle(3)
print("Àrea del cercle:", round(c.area(), 2))
