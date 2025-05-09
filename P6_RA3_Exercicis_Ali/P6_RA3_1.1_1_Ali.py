# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Cotxe amb atributs bàsics i mètode per mostrar informació

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Model: {self.model}, Any: {self.any}")
