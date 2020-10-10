class Tomate():
    def tipo(self):
        print("Vegetal")
    def color(self):
        print("Rojo")


class Manzana():
    def tipo(self):
        print("fruta")
    def color(self):
        print("Rojo")

def func(obj):
    obj.tipo()
    obj.color()

unTomate = Tomate()
unaManzana = Manzana()

func(unTomate)
func(unaManzana)