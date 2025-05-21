
#scope 
#global y local

name = "Juan" #global

def say_hello():
    #global name = 'juancito' #global
    name = "Juancito" #local
    print(f"Hello {name}")

say_hello()

print(name)




