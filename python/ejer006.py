# ingrese un numero y diga si es par o impar
"""
1. pedir al usuario ingrear un numero
2. hacer el calculo para ver si es par o impar (variable % 2 == 0 es par)
3. mostrar mensaje
"""

num1 = int(input("Ingrese un numero: "))

if num1 %2 == 0 :
    print("numero es par")
else :
    print("numero es impar")