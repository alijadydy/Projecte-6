# Autor: Ali
# Data: 07/05/2025
# Descripció: Comprova si un fitxer existeix abans de llegir-lo. Mostra error si no existeix.

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as fitxer:
        print(fitxer.read())
else:
    print("Error: El fitxer 'dades.txt' no existeix.")
