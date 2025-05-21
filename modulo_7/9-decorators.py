# A(B) -> C
# A es la funcion original (func)
# B es la funcion decoradora (decorator)
# C es la funcion decorada (wrapper)


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes de la funcion")
        result = func(*args, **kwargs)
        print("Despues de la funcion")
        return result
    return wrapper


@decorator
def saludo(nombre):
    return print(f"Hola, {nombre}!")


saludo("Juan")
