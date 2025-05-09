# Autor: Ali
# Data: 09/05/2025
# Exercici: 4 - Contrasenya segura
# Descripció: Classe Usuari amb mètodes per canviar i verificar una contrasenya privada.

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova

    def verificar_contrasenya(self, clau):
        return self.__contrasenya == clau
