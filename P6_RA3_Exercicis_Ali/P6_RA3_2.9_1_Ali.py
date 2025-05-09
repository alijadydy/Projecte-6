# Autor: Ali
# Data: 09/05/2025
# Descripció: Mostra cercles amb àrea > 50

from P6_RA3_1.7_1_Ali import Cercle

cercles = [Cercle(3), Cercle(5), Cercle(10)]

for c in cercles:
    if c.area() > 50:
        print("Àrea:", c.area())
