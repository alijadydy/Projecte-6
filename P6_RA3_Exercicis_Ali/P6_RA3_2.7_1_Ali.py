# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Gos que hereta d'Animal

from P6_RA3_1.8_1_Ali import Animal

class Gos(Animal):
    def fer_soroll(self):
        print("Bup bup!")

gos = Gos("Toby", "Gos")
gos.fer_soroll()
