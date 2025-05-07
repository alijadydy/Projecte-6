# Autor: Ali
# Data: 07/05/2025
# Descripció: Llegeix un fitxer i mostra quantes línies té.

with open("sortida.txt", "r") as fitxer:
    linies = fitxer.readlines()
    print(f"El fitxer té {len(linies)} línies.")
