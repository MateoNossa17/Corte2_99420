# Getters y setters
# Son metodos que permiten acceder o aignar un valor a los campos de un objertos
# Por ejemplo: "atributo Calificavón =>-1"
# Campo privado 
# "self.__" para no modifcar 



class Persona():
    def __init__(self): #Consturctor
        self.__nombre:str|None=None
        self.__altura:float=0.0
        self.__masa:float=0.0
    #-----------Getters---------------- de volver valores
    def get_name(self):
        return self.__nombre
    def get_altura(self):
        return self.__altura
    def get_masa(self):
        return self.__masa
    #-----------Setters---------------- modificar valores
    def set_name(self,nombre:str):
        self.__nombre=nombre
    def set_altura(self,altura:float):
        self.__altura=altura
    def set_masa(self,masa:float):
        self.__masa=masa

    #-----------Metodo IMC-------------

    def __imc(self): #Pertenece a la clase por ende es un metodo
        imc=(self.__masa)/(self.__altura/100)**2
        if imc <=18.5:
            return str ('Por debajo')
        elif 18.5<imc<24.9:
            return str ('saludable')
        elif 25<imc<29.9:
            return str ('sobrepeso')
        elif 30<imc<34.9:
            return str ('obesidad I')
        elif 35<imc<39.9:
            return str ('obesidad II')
        else:
            return str ('obesidad III')
    def get_imc(self):
        return self.__imc()

def main():
    estudiante_1=Persona()
    estudiante_1.set_name('Pedro Caceres')
    estudiante_1.set_altura(188)
    estudiante_1.set_masa(97)
    estudiante_2=Persona()
    estudiante_2.set_name('Maria Perez')
    estudiante_2.set_altura(160)
    estudiante_2.set_masa(47)
    estudiante_3=Persona()
    estudiante_3.set_name('Julian Dominguez')
    estudiante_3.set_altura(158)
    estudiante_3.set_masa(58)
    estudiante_4=Persona()
    estudiante_4.set_name('Jessica')
    estudiante_4.set_altura(170)
    estudiante_4.set_masa(73)

    print(f'Estuciantes {estudiante_1.get_name()} resultado: {estudiante_1.get_imc()}')
    print(f'Estuciantes {estudiante_2.get_name()} resultado: {estudiante_2.get_imc()}')
    print(f'Estuciantes {estudiante_3.get_name()} resultado: {estudiante_3.get_imc()}')
    print(f'Estuciantes {estudiante_4.get_name()} resultado: {estudiante_4.get_imc()}')
if __name__=='__main__':
    main()
    

