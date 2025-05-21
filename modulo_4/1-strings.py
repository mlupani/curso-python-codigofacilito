
string = "Hello, world!"

#len
print(len(string))

#encontrar un elemento en la cadena
print(string.find("o"))

print('Hello' in string)

#reemplazar un elemento en la cadena
print(string.replace("world", "python"))

#leer en indice
print(string[0])
print(string[-1])

#slicing
print(string[0:5])
print(string[6:])
print(string[:5])
print(string[::2])

#shallow copy
string_2 = string[:]
print(string_2)

# el string es inmutable, no se puede cambiar el valor de un elemento
# string[0] = 'H'
# print(string)





