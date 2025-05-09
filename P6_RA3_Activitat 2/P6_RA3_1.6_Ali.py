# Autor: Ali
# Data: 09/05/2025
# Exercici: 6 - Producte amb preu controlat
# Descripció: Classe Producte amb nom públic i preu privat. El preu només es pot modificar si és major que 0.

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def get_preu(self):
        return self.__preu

    def set_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
