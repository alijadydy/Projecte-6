# Autor: Ali
# Data: 07/05/2025
# Descripció: Gestiona l'error si no es pot escriure en un fitxer per problemes de permisos.

try:
    with open("resultats.txt", "w") as fitxer:
        fitxer.write("Escrivint resultats...\n")
except PermissionError:
    print("No tens permisos per escriure en aquest fitxer.")
