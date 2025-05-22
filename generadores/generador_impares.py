
#generador de impares
def generador_impares(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

generador = generador_impares(10)

for numero in generador:
    print(numero)

#breve explicacion de los generadores
#los generadores son funciones que generan valores sobre la marcha
#son mas eficientes que las funciones normales
#son mas faciles de leer que las funciones normales
#son mas faciles de entender que las funciones normales

