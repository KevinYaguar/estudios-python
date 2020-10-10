class Argentina():
    def capital(self):
        print("CABA")
    def idioma(self):
        print("Español")

class EEUU():
    def capital(self):
        print("Wachinton DC")
    def idioma(self):
        print("Inglés")
paisArgentina = Argentina()
paisEEUU = EEUU()

for unPais in (paisArgentina, paisEEUU):
    unPais.capital()
    unPais.idioma()