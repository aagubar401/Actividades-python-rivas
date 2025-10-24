sumatorio = 0
for i in range(1, 101):
    if i % 2 == 0:
        sumatorio += i
print(f"La suma de los números pares del 1 al 100 es: {sumatorio}")