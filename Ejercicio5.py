cadena = input("Ingrese una frase larga: ")
numero = int(input("Ingrese un número de inicio: "))
numero2 = int(input("Ingrese un número de fin: "))
subcadena = cadena[numero:numero2]
print(f"La subcadena desde el índice {numero} hasta el índice {numero2} es: '{subcadena}'")