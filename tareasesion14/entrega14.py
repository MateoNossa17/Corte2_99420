class Ciudadano():
    def __init__(self,nombre:str,edad:int,documento:int):
            self.__nombre=nombre
            self.__edad=edad
            self.__doc=documento
    def getNombre(self):
        return self.__nombre
    def getEdad(self):
        return self.__edad
    def getCc(self):
        return self.__doc
    def setNombre(self,name:str):
        self.__nombre=name
    def setEdad(self,edad:int):
         self.__edad=edad
    def setDoc(self,documento:int):
         self.__doc=documento
    def legado(self):
        return 'No se va a quedar en el olvido'
class Ingeniero(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, especialidad:str,añosxp:int):
        super().__init__(nombre, edad, documento)
        self.__especialidad=especialidad
        self.__añosxp=añosxp
    def getEspecialidad(self):
        return self.__especialidad
    def getAñosxp(self):
        return self.__añosxp
    def setNombre(self,especialidad:str):
        self.__especialidad=especialidad
    def setEdad(self,añosxp:int):
         self.__añosxp=añosxp
    def logro(self):
         return 'Felicidades por su ingeniería'
class Medico(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, especialización:str,vidass:int):
        super().__init__(nombre, edad, documento)
        self.__especialización=especialización
        self.__vidass=vidass
    def getEspecialización(self):
        return self.__especialización
    def getVidass(self):
        return self.__vidass
    def setNombre(self,especialización:str):
        self.__especialización=especialización
    def setEdad(self,vidass:int):
         self.__vidass=vidass
    def labor(self):
         return 'Gracias por su servicio'
    

class Escritor(Ciudadano):
    def __init__(self, nombre: str, edad: int, documento: int, genero:str,nlibros:int):
        super().__init__(nombre, edad, documento)
        self.__genero=genero
        self.__nlibros=nlibros
    def getGenero(self):
        return self.__genero
    def getNliblos(self):
        return self.__nlibros
    def setGenero(self,genero:str):
        self.__genero=genero
    def setEdad(self,nlibros:int):
         self.__nlibros=nlibros
    def legado(self):
         return 'Va a quedar en la historia con sus historias'
def main():
    profecional1=Ingeniero('Ramón',45,10587459,'Sistemas',15)
    profecional2=Medico('Sara',35,362541987,'Pediatra',10)
    profecional3=Escritor('Gabriel',50,25641397,'Narrativo',5)
    print(f'Su nombre es: {profecional1.getNombre()}\nSu edad: {profecional1.getEdad()}\nSu documento es: {profecional1.getCc()}\nSu profeción es ingeniero y se especializa en {profecional1.getEspecialidad()}\nTiene una experiencia de: {profecional1.getAñosxp()} ')
    print(profecional1.logro())
    print('=====================================================')
    print(f'Su nombre es: {profecional2.getNombre()}\nSu edad: {profecional2.getEdad()}\nSu documento es: {profecional2.getCc()}\nSu profeción es medico y se especializa en {profecional2.getEspecialización()}\nHa salvado {profecional2.getVidass()} vidas ')
    print(profecional2.labor())
    print('=====================================================')
    print(f'Su nombre es: {profecional3.getNombre()}\nSu edad: {profecional3.getEdad()}\nSu documento es: {profecional3.getCc()}\nSu profeción es escritor y se especializa en el genero {profecional3.getGenero()}\nHa escrito {profecional3.getNliblos()} obras literarias')
    print(profecional3.legado())
if __name__=='__main__':
    main()
    
    
        