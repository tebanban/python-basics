class Humano:
    def __init__(self, edad):
        self.edad=edad

    def hablar(self,mensaje):
        print (mensaje)



class Arquitecto(Humano):
    def __init__(self, casas):
        print ('Debo construir una ', casas)

pedro = Humano(25)

print('Soy pedro y tengo', pedro.edad)

pedro.hablar('Hola Pedro')