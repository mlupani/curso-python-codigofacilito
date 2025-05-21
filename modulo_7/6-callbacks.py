def saludar(callback, *args, **kwargs):
    nombre = args[0] if args else kwargs.get("nombre")
    if nombre is None:
        callback("Invitado")
    else:
        callback(nombre)

saludar(lambda nombre: print(f"Hola, {nombre}!"), "Juan")
saludar(lambda nombre: print(f"Adiós, {nombre}!"), name=None)
