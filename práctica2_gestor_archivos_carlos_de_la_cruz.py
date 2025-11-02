import os
import time

def mostrar_menu():
    print("\n=== GESTOR DE ARCHIVOS ===")
    print(f"Directorio actual: {os.getcwd()}")
    print("1. Listar contenido del directorio actual")
    print("2. Crear un nuevo directorio")
    print("3. Crear un archivo de texto")
    print("4. Escribir texto en un archivo existente")
    print("5. Eliminar un archivo o directorio")
    print("6. Mostrar información del archivo o carpeta")
    print("7. Salir")

def listar_contenido():
    print("\nContenido del directorio actual:\n")
    try:
        elementos = os.listdir()
        if not elementos:
            print("No hay archivos ni carpetas aquí.")
        else:
            for e in elementos:
                if os.path.isdir(e):
                    print(f"[CARPETA] {e}")
                else:
                    print(f"[ARCHIVO] {e}")
    except Exception as e:
        print("Error al listar el contenido:", e)

def crear_directorio():
    nombre = input("Introduce el nombre del nuevo directorio: ")
    if os.path.exists(nombre):
        print("Ya existe una carpeta con ese nombre.")
        return
    try:
        os.mkdir(nombre)
        print("Carpeta creada correctamente.")
    except Exception as e:
        print("Error al crear la carpeta:", e)

def crear_archivo():
    nombre = input("Introduce el nombre del archivo (con extensión .txt): ")
    if os.path.exists(nombre):
        print("Ese archivo ya existe.")
        return
    try:
        contenido = input("Escribe el contenido inicial: ")
        with open(nombre, "w", encoding="utf-8") as f:
            f.write(contenido)
        print("Archivo creado correctamente.")
    except Exception as e:
        print("Error al crear el archivo:", e)

def escribir_en_archivo():
    nombre = input("Nombre del archivo donde escribir: ")
    if not os.path.exists(nombre):
        print("El archivo no existe.")
        return
    try:
        texto = input("Escribe el texto que quieres añadir: ")
        with open(nombre, "a", encoding="utf-8") as f:
            f.write("\n" + texto)
        print("Texto añadido correctamente.")
    except Exception as e:
        print("Error al escribir en el archivo:", e)

def eliminar_elemento():
    nombre = input("Introduce el nombre del archivo o carpeta a eliminar: ")
    if not os.path.exists(nombre):
        print("El elemento no existe.")
        return
    try:
        if os.path.isdir(nombre):
            os.rmdir(nombre)
            print("Carpeta eliminada correctamente.")
        else:
            os.remove(nombre)
            print("Archivo eliminado correctamente.")
    except Exception as e:
        print("Error al eliminar el elemento:", e)

def mostrar_informacion():
    nombre = input("Introduce el nombre del archivo o carpeta: ")
    if not os.path.exists(nombre):
        print("No existe ese archivo o carpeta.")
        return
    try:
        tamano = os.path.getsize(nombre)
        fecha = time.ctime(os.path.getmtime(nombre))
        tipo = "Carpeta" if os.path.isdir(nombre) else "Archivo"
        print("\n=== INFORMACIÓN ===")
        print("Nombre:", nombre)
        print("Tipo:", tipo)
        print("Tamaño:", tamano, "bytes")
        print("Última modificación:", fecha)
    except Exception as e:
        print("Error al obtener la información:", e)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            listar_contenido()
        elif opcion == "2":
            crear_directorio()
        elif opcion == "3":
            crear_archivo()
        elif opcion == "4":
            escribir_en_archivo()
        elif opcion == "5":
            eliminar_elemento()
        elif opcion == "6":
            mostrar_informacion()
        elif opcion == "7":
            print("Saliendo del gestor...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()