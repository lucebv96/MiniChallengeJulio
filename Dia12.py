""" Figura y Círculo: Crea una clase base Figuracon un método 
imprimir una clase derivada Círculoque extiende Figura sobreescribe el método imprimir. """

class Figura:
    def imprimir(self):
        print("Esto es una figura.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Esto es un círculo con radio: {self.radio}")

# Ejemplo 
figura = Figura()
figura.imprimir()  # Imprimimos
circulo = Circulo(5)
circulo.imprimir()  # Imprimimos
