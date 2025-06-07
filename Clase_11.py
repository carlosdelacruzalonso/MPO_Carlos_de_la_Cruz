# Una función es un bloque de código con nombre que se puede ejecutar cuando se necesite.
# Sirve para resolver una tarea específica y puede recibir datos (llamados parámetros) y devolver un resultado (valor de retorno).
import math


# Piensa en una función como una máquina: Le das ingredientes (parámetros), hace un trabajo (instrucciones), y puede darte un resultado (valor de retorno).

# Ventajas de usar funciones¶
# Reutilización de código: Escribes una vez, usas muchas.
# Modularidad: Puedes dividir un programa en partes más pequeñas, claras y fáciles de entender.
# Facilita la prueba de errores: Puedes probar una función de forma aislada.
# Mejora la legibilidad: Los programas con funciones bien nombradas se entienden mejor.
# ¿Cómo se define una función en Python?¶
# Sintaxis básica¶

# def nombre_funcion(parámetros):
#     """Descripción de lo que hace la función (opcional pero recomendable)"""
#     instrucciones
#     return valor  # opcional

# Ejercicio 1 - Calcular el área de un círculo
# Escribe un programa que pida al usuario el radio de un círculo y calcule su área.
# El programa debe definir una función que reciba el valor del radio, realice el cálculo del área y luego imprima el resultado.

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

radio = int(input("Introduce el radio: \n"))
print(calcular_area_circulo(radio))

# Ejercicio 2 - Configura un mensaje de bienvenida
# Escribe un programa que pida al usuario un nombre, un apellido y una edad.
# El programa debe definir una función que reciba estos datos y luego imprima un mensaje de bienvenida personalizado.

def mensaje_bienvenida(nombre, apellido, edad):
    print(f"Bienvenid@ {nombre} {apellido}, tienes {edad} años")

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))

mensaje_bienvenida(nombre, apellido, edad)

# Ejercicio 3 - Calcular el factorial de un número
# Escribe un programa que pida al usuario un número entero y calcule su factorial.
# El programa debe definir una función que reciba el número, realice el cálculo del factorial y luego imprima el resultado.

def calculo_factorial(numero):
    resultado = 1
    for i in range(numero,1,-1):
        resultado *= i
    return resultado

numero = int(input("Introduce un numero entero positivo: "))
print(calculo_factorial(numero))

# Ejercicio 4 - Verificar si un número es primo
# Escribe un programa que pida al usuario un número entero y verifique si es primo.
# El programa debe definir una función que reciba el número, realice la verificación y luego imprima si el número es primo o no.

def es_primo(numero):
    """un numero es primo si solo es divisible entre 1 y si mismo"""
    for i in range(2, numero):
        if numero%i == 0:
            return False
    return True

numero = int(input())
print(es_primo(numero))

# Ejercicio 5 - Calcular la suma de dígitos de un número
# Escribe un programa que pida al usuario un número entero y calcule la suma de sus dígitos.
# El programa debe definir una función que reciba el número, realice el cálculo de la suma de los dígitos y luego imprima el resultado.

def suma_digitos(numero):
    resultado = 0
    while numero > 0:
        resultado += numero%10
        numero //= 10
    return resultado

numero = int(input("Introduce un numero entero positivo:\n"))
print(f"La suma de los digitos del numero {numero} es {suma_digitos(numero)}")

# Ejercicio 7 - Incrementar cada elemento de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y un número entero.
# El programa debe definir una función que reciba la lista y el número, incremente cada elemento de la lista por el número dado y luego imprima la lista resultante.

def incrementa_lista(lista, numero):
    for i in range(len(lista)):
        lista[i] += numero
    return lista

numeros = input("Introduce una lista de numeros separados por coma\n").split(",")
lista = [int(num) for num in numeros]
numero = int(input("Introduce el incremento\n"))
print(incrementa_lista(lista, numero))