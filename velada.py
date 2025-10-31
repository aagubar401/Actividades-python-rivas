lista_pesos = ["LIGERO", "MEDIO", "PESADO"]

class combate_invalido_error(Exception):
    def __init__(self, titulo):
        super().__init__(f"El combate {titulo} no existe o ya ha sido cerrado")

class ganador_no_esta_en_luchadores(Exception):
    def __init__(self, ganador):
        super().__init__(f"El supuesto ganador no estaba en el combate")

class unidades_no_positivas(Exception):
    def __init__(self, unidades):
        super().__init__(f"Unidades no positivas")

class rounds_no_positivas(Exception):
    def __init__(self, rounds):
        super().__init__(f"Rounds no positivas")

evento = {
    "combates": {

    },
    "artistas": [

    ],
    "entradas": {
        "vendidas": 0,
        "tipos": {"general": 25.0, "premium": 60.0, "vip": 120.0}
    },
    "staff": {
        "seguridad": {"miembros": {"Ana", "Luis", "Eva"}},
        "ring": {"miembros": {"Pablo", "Irene"}}
    }
}



class Persona:
    total_objetos = 0
    def __init__(self, nombre):
        self.nombre = nombre
        Persona.total_objetos += 1
    def __str__(self):
        return f"{self.nombre}"
    def __repr__(self):
        return f"{self.nombre}"
    @classmethod
    def contar(cls):
        return f"{cls.total_objetos}"
    
class Luchador(Persona):
    total_objetos = 0
    def __init__(self, nombre, peso):
        super().__init__(nombre)
        self.peso = peso
        Luchador.total_objetos += 1
    def __str__(self):
        return f"{self.nombre}"
    def __repr__(self):
        return f"{self.nombre}"
    def __eq__(self, otro_luchador):
        return self.nombre == otro_luchador.nombre
    @classmethod
    def contar(cls):
        return f"{cls.total_objetos}"
    
class Artista(Persona):
    total_objetos = 0
    def __init__(self, nombre, temas):
        super().__init__(nombre)
        self.temas = temas
        Artista.total_objetos += 1
    def __str__(self):
        return f"{self.nombre}"
    def __repr__(self):
        return f"{self.nombre}"
    def mostrar_lista_temas(self):
        return self.temas
    @classmethod
    def contar(cls):
        return f"{cls.total_objetos}"
    
class Tema:
    total_objetos = 0
    def __init__(self, titulo):
        self.titulo = titulo
        Tema.total_objetos += 1
    def __str__(self):
        return f"{self.titulo}"
    def __repr__(self):
        return f"{self.titulo}"
    @classmethod
    def contar(cls):
        return f"{cls.total_objetos}"


def vender_entradas(evento, tipo, unidades):
    if tipo not in evento["entradas"]["tipos"].keys():
        raise ValueError
    elif unidades <= 0:
        raise unidades_no_positivas(unidades)
    else:
        evento["entradas"]["vendidas"] += unidades
        precio = unidades * evento["entradas"]["tipos"][tipo]
        print(f"Se han vendido {unidades} entradas {tipo} por un total de {precio}")


def agregar_artista(evento, nombre, *temas):
    lista_temas = []
    for tema in temas:
        tema_objeto = Tema(tema)
        lista_temas.append(tema_objeto)
    artista = Artista(nombre, lista_temas)
    diccionario_artista = {}
    diccionario_artista["nombre"] = artista
    diccionario_artista["setlist"] = artista.mostrar_lista_temas()
    if diccionario_artista in evento["artistas"]:
        del evento["artistas"][diccionario_artista]
        print("Artista borrado correctamente y listo para reemplazar")
    evento["artistas"].append(diccionario_artista)
    print("Artista añadido correctamente")


def programar_combate(evento, titulo, luchador1, luchador2, rounds, peso):
    if rounds <= 0:
        raise rounds_no_positivas(rounds)
    else:
        peso_mayus = peso.upper()
        if peso_mayus not in lista_pesos:
            print("No existe este peso")
        else:
            luchador1_clase = Luchador(luchador1, peso_mayus)
            luchador2_clase = Luchador(luchador2, peso_mayus)
            diccionario_combate = {}
            diccionario_combate["luchadores"] = [luchador1_clase, luchador2_clase]
            diccionario_combate["rounds"] = rounds
            diccionario_combate["peso"] = peso_mayus
            diccionario_combate["resultado"] = None
            evento["combates"][titulo] = diccionario_combate
            print("Combate programado correctamente")

def cantidad_clase(clase):
    if clase not in ["Persona", "Luchador", "Artista", "Tema"]:
        print("Esta clase no existe")
    else:
        match clase:
            case "Persona":
                print(Persona.contar())
            case "Luchador":
                print(Luchador.contar())
            case "Artista":
                print(Artista.contar())
            case "Tema":
                print(Tema.contar())

def cerrar_resultado(evento, titulo, ganador):
    ganador_clase = Luchador(ganador, None)
    Luchador.total_objetos -= 1
    Persona.total_objetos -= 1
    if (titulo not in list(evento["combates"].keys()) or evento["combates"][titulo]["resultado"] != None):
        raise combate_invalido_error(titulo)
    elif any([ganador_clase == luchador for luchador in evento["combates"][titulo]["luchadores"]]) == False:
        raise ganador_no_esta_en_luchadores(ganador)
    else:
        evento["combates"][titulo]["resultado"] = f"gano {ganador}"
        print(f"Resultado registrado: ganó {ganador}")

def informe_completo(evento):
    print("INFORME DE LA VELADA", end="\n")
    combates_totales = len(list(evento["combates"].keys()))
    combates_cerrados = 0
    combates_pendientes = 0 
    for combate in list(evento["combates"].keys()):
        if evento["combates"][combate]["resultado"] == None:
            combates_pendientes += 1
        else:
            combates_cerrados += 1
    print(f"Combates totales: {combates_totales}", end="\n")
    print(f"     - Cerrados: {combates_cerrados}", end="\n")
    print(f"     - Pendientes: {combates_pendientes}", end="\n")
    luchadores = []
    for combate in list(evento["combates"].keys()):
        for luchador in evento["combates"][combate]["luchadores"]:
            luchadores.append(luchador.nombre)
    print("Luchadores inscritos: ", end="\n")
    for luchador in luchadores:
        print(f"     - {luchador}", end="\n")
    print("Artistas y canciones: ", end="\n")
    artistas = []
    for artista in evento["artistas"]:
        artistas.append(artista["nombre"])
    for artista in artistas:
        print(f"*{artista.nombre}", end="\n")
        for artista_evento in evento["artistas"]:
            if artista_evento["nombre"] == artista:
                lista_temas_artista = artista_evento["setlist"]
            for tema in lista_temas_artista:
                print(f"     - {tema.titulo}", end="\n")
    print("Tipos de entradas: ", end="\n")
    for entrada in list(evento["entradas"]["tipos"].keys()):
        print(f"     - {entrada}: {evento["entradas"]["tipos"][entrada]}", end="\n")
    print(f"Entradas vendidas: {evento["entradas"]["vendidas"]}", end="\n")
    print("Staff por área: ", end="\n")
    areas = []
    for area in list(evento["staff"].keys()):
        areas.append(area)
    for area in areas:
        print(f"[{area}]", end="\n")
        for staff in evento["staff"][area]["miembros"]:
            print(f"    - {staff}")


while True:
    print("=== La Velada – Backstage Manager === \n 1. Vender entradas \n 2. Añadir artista \n 3. Programar combate \n 4. Cerrar combate \n 5. Ver informe completo \n 6. Contar elementos de una clase \n 7. Salir")
    opcion = int(input("Escoge una opción: "))
    match opcion:
        case 1:
            tipo = ((input("Escoge el tipo de entrada a comprar: ")).strip()).lower()
            cantidad = int(input("Escoge cuantas entradas deseas comprar: "))
            try:    
                vender_entradas(evento, tipo, cantidad)
            except unidades_no_positivas as e:
                print(e)
            except ValueError:
                print("Entrada no disponible")
        case 2:
            nombre = (input("Introduce el nombre del artista: ")).strip()
            temas_input = (input("Introduce los temas que va a cantar el artista separados por comas: ")).strip()
            temas = temas_input.split(",")
            lista_temas_format = []
            for tema in temas:
                lista_temas_format.append(tema.strip())
            agregar_artista(evento, nombre, *lista_temas_format)
        case 3:
            titulo = (input("Introduce el título del combate: ")).strip()
            luchador1 = (input("Introduce el nombre del primer luchador: ")).strip()
            luchador2 = (input("Introduce el nombre del segundo luchador: ")).strip()
            rounds = int(input("Introduce el número de rounds: "))
            peso = (input("Introduce el peso del combate (LIGERO, MEDIO, PESADO): ")).strip()
            try: 
                programar_combate(evento, titulo, luchador1, luchador2, rounds, peso)
            except rounds_no_positivas as e:
                print(e)
        case 4:
            titulo = (input("Introduce el título del combate: ")).strip()
            ganador = (input("Introduce el ganador del combate: ")).strip()
            try:
                cerrar_resultado(evento, titulo, ganador)
            except combate_invalido_error as e:
                print(e)
            except ganador_no_esta_en_luchadores as f:
                print(f)
        case 5:
            informe_completo(evento)
        case 6:
            clase = ((input("Introduce una clase: ")).strip()).capitalize()
            cantidad_clase(clase)
        case 7:
            break
        case _:
            print("Opcion no disponible")