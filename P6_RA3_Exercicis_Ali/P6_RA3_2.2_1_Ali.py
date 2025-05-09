# Autor: Ali
# Data: 09/05/2025
# Descripció: Crea 3 rectangles i mostra l’àrea de cadascun

from P6_RA3_1.2_1_Ali import Rectangle

rectangles = [
    Rectangle(3, 4),
    Rectangle(5, 6),
    Rectangle(2, 8)
]

for r in rectangles:
    print("Àrea:", r.area())
