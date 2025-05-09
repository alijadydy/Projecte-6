# Autor: Ali
# Data: 09/05/2025
# Exercici: 1 - Compte Bancari Simple
# Descripció: Classe CompteBancari amb atribut privat __saldo i mètodes públics per ingressar, retirar i consultar el saldo.

class CompteBancari:
    def __init__(self):
        self.__saldo = 0

    def ingressar(self, quantitat):
        if quantitat > 0:
            self.__saldo += quantitat

    def retirar(self, quantitat):
        if 0 < quantitat <= self.__saldo:
            self.__saldo -= quantitat

    def consultar_saldo(self):
        return self.__saldo
