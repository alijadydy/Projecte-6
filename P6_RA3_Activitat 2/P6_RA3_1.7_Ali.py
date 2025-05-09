# Autor: Ali
# Data: 09/05/2025
# Exercici: 7 - Temps en hores
# Descripció: Classe Rellotge amb hores entre 0 i 23 i format “HH:00”.

class Rellotge:
    def __init__(self, hores=0):
        self.__hores = hores

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, h):
        if 0 <= h <= 23:
            self.__hores = h

    def mostrar(self):
        return f"{self.__hores:02d}:00"
