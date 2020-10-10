class Ave():
    def introduccion(self):
        print("Existen muchos tipos de aves")
    def vuelo(self):
        print("Algunas aves pueden volar y otras no")

class perico(Ave):
    def vuelo(self):
        print("Los pericos pueden volar")

class pinguinos(Ave):
    def vuelo(self):
        print("Los pingüinos no pueden volar")

unAve = Ave()
unPerico = perico()
unPinguino = pinguinos()

unAve.introduccion()
unAve.vuelo()

unPerico.introduccion()
unPerico.vuelo()

unPinguino.introduccion()
unPinguino.vuelo()

