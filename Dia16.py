""" Formas geométricas: Defina una clase base FormaGeometricacon métodos calcular_areay calcular_perimetro.
 Crea clases derivadas Rectanguloy Circuloque sobrescriben estos métodos. """

class FormaGeometrica:
    def area(self):
        # Método base para calcular el área (se sobrescribirá en las subclases)
        pass

    def perimetro(self):
        # Método base para calcular el perímetro (se sobrescribirá en las subclases)
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, largo, ancho):
        # Inicializar las dimensiones del rectángulo
        self.largo = largo
        self.ancho = ancho

    def area(self):
        # Calcular el área del rectángulo
        return self.largo * self.ancho

    def perimetro(self):
        # Calcular el perímetro del rectángulo
        return 2 * (self.largo + self.ancho)

class Circulo(FormaGeometrica):
    PI = 3.1416  # Aproximación de π

    def __init__(self, radio):
        # Inicializar el radio del círculo
        self.radio = radio

    def area(self):
        # Calcular el área del círculo
        return Circulo.PI * (self.radio ** 2)

    def perimetro(self):
        # Calcular el perímetro (circunferencia) del círculo
        return 2 * Circulo.PI * self.radio

# Ejemplo de uso
rectangulo = Rectangulo(5, 3)
circulo = Circulo(4)

# Imprimir los resultados usando f-strings para formato
print(f"Área del rectángulo con largo {rectangulo.largo} y ancho {rectangulo.ancho}: {rectangulo.area()}")
print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")

print(f"Área del círculo con radio {circulo.radio}: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")
