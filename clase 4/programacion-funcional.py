def mi_mensaje(f):
    def wrapper():
        print("Estan funcion esta por comenzar")
        f()
        print("Mi funcion ha terminado")
    return wrapper

@mi_mensaje
def hola():
    for miNumero in range(3):
        print(miNumero)

hola()