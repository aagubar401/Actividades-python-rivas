vinos_jerez = ["Sherry Classic", "Vino Blanco", "Fino SHERRY", "Moscatel", "ShErry Cream"]
def sherry(vino):
    return "sherry" in vino.lower()
diccionario_vinos = {}
for vino in vinos_jerez:
    diccionario_vinos[vino] = sherry(vino)
print(diccionario_vinos)
lista_vinos_sherry = list(filter(sherry, vinos_jerez))
print(lista_vinos_sherry)