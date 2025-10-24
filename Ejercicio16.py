invitados = ["Francisco", "Julia", "Aiden", "Alexander"]
for item in invitados:
    print("Te invito a una cena, ",item)
print("El invitado ",invitados[2]," no podrá asistir a la cena.")
invitados[2] = "Pedro"
for item in invitados:
    print("Te invito a una cena, ",item)