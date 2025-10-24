cadena = input("Introduce una cadena de texto: ")
vocales = 0
for caracter in cadena:
    if caracter.lower() in 'aeiou':
        vocales += 1
print(f"La cadena contiene {vocales} vocales.")