""" Recorrido en amplitud (BFS): Implementa un recorrido BFS para un grafo simple con 5 nodos. """

# Representación del grafo como un diccionario de listas de adyacencia
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Implementar BFS
nodo_inicial = 0  # Nodo inicial para empezar el BFS
cola = [nodo_inicial]  # Lista para gestionar los nodos por explorar
visitados = []  # Lista para almacenar los nodos visitados

while cola:
    # Toma el primer nodo de la cola
    nodo = cola.pop(0)
    if nodo not in visitados:
        # Marca el nodo como visitado
        visitados.append(nodo)
        # Agrega los nodos adyacentes a la cola para explorarlos
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                cola.append(vecino)

print("Recorrido BFS:", visitados)
