# Autor: Ali
# Data: 09/05/2025
# Exercici: 9 - Gestor de puntuació
# Descripció: Classe Joc amb puntuació inicial a 0, sumar punts i reiniciar.

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    def get_puntuacio(self):
        return self.__puntuacio
