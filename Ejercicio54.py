class Empleado:
    lista_dni = []
    salario_medio = []
    def __init__(self, nombre, salario, dni):
        self.__Nombre = nombre
        self.__Salario = salario
        Empleado.salario_medio.append(salario)
        if dni not in Empleado.lista_dni:
            Empleado.lista_dni.append(dni)
            self.__DNI = dni
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def GetNombre(self):
        return self.__Nombre
    def SetSalario(self, salario):
        self.__Salario = salario
    def GetSalario(self):
        return self.__Salario
    def SetDNI(self, dni):
        if dni not in Empleado.lista_dni:
            Empleado.lista_dni.append(dni)
            self.__DNI = dni
    def GetDNI(self):
        return self.__DNI
    def detalles_empleado(self):
        return f"Nombre: {self.__Nombre}, Salario: {self.__Salario}, DNI: {self.__DNI}"
    def __del__(self):
        print(f"Empleado {self.__Nombre} con DNI {self.__DNI} ha sido eliminado.")
    @classmethod
    def salario_promedio(cls):
        return sum(Empleado.salario_medio) / len(Empleado.salario_medio)

class Gerente(Empleado):
    def __init__(self, nombre, salario, dni, departamento):
        super().__init__(nombre, salario, dni)
        self.__Departamento = departamento
    def SetDepartamento(self, departamento):
        self.__Departamento = departamento
    def GetDepartamento(self):
        return self.__Departamento
    def detalles_empleado(self):
        detalles_base = super().detalles_empleado()
        return f"{detalles_base}, Departamento: {self.__Departamento}"
    def descuento_salario(self):
        descuento = self.GetSalario() * 0.10
        nuevo_salario = self.GetSalario() - descuento
        self.SetSalario(nuevo_salario)
        return nuevo_salario
    @staticmethod
    def impuesto(salario):
        impuesto = salario * 0.21
        return impuesto