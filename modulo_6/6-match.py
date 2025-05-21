# match es como el switch de otros lenguajes

score = 100

match score:
    case 100:
        print('El score es 100')
    case 200:
        print('El score es 200')
    case 300 | 400:
        print('El score es 300 o 400')
    case _:
        print('El score no es 100 o 200')




