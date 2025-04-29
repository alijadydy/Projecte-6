try:
    num = int(input("Introdueix un número enter: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
except ValueError:
    print("Error: No has introduït un número enter.")
