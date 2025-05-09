# Autor: Ali
# Data: 09/05/2025
# Exercici: 8 - Alumne amb edat controlada
# Descripció: Classe Alumne amb atribut __edat que no pot ser negatiu.

class Alumne:
    def __init__(self, edat):
        self.__edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
