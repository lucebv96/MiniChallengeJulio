""" Pilas y colas: Implementa las operaciones básicas de una pila y/o una cola para 5 elementos. """

# Implementación de una Pila
pila = []

# Operación para añadir un elemento a la pila
def apilar(pila, elemento):
    pila.append(elemento)

# Operación para quitar el último elemento de la pila
def desapilar(pila):
    if len(pila) > 0:
        return pila.pop()
    else:
        return None

# Ejemplo de uso
apilar(pila, 1)
apilar(pila, 2)
apilar(pila, 3)
apilar(pila, 4)
apilar(pila, 5)

print("Pila después de apilar 5 elementos:", pila)

print("Elemento desapilado:", desapilar(pila))
print("Elemento desapilado:", desapilar(pila))
print("Pila después de desapilar 2 elementos:", pila)
