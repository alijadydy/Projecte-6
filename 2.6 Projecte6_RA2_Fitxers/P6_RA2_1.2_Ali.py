# Autor: Ali
# Data: 07/05/2025
# Descripció: Escriu tres línies a un fitxer nou anomenat sortida.txt, esborrant-ne el contingut anterior.

with open("sortida.txt", "w") as fitxer:
    fitxer.write("Primera línia\n")
    fitxer.write("Segona línia\n")
    fitxer.write("Tercera línia\n")
