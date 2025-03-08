import math
import random

#1. len para mirar la longitud de una cadena o String
nombre = "Clippy microsoft"
print("Longitud del nombre: " , len(nombre))

#2. Upper y Lower para convertir los textos en mayusculas o minusculas
print("Quiero convertir mi nombre en mayusculas: " , nombre.upper())
print("Quiero convertir mi nombre en minusculas: " , nombre.lower())

#3. Slicing. Extraer partes de una cadena o String.
# Dame los primeros 3 caracteres
print("Los primero 3 caracteres de mi nombre ", nombre[:3])
# Dame los ultimos 4 caracteres
print("Los cuatro ultimos caracteres de mi nombre ", nombre[-4:])

#4. Reemplazar palabras en un String
frase = "Me encanta Java"
print("Quiero cambiar una palabra:" , frase.replace("Java", "Python"))
print("Impresión tras reemplazo de palabra:", frase) #El cambio se aplica solo para la frase, no se modifica la variable

#5. Verificar si una cadena tiene o contiene a otra
print("Python" in frase) #False
nueva_frase = "Me encanta Python"
print("Python" in nueva_frase) #True

#6. Unir varias palabras en un solo string o cadena
palabras = ["Hola", "mundo", "Python"]
print("La frase completa es: "," ".join(palabras))

#7. Dividir una cadena en partes
oracion = "Python es divertido"
palabras = oracion.split()
print("Lista de palabras:" , palabras)

#8 Redondear un numero que sea decimal
numero = 3.1416
print("El numero PI redondeado es: ", round(numero,2))

#9 Formatear numeros con decimales
precio = 19.99
print("Precios con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un caracter
print("Codigo ASCII de 'A': ", ord('A'))

#11 Elevar un numero al cuadrado
numerito = 5
print("5 elevado al cuadrado es: ", numerito **3)

#12 Obtener raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25 ** 0.5)
#Alternativa importando sqrt con Math. Piensa que tienes el import arriba
numero_raiz = 16
raiz_numero = math.sqrt(numero_raiz)

print("Raiz cuadrada del numero es: ", raiz_numero)

#13 Divisiones, restos y modulos
print("Division normal: ",10/3)
print("Division entera: ",10//3)
print("Resto: ", 10%3)

#14 Generar numeros aleatorios
print("Numero aleatorio del 1 al 10: ", random.randint(1,10))

#15 Convertir cadenas a numeros y viceversa
numero_a_cadena = 100
texto = str(numero_a_cadena)
print("Convertido a texto, queda ", texto)

cadena_a_numero = "200"
numero_a_cadena = int(cadena_a_numero)
print("Convertido a entero, queda: ", numero_a_cadena)
print(numero_a_cadena , texto)

#16 Redondear siempre hacia arriba
print("Redondeo hacia arriba del numero 3,2: ", math.ceil(3.2))
print("Redondeo hacia abajo del numero 3,2: ", math.floor(3.2))

#17 Convertir una lista en un conjunto (eliminando duplicados)
numeros = [1,2,2,3,4,4,5]
sin_duplicados = set(numeros)
print("Lista sin duplicados: ", sin_duplicados)

#18 Absurdo PER0 .Repetir una cadena varias veces
print("Python!" * 3)

#19 Obtener el tipo de una variable
dato = 9.98
print("Tipo de dato: ", type(dato))

#20 Combinar cadenas y variable en un print
nombreAlumno = "Carlos"
edad = 25
print(f"Hola soy {nombreAlumno} y tengo {edad} años.")