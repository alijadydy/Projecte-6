# Autor: Ali
# Data: 09/05/2025
# Exercici: 3 - Termòstat
# Descripció: Classe Termostat amb getter i setter per __temperatura, limitat entre 10 i 30 °C.

class Termostat:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temp):
        if 10 <= nova_temp <= 30:
            self.__temperatura = nova_temp
