# Autor: Ali
# Data: 07/05/2025
# Descripció: Llegeix el contingut d’un fitxer anomenat missatge.txt i el mostra per pantalla.

with open("missatge.txt", "r") as fitxer:
    contingut = fitxer.read()
    print(contingut)
