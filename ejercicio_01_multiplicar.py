"""
EJERCICIO 01: Tabla de multiplicar

1. Pide al usuario ingresar un número
2. Garantice la entrada correcta
3. Imprime la tabla de multiplicar del 1 al 10 del número ingresado. Utilice un bucle for
"""

try:
    numero = int(input("ingrese un numero para mostrar su tabla de multiplicar: "))
    print(f"tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
except ValueError:
    print("por favor ingrese un numero valido")

    
