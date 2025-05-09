# Autor: Ali
# Data: 09/05/2025
# Exercici 1 - Baix acoplament amb injecció de dependències

class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class ImpressoraPaper:
    def imprimir(self, contingut):
        print(f"Imprimint en paper: {contingut}")

class Factura:
    def __init__(self, client, import_total, impressora):
        self.client = client
        self.import_total = import_total
        self.impressora = impressora  # Injecció de dependència

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {self.import_total} €"
        self.impressora.imprimir(contingut)