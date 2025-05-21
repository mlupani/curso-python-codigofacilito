
#for each & while

numbers = [1, 2, 3, 4, 5]

#usamos el for each e interpolacion de strings
for number in numbers:
    print(f'El numero es {number}')

#usamos el for en un diccionario
person = {
    'name': 'Juan',
    'age': 20,
    'city': 'Madrid'
}

#aplicamos el for y el desempaquetado de tuplas
for key, value in person.items():
    print(f'la llave es {key} y el valor es {value}')





