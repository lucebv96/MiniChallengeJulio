""" Árbol binario de búsqueda (BST):
 Implemente solo la inserción en un árbol binario de búsqueda para 5 elementos. """

# Definimos el nodo del árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Clase del Árbol Binario de Búsqueda
class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    # Método para insertar un nuevo valor
    def insertar(self, valor):
        # Creamos un nuevo nodo
        nuevo_nodo = Nodo(valor)
        
        # Si el árbol está vacío, el nuevo nodo es la raíz
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            #Se Llama a la función recursiva para encontrar la posición correcta
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    # Función recursiva para insertar un nodo
    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        # Si el valor del nuevo nodo es menor, se va a la izquierda
        if nuevo_nodo.valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = nuevo_nodo
            else:
                # Continúa buscando en el subárbol izquierdo
                self._insertar_recursivo(nodo_actual.izquierda, nuevo_nodo)
        # Si el valor del nuevo nodo es mayor, va a la derecha
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = nuevo_nodo
            else:
                # Continúa buscando en el subárbol derecho
                self._insertar_recursivo(nodo_actual.derecha, nuevo_nodo)

# Ejemplo 
bst = ArbolBinarioBusqueda()
elementos = [10, 5, 15, 3, 7]

for elemento in elementos:
    bst.insertar(elemento)

# función que imprime los valores en orden ascendente
def imprimir_en_orden(nodo):
    if nodo:
        imprimir_en_orden(nodo.izquierda)
        print(nodo.valor, end=' ')
        imprimir_en_orden(nodo.derecha)

print("Elementos en el BST en orden:")
imprimir_en_orden(bst.raiz)
