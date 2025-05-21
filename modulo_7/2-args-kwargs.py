
# * posicion (args) agrupa los valores por posicion en una tupla
# ** nombre (kwargs) agrupa los valores por nombre en un diccionario

def get_user_info(*args, **kwargs):
    print(args)
    print(type(args)) #tuple
    print(kwargs)
    print(type(kwargs)) #dict

get_user_info("Juan", "Perez", "25", name="Juan", lastname="Perez", age=25)
