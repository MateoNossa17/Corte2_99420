# Hrencia y jerarquia  
class Deportista: #Super clase
    def __init__(self,nombre:str,documenteo:int,edad:int):
        self.__name=nombre
        self.__doc=documenteo
        self.__edad=edad

    def get_name(self):
        return self.__name
    def get_doc(self):
        return self.__doc
    def get_edad(self):
        return self.__edad
    
    def set_name(self,name:str):
        self.__name=name
    def set_doc(self,doc:int):
        self._doc=doc
    def set_edad(self,edad:int):
        self.__edad=edad
    # -----------------Sobrecarga---------------------
    def medalla(self):
        return 'Ha ganado una madella'

class DeportistaTenis(Deportista): #Subclase
    def __init__(self,nombre:str,documenteo:int,edad:int,setganadso:int,setperdidso:int):
        super().__init__(nombre,documenteo,edad)
        self.__setsGanados=setganadso
        self.__setsPerdidos=setperdidso
    def get_setsGanados(self):
        return self.__setsGanados
    def get_setsPerdidos(self):
        return self.__setsPerdidos
    def set_setsGanados(self,ganados:int):
        self.__setsGanados=ganados
    def set_setsPerdidos(self,perdidos:int):
        self.__setsPerdidos=perdidos


class DeportistaBasket(Deportista):
    def __init__(self, nombre: str, documenteo: int, edad: int, name_equipo:str,cestas:int):
        super().__init__(nombre, documenteo, edad)
        self.__nombreEquipo=name_equipo
        self.__cestasAnotadas=cestas
    def get_name_equpo(self):
        return self.__nombreEquipo
    def get_golesAnotados(self):
        return self.__cestasAnotadas
    def set_name_equpo(self,nameequi:str):
        self.__nombreEquipo=nameequi
    def set_golesAnorados(self,cestas:int):
        self.__cestasAnotadas=cestas

class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str, documenteo: int, edad: int, name_equipo:str,goles:int):
        super().__init__(nombre, documenteo, edad)
        self.__nombreEquipo=name_equipo
        self.__golesAnotados=goles
    def get_name_equpo(self):
        return self.__nombreEquipo
    def get_golesAnotados(self):
        return self.__golesAnotados
    def set_name_equpo(self,nameequi:str):
        self.__nombreEquipo=nameequi
    def set_golesAnorados(self,goles:int):
        self.__golesAnotados=goles
    def medalla(self):
        return 'Gano la Europa UEFA'

    

 
def main():
    futbolista=DeportistaFutbol('Falcao',13151463131,36,'Seleccion Colombia',35)
    print(f'Deportista: {futbolista.get_name()}\nDocumento: {futbolista.get_doc()}\nEdad: {futbolista.get_edad()}\nEquipo: {futbolista.get_name_equpo()}\nGoles: {futbolista.get_golesAnotados()}\nMedalla: {futbolista.medalla()}')
    futbolista2=Deportista('Alguien',31515613115315,68)
    print(f'Deportista: {futbolista2.get_name()}\nDocumento: {futbolista2.get_doc()}\nEdad: {futbolista2.get_edad()}')

if __name__=='__main__':
    main()