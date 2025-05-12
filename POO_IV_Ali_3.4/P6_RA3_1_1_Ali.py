# Autor: Ali
# Data: {data}
# Exercici 1 - Herència: Animals

class Animal:
    def parlar(self):
        print("L'animal fa un so")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")

g = Gos()
g.parlar()

gat = Gat()
gat.parlar()
