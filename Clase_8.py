#buble while

#Ejercicio 9 - Suma acumulativa
# Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa de esos números.
# El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime la suma total.

print("Los números que introduzcas se sumaran. Para finalizar introduce 0")
numero = int(input())
resultado = 0

while numero != 0:
    resultado += numero #resultado = resultado + numero
    numero = int(input())
print(f"El resultado es {resultado}")

# Ejercicio 10 - Akinator numérico¶
# Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número.
# El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido.
# El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.

import random

random_num = random.randint(1,100)
user_num = int(input("Adivina el número que he elegido del 1 al 100: "))

while random_num != user_num:
    if user_num > random_num:
        print("Lo siento, tu sucio número es demasiado alto")
    else:
        print("Lo siento, tu sucio número es demasiado pequeño")

    user_num = int(input("Vuelve a intentarlo, adivina el número que he elegido del 1 al 100: "))

print("Enhorabuena, ¿eres adivino? ")

# Ejercicio 11 - Media de notas
# Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar.
# Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y calcule la media de esas notas.
# El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1. Al final, imprime la media. Ejemplo:
# Introduce el número de evaluaciones: 3
# Notas de la evaluación 1: 6 8 4 3.5 9 -1
# Notas de la evaluación 2: 7 5 8.5 -1
# Notas de la evaluación 3: 9 10 8.5 -1
# La media de la evaluación 1 es: 6.5
# La media de la evaluación 2 es: 7.5
# La media de la evaluación 3 es: 9.0

evaluaciones = int(input("Introduce el número de evaluaciones: "))

for i in range(evaluaciones):
    nota = float(input("Introduce la siguiente nota: "))
    num_notas = 0
    suma_notas = 0
    while nota != -1:
        num_notas += 1
        suma_notas += nota
        nota = float(input("Introduce la siguiente nota: "))
    print(f"Nota media evaluación {i+1}: {suma_notas/num_notas}")

# Ejercicio 12 - Mayor y menor
# Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y cuál es el menor.
# El programa debe seguir pidiendo números hasta que el usuario ingrese un 0. Al final, imprime el mayor y el menor.

mayor = -float('inf')
menor = float('inf')
numero = int(input("Introduce un valor (0 para terminar): "))

while numero != 0:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero

    numero = int(input("Introduce un valor (0 para terminar): "))

print(f"Mayor: {mayor}, Menor: {menor}")

# Ejercicio 13 - Número de cifras
# Escribe un programa que pida al usuario una serie de números enteros positivos hasta la introducción de un valor -1 para cada número debe contar cuántas cifras tiene.
# El programa debe imprimir la longitud de cada número.
# No podéis usar la función len() para contar las cifras ni convertir el número a cadena.

numero = int(input("Introduce un número (-1 para acabar): "))

while numero != -1:
    cifras = 1
    copia_num = numero
    while numero >= 10:
        cifras += 1
        numero //= 10
    print(f"El número de dígitos de {copia_num} es {cifras}")

# Ejercicio 15 - Banca online
# Escribe un programa que simule una cuenta bancaria.
# El programa debe permitir al usuario realizar las siguientes operaciones:

# 1Ingresar dinero
# 2Retirar dinero
# 3Consultar saldo
# 4Salir
# Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.

saldo = 0
opcion = -1

while opcion != 4
    print("Escoge una opción: ")
    print("1. Ingresar dinero ")
    print("2. Retirar dinero ")
    print("3. Consultar saldo ")
    print("4. Salir ")

    opcion =int(input())

    if opcion == 1:
        saldo += (int(input("¿Qué cantidad deseas ingresar?: "))
    elif opcion == 2:
        saldo -= (int(input("¿Qué cantidad deseas retirar?: "))
    elif opcion == 3:
        print(f"Tu saldo es {saldo}")
    else:
        print("Escoge una opción de la 1 a la 4")
