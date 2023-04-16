class Ciudadano():
    def __init__(self,nombre:str,edad:int,cc:int):
        self.__name=nombre
        self.__edad=edad
        self.__cc=cc
    def get_name(self):
        return self.__name
    def get_edad(self):
        return self.__edad
    def get_cc(self):
        return self.__cc
    def set_name(self,name:str):
        self.__name=name
    def set_edad(self,edad:int):
        if edad<0:
            self.__edad='La edad debe ser mayor a cero'
        else:
            self.__edad=edad
            
    def set_cc(self,cc:int):
        if 1000000>cc or cc>9999999999:
            self.__cc='Debe tener de 8 a 10 digitos'
        else:
            self.__cc=cc
    def __mostrar(self):
        return print(f'Nombre:{self.__name} -Edad:{self.__edad} -CC:{self.__cc}')
    
    def __esMayorDeEdad(self):
        if self.__edad>=18:
            return print(f'Es mayor de edad')
        else:
            return print(f'Es menor de edad')
    def getMostrar(self):
        if self.__name==None or self.__edad==None or self.__cc==None:
            return print('Ingrese datos validos')
        else:
            self.__mostrar()
    def getEsMayorDeEdad(self):
        if self.__edad==None:
            return print('Ingrese un valor para la edad')
        else:
            self.__esMayorDeEdad()

def main():
    persona=Ciudadano('Nicolás',28,1289384734)
    persona.set_name('Nicolás')
    persona.set_edad(28)
    persona.set_cc(1289384734)
    persona.getMostrar()
    persona.getEsMayorDeEdad()
if __name__=='__main__':
    main()