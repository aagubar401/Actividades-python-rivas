lista_celsius = [0, 10, 20, 30, 40]
lista_farenheit = list(map(lambda x: (x * 9/5 + 32), lista_celsius))
print(lista_farenheit)