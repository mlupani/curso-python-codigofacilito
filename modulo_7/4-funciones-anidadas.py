def outer_function():
    x = "Hello dese el scope de outer_function"

    def inner_function():
        #nonlocal x
        x = "hola dese el scope de inner_function"
        print(x)

    inner_function()

outer_function()
