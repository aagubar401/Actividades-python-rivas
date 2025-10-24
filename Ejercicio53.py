numeros = [x for x in range(1,21)]
divisibles_por_3 = list(filter(lambda x: x % 3 == 0, numeros))
print(divisibles_por_3)