class estudiante():
    def __init__(self,nombre:str,edad:int):
        self.__nombre=nombre
        self.setEdad(edad)
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def setNombre(self,nombe:str):
        self.__nombre=nombe
    def setEdad(self,edad:int):
        if edad<=0:
            self.__edad=''
        else:
            self.__edad=edad 
def main():
    x=''
    listaestu=[]
    while x!='salir':
        x=input('Ingrese el nombre: ')
        if x=='salir':
            break
        else:
            n=int(input('Ingrese edad: '))
            estu=estudiante(x,n)
            listaestu.append(estu)
    print(listaestu[0].getNombre())
    print(listaestu[0].getEdad())
    print(listaestu[1].getNombre())
if __name__=='__main__':
    main() 
    