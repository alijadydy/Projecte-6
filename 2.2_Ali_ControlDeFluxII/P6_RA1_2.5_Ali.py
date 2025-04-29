num = int(input("Introdueix un número enter positiu: "))
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("No és un nombre primer.")
            break
    else:
        print("És un nombre primer.")
else:
    print("No és un nombre primer.")