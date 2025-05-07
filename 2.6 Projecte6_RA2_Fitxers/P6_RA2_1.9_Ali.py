# Autor: Ali
# Data: 07/05/2025
# Descripció: Obre un fitxer. Si no existeix, el crea automàticament i escriu una línia per defecte.

try:
    with open("nou_fitxer.txt", "r") as fitxer:
        print(fitxer.read())
except FileNotFoundError:
    with open("nou_fitxer.txt", "w") as fitxer:
        fitxer.write("Fitxer creat automàticament.\n")
        print("Fitxer creat i línia afegida.")
