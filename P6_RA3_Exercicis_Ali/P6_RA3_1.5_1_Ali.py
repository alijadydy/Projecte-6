# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Estudiant amb mètode per saber si ha aprovat

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5
