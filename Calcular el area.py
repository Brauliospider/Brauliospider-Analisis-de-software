# este import math hace que podamos usar funciones matemáticas como pi, y que sea mas exacto el cálculo
import math

# Calcular el área de diferentes figuras geométricas
# Este programa permite calcular el área de un cuadrado, un círculo y un triángulo
# Cada figura tiene su propia función para calcular el área
# Las funciones verifican que los valores ingresados sean positivos antes de realizar el cálculo
def area_cuadrado(lado):
    if lado <= 0:
        print("Error: el lado debe ser un número positivo.")
        return None
    return lado * lado

def area_circulo(radio):
    if radio <= 0:
        print("Error: el radio debe ser un número positivo.")
        return None
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    if base <= 0 or altura <= 0:
        print("Error: la base y la altura deben ser números positivos.")
        return None
    return (base * altura) / 2

# Menú interactivo para seleccionar la figura y calcular su área
# El menú permite al usuario elegir qué figura calcular y solicita los datos necesarios
def menu():
    print("CÁLCULO DE ÁREAS")
    print("1. Área de un Cuadrado")
    print("2. Área de un Círculo")
    print("3. Área de un Triángulo")
    print("4. Salir")

    # Bucle para mostrar el menú y procesar la opción seleccionada
    while True:
        try:
            # Solicita al usuario que seleccione una opción del menú
            opcion = int(input("\nSelecciona una opción (1-4): "))

            # Verifica la opción seleccionada y llama a la función correspondiente
            if opcion == 1:
                lado = float(input("Ingresa el lado del cuadrado: "))
                resultado = area_cuadrado(lado)
                # Si el resultado no es None, significa que el cálculo fue exitoso
                # y se imprime el área del cuadrado
                if resultado is not None:
                    print("Área del cuadrado: ", resultado)

            # verifica si la opción es 2, 3 o 4
            elif opcion == 2:
                radio = float(input("Ingresa el radio del círculo: "))
                resultado = area_circulo(radio)
                # Si el resultado no es None, significa que el cálculo fue exitoso
                # y se imprime el área del círculo
                if resultado is not None:
                    print("Área del círculo: ", resultado)

            # verifica si la opción es 3, 4 o una opción no válida
            elif opcion == 3:
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                resultado = area_triangulo(base, altura)
                # Si el resultado no es None, significa que el cálculo fue exitoso
                # y se imprime el área del triángulo
                if resultado is not None:
                    print("Área del triángulo: ", resultado)

            # verifica si la opción es 4, que es salir del programa
            elif opcion == 4:
                print("¡Hasta luego!")
                # Sale del bucle y termina el programa
                break
            # Si la opción no es 1, 2, 3 o 4, muestra un mensaje de error
            else:
                print("Opción no válida. Elige entre 1 y 4.")
        
        # Maneja errores de entrada, como si el usuario ingresa un valor no numérico
        except ValueError:
            print("Entrada inválida. Por favor ingresa números correctamente.")

# Punto de entrada del programa
# Llama a la función menu para iniciar el programa
menu()