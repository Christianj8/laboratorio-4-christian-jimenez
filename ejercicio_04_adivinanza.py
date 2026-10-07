"""
EJERCICIO 04: Adivina el número

1. Selecciona un número entero y almacenalo en una variable. 
2. Pide al usuario que lo adivine dentro de un bucle while. 
3. En cada intento, el programa debe indicar si el número buscado es mayor o menor que el ingresado, hasta que lo adivine.
"""

numero_secreto = 7 # numero secreto a adivinar
while True:
    try:
        intento = int(input("adivina el numero secreto (entre 1 y 10): "))
        if intento < 1 or intento > 10:
            print("por favor ingrese un numero entre 1 y 10")
            continue
        if intento < numero_secreto:
            print("el numero secreto es mayor que tu intento.")
        elif intento > numero_secreto:
            print("el numero secreto es menor que tu intento.")
        else:
            print("¡felicidades! has adivinado el numero secreto.")
            break
    except ValueError:
        print("por favor ingrese un numero valido.")