# Ejercicio 1 - Sumar elementos de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas
# y calcule la suma de todos los elementos de la lista. El programa debe imprimir el resultado.

lista_numeros = input("Escribe una lista de numeros separados por coma: ").split(",")
resultado = 0

for i in range (len(lista_numeros)):
    resultado += int(lista_numeros[i])

print(f"Resultado: {resultado}")

# Ejercicio 2 - Contar elementos de una lista
# Escribe un programa que pida al usuario una lista de palabras separadas por comas
# y cuente cuántas palabras hay en la lista. El programa debe imprimir el resultado.

# print("La longitud de la lista es: ", len(input("Introduce una lista de palabras separadas por coma: ").split(",")))

lista_palabras = input("Introduce una lista de palabras separadas por coma: ").split(",")
resultado = 0

for palabra in lista_palabras:
    resultado += 1

print("La longitud de la lista es: ", resultado)

# Ejercicio 3 - Mayor y menor elemento de una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por comas
# y encuentre el mayor y el menor elemento de la lista. El programa debe imprimir ambos resultados.

lista_numero = input("Introduce una lista de números separados por coma: ").split(",")
lista_numero = [int(num) for num in lista_numeros]
print(f"menor: {min(lista_numero)} mayor: {max(lista_numero)})

# Ejercicio 4 - Sumar dos listas de igual longitud
# Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos de ambas listas.
# El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el programa debe imprimir un mensaje de error.

lista1 = input("Introduce la primera lista de números separados por coma: ").split(",")
lista2 = input("Introduce la segunda lista de números separados por coma: ").split(",")

if len(lista1) != len(lista2):
    print("La longitud de las listas no es la misma")
else:
    suma_listas = []
    for i in range(len(lista1)):
        suma_listas.append(int(lista1[i]) + int(lista2[i]))

    print(suma_listas)

# Ejercicio 5 - Invertir una lista
# Escribe un programa que pida al usuario una lista de números enteros separados por espacios y la invierta.
# El programa debe imprimir la lista invertida.

lista = input("Introduce una lista de números separados por espacios: ").split()
lista.reverse()
print(lista)

# Ejercicio 6 - Dias de la semana
# Escribe un programa que reciba números enteros positivos hasta la introducción de un 0.
# Por cada número, suponiendo que el 1 representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.
#
# Ejemplo:
#
#
# Ingrese un número (0 para salir): 1
# Lunes
# Ingrese un número (0 para salir): 3
# Miércoles
# Ingrese un número (0 para salir): 8
# Lunes
# Ingrese un número (0 para salir): 0

lista_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

while True:
    numero = int(input("Ingrese un número (0 para salir): "))
    if numero == 0:
        print("Programa terminado")
        break
    print(lista_dias[(numero%7)-1])
    