# Autor: Ali
# Data: 07/05/2025
# Descripció: Obre un fitxer en mode lectura i escriptura, mostra el contingut i afegeix una línia al final.

with open("sortida.txt", "r+") as fitxer:
    contingut = fitxer.read()
    print(contingut)
    fitxer.write("\nAquesta línia ha estat afegida en mode r+.")
