# Polimorfismo: objetos puede tener muchas formas 
class Ciudadano():
    def __init__(self,idioma:str,nombre:str):
        self.__idioma=idioma
        self.__nombre=nombre
    def get_idioma(self):
        return self.__idioma
    def get_nombre(self):
        return self.__nombre
    def set_idioma(self,idioma:str):
        self.__idioma=idioma
    def set_nombre(self,nombre:str):
        self.__nombre=nombre
    def saludo(self):
        return 'Quoi de Beau!' 
    
class Colombia(Ciudadano):
    def __init__(self, idioma: str, nombre: str,cc:int):
        super().__init__(idioma, nombre)
        self.__cc=cc
    def get_cc(self):
        return self.__cc 
    def set_nombre(self,cc:int):
        self.__cc=cc
    def saludo(self):
        return 'Buenas tardes' 
    

class Ingles(Ciudadano):
    def __init__(self, idioma: str, nombre: str,id:int):
        super().__init__(idioma, nombre)
        self.__id=id
    def get_cc(self):
        return self.__id
    def set_nombre(self,id:int):
        self.__id=id
    def saludo(self):
        return 'Hello' 
class China(Ciudadano):
    def __init__(self, idioma: str, nombre: str,shengfenzheng:int):
        super().__init__(idioma, nombre) 
        self.__shengfenzheng=shengfenzheng
    def get_shengfenzheng(self):
        return self.__shengfenzheng
    def set_shengfenzheng(self,shengfenzheng:int):
        self.__shengfenzheng=shengfenzheng       
    def saludo(self):
        return 'NiGanMaYa!!' 

def dar_saludo(obj:Ciudadano):
    return obj.saludo()

def main():
    p1=Colombia('Español','H',1025478548)
    p2=Ingles('Ingles','A',64648678548)
    p3=China('Mandarin','J',61365478548)
    p4=Ciudadano('Frances','c')
    print(dar_saludo(p1))
    print(dar_saludo(p2))
    print(dar_saludo(p3))
    print(dar_saludo(p4))


if __name__ =='__main__':
    main()
