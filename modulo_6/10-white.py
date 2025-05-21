import random

#while

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print('El bucle ha terminado')


#ejemplo

random_number = random.randint(1, 10)
number = None
hits = 0

while number != random_number and hits < 3:
    number = int(input('Adivina el numero: '))
    hits += 1

    if number == random_number:
        print(f'¡Felicidades! Has adivinado el numero {random_number}')
    else:
        print('El numero es incorrecto')

if hits == 3:
    print(f'¡Game over! Has perdido. El numero era {random_number}')





