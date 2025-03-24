#Mini app 1 - Fahrenheit to Celsius program

fahrenheit_to_celsius = input("Write here the temperature in fahrenheit to convert it to Celsius: ")
to_int = int(fahrenheit_to_celsius)
celsius = (to_int - 32) / 1.8
print(f"Equivale a {round(celsius, 2)} °C")


#Mini app 2 - Body mass index

peso = int(input("Escribe aquí tu peso en kg: "))
altura = float(input("Escribe aquí tu altura en metros: "))

i_m_c = peso / (altura**2)

print(f"Tu indice de masa corporal es: {round(i_m_c, 2)}")


#Mini app 3 - Calcula la hipotenusa

cateto1 = int(input("Introduce el primer cateto del triángulo: "))
cateto2 = int(input("Introduce el segundo cateto del triángulo: "))
resultado = (cateto1**2 + cateto2**2)
hipotenusa = (resultado ** 0.5)

print(f"La longitud de la hipotenusa es: {round(hipotenusa, 2)}")


#Mini app 4 - Spare change in Colombian pesos, peruvian soles and brazilian reais to EUR.

pesos_left = float(input("What do you have left in pesos? "))
soles_left = float(input("What do you have left in soles? "))
reales_left = float(input("What do you have left in reales? "))

peso_a_euro = 0.00022
sol_a_euro = 0.25
real_a_euro = 0.1590

peso_euro = pesos_left * peso_a_euro
sol_euro = soles_left * sol_a_euro
real_euro = reales_left * real_a_euro

eur_total = peso_euro + sol_euro + real_euro

print(f"You have a total of {round(eur_total, 2)} €")


###Mini script (¿He aprobado?)

grade = int(input("Escribe que nota has sacado del 0-100: "))
if  grade >= 55:
  print("You passed.")
else:
  print("You failed little piece of shit.")
  

###Mini script (pH level)

value = int(input("Insert pH value between 1-14: "))
if value > 7:
  print("Basic")
elif value < 7:
  print("Acidic")
else:
  print("Neutral")
  

#Mini app 5 - The magic 8 Ball

import random
question = input("Write your question for the Magic 8 Ball: ")

num = random.randint(1,9)
if num == 1:
  print("Magic 8 Ball: Yes - definitely.")
elif num == 2:
  print("Magic 8 Ball: It is decidedly so.")
elif num == 3:
  print("Magic 8 Ball: Without a doubt.")
elif num == 4:
  print("Magic 8 Ball: Reply hazy, try again.")
elif num == 5:
  print("Magic 8 Ball: Ask again later.")
elif num == 6:
  print("Magic 8 Ball: Better not tell you now.")
elif num == 7:
  print("Magic 8 Ball: My sources say no.")
elif num == 8:
  print ("Magic 8 Ball: Outlook not so good.")
else:
  print("Magic 8 Ball: Very doubtful")


#Mini app 6 - The Cyclone roller coaster

altura = float(input("¿Cuál es tu altura en metros? "))
creditos = int(input("¿Cuántos créditos tienes? "))

#requisitos minimos : altura >= 1.37m. Creditos >= 10.

if altura >= 1.37 and creditos >= 10:
  print("¡Disfruta del viaje!")
elif altura < 1.37 and creditos >= 10:
  print("No eres lo suficientemente alto para subir.")
elif altura >= 1.37 and creditos < 10:
  print("No tienes suficientes créditos.")
else:
  print("No cumples ninguno de los requisitos")
  

#Mini app 7 - The Sorting Hat

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("Question 1, Do you like Dawn(1) or dusk(2)?")
answer1 = int(input("Enter your answer: "))

if answer1 == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif answer1 == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:
    print("Wrong input")

print("Question 2, When I’m dead, I want people to remember me as: The Good(1), The Great(2), The Wise(3), The Bold(4)")
answer2 =  int(input("Enter your answer here: "))

if answer2 == 1:
    Hufflepuff = Hufflepuff + 2
elif answer2 == 2:
    Slytherin = Slytherin + 2
elif answer2 == 3:
    Ravenclaw = Ravenclaw + 2
elif answer2 == 4:
    Gryffindor = Gryffindor + 2
else:
    print("Wrong input")

print("Question 3, Which kind of instrument most pleases your ear? The violin(1), The trumpet (2), The piano (3), The drum(4)")
answer3 = int(input("Enter your answer here: "))

if answer3 == 1:
    Slytherin = Slytherin + 4
elif answer3 == 2:
    Hufflepuff = Hufflepuff + 4
elif answer3 == 3:
    Ravenclaw = Ravenclaw + 4
elif answer3 == 4:
    Gryffindor = Gryffindor + 4
else:
    print("Wrong input")

if Gryffindor == max(Gryffindor,Ravenclaw,Hufflepuff,Slytherin):
    print("You belong to Gryffindor! 🦁")
elif Ravenclaw == max(Gryffindor,Ravenclaw,Hufflepuff,Slytherin):
    print("You belong to Ravenclaw! 🦅")
elif Hufflepuff == max(Gryffindor,Ravenclaw,Hufflepuff,Slytherin):
    print("You belong to Hufflepuff! 🦡")
elif Slytherin == max(Gryffindor,Ravenclaw,Hufflepuff,Slytherin):
    print("You belong to  Slytherin! 🐍")

print(f"In case you want to see the complete score: Gryffindor: {Gryffindor}, Ravenclaw: {Ravenclaw}, Hufflepuff: {Hufflepuff}, Slytherin: {Slytherin}")

