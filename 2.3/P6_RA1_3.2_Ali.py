try:
    num = int(input("Introdueix un número enter positiu: "))
    if num > 0:
        print("La suma és:", sum(range(1, num + 1)))
    else:
        print("Error: Has d'introduir un número positiu.")
except ValueError:
    print("Error: No has introduït un número enter.")
