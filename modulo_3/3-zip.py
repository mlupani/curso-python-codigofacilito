
#zip

my_list = [1, 2, 3, 4, 5]
my_tuple = ("Juan", "Perez", "Gomez")
my_set = {"python", "django", "flask"}


my_zip = zip(my_list, my_tuple, my_set)

print(my_zip)
print(type(my_zip))

# lista de tuplas
response = list(my_zip)
print(response)

# tupla de tuplas
response_2 = tuple(my_zip)
print(response_2)




