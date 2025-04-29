frase = input("Introdueix una frase: ").lower()
vocals = "aeiou"
comptador = sum(1 for lletra in frase if lletra in vocals)
print("Nombre de vocals:", comptador)