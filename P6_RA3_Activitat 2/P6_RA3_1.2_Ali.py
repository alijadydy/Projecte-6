# Autor: Ali
# Data: 09/05/2025
# Exercici: 2 - Estudiant amb nota protegida
# Descripció: Classe Estudiant amb atribut protegit _nota i mètodes per llegir i modificar la nota.

class Estudiant:
    def __init__(self, nota):
        self._nota = nota

    def get_nota(self):
        return self._nota

    def set_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota
