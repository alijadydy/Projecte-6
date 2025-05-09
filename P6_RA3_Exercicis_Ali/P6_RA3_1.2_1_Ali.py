# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Rectangle amb càlculs d'àrea i perímetre

class Rectangle:
    def __init__(self, amplada, alcada):
        self.amplada = amplada
        self.alcada = alcada

    def area(self):
        return self.amplada * self.alcada

    def perimetre(self):
        return 2 * (self.amplada + self.alcada)
