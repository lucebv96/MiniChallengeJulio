""" Recursión Factorial: Implementa una función recursiva para calcular 
el factorial de un número pequeño (por ejemplo, 5). """

# Función recursiva para calcular el factorial de un número
def factorial(n):
    # Caso base: 
    if n == 0 or n == 1:
        return 1
    else:
        # Caso recursivo: n * factorial(n - 1)
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

