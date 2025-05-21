
""""
class NombreClase
"""

class Persona:

    #atributos de clase
    _password: str = None #privado pero para nosotros ya que en python no existe el concepto de privado
    #__password: str = None #privado real

    #constructor
    def __init__(self, nombre, edad):
        #atributos de instancia
        self.nombre = nombre
        self.edad = edad

    #si no agrego el setter, el atributo es de solo lectura
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        #logica para validar el password
        self._password = password

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"



persona_1 = Persona("Juan", 25)
persona_2 = Persona("Maria", 30)

print(persona_1.saludar())
print(persona_2.saludar())

#sobreescribo el atributo de clase password
persona_1.password = "123456"

print("el password de la persona 1 es:", persona_1.password)
print("el password de la persona 2 es:", persona_2.password)


