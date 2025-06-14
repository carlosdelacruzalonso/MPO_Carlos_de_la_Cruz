# Módulos
# ¿Qué es un módulo?
# Un módulo es un archivo con extensión .py que contiene código Python organizado para ser reutilizado. Este código puede incluir:

# Funciones (bloques de código reutilizables)
# Clases (plantillas para crear objetos)
# Variables (datos almacenados)
# Código ejecutable (que se corre al importar el módulo)

import os
from colorama import Fore, Style

def listar_archivos(ruta):
    try:
        return os.listdir(ruta)
    except FileNotFoundError:
        raise FileNotFoundError

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(nombre):
    return open(nombre, "w")

def crear_directorio(nombre):
    try:
        os.mkdir(nombre)
    except FileExistsError:
        raise FileExistsError

def color_extension(ruta, archivo):
    if os.path.isdir(ruta + archivo):
        return "orange"
    elif len(archivo.split(".")) == 1:
        return "white"
    elif archivo.split(".")[-1] == "txt":
        return "green"
    elif archivo.split(".")[-1] in ["jpg", "png"]:
        return "blue"
    elif archivo.split(".")[-1] in ["mp3", "wav", "m4a"]:
        return "yellow"
    return "white"

def colorear(color):
    if color == "orange":
        return Fore.MAGENTA
    elif color == "blue":
        return Fore.BLUE
    elif color == "yellow":
        return Fore.YELLOW
    elif color == "green":
        return Fore.GREEN
    return Fore.WHITE


def main():
    opcion = -1
    while opcion != 5:
        print("### MENU ###\n")
        print("1. Listar archivos")
        print("2. Verificar existencia archivo")
        print("3. Crear archivo")
        print("4. Crear directorio")
        print("5. Salir\n")

        opcion = int(input("Por favor, escoge una opción: \n"))

        if opcion == 1:
            ruta = input("Introduce la ruta que quieres consultar\n")
            try:
                archivos = listar_archivos(ruta)
                for archivo in archivos:
                    print(colorear(color_extension(ruta, archivo)) + archivo + Style.RESET_ALL)
            except FileNotFoundError:
                print(f"La ruta {ruta} no existe")
            except:
                print("Error al consultar la ruta, intentalo de nuevo")

        elif opcion == 2:
            archivo = input("¿Qué archivo quiere comprobar?\n")
            if existe_archivo(archivo):
                print("✅ El archivo existe")
            else:
                print("❌ El archivo no existe")
        elif opcion == 3:
            nombre = input("¿Cómo quieres nombrar al archivo?\n")
            if existe_archivo(nombre):
                print("Este archivo ya existe")
            else:
                archivo = crear_archivo(nombre)
                print(f"Archivo {archivo.name} creado con éxito")
        elif opcion == 4:
            nombre = input("¿Cómo quieres nombrar al directorio?\n")
            try:
                crear_directorio(nombre)
                print(f"Directorio {nombre} creado con éxito")
            except FileExistsError:
                print(f"El directorio {nombre} ya existe")
        elif opcion > 5:
            print("Opción no válida")



if __name__ == "__main__":
    main()
