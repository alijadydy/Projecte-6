# Autor: Ali
# Data: 09/05/2025
# Descripció: Aplica un descompte del 10% a una llista de productes

from P6_RA3_1.4_1_Ali import Producte

def aplicar_descompte_a_tots(productes):
    for p in productes:
        p.aplicar_descompte(10)

llista = [
    Producte("Producte1", 100),
    Producte("Producte2", 50)
]

aplicar_descompte_a_tots(llista)

for p in llista:
    print(f"{p.nom}: {p.preu}")
