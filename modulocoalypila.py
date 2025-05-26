"""
Módulo que define una cola para almacenar números pares y una pila para números impares.
siguiendo  el orden en colo FIFO (Fist In First Out ) para la cola y LIFO (Last In First Out) para la pila.
"""
# Clase Nodo para representar cada elemento en la pila o cola
class Nodo:
    def __init__(self, dato):
        self.dato = dato      # Dato almacenado
        self.siguiente = None # Referencia al siguiente nodo

# Clase Pila para almacenar los números impares (LIFO)
class Pila:
    def __init__(self):
        self.tope = None  # Inicio vacío, sin nodos

    def apilar(self, dato):
        # Crear nuevo nodo y ponerlo en el tope
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo
        print(f"{dato} agregado a la pila.")

    def recorrer(self):
        # Imprime los elementos de la pila desde el tope hacia abajo
        actual = self.tope
        print("Pila (impares): ", end="")
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

# Clase Cola para almacenar números pares (FIFO)
# Además, contiene una pila interna para guardar los impares
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.pila_impares = Pila()  # Pila para guardar impares

    def encolar(self, dato):
        if dato % 2 == 0:
            # Si es par, lo agregamos a la cola
            nuevo_nodo = Nodo(dato)
            if self.final is None:
                # Cola vacía: frente y final apuntan al nuevo nodo
                self.frente = nuevo_nodo
                self.final = nuevo_nodo
            else:
                # Encolamos al final
                self.final.siguiente = nuevo_nodo
                self.final = nuevo_nodo
            print(f"{dato} es par agregado a la cola.")
        else:
            # Si es impar, lo agregamos a la pila de impares
            self.pila_impares.apilar(dato)
            print(f"{dato} es impar enviado a la pila.")

    def recorrer(self):
        # Imprime los elementos de la cola desde el frente hacia el final
        actual = self.frente
        print("Cola (pares): ", end="")
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()
