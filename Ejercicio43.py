numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print(f"{numero1} es mayor que {numero2}" if numero1 > numero2 else f"{numero2} es mayor que {numero1}" if numero2 > numero1 else "Ambos números son iguales.")