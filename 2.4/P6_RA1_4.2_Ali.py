frase = input("Introdueix una frase: ")
vocales = "aeiouAEIOU"
comptador = sum(1 for lletra in frase if lletra in vocales)
print("Nombre de vocals:", comptador)
