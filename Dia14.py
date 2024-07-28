""" Polimorfismo: Crea una clase base Animalcon un método 
hacer Sonido y una clase derivada Perroque sobrescribe este método. """

class Animal:
    def hacerSonido(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hacerSonido(self):
        print("El perro ladra: ¡Guau, guau!")

# Ejemplo 
# Instancia de la clase base Animal
animal = Animal()
animal.hacerSonido()  # Imprime 

# Instancia de la clase derivada Perro
perro = Perro()
perro.hacerSonido()  # Imprime 
