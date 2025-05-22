#generador de fibonacci

def generador_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

generador = generador_fibonacci(10)

for numero in generador:
    print(numero)

# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))
# print(next(generador))

