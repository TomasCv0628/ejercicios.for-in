# Diagrama de flujo y programa que lea un número entero y positivo , calcule su factorial y que lo imprima junto al número leido

numero = int(input("Ingrese un numero entero positivo: "))

factor = 1

for i in range (2,numero):
    factor *= i
print(f"El calculo de {numero}! = {factor}")