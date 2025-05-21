
person = {
    'name': 'Juan',
    'lastname': 'Perez',
    'age': 25,
    'courses': ['Python', 'Django', 'Flask'],
    'settings': (123, True, 'Hola')
}

#longitud del diccionario
print(
    len(person)
)

person['age'] = 26

print(person)

#agregar valores
person['nueva_llave'] = 'Hola'

print(len(person))
print(person)

#update llaves que queremos actualizar
person.update({
    'name': 'Juancito',
    'lastname': 'Rodriguez',
})

print(person)

# set default, devuelve el valor de la llave si existe, si no existe, lo agrega y devuelve el valor
id = person.setdefault('id', 123)

print(person)
print(id)

# si no existe la llave, devuelve el valor por defecto
settings = person.get('settings', ())

print(settings)

#eliminar valores

del person['settings']

print(person)

#pop, elimina el ultimo elemento y lo retorna
value = person.pop('age')

print(value)
print(person)

#popitem, elimina el ultimo elemento y lo retorna
value = person.popitem()

print(value)
print(person)

#limpiar el diccionario
person.clear()

print(person)