# #Ejercicio 1
#
# numero = int(input("Introduce un número entero: "))
#
# #Comprobar si un numero eso positivo
#
# if numero >= 0:
#     print("Positivo")
# else:
#     print("Negativo")


# #Ejercicio 2
#
# edad = int(input("¿Cuantos años tienes? "))
#
# if edad >= 16 and edad <=17 :
#     print("Vete a kinderGarden")
# elif edad >= 18 and edad <= 60:
#     print("Puedes entrar")
# elif edad > 60:
#     print("Vete a oldSkoolVeterans")
# else:
#     print("Vete a tu casa")


# #Ejercicio 3
#
# pos_pacman = int(input("¿Cuál es la posición de pacman? "))
# pos_fantasma = int(input("¿Cuál es la posición del fantasma? "))
#
# #Comprobamos si la posición es igual
# if pos_pacman == pos_fantasma:
#     #Caramelo -> Pacman come fantasma
#     #Invisible -> Pacman escapa
#     #Normal -> Pacman atrapado
#     estado_pacman = input("¿Cómo está pacman? ")
#     if estado_pacman == "Caramelo":
#         print("Pacman se ha comido al fantasma")
#     elif estado_pacman == "Invisible":
#         print("Pacman ha escapado")
#     else:
#         print("Pacman ha sido atrapado")
# else:
#     print("Pacman ha escapado")


# #Ejercicio 4
#
# multiplo = int(input("Introduce un número entero: "))
#
# if multiplo % 3 == 0 and multiplo % 5 == 0:
#     print(f"{multiplo} es múltiplo de 3 y 5")
# elif multiplo % 3 == 0:
#     print(f"{multiplo} es múltiplo de 3")
# elif multiplo % 5 == 0:
#     print(f"{multiplo} es múltiplo de 5")
# else:
#     print(f"{multiplo} no es múltiplo de 3 ni de 5")


#Ejercicio 5

rol = input("Introduce el rol: ").lower()
academia = input("Introduce la academia: ").lower()

if rol == "alumno" and academia == "prometeo":
    print("Acceso al servidor de Discord oficial y extraoficial")
elif rol == "profesor" and academia == "prometeo":
    print("Acceso al servidor de Discord oficial")
else:
    print("No tienes acceso al servidor de discord")
