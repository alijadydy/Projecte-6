parells = []
senars = []

for i in range(10):
    num = int(input(f"Introdueix el número {i+1}: "))
    if num % 2 == 0:
        parells.append(num)
    else:
        senars.append(num)

print("Parells:", parells)
print("Senars:", senars)
