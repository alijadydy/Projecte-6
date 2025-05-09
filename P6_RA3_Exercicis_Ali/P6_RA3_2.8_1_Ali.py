# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Biblioteca que gestiona llibres

from P6_RA3_1.9_1_Ali import Llibre

class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for llibre in self.llibres:
            llibre.mostrar_info()

b = Biblioteca()
b.afegir_llibre(Llibre("1984", "George Orwell", 1949))
b.mostrar_llibres()
