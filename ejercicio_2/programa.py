# cuantos multiplos de 7 y 9 hay comprendidos entre 1000 y 5000

multiplos_7 = 0
multiplos_9 = 0

for i in range (1000,5001):
    z = i % 7
    if z == 0:
        multiplos_7 += 1
    z1 = i % 9
    if z1 == 0:
        multiplos_9 += 1

print(f"Entre 1000 y 5000 hay {multiplos_7} multiplos de 7 y {multiplos_9} multiplos de 9")