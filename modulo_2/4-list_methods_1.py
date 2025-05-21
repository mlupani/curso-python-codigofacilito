#append

my_list = [1, 2, 3, 4, 5]

my_list.append(6)
my_list.append(7)

print(my_list)

#insert

my_list = [1, 2, 3, 4, 5]

my_list.insert(0, 0)
my_list.insert(3, 3.5)

print(my_list)

#extend

my_list = [1, 2, 3, 4, 5]

my_list.extend([6, 7, 8, 9, 10])

print(my_list)

#in

my_list = [1, 2, 3, 4, 5]

print(6 in my_list)
print(6 not in my_list)

#index

my_list = [1, 2, 3, 4, 5]

print(my_list.index(3))

#remove

my_list = [1, 2, 3, 4, 5]

my_list.remove(3)

print(my_list)

#pop

my_list = [1, 2, 3, 4, 5]

last_item = my_list.pop() # by default removes the last item

first_item = my_list.pop(0) # removes the first item


print(last_item)
print(first_item)
print(my_list)

#clear

my_list = [1, 2, 3, 4, 5]

my_list.clear()

print(my_list)
