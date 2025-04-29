try:
    num = int(input("Introdueix un número enter: "))
    for i in range(num + 1):
        print(i)
except ValueError:
    print("Error: No has introduït un número enter.")
