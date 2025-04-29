import random
num_secret = random.randint(1, 100)
endevinat = False

while not endevinat:
    intent = int(input("Endevina el número (entre 1 i 100): "))
    if intent < num_secret:
        print("Massa baix.")
    elif intent > num_secret:
        print("Massa alt.")
    else:
        print("Correcte! Has endevinat el número.")
        endevinat = True