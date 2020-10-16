# Exercise 1

# b = float(input('Ingresa la base del triángulo: '))
# h = float(input('Ingresa la altura del triángulo: '))

# r = (b*h)/2


# //////////////
# Ejercicio 2

# dolars = float(input("Ingresa el monto de dolares que desea convertir a pesos: "))
# tasa = 3850
# pesos = dolars * tasa

# print("El total de pesos es: ",pesos)


# ////////////
# Ejercicio 3 

# celsius = float(input("Ingresa los grados celsius que desea convertir a fahrenheit: "))
# result = (celsius * 9/5) + 32

# print("Los grados fahrenheit son: ",result)


# ////////////
# Ejercicio 4

# lustro = 157700000
# print("Un lustro tiene",lustro,"segundos")

# ////////////
# Ejercicio 5

# result = 1 * 227940000 / 300000

# print ("La cantidad de segundos que viaja la luz desde el sol a marte es:",result)

# ////////////
# Ejercicio 6

# diametro = 50
# pi = 3.1416
# desplazamiento = pi * diametro
# km = 100000

# result = km / desplazamiento

# print("La cantidad de vueltas es: ",result)

# ////////////
# Ejercicio 7

# tang = 0.40
# sombra = 20 / tang 

# print(sombra)

# ////////////
# Ejercicio 8

# uno = int(input('Ingrese la edad de persona 1: '))
# dos = int(input('Ingresa la edad de persona 2: '))

# if uno == dos:
#     print("TRUE")
# else:
#     print("FALSE")


# ////////////
# Ejercicio 9
# from datetime import date

# today = date.today()
# born = date(2000,5,16)

# timeTranscurred = (today.year-born.year) * 12 + today.month - born.month
# print(f"The number of months transcurred since {born} is: {timeTranscurred}")


# ////////////
# Ejercicio 10

español = int(input("Ingrese la nota de Español: "))
mate = int(input("Ingrese la nota de Matemática: "))
eco = int(input("Ingrese la nota de Economía: "))
pro = int(input("Ingrese la nota de Programación: "))
ing = int(input("Ingrese la nota de Inglés: "))

promedio = (español + mate + eco + pro + ing) / 5

print("El promedio del estudiante es:",promedio)
