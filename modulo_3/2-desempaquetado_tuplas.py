
courses = (
    "python",
    "django",
    "flask",
    "sqlalchemy",
    "nosql"
)

#desempaquetado de tuplas

var1 = courses[0]
var2 = courses[1]
var3 = courses[2]
var4 = courses[3]
var5 = courses[4]

print(var1, var2, var3, var4, var5)

#otra forma de desempaquetar una tupla
course1, course2, course3, course4, course5 = courses

print(course1, course2, course3, course4, course5)

#desempaquetado de tuplas con _ (omitir un valor)

course1, course2, course3, course4, _ = courses

print(course1, course2, course3, course4)

#desempaquetado de tuplas con * (recibir varios valores)

course1, *courses_rest = courses

print(course1)
print(courses_rest)




