# Autor: Ali
# Data: 09/05/2025
# Descripció: Mostra els estudiants que han aprovat

from P6_RA3_1.5_1_Ali import Estudiant

estudiants = [
    Estudiant("Anna", 7),
    Estudiant("Joan", 4),
    Estudiant("Pau", 9)
]

for e in estudiants:
    if e.ha_aprovat():
        print(f"{e.nom} ha aprovat.")
