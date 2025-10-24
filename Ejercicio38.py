estudiantes = {"Juan": [16, "Matemáticas", "Lengua"],"Yoel": [17, "Biología", "Química"],"Ana": [16, "Historia", "Matemáticas"]}
estudiantes["Carlos"] = [18, "Física", "Química"]
print(estudiantes)
estudiantes["Ana"].append("Inglés")
print(estudiantes)
print(estudiantes["Yoel"])
estudiantes.pop("Juan")
print(estudiantes)
print("Yoel" in estudiantes)
k = estudiantes.keys()
v = estudiantes.values()
print(k)
print(v)
for i in estudiantes.keys():
    print(estudiantes[i])