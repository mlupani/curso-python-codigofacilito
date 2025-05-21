#1 +

name = "Juan"
lastname = "Perez"

print(name + " " + lastname)

#2 join

name = "Juan"
lastname = "Perez"

print(" ".join([name, lastname]))

#3 %s

name = "Juan"
lastname = "Perez"

print("El nombre es %s y el apellido es %s" % (name, lastname))

#4 format (usando placeholders)

name = "Juan"
lastname = "Perez"
base = "El nombre es {} y el apellido es {}"

print(base.format(name, lastname))

#5 format (usando indices)

name = "Juan"
lastname = "Perez"
base = "El nombre es {0} y el apellido es {1}"

print(base.format(name, lastname))

#6 format (usando variables)

name = "Juan"
lastname = "Perez"
base = "El nombre es {name} y el apellido es {lastname}"

print(base.format(name=name, lastname=lastname))

#7 f-string

name = "Juan"
lastname = "Perez"

print(f"El nombre es {name} y el apellido es {lastname}")



