# Programa que permita simular el lanzamiento de n dados y que muestre en forma de histograma la frecuencia con la que salio cada uno de los 6 números


from random import randint


dados = int(input("Ingrese el numero de dados desea lanzar: "))

cero = ""
uno = ""
dos = ""
tres = ""
cuatro = ""
cinco = ""
seis = ""

numrandom = [randint(1,6) for _ in range(dados)]
while dados != 'X':
    print(numrandom)
    for num in numrandom:
        if num == 1:
            uno += "#"
        if num == 2:
            dos += "#"
        if num == 3:
            tres += "#"
        if num == 4:
            cuatro += "#"
        if num == 5:
            cinco += "#"
        if num == 6:
            seis += "#"
        if dados == 'X':
            break
    print("-------------------------------------")
    print(f"UNO    |{uno}")
    print(f"DOS    |{dos}")
    print(f"TRES   |{tres}")
    print(f"CUATRO |{cuatro}")
    print(f"CINCO  |{cinco}")
    print(f"SEIS   |{seis}")
    dados = int(input("Ingrese el numero de dados desea lanzar: "))
