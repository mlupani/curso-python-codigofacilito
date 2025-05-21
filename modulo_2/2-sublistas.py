
#slicing [desde:cuantos]
my_list = ["Juan", "Perez", 20, "Juancito", "Lopez", 30]

print(my_list)

new_list = [
    my_list[0],
    my_list[1],
    my_list[2],
]

print(new_list)

#lo haremos con slicing

new_list = my_list[0:3]

print(new_list)

new_list = my_list[3:6]

print(new_list)

#podemos obviar el inicio

new_list = my_list[:3]

print(new_list)

#podemos obviar el final

new_list = my_list[3:]

print(new_list)

#shallow copy

my_list = ["Juan", "Perez", 20, "Juancito", "Lopez", 30]

my_list_copy = my_list[:]

my_list_copy[0] = "Juanito"

print(my_list)
print(my_list_copy)


#skips (opcional)

my_list = ["Juan", "Perez", 20, "Juancito", "Lopez", 30]

print(my_list[::2])

#reverse

my_list = ["Juan", "Perez", 20, "Juancito", "Lopez", 30]

print(my_list[::-1])




