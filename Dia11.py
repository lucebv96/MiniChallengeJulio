""" Clase de Punto 2D: Crea una clase Punto2Dcon atributos x& y, y un método para imprimir sus coordenadas. """

class Punto2D:
    def __init__(self, x, y):
        # Inicializamos los atributos 
        self.x = x
        self.y = y

    def imprimir_coordenadas(self):
        # Imprimimos las coordenadas del punto
        print(f"Coordenadas del punto: ({self.x}, {self.y})")

# Ejemplo 
# Creamos una instancia de Punto2D con coordenadas (3, 4)
punto = Punto2D(3, 4)
# Llamamos al método para imprimir las coordenadas del punto
punto.imprimir_coordenadas()
