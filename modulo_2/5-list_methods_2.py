#copy

my_list = [1, 2, 3, 4, 5]

my_list_copy = my_list.copy()

my_list_copy[0] = "Juanito" #reemplaza el primer elemento de la lista

print(my_list)
print(my_list_copy)

#reverse (modifica la lista original)

my_list = [1, 2, 3, 4, 5]

my_list.reverse()

print(my_list)

#sort ascendente (modifica la lista original)

my_list = [5, 4, 3, 2, 1]

my_list.sort()

print(my_list)

#sort descendente (modifica la lista original)

my_list = [5, 4, 3, 2, 1]

my_list.sort(reverse=True)

print(my_list)


