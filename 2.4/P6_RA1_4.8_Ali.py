def eliminar_espais(cadena):
    return cadena.replace(" ", "")

text = input("Introdueix una cadena: ")
print("Sense espais:", eliminar_espais(text))
