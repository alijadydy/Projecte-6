# Autor: Ali
# Data: 09/05/2025
# Descripció: Classe Llibre amb mètode per mostrar informació

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"{self.titol}, {self.autor}, {self.any}")
