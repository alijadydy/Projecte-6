# Autor: Ali
# Data: {data}
# Exercici 3 - Herència: Persones i treballadors

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")

t = Treballador("Ali", 21, "tècnic informàtic")
t.saludar()
t.mostrar_feina()
