# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Cercle amb càlcul d'àrea i perímetre

import math

class Cercle:
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * self.radi ** 2

    def perimetre(self):
        return 2 * math.pi * self.radi
