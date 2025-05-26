"""
En este se encuentra el main, donde se ejecuta el programa  
Hecho por Allysson Palma, Nicole Ramos y Andres Porras 
26/05/2025
Ejercicio: Separación de elementos usando Pila y Cola

Objetivo:
Dado una cola con elementos y una pila vacía, desarrollar un programa que procese la cola de forma que:
	Los elementos que se encuentran en posiciones pares (0, 2, 4, ...) permanezcan en la cola.
	Los elementos que se encuentran en posiciones impares (1, 3, 5, ...) se transfieran a la pila.

Consideraciones:
	La posición de los elementos se cuenta a partir de cero (la primera posición es la 0, la segunda es la 1, etc.).
	La operación debe realizarse recorriendo la cola una sola vez.
	Al finalizar, la pila contendrá los elementos impares en orden LIFO y la cola solo los elementos pares en su orden original.
Ejemplo:
Cola original: [A, B, C, D, E]
Resultado:
	Cola: [A, C, E]
	Pila: ['D', 'B'] (último en entrar, primero en salir)
	
			
-	Actividad en grupo.
-	Implementar módulos y conceptos básicos de POO.

"""
from modulocoalypila import Cola, Pila  # Importamos la clase Cola desde el módulo Modulo
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)  # Inicializamos colorama para colores en terminal

def main():
    cola = Cola()  # Creamos una instancia de Cola

    print(Fore.BLUE + Style.BRIGHT + "Ingrese números Para terminar, escriba 'fin'.")
    while True:
        entrada = input(Fore.LIGHTBLUE_EX+ Style.BRIGHT + "Número:" + Style.RESET_ALL)
        if entrada.lower() == "fin":
            break
        if not entrada.isdigit():
            print (Fore.RED + Style.BRIGHT + "Por favor, ingrese un número válido o 'fin' para salir.")
            continue
        numero = int(entrada)
        cola.encolar(numero)

    print(Fore.GREEN + Style.BRIGHT + "\nContenido de la cola (pares):")
    cola.recorrer()

    # Mostrar contenido de la pila de impares
    print(Fore.WHITE + Style.BRIGHT + "\nContenido de la pila (impares):")
    cola.pila_impares.recorrer()

if __name__ == "__main__":
    main()
# Ejecutamos la función main en este archivo  el  cual es el principal