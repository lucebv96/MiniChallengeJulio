"""  Camino más corto: Encuentra el camino más corto entre dos nodos en un grafo simple con 5 nodos y 6 aristas. """

# Representación del grafo como un diccionario de listas 
grafo = {
    0: [1, 2],
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: [0]
}

def camino_mas_corto(grafo, inicio, objetivo):
    # Si el nodo de inicio es el mismo que el de objetivo, devolver directamente
    if inicio == objetivo:
        return [inicio]

    # Inicialización
    cola = [[inicio]]  # Cola para almacenar caminos a explorar
    visitados = set()  # Conjunto para registrar nodos visitados

    while cola:
        # Toma el primer camino de la cola
        camino = cola.pop(0)
        nodo = camino[-1]

        if nodo not in visitados:
            # Marca el nodo como visitado
            visitados.add(nodo)

            # Explora los vecinos del nodo actual
            for vecino in grafo[nodo]:
                # Construye un nuevo camino extendiendo el camino actual
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)

                # Si se encuentra el nodo objetivo, devolver el camino
                if vecino == objetivo:
                    return nuevo_camino

    # Si no se encuentra un camino, devolver None
    return None

# Ejemplo de uso
inicio = 0
objetivo = 3
resultado = camino_mas_corto(grafo, inicio, objetivo)
print("El camino más corto de", inicio, "a", objetivo, "es:", resultado)
