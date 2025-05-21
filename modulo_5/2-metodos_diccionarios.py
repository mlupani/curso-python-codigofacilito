#keys, values, items

person = {
    'name': 'Juan',
    'lastname': 'Perez',
    'age': 25,
    'courses': ['Python', 'Django', 'Flask'],
    'settings': (123, True, 'Hola')
}

print(
    person.keys()
)

#para tener una lista de keys
print(
    list(person.keys())
)

#para tener una tupla de keys
print(
    tuple(person.keys())
)

#para tener una lista de values
print(
    list(person.values())
)

#items

print(
    person.items()
)

print(
    list(person.items())
)
