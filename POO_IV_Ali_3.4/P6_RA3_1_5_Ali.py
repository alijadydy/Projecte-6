# Autor: Ali
# Data: {data}
# Exercici 5 - Herència: Biblioteca

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"Títol: {self.titol}, Autor: {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"Llibre en paper - Títol: {self.titol}, Autor: {self.autor}, Pàgines: {self.n_pagines}")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"Llibre digital - Títol: {self.titol}, Autor: {self.autor}, Format: {self.format}")

paper = LlibrePaper("El llibre", "Autor X", 300)
digital = LlibreDigital("El llibre digital", "Autor Y", "PDF")

paper.mostrar_info()
digital.mostrar_info()
