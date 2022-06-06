# Hacer el diagrama de flujo y programa en Python que genere 1000 numeros aleatorios y que averigue e imprima cuantos son pares y cuantos son impares

from random import randint

par = 0
impar = 0

numrandom = [randint(1,100000) for _ in range(1000)]

for i in numrandom:
    print(i)
    d = i % 2
    if d != 0:
        par += 1
    else:
        impar += 1


print (f"La cantidad de numeros pares es {par} ,la cantidad de numeros impares es {impar}")

