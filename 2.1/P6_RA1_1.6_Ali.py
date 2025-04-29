lletra = input("Introdueix una lletra: ").lower()
vocals = "aeiou"

if lletra.isalpha() and len(lletra) == 1:
    if lletra in vocals:
        print("És una vocal.")
    else:
        print("És una consonant.")
else:
    print("Introdueix només una lletra vàlida.")