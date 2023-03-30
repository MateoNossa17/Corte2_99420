# Programcion orientada objetos:
#  Clase y objetos 
# inastacnias , atributo , metodo 
#  class un molde misma forma ; atributos (campos) por ejemplo la forma de vestir; metodos acciones lo que puede hacer
# instancia invocacion 
# self == llama asi mismo
class Persona(): 
    def __init__(self):
        self.nombre:str|None=None
        self.apellido:str|None=None
        self.edad:int|None=None
        self.frase:str|None=None
    def speak(self):
        return self.frase

def main():
    estudiante=Persona()
    estudiante.nombre='Mateo'
    estudiante.apellido='Nossa'
    estudiante.edad=19
    estudiante.frase='Dedo estudiar'

    futbolista=Persona()
    futbolista.nombre='Radamel'
    futbolista.apellido='García'
    futbolista.edad=36
    futbolista.frase='Gol'

    print(estudiante.speak())
    print(futbolista.speak())





if __name__=='__main__':
    main()
