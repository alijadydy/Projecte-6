# Autor: Ali
# Data: 07/05/2025
# Descripció: Afegeix una línia nova a un fitxer existent (sortida.txt) sense esborrar el contingut.

with open("sortida.txt", "a") as fitxer:
    fitxer.write("Aquesta és una línia afegida.\n")
