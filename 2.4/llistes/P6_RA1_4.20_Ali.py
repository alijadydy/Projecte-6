paraules = input("Introdueix paraules separades per espai: ").split()
comencen_vocal = [p for p in paraules if p[0].lower() in "aeiou"]
print("Paraules que comencen per vocal:", comencen_vocal)
