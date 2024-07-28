"""Escribe una función que ordene una lista de 5 enteros utilizando cualquier método de 
ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección)."""

def ordenamiento_burbuja(lista):
    n = len(lista)
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n-i-1):
            # Comparamos el elemento actual con el siguiente
            if lista[j] > lista[j+1]:
                # Intercambiamos si el elemento actual es mayor que el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j]

# Ejemplo 
lista_enteros = [64, 34, 25, 12, 22]

# Llamamos a la función para ordenar la lista
ordenamiento_burbuja(lista_enteros)

# Imprimimos la lista ordenada
print("Lista ordenada:", lista_enteros)
