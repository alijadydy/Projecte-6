try:
    num = int(input("Introdueix un número enter positiu: "))
    if num >= 0:
        for i in range(0, num + 1, 2):
            print(i)
    else:
        print("Error: Has d'introduir un número positiu.")
except ValueError:
    print("Error: No has introduït un número enter.")
