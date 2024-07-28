"""Búsqueda Binaria: Determina si un número está en una lista ordenada de 10 elementos."""

def busqueda_binaria(lista_ordenada, objetivo):
    # Variables para labúsqueda
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    # Este Bucle  se ejecuta mientras el incio y el fin no se crucen
    while izquierda <= derecha:
        # Se alcula el punto medio de la lista
        medio = (izquierda + derecha) // 2
        # Obtiene el valor del medio
        valor_medio = lista_ordenada[medio]

        # Verifica si  es el objetivo
        if valor_medio == objetivo:
            return True
        # Si el objetivo es mayor:
        elif valor_medio < objetivo:
            izquierda = medio + 1
        # Si el objetivo es menorÑ
        else:
            derecha = medio - 1

    # Si no se encuentra el objetivo retorna False
    return False

# Ejemplo:
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
objetivo = int(input("Ingresa un número para buscar: "))

# Llamamos a la función y mostrmos el resultado
resultado = busqueda_binaria(lista_ordenada, objetivo)
print(f"El número {objetivo} está en la lista? {resultado}")
