# Autor: Ali
# Data: 09/05/2025
# Descripció: Imprimeix persones amb més de 30 anys

from P6_RA3_1.3_1_Ali import Persona

persones = [
    Persona("Maria", 25),
    Persona("Jordi", 35),
    Persona("Carla", 40)
]

for p in persones:
    if p.edat > 30:
        p.presentar_se()
