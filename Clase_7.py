#bucle for y bucle while#

# cuando sepamos cuantas repeticiones vamos a hacer utilizaremos un for
# cuando no sepamos exactamente cuantas repeticiones vamos a hacer usaremos un while

#Ejercicio 1 - Contador

# Escribe un programa que pida al usuario un número entero positivo e imprima los números desde el 0 hasta ese número (incluido).
# El programa debe imprimir los números en cada iteración.

# numero = int(input("Introduce un número entero positivo: "))
# for i in range(0, numero+1):
#     print(i)


# Ejercicio 2 - Contador de números pares

# Escribe un programa que pida al usuario un número entero positivo y cuente cuántos números pares hay desde 0 hasta ese número (incluido).
# El programa debe imprimir el resultado

# #Recibo el numero del usuario
# numero_pares = int(input("Introduce un número entero positivo: "))
# #Inicio una variable para ir contando los pares que hay en esa secuencia de números
# par = 0
# #Para i en la secuencia [0,1,2,3,4,5...numero+1]
# for i in range(0, numero_pares+1):
#     #Miro si i es par
#     if i % 2 == 0:
#         #Si i es par, sumamos uno a la variable par
#         par = par + 1
# print(f"Número de pares: {par}")


# Ejercicio 3 - Cuenta atrás

# Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número hasta 0.
# El programa debe imprimir cada número en la cuenta atrás.

# numero_2 = int(input("Introduce un número entero positivo: "))
# for i in range(numero_2,-1-1):
#     print(i)


# Ejercicio 4 - Factorial

# Escribe un programa que pida al usuario un número entero positivo y calcule su factorial.
# El programa debe imprimir el resultado.
# El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

# numero_3 = int(input("Introduce un número entero positivo: "))
# factorial = 1
# for i in range(1,numero_3+1):
#     factorial = factorial * i
# print(f"El factorial de {numero_3} es {factorial}")


# Ejercicio 5 - Múltiple de 3 o 5

# Escribe un programa que pida al usuario un número entero positivo e imprima solamente los números múltiplos de 3 o de 5 dentro de ese rango.
# Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3".
# Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo de 5".
# Si el número es múltiplo de ambos no debes imprimir nada.

# numero_4 = int(input("Introduce un número entero positivo: "))

# for i in range(numero_4+1):
#     if i%3 == 0 and i%5 == 0:
#         continue
#     elif i%3 == 0:
#         print(f"{i} es múltiplo de 3")
#     elif i%5 == 0:
#         print(f"{i} es múltiplo de 5")


# Ejercicio 6 - Triángulo de asteriscos

# Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con la altura especificada.

# altura = int(input("Introduce la altura del triángulo: "))

# for i in range(1, altura+1):
#     print("*"*i)


#Ejercicios de nivel básico. Ejercicio 13
# Escribe un programa que pida al usuario un número entero positivo e imprima la tabla de multiplicar de ese número (del 1 al 10).

# numero_5 = int(input("Introduce un número entero positivo: "))

# for i in range(1, 11):
#     print(f"{numero_5} x {i} = {numero_5*i}")