""" Eliminar duplicados: Implementa una función que elimina los 
elementos duplicados de una lista de 10 enteros. """

# Función para eliminar duplicados de una lista
def eliminar_duplicados(lista):
    # Lista para almacenar los elementos sin duplicados
    lista_sin_duplicados = []
    
    # Iteramos sobre cada elemento en la lista original
    for elemento in lista:
        # Si el elemento no está en la lista de elementos únicos
        if elemento not in lista_sin_duplicados:
            # Añadimos el elemento a la lista sin duplicados
            lista_sin_duplicados.append(elemento)
        else:
            # El elemento ya está en la lista sin duplicados,pasamos al sgte
            pass
    
    return lista_sin_duplicados

# Ejemplo 
lista = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
resultado = eliminar_duplicados(lista)
print("Lista sin duplicados:", resultado)
