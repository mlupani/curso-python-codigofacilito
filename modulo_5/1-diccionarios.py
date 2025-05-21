#clave: valor

person = {
    'name': 'Juan',
    'lastname': 'Perez',
    'age': 25,
    'courses': ['Python', 'Django', 'Flask'],
    'settings': (123, True, 'Hola')
}

print(person)

print(person['name'])

print('name' in person)

print('passowrd' in person)

print(person.get('name'))

print(person.get('password')) #si no existe, devuelve none

print(person.get('password', 'No existe el password')) #si no existe, devuelve el valor que le pasamos, (fallback)

person['nueva_propiedad'] = 'Hola'

print(person)

person.pop('nueva_propiedad')

print(person)

person.popitem()

print(person)
