# Un diccionario es una estructura de datos en Python que almacena pares clave-valor.
# Cada clave es única y se utiliza para acceder a su valor asociado.

# persona = {
#     "nombre": "Ana",
#     "edad": 30,
#     "ciudad": "Valencia"
# }

# Una tupla es una colección ordenada e inmutable de elementos.
# Una vez creada, no se puede modificar (ni añadir, ni eliminar, ni cambiar elementos).

# mi_tupla = (1, 2, 3)

# Ejercicio 1 - Capitales y países
# Escribe un programa que almacene en un diccionario las capitales de varios países,
# se introducirán los datos con la forma PAIS-CAPITAL.
# Esto debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
# El programa debe permitir al usuario consultar la capital de un país introduciendo su nombre.
# Si el país no está en el diccionario, el programa debe informar al usuario.

"""
1. variables
2. bucle que lee y registra las entradas de pais-capital
3. pedir un pais y mirar si existe en el diccionario
"""

paises = {}
entrada = input("Indica un valor de la forma 'Pais:Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

while entrada != "fin inserciones":
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    entrada = input("Indica un valor de la forma 'Pais:Capital' o escribe FIN INSERCIONES para finalizar\n").lower()

pais_usuario = input("Introduce el nombre del pais que quieres consultar").lower()
if pais_usuario in paises:
    print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario.capitalize()]}")
else:
    print("No existe ese registro en el diccionario.")

# Ejercicio 2 - Contar palabras en un texto
# Escribe un programa que pida al usuario un texto y cuente cuántas veces aparece cada palabra en el texto.
# El programa debe imprimir un diccionario donde las claves son las palabras y los valores son sus respectivas frecuencias.
# Ignora la puntuación y considera las palabras en minúsculas.

"""
"Hola que tal que te cuentas"
frecuencia = {
    "hola":1,
    "que":2,
    "tal":1,
    "te":1,
    "cuentas":1
}

1. Definir las variables
2. Bucle que recorra las palanbras y mire si:
    2.1 Si ya existian: Sumo 1 a la frecuencia anterior
    2.2 Creo una entrada en el diccionario con frecuencia 1
3. Imprimir diccionario
"""

palabras = {}
texto = input("Introduce una frase\n").lower().split()

for palabra in texto:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1
print(palabras)

# Ejercicio 3 - Inventario de productos
# Escribe un programa que gestione un inventario de productos utilizando un diccionario.
# El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos,
# y consultar la cantidad de un producto específico.
# El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

inventario = {}
opcion = -1

while opcion != 4:
    print("Escoge una opción: ")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Consultar producto")
    print("4. Salir")
    opcion = int(input("Introduce una opción: "))

    if opcion == 1:
        nombre = input("Introduce un producto: ")
        cantidad = int(input("Introduce una cantidad: "))
        inventario[nombre] = cantidad
    elif opcion == 2:
        nombre = input("Introduce el producto a eliminar: ")
        if nombre in inventario:
            del inventario[nombre]
            print(f"Producto {nombre} ha sido eliminado correctamente.")
        else:
            print((f"No existe el producto {nombre} en el inventario"))
    elif opcion == 3:
        nombre = input("Introduce el producto a consultar: ")
        if nombre in inventario:
            print(f"El Producto {nombre} tiene una cantidad de {inventario[nombre]} unidades")
        else:
            print((f"No existe el producto {nombre} en el inventario"))
    elif opcion > 4 or opcion <1:
            print(f"La opcion {opcion} no existe en la lista de comandos")

print("Saliendo...")

# Ejercicio 4 - Tupla de números
# Escribe un programa que pida al usuario una lista de números enteros separados por comas y almacene estos números en una tupla.
# Luego, el programa debe calcular y mostrar la suma, el promedio, el número máximo y el número mínimo de la tupla.

numeros = input("Introduce una lista de numeros separados por coma\n").split(",")
numeros = [int(num) for num in numeros]

tupla = tuple(numeros)

suma = 0
promedio = 0.0
maximo = float('-inf')
minimo = float('inf')

for numero in tupla:
    suma += numero
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero

promedio = suma / len(tupla)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Maximo: {maximo}")
print(f"Minimo: {minimo}")
