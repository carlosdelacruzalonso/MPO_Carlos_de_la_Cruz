#Ejercicio 1

num1 = 5
num2, num3, num4, num5 = 10, 3, 8.7, 4+2j
resultado = (f"Potencia: {num1 ** num2}, "
             f"\nDivisión entera: {num1 // num2}, "
             f"\nModulo: {num1 % num2}, "
             f"\nMultiplicación: {num3 * num4}" ,
             f"\nComplejo: {num5}")
#Revisar por que no me está aplicando el salto de linea \n
# print(resultado)


#Ejercicio 2

num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado: ", "La suma es: ", "y la división es: "
resultado = (cadena1 + " " + cadena2 + " " + str(num_int+num_float) +
             " " + cadena3 + " " + str(num_int/num_float))

print(resultado)


#Ejercicio 3

cadena = "  Esto es un ejemplo con huecos delante y detrás "
nueva_cadena = cadena.strip().upper().split()
print(nueva_cadena)


#Ejercicio 4

cadenon = "Esto es una cadena muymuymuymuymuymuymuymuymuymuymuymuymuymuymuymuymuymuymuy larga"
subcadena = (cadenon[0:6] + "" +
             cadenon[11:20] + "" +
             cadenon[-9:])

resultado =subcadena[::-1]
print(resultado) #modo drunk


#Ejercicio 5 Hasta aquí nos quedamos en clase
 
 entero, flotante, complejo = 12, 356.7685858, 5+3j
 formato = (f"Entero: {entero}, Flotante: {flotante:.2f},"
            f" Notación científica: {flotante:.2e} , Complejo: {complejo}")
 print(formato)


# Ejercicio 6: Operaciones combinadas entre números y cadenas
# Define dos variables numéricas enteras y dos cadenas.
# Realiza cálculos matemáticos diversos y genera una cadena formateada que explique cada operación
# (sumas, restas, multiplicaciones, módulo) claramente utilizando métodos de cadenas.

numint1, numint2 = 20, 10
string1, string2 = "el resultado de la multiplicación es: " , "el resto es igual a: "

resultado = f"{string1}{numint1*numint2} y {string2}{numint1%numint2}"
print(resultado)


#Ejercicio 7: Cálculo del área y perímetro
# Define variables numéricas que representen dimensiones (largo, ancho, radio, altura).
# Calcula el área y perímetro de distintas figuras geométricas (rectángulo, círculo, triángulo rectángulo)
# y presenta todos los resultados claramente en una sola cadena formateada usando conversiones explícitas.

largo, ancho, radio, altura = 9, 6, 2, 1
a_rectangulo = largo*ancho
p_rectangulo = 2*(largo+ancho)
a_circulo = 3.14*radio**2
p_circulo = 2*3.14*radio
a_t_rectangulo = (largo*ancho) / 2
p_t_rectangulo = largo+ancho+altura

resultado = f"El area del rectangulo es: {a_rectangulo}, el perimetro: {p_rectangulo}. El area del circulo es: {a_circulo}, el perimetro: {p_circulo}. El area del triangulo rectangulo es: {a_t_rectangulo} y el perimetro: {p_t_rectangulo}"

print(resultado)


# Ejercicio 8: Análisis de texto complejo
# Define una cadena extensa que represente un párrafo completo.
# Utilizando únicamente métodos de cadenas y funciones integradas (len, upper, split),
# obtén el número total de caracteres, palabras y el resultado de transformar el texto completamente a mayúsculas,
# presentándolo claramente en una cadena nueva.

parrafo = "Esto es un parrafo extenso pero que muy muy muy extenso madre mia que extensidad tan larga"
parrafo_len = len(parrafo)
parrafo_upper = parrafo.upper()
cantidad_palabras = len(parrafo.split())
print(f"El número total de letras es: {parrafo_len}, El número total de palabras es: {cantidad_palabras} y ahora vas a ver el texto en mayusculas: {parrafo_upper}")


# Ejercicio 9: Fórmula cuadrática
# Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática,
# resuelve la fórmula cuadrática para obtener las raíces reales o complejas.
# Imprime claramente en una cadena formateada los coeficientes y las raíces encontradas.

import math

a,b,c = 1,2,3   #Discriminante = b**2 - 4ac
discriminante = (b**2 - 4*a*c)
raiz1 = (-b+discriminante)/(2*a)
raiz2 = (-b-discriminante)/(2*a)
resultado = f"Los coeficientes son: a: {a}, b: {b} y c: {c}. Por otro lado, las raices son: {raiz1}, {raiz2}"

print(resultado)

#Este ejercicio no he sabido hacerlo. No recuerdo muy bien las formulas cuadraticas.


# Ejercicio 10: Manejo y transformación de datos personales
# Crea variables para representar datos personales (nombre, edad, peso, altura).
# Calcula el índice de masa corporal (IMC) sin usar bucles, y presenta un resumen detallado y
# formateado de todos estos datos personales, incluyendo el IMC con dos decimales.

#IMC = peso / altura ** 2

nombre = "Carlos"
edad = 25
peso = 68
altura = 1.7

imc = peso / (altura**2)

print(f"Su nombre es: {nombre}, con los datos aportado, nuestro sistema avanzado ha calculado su IMC, que equivale a: {round(imc,2)}")
