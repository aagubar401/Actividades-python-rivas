invitados = ["Francisco", "Julia", "Aiden", "Alexander"]
for item in invitados:
    print("Te invito a una cena, ",item)
print("El invitado ",invitados[2]," no podrá asistir a la cena.")
invitados[2] = "Pedro"
for item in invitados:
    print("Te invito a una cena, ",item)
print("He encontrado una mesa más grande, así que puedo invitar a más personas.")
invitados.insert(0, "María")
invitados.insert(2, "Lucía")
invitados.append("Javier")
for item in invitados:
    print("Te invito a una cena, ",item)
print("Lo siento, solo puedo invitar a dos personas a la cena.")
while len(invitados) > 2:
    eliminado = invitados.pop()
    print("Lo siento ",eliminado,", no puedo invitarte a la cena.")
for item in invitados:
    print("Aún estás invitado a la cena, ",item)
del invitados[0]
del invitados[0]
print(invitados)