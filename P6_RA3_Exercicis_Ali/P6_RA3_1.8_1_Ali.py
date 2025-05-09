# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Animal amb mètode fer_soroll

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print("Fa un soroll")
