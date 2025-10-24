tienda = {"Boli": {"Precio": 1.20, "Stock": 100, "Reseñas": [9.3, 8.7, 4.5]}, "Cuaderno": {"Precio": 2.50, "Stock": 200, "Reseñas": [6.3, 7.7, 8.5]}, "Mochila": {"Precio": 25.00, "Stock": 50, "Reseñas": [9.0, 9.5, 8.0]}}
tienda["Libro"] = {"Precio": 15.00, "Stock": 80, "Reseñas": [7.5, 8.0, 9.0]}
print(tienda)
tienda["Boli"]["Precio"] = 1.50
tienda["Boli"]["Stock"] = 90
print(tienda)
print(tienda["Cuaderno"])
tienda.pop("Mochila")
print(tienda)
print("Libro" in tienda)
k = tienda.keys()
v = tienda.values()
print(k)
print(v)
for producto in tienda.keys():
    print(tienda[producto])