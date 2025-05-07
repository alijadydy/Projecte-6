# Autor: Ali
# Data: 07/05/2025
# Descripció: Llegeix un fitxer i assegura el tancament encara que hi hagi un error.

fitxer = None
try:
    fitxer = open("sortida.txt", "r")
    for linia in fitxer:
        print(linia.strip())
        if "error" in linia:
            raise ValueError("Error simulat durant la lectura")
except Exception as e:
    print(f"S'ha produït un error: {e}")
finally:
    if fitxer:
        fitxer.close()
        print("Fitxer tancat correctament.")
