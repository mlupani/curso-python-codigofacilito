
#generador de procesar archivo grande
def procesar_archivo_grande(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip() #elimina el salto de linea al final de cada linea



generador = procesar_archivo_grande('archivo_grande.txt')

for linea in generador:
    print(linea)
