"""
def <nombre_funcion>(parametros):
"""

def say_hello(name):
    print(f"Hello {name}")

say_hello("Juan")

#con valor de retorno
def sum(a, b):
    return a + b

result = sum(1, 2)
print(result)



#return tuplas
def get_user_info():
    name = "Juan"
    lastname = "Perez"
    age = 25
    return name, lastname, age

name, lastname, age = get_user_info()
print(name, lastname, age)


#parametros por nombres
def get_user_info(name, lastname, age):
    print(f"Name: {name}, Lastname: {lastname}, Age: {age}")

get_user_info(age=25, name="Juan", lastname="Perez")


