#Diccionarios
#Ejercicio 1. Crea un diccionario simple

persona = {
    "nombre" : "Carlos",
    "edad" : 25,
    "registradoEnElCenso" : True,
    "esAtractivo" : True
}
print(persona)


#Ejercicio 2. Sub-apartado del 1

print(persona["edad"])


#Ejercicio 3.

#Añadir una nueva clave-valor

persona["ciudad"] = "Burgos"
print(persona)


#Ejercicio 4.

persona["edad"] = 26
print(persona)


#Ejercicio 5
#Elimina una clave

del persona["ciudad"]
print(persona)


#Ejercicio 6
#Comprobar si una clave existe

existe_nombre = "nombre" in persona
print(existe_nombre)


#Ejercicio 7
#Compara dos valores booleanos

es_mayor_y_registrado = persona["edad"]>18 and persona["registradoEnElCenso"]
print(es_mayor_y_registrado)


#Ejercicio 8
#Uso de NOT con un boolean

no_registrado = not persona["registradoEnElCenso"]
print(no_registrado)


#Ejercicio 9
#Elimina duplicados

numeros =  [1,2,3,2,4,5,6,7,1,1,2]
conjunto = set(numeros)
print(conjunto)


#Ejercicio 10
#Compara si dos colecciones tienen los mismos elementos unicos

lista_a = set([1,2,3,4])
lista_b = set([4,3,2,1,1,1,4])

mismos_elementos = lista_b == lista_a
print(mismos_elementos)