#EJERCICIOS
#1️⃣ Generador de nombres de usuario
#Pide al usuario su nombre y apellido.
#Genera un nombre de usuario en minúsculas, sin espacios.
#Añade un número aleatorio al final.
#Muestra el nombre de usuario generado.

import random

"""
tunombre = input("Escribe aquí tu nombre: ")
tuapellido = input("Escribe aquí tu apellido: ")
print(f"{tunombre.lower()}{tuapellido.lower()}{random.randint(100,1000)}")
"""

#2️⃣ Analizador de frases
#Pide al usuario que ingrese una frase.
#Muestra la cantidad de caracteres de la frase.
#Indica si la frase contiene la palabra "Python".
#Convierte la frase a mayúsculas.
#Muestra la frase invertida.

"""
frase_usuario = input("Escribe aqui tu frase random: ")
print(len(frase_usuario))
print("Python" in frase_usuario)
frase_usuario = frase_usuario.upper()
print(frase_usuario)
print(frase_usuario[::-1])
"""

#3️⃣ Cálculo de descuentos
#Pide al usuario el precio de un producto.
#Aplica un 15% de descuento.
#Muestra el precio final con dos decimales.
#Muestra el precio redondeado hacia arriba.

import math

"""
precio_usuario = input("Escribe el precio del producto: ")
precio_usuario = float(precio_usuario)
porcentaje_de_descuento = precio_usuario * 0.15
precio_descuento = precio_usuario - porcentaje_de_descuento
print(round(precio_descuento, 2))
print(math.ceil(precio_descuento))
"""

#4️⃣ Generador de etiquetas de productos
#Pide el nombre de un producto y su precio.
#Convierte el nombre del producto a mayúsculas.
#Muestra el precio con dos decimales.
#Genera un código basado en el valor ASCII de la primera letra del producto.

"""
product = input("Introduce el nombre del producto: ")
price = float(input("Introduce el precio del producto: "))
product = product.upper()
print(product)
print(round(price, 2))
print("Codigo ACII de la primera letra: ", ord(product[0]))
"""

#5️⃣ Conversión de tipos y manipulación de listas
#Pide al usuario una lista de números separados por comas.
#Convierte cada número a entero.
#Elimina los números repetidos.
#Muestra la lista ordenada sin duplicados.

"""
list = input("Introduce numeros separados por comas: ")
string_list = list.split(",")
int_list = map(int, string_list)
no_duplicates_list = set(int_list)
print(sorted(no_duplicates_list))
"""

#6️⃣ Creación de mensajes personalizados
#Pide al usuario su nombre, edad y ciudad.
#Muestra un mensaje con toda la información.
#Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.

"""
name = input("Escribe aquí tu nombre: ")
age = int(input("Escribe aquí tu edad: "))
city = input("Escribe aquí tu ciudad: ")
if age < 18:
    age = 18
print(f"Hola, soy {name}, tengo {age} años y vivo en {city}.")
"""

#7️⃣ Generador de contraseñas aleatorias
#Pide al usuario su nombre.
#Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
#Muestra la contraseña generada.

"""
name1 = input("Escribe aquí tu nombre: ")
simbolo_especial = ["€", "$", "@", "#"]
print(f"Esta es tu nueva contraseña: {name1[0].upper()}{random.randint(1,1000)}{random.choice(simbolo_especial)}")
"""

#8️⃣ Verificación de nombres en listas
#Pide al usuario su nombre.
#Verifica si su nombre está en una lista de invitados predefinida.
#Si está en la lista, muestra su posición.

"""
name2 = input("Escribe aquí tu nombre: ")
usuarios_vip = ["Carlos", "Mario", "Luigi", "Goku", "Maya"]
if name2 in usuarios_vip:
    print(f"Bienvenido, {name2}, eres el {usuarios_vip.index(name2)} en la cola.")
else:
    print("Error 404")
"""

#9️⃣ Manipulación de nombres
#Pide al usuario su nombre y apellido.
#Convierte el nombre a minúsculas y el apellido a mayúsculas.
#Genera un alias combinando las primeras 3 letras del nombre y del apellido.
#Muestra el alias generado.

"""
name3 = input("Escribe aquí tu nombre: ")
apellido3 = input("Escribe aquí tu apellido: ")
name3minus = name3.lower()
apellido3mayus = apellido3.upper()
print(f"{name3minus[:3]}{apellido3mayus[:3]}")
"""

#🔟 Formatear y mostrar datos matemáticos
#Pide al usuario un número decimal.
#Muestra el número redondeado a dos decimales.
#Calcula y muestra su cuadrado.
#Calcula y muestra su raíz cuadrada.

"""
decimal_number = input ("Escribe aquí un numero decimal: ")
decimal_number = float(decimal_number)
print("Número redondeado a dos decimales: ", round(decimal_number, 2))
print("El cuadrado de tu número es: ", decimal_number ** 2)
print("La raíz cuadrada de tu número es: ", decimal_number ** (1/2))
"""