
def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}!"


def saludo(nombre):
    return saludar(nombre)

def despedida(nombre):
    return despedir(nombre)


print(saludo("Juan"))
print(despedida("Juan"))

