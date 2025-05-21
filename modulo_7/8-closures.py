#funciones anidadadas o nested functions que retornan funciones y tienen memoria de la variable local

def multiply(number):
    def multiply_by(n):
        return number * n
    return multiply_by

print(f"El resultado de la multiplicación es: {multiply(2)(4)}")
