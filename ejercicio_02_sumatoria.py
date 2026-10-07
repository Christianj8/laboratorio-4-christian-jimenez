"""
EJERCICIO 02: Sumatoria

1. Pide números enteros al usuario constantemente usando un bucle while. 
2. Suma los valores ingresados.
3. Detén el bucle únicamente cuando el usuario ingrese el número 0. 
4. Al final, muestra la suma total.
"""


suma = 0
while True:
    try:
        numero = int(input("ingrese un numero entero (0 para salir): "))
        if numero == 0:
            break
        suma += numero
    except ValueError:
        print("por favor ingrese un numero valido")

print(f"la suma total de los numeros ingresados es: {suma}")
