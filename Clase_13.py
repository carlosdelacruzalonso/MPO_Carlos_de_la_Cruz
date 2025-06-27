"""
Funciones para leer diferentes tipos de datos con control de errores

leer_entero()
-> hola
-> ValueError
"""

from colorama import Fore, Style

colores_mensajes = {
    "ERROR" : Fore.LIGHTRED_EX,
    "MENU" : Fore.BLUE,
    "INPUT" : Fore.LIGHTYELLOW_EX,
    "SUCCESS" : Fore.LIGHTGREEN_EX
}


def leer_entero(mensaje, color=None):
    try:
        imprimir(mensaje, color)
        entero = int(input())
    except:
        raise ValueError("Debes introducir un número entero")

    return entero

def leer_string(mensaje, color=None):
    imprimir(mensaje, color)
    return input(mensaje)

def leer_string_en_lista(mensaje, color=None):
    imprimir(mensaje, color)
    return input(mensaje).split(" ")

"""
Quiero crear una función imprimir que:
1- reciba el mensaje a imprimir
2- opcionalmente reciba un color para que imprima el mensaje de ese color
"""

def imprimir(mensaje, color=None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL

        print(mensaje)

def imprimir_con_marco(mensaje, color=None):
    mensaje = f"| {mensaje} |"
    barra = "-"*len(mensaje)
    print(color + barra + "\n" + mensaje + "\n" + barra + Style.RESET_ALL)
    pass