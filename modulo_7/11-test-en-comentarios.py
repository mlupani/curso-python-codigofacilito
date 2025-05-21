#los docstrings son para documentar el codigo, van en la primera linea de la funcion
#los tests van despues de los docstrings

def test(a, b):
    """
    Esta funcion recibe dos parametros y retorna la suma de ambos
    args:
        - a: int
        - b: int
    returns:
        - int


    >>> test(1, 2)
    3

    >>> test(2, 2)
    4
    """
    return a + b


#print(test(1, 2))
#python -m doctest 11-test-en-comentarios.py -> llamamos al modulo doctest para ejecutar los tests
