#print("Hello world")

#Hecho por mi en clase.

#Enteros (int)
#numero entero sin decimal (positivo o negativo)

#numero_entero = 19
#numero = 20
#numero_negativo = -12

#print("Soy un número entero, en concreto, soy el", numero_entero)
#print("PONGO LO QUE QUIERO IMPRIMIR")

#Decimales (float) numeros flotantes
numero_decimal = 3.14
numero_decimal_negativo = -3.14
#print("Soy un número decimal:",numero_decimal)
#print("Soy un número decimal:",numero_decimal_negativo)

#Números complejos (complex)
num_complejo = 2 +3j
#print("Soy un número muy complejo", num_complejo)
#print("Parte real", num_complejo.real)
#print("Parte imaginaria", num_complejo.imag)
#print("Tipo de dato:", type(num_complejo))

#Operacines
#suma = 10 + 5
#resta = 10 - 5
#multiplicación = 4 * 2
#division = 10/5
#division_entera = 10%5 #RESTO
#potencia = 2**5

#print("0peraciones matemáticas:")
#print("\n0peraciones matemáticas:") #Salto de linea \n
#print("Suma:", suma, "| Division:", division, "| Division entera:", division_entera)


#Nos va a pasar el ejercicio

#Booleanos (bool) verdadero o falso
es_python_facil = True
es_python_dificil = False

#print("\nBooleanos")
#print("\n¿Es Python fácil?:",es_python_facil)
#print("¿Es Python dificil?:",es_python_dificil)

#comparaciones

mayor_que = 10<5 #Me devuelve TRUE
menor_que = 10>5 #Me devuelve FALSE
igualdad = 10 == 10 #Me devuelve TRUE
diferente = 10 != 5 #Me devuelve TRUE


#Del profesor

# -----------------------------------------------------------------------------
# 📌 1️⃣ TIPOS NUMÉRICOS EN PYTHON
# -----------------------------------------------------------------------------

# 🔹 Enteros (int)
# Los enteros son números sin decimales, pueden ser positivos o negativos.
numero_entero = 19
numero_negativo = -12
#print("Soy un número entero, en concreto, soy el", numero_entero)
#print("Soy un número entero, en concreto, soy el 19")

# 🔹 Decimales (float)
# Los números flotantes son aquellos que tienen decimales.
numero_decimal = 3.14
numero_decimal_negativo = -10.5
#print("Soy un número decimal:",numero_decimal)
#print("Soy un número decimal:",numero_decimal_negativo)

# 🔹 Números complejos (complex)
# Los números complejos tienen una parte real y una imaginaria (se usa "j").
num_complejo = 2 + 3j
#print("Soy un número muy complejo",num_complejo)
#print("Parte real",num_complejo.real)
#print("Parte imaginaria",num_complejo.imag)
#print("Tipo de dato:", type(num_complejo))
# 🔹 Operaciones matemáticas básicas con números
suma = 10 + 5
resta = 10 - 3
multiplicacion = 4 * 2
division = 10/3
division_entera= 10%3
potencia = 2**3
#print("Operaciones matemáticas:")
#print("\nOperaciones matemáticas:")
#print("Suma:",suma,"| División:", division, "| División entera: ", division_entera)


# 📌 EJERCICIO PRÁCTICO 1️⃣:
# 📌 Crea dos números enteros y muestra la suma y la resta de ellos.

numero_entero_ejercicio = 10
numero_entero_ejercicio_2 = 20

sum_result = numero_entero_ejercicio + numero_entero_ejercicio_2
print(sum_result)

difference_result = numero_entero_ejercicio_2 - numero_entero_ejercicio
print(difference_result)

# 📌 Declara un número flotante y muestra su valor dividido entre 3.
#Decimales (float) numeros flotantes
#numero_decimal = 3.14
#numero_decimal_negativo = -3.14
#print("Soy un número decimal:",numero_decimal)
#print("Soy un número decimal:",numero_decimal_negativo)

numero_float = 33.3
print(numero_float/3)



# -----------------------------------------------------------------------------
# 📌 2️⃣ BOOLEANOS (bool)
# -----------------------------------------------------------------------------

# Un booleano solo puede tener dos valores: True (verdadero) o False (falso)
es_python_facil = True
es_python_dificil = False

#print("Booleanos")
#print("\n¿Es Python fácil?:",es_python_facil)
#print("¿Es Python difícil?:",es_python_dificil)

# 🔹 Comparaciones que devuelven valores booleanos
mayor_que = 10>5 #ME DEVUELVE TRUE
menor_que = 10<5 #ME DEVUELVE FALSE
igualdad = 10 == 10 #ME DEVUELVE TRUE 
diferente = 10 != 5 #ME DEVUELVE TRUE

#print("es diferente:" ,diferente)
# NOS QUEDAMOS AQUÍ, NO HAGAS NADA DE LO QUE ESTÁ ABAJO.
# 🔹 Operaciones lógicas con booleanos

