""" Recorrido en profundidad (DFS): Implementa un recorrido DFS para un gráfico simple con 5 nodos. """


grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

# Implementamos DFS
nodo_inicial = 0  # Nodo inicial para empezar 
pila_exploracion = [nodo_inicial]  # Pila para gestionar los nodos por explorar
nodos_visitados = []  # Lista para almacenar los nodos visitados

while pila_exploracion:
    # Tomamos el último nodo agregado a la pila
    nodo_actual = pila_exploracion.pop()
    if nodo_actual not in nodos_visitados:
        # Marcamos el nodo como visitado
        nodos_visitados.append(nodo_actual)
        # Agregamos los nodos adyacentes a la pila para explorarlos
        for vecino in grafo[nodo_actual]:
            if vecino not in nodos_visitados:
                pila_exploracion.append(vecino)

print("Recorrido DFS:", nodos_visitados)
