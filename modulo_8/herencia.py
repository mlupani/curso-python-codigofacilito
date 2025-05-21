

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy una persona"



class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #llamo al constructor de la clase padre
        self.sueldo = sueldo

    #sobreescribo el metodo de la clase padre
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y gano {self.sueldo} pesos"


#herencia multiple
# class Jefe (Persona, Empleado):
#     def __init__(self, nombre, edad, sueldo, departamento):
#         super().__init__(nombre, edad, sueldo)
#         self.departamento = departamento

#     def saludar(self):
#         return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y gano {self.sueldo} pesos y soy el jefe de {self.departamento}"


persona_1 = Persona("Juan", 25)
empleado_1 = Empleado("Juan", 25, 100000)
# jefe_1 = Jefe("Juan", 25, 100000, "IT")

print(persona_1.saludar())
print(empleado_1.saludar())
# print(jefe_1.saludar())

