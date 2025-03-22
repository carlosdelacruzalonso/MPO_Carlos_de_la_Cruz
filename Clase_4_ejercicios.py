#Ejercicio 1 : Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# ●	Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# ●	Muestra el valor booleano de cada una.

expresion1 = 10>5
expresion2 = 7+3 == 10
expresion3 = 20<15
expresion4 = 4*2 == 9

print(expresion1, expresion2, expresion3, expresion4)


# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# ●	Suma True + True y False + True.
# ●	Multiplica True * 10 y False * 50.
# ●	Muestra los resultados y explica qué ocurre.

print(True+True) #Es igual que si imprimes (1+1)
print(False+True)
print(False+False)
print(True * 10)
print(False*50)


# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# ●	Convierte un número en cadena y muéstralo.
# ●	Convierte una cadena numérica en un entero.
# ●	Convierte un booleano en un número. #Solo hemos hecho este en clase, el resto por hacer.

num = 1999
num_string = str(num) #numero a string
print(num_string)

string = "2000"
string_num = int(string) #string a numero
print(string_num)

print(int(True))
print(int(False))


# Ejercicio 4: Propiedades de las Cadenas
# 📌 Objetivo: Manipular cadenas y explorar sus propiedades.
# ●	Crea una cadena con tu nombre.
# ●	Muestra el primer y último carácter.
# ●	Muestra la longitud de la cadena.
# ●	Convierte la cadena a mayúsculas y minúsculas.

nombre = "Carlos"
print(nombre[0])
print(nombre[-1])
print(nombre[5])
print(nombre[4])
print(nombre[-2])
print(nombre[-4])
print(nombre[-5])
print(len(nombre)) #muestra la longitud del string
print(nombre.upper())
print(nombre.lower())


# Ejercicio 5: Operaciones con Cadenas y Números
# 📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
# ●	Concatenar cadenas con números usando str().
# ●	Multiplicar una cadena para repetirla varias veces.

numero1 = 1999
numero2 = 25
texto = "Nací en " + str(numero1) + ", por tanto, tengo " + str(numero2) + " años"
print(texto)

print("MONEY " * 10 + " I WANT MORE MONEY" * 5)


# Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
# 📌 Objetivo: Explorar caracteres y su representación en ASCII.
# ●	Obtén el código ASCII de la letra 'A'.
# ●	Convierte un número en su carácter ASCII correspondiente.

print("Código ASCII de 'A':", ord('A'))
num_ascii = chr(77)
print(num_ascii) #Letra M de Mario 😉


# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# ●	Evalúa expresiones lógicas combinando números y operadores lógicos.
# ●	Muestra los resultados.

print(9==9 and 199<200)
print(200<201 or 300<3)
print(not(1==1 and 1000>1)) #Es True pero not invierte el resultado en false


####################################################################################################

# Ejercicios para casa


# Ejercicio 1: Comparación de números y booleanos
# 📌 Objetivo: Usar comparaciones con números y analizar los resultados booleanos.
# Crea tres variables numéricas con valores diferentes.
# Compara los valores entre sí (>, <, >=, <=, ==, !=).
# Almacena los resultados en nuevas variables booleanas y muéstralos.

num1 = 1
num2 = 2
num3 = 3

igual = (num2 == num2)
mayor = (num1 > num3)
distinto = (num3 != num1)
menor_o_igual = (num1 <= num2)

print(igual, mayor, distinto, menor_o_igual)


# Ejercicio 2: Propiedades y manipulación de cadenas
# 📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
# Crea una cadena con una frase corta.
# Muestra cuántos caracteres tiene la cadena.
# Convierte toda la cadena a mayúsculas y minúsculas.
# Cuenta cuántas veces aparece una letra específica en la cadena.

short_string = "Me llamo otto el italiano"
print(len(short_string))
print(short_string.upper())
print(short_string.lower())
print(short_string.count("o"))


# Ejercicio 3: Operaciones matemáticas con números y booleanos
# 📌 Objetivo: Realizar cálculos numéricos usando valores booleanos.
# Define dos variables booleanas (verdadero, falso) con los valores True y False.
# Realiza operaciones matemáticas con estos valores (+, *, -).
# Muestra los resultados y analiza qué sucede.

las_patatas_son_un_vicio = True
el_brocoli_no_es_un_vicio = False

print(las_patatas_son_un_vicio + el_brocoli_no_es_un_vicio)
print(el_brocoli_no_es_un_vicio * las_patatas_son_un_vicio)
print(las_patatas_son_un_vicio - el_brocoli_no_es_un_vicio)

#Lo que sucede es que a True se le asigna un valor de 1 y a false un valor de 0.


# Ejercicio 4: Extracción de caracteres en una cadena
# 📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
# Define una cadena con una palabra o nombre.
# Extrae y muestra los tres primeros caracteres.
# Extrae y muestra los tres últimos caracteres.
# Extrae los caracteres en posiciones impares de la cadena.

gata = "Maya"
print(gata[:3]) #Extrae los primeros tres caracteres
print(gata[-3:]) #Extrae los ultimos tres caracteres
print(gata[::2]) #Extrae los caracteres en posiciones impares


# Ejercicio 5: Conversión de tipos y evaluación booleana
# 📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
# Convierte un número en una cadena y muestra el tipo de dato.
# Convierte una cadena numérica en un número entero y muestra el tipo.
# Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.

num4 = 1999
string4 = str(num4)
print(type(string))

string8 = "1999"
num8 = int(string8)
print(type(num8))

print(bool("")) #Al ser una cadena vacia, el resultado es falso
print(bool("hola k ase")) #Al tener contenido, es true
print(bool(0)) # 0 es falso
print(bool(1)) # 1 es true
print(bool(-1)) # -1 es true
print(bool(None)) #None es falso