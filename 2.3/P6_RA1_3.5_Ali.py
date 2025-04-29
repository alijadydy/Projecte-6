def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input("Introdueix un número enter positiu: "))
    if num >= 2:
        for i in range(2, num + 1):
            if es_primer(i):
                print(i)
    else:
        print("Error: Has d'introduir un número major o igual a 2.")
except ValueError:
    print("Error: No has introduït un número enter.")
