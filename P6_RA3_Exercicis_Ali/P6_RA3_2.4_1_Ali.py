# Autor: Ali
# Data: 09/05/2025
# Descripció: Simula operacions amb un compte bancari

from P6_RA3_1.6_1_Ali import CompteBancari

compte = CompteBancari()
compte.ingressar(100)
compte.retirar(30)
compte.retirar(80)
print("Saldo final:", compte.veure_saldo())
