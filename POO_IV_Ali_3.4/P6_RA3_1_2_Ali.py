# Autor: Ali
# Data: {data}
# Exercici 2 - Herència: Vehicles

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El vehicle {self.marca} ha arrencat.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")

cotxe = Cotxe("Toyota")
cotxe.arrencar()
cotxe.tocar_claxon()
