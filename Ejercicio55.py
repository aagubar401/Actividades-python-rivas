habitaciones_precios = {"normal": 50, "suite": 80}


class ReservaExistenteError(Exception):
    def __init__(self, nombre_cliente):
        super().__init__(f"El cliente {nombre_cliente} ya tiene una reserva registrada")

class TipoHabitacionInexistente(Exception):
    def __init__(self, tipo_habitacion):
        super().__init__(f"La habitación {tipo_habitacion} no existe")

class OpcionNoDisponible(Exception):
    def __init__(self, opcion):
        super().__init__("Esta opcion no existe")

class Reserva:
    def __init__(self, noches, tipo_habitacion):
        self.noches = noches
        self.tipo_habitacion = tipo_habitacion
    def __str__(self):
        return f"{self.tipo_habitacion} por {self.noches} noches"
    
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = {}
    def agregar_reserva(self, nombre_cliente, noches, tipo_habitacion):
        if nombre_cliente in self.reservas:
            raise ReservaExistenteError(nombre_cliente)
        elif tipo_habitacion not in habitaciones_precios.keys():
            raise TipoHabitacionInexistente(tipo_habitacion)
        else:
            self.reservas[nombre_cliente] = {"noches": noches, "tipo_habitacion": tipo_habitacion}
            print(f"El cliente {nombre_cliente} ha realizado correctamente su reserva")
    def eliminar_reserva(self, nombre_cliente):
        if nombre_cliente in self.reservas:
            del self.reservas[nombre_cliente]
            print(f"La reserva del cliente {nombre_cliente} ha sido eliminada exitosamente")
        else:
            print(f"El cliente {nombre_cliente} no tiene ninguna reserva a su nombre")
    def mostrar_reservas(self):
        if not self.reservas:
            print("No hay reservas registradas")
        else:
            print(f"Reservas del hotel {self.nombre}:")
            for cliente, datos in self.reservas.items():
                print(f" - {cliente}: {datos["tipo_habitacion"]} por {datos["noches"]} noches")
    def buscar_reserva(self, nombre_cliente):
        reserva = self.reservas.get(nombre_cliente)
        if reserva:
            print(f" {nombre_cliente} ha reservado una habitacion {reserva["tipo_habitacion"]} por {reserva["noches"]} noches")
        else:
            print(f"El cliente {nombre_cliente} no tiene ninguna reserva a su nombre")
    def calcular_precio_reserva(self, nombre_cliente):
        reserva = self.reservas.get(nombre_cliente)
        if reserva:
            coste = habitaciones_precios[reserva["tipo_habitacion"]] * reserva["noches"]
            print(f"El precio de la reserva del cliente {nombre_cliente} es de {coste} €")
        else:
            print(f"El cliente {nombre_cliente} no tiene ninguna reserva a su nombre")

hotel = Hotel("Camas de algodón")
while True:
    try:    
        opcion = int(input("Introduce una opcion (1: Agregar reserva, 2: Cancelar reserva, 3: Calcular el coste de la reserva, 4: Mostrar resumen de reservas, 5: Salir): "))
    except ValueError:
        print("Eleccion con formato incorrecto")
    else:
        match opcion:
            case 1:
                try:
                    cliente = input("Introduce el nombre del cliente: ")
                    noches = int(input("Introduce el numero de noches: "))
                    tipo_habitacion = input("Introduce el tipo de habitacion: ")
                except ValueError:
                    print("Alguna de las opciones es inválida")
                else:
                    hotel.agregar_reserva(cliente, noches, tipo_habitacion)
            case 2:
                try:
                    cliente = input("Introduce el nombre del cliente: ")
                except ValueError:
                    print("Alguna de las opciones es inválida")
                else:
                    hotel.eliminar_reserva(cliente)
            case 3:
                try:
                    cliente = input("Introduce el nombre del cliente: ")
                except ValueError:
                    print("Alguna de las opciones es inválida")
                else:
                    hotel.calcular_precio_reserva(cliente)
            case 4:
                hotel.mostrar_reservas()
            case 5:
                break
            case _:
                raise OpcionNoDisponible(opcion)