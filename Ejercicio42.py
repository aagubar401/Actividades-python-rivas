nota = int(input("Introduce una nota del 0 al 10: "))
if nota >= 0 and nota <= 4:
    print("Suspenso")
elif nota >=5 and nota <= 6:
    print("Aprobado")
elif nota >= 7 and nota <= 8:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("La nota introducida no es válida.")