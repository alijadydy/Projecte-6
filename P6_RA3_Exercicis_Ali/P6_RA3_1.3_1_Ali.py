# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Persona amb mètode de presentació

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")
