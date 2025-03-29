# Crear una lista con los días de la semana y mostrar el primer y último día.
#ALT + shift + E (ejecutar una parte del código)

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
print("Primer dia de la semana: ", dias[0])
print("Ultimo dia de la semana: ", dias[-1])


# Modificar un elemento de una lista de frutas y agregar una fruta nueva al final.

frutas = ["Manzana", "Platano", "Pera"]
frutas[0] = "Mango" #Remplaza manzana con mango
print(frutas)
frutas.append("Sandia") #añade una fruta al final
print(frutas)


# Crear una lista vacía y llenarla con tres colores usando append().

colores = []
print(colores)
colores.append("Rojo")
colores.append("Amarillo")
colores.append("Rojo")
print(colores)


# Ordenar una lista de números desordenados y mostrarla al revés.

numeros = [6,2,4,0,1,12,64,1999,6,8]
#ordenar lista
numeros.sort()
print(numeros)
#invierto orden
numeros.reverse()
print(numeros)


# Eliminar un elemento de una lista y mostrar el resultado.

animales = ["Perro", "Pulpo", "Gato", "Rinoceronte"]
print(animales)
animales.remove("Gato")
print(animales)


# Contar cuántas veces aparece un número en una lista.

numeritos = [4,6,7,8,2,3,4,5,6,7,8,9]
cantidad = numeritos.count(9)
print("El numero de veces que se repite el numero es: ", cantidad)


# Crear una tupla con tres elementos de distinto tipo y mostrar cada uno.

mi_tupla = (25, "Carlos", True)
print("Numero: ", mi_tupla[0])
print("String: ", mi_tupla[1])
print("Boolean: ", mi_tupla[2])


# Acceder al segundo elemento de una tupla anidada dentro de una lista.

datos = ["Nombre", (100,200), "Apellido"]
tupla_intermedia = datos[1]
print(tupla_intermedia) #(100,200)


# Desempaquetar una tupla en tres variables y mostrarlas con print().

persona = ("Sara", 32, "Madrid")
nombre, edad, ciudad = persona
print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)


# Crear una lista con nombres de alumnos, cambiar el nombre del segundo y mostrar la lista completa.

alumnos = ["Carlos", "Alberto", "Hugo", "Dani"]
print(alumnos)
alumnos[1] = "Alex"
print(alumnos)

