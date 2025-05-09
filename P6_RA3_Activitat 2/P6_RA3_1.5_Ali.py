# Autor: Ali
# Data: 09/05/2025
# Exercici: 5 - Sensor amb valors limitats
# Descripció: Classe Sensor amb getter i setter per __valor, limitat entre 0 i 100.

class Sensor:
    def __init__(self, valor=0):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
