""" Piloto de eventos (Priority Queue): Implementa una cola de prioridad 
utilizando una lista para insertar y eliminar 5 elementos."""

class ColaDePrioridad:
    def __init__(self):
        # Inicializamos la lista vacía para la cola de prioridad
        self.cola = []

    def insertar(self, elemento, prioridad):
        # Añadimos el elemento con su prioridad a la lista
        self.cola.append((elemento, prioridad))
        # Ordenamos la lista en orden ascendente por prioridad
        self.cola.sort(key=lambda x: x[1])

    def eliminar(self):
        # Verificamos si la cola no está vacía
        if len(self.cola) > 0:
            # Eliminamos y devolvemos el primer elemento de la lista (el de mayor prioridad)
            return self.cola.pop(0)
        else:
            # Si la cola está vacía, devolvemos None
            return None

    def esta_vacia(self):
        # Devolvemos True si la cola está vacía, de lo contrario False
        return len(self.cola) == 0

    def ver_cola(self):
        # Devolvemos la lista de elementos en la cola
        return self.cola

# Ejemplo de uso
cola_prioridad = ColaDePrioridad()
elementos_con_prioridad = [('Tarea1', 2), ('Tarea2', 1), ('Tarea3', 5), ('Tarea4', 3), ('Tarea5', 4)]

# Insertar elementos en la cola con sus prioridades
for elemento, prioridad in elementos_con_prioridad:
    cola_prioridad.insertar(elemento, prioridad)

# Mostrar la cola de prioridad después de insertar elementos
print("Cola de prioridad después de insertar elementos:")
print(cola_prioridad.ver_cola())

# Eliminar elementos de la cola según su prioridad
print("\nEliminando elementos según su prioridad:")
while not cola_prioridad.esta_vacia():
    elemento = cola_prioridad.eliminar()
    print(f"Elemento eliminado: {elemento}")
