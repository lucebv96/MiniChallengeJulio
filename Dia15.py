""" Auto y Motor: Implementa una clase Autoque contiene una instancia de una
 clase Motor con un método para describir el motor. """

class Motor:
    def __init__(self, tipo, potencia):
        # Inicializamos los atributos tipo y potencia
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        # Método para describir el tipo y la potencia del motor
        print(f"Motor tipo: {self.tipo}, Potencia: {self.potencia} HP")

class Auto:
    def __init__(self, marca, modelo, motor):
        # Inicializamos los atributos marca, modelo y motor
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        # Método para describir el auto
        print(f"Auto marca: {self.marca}, modelo: {self.modelo}")
        # Llamamos al método describir del motor para mostrar su descripción
        self.motor.describir()

# Ejemplo de uso con diferentes tipos de motores
# Motor eléctrico
motor_electrico = Motor("Eléctrico", 150)
auto_electrico = Auto("Tesla", "Model S", motor_electrico)
auto_electrico.describir_auto()
print()

# Motor híbrido
motor_hibrido = Motor("Híbrido", 200)
auto_hibrido = Auto("Toyota", "Prius", motor_hibrido)
auto_hibrido.describir_auto()
