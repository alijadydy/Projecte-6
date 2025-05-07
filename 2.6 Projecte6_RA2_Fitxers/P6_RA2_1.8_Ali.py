# Autor: Ali
# Data: 07/05/2025
# Descripció: Llegeix línies d’un fitxer amb enters. Si hi ha errors de format, es capturen.

with open("nombres.txt", "r") as fitxer:
    for linia in fitxer:
        try:
            numero = int(linia.strip())
            print(f"Número: {numero}")
        except ValueError:
            print(f"Format incorrecte: {linia.strip()}")
