# Autor: Ali
# Data: 25/04/2025
# Descripció: 

num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
operacio = input("Introdueix l'operació (+, -, *, /): ")

if operacio == '+':
  resultat = num1 + num2
  print(f"El resultat de {num1} + {num2} és: {resultat}")
elif operacio == '-':
  resultat = num1 - num2
  print(f"El resultat de {num1} - {num2} és: {resultat}")
elif operacio == '*':
  resultat = num1 * num2
  print(f"El resultat de {num1} * {num2} és: {resultat}")
elif operacio == '/':
  if num2 == 0:
    print("Error! No es pot dividir per zero.")
  else:
    resultat = num1 / num2
    print(f"El resultat de {num1} / {num2} és: {resultat}")
else:
  print("Operació no vàlida. Si us plau, introdueix +, -, *, o /.")