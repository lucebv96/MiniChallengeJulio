""" Cuenta bancaria: Implementa una clase CuentaBancaria con métodos para depositar y consultar el saldo. """

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        # Inicializamos el saldo con el valor proporcionado
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        # Aumentamos el saldo con la cantidad depositada
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} unidades. Saldo actual: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def consultar_saldo(self):
        # Imprimimos el saldo actual de la cuenta
        print(f"El saldo actual es: {self.saldo}")

# Ejemplo 
# Creamos una cuenta bancaria con un saldo inicial de 100
cuenta = CuentaBancaria(100)
cuenta.consultar_saldo()  # Imprimimos

# Depositamos 50 unidades en la cuenta
cuenta.depositar(50)
cuenta.consultar_saldo()  #  Imprimimos

# Intentamos depositar una cantidad negativa
cuenta.depositar(-30)  # Imprimimos
