from datetime import datetime

any_naixement = int(input("Introdueix l'any de naixement: "))
any_actual = datetime.now().year
edat = any_actual - any_naixement

print(f"Tens {edat} anys.")
if edat >= 18:
    print("Ets major d'edat.")
else:
    print("No ets major d'edat.")