# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Punt amb càlcul de distància a un altre punt

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre):
        return math.sqrt((self.x - altre.x)**2 + (self.y - altre.y)**2)
