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