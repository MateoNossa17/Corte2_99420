class Articulos:
    def __init__(self, id:int, precio_base:float, unid_existencia:int):
        self.__id = id
        self.__precio_base = precio_base
        self.__unid_existencia = unid_existencia
    def get_id(self):
        return self.__id
    def get_precio_base(self):
        return self.__precio_base
    def get_unid_existencia(self):
        return self.__unid_existencia
    def set_precio_base(self, precio_base:float):
        self.__precio_base = precio_base
    def set_unid_existencia(self, unid_existencia:int):
        self.__unid_existencia = unid_existencia
    def set_id(self,id:int):
        self.__id=id
    def precio_final(self):
        pass
class Bebidas(Articulos):
    def __init__(self, id: int, precio_base: float, unid_existencia: int,canUnidad:str,proveedor:str):
        super().__init__(id, precio_base, unid_existencia)
        self.__canUnidad = canUnidad
        self.__proveedor = proveedor
    def getCanUnidad(self):
        return self.__canUnidad
    def getProveedor(self):
        return self.__proveedor
    def setCanUnidad(self, canUnidad:str):
        self.__canUnidad = canUnidad
    def setProveedor(self, proveedor:str):
        self.__proveedor = proveedor
    def precio_final(self):
        pass
class Lacteos(Articulos):
    def __init__(self, id: int, precio_base: float, unid_existencia: int,canUnidad:str,proveedor:str):
        super().__init__(id, precio_base, unid_existencia)
        self.__canUnidad = canUnidad
        self.__proveedor = proveedor
    def getCanUnidad(self):
        return self.__canUnidad
    def getProveedor(self):
        return self.__proveedor
    def setCanUnidad(self, canUnidad:str):
        self.__canUnidad = canUnidad
    def setProveedor(self, proveedor:str):
        self.__proveedor = proveedor
    def precio_final(self):
        pass
class Condimentos(Articulos):
    def __init__(self, id: int, precio_base: float, unid_existencia: int,canUnidad:str,proveedor:str):
        super().__init__(id, precio_base, unid_existencia)
        self.__canUnidad = canUnidad
        self.__proveedor = proveedor
    def getCanUnidad(self):
        return self.__canUnidad
    def getProveedor(self):
        return self.__proveedor
    def setCanUnidad(self, canUnidad:str):
        self.__canUnidad = canUnidad
    def setProveedor(self, proveedor:str):
        self.__proveedor = proveedor
    def precio_final(self):
        pass
f=open('Catalogo.csv','rt')
n=f.readline()
f.seek(0)
line=f.readlines()
listaLacteos=[]
listaCondimentos=[]
listaBebidas=[]
for i in line:
    va=i.rstrip('\n').split(',')
    if va[5]=='PrecioUnidad':
        pass
    elif va[3]=='Bebidas':
        x=va[5].rstrip('USD')
        a=Bebidas(int(va[0]),float(x),int(va[6]),va[4],va[2])
        listaBebidas.append(a)
    elif va[3]=='Condimentos':
        x=va[5].rstrip('USD')
        a=Bebidas(int(va[0]),float(x),int(va[6]),va[4],va[2])
        listaCondimentos.append(a)
    else:
        x=va[5].rstrip('USD')
        a=Bebidas(int(va[0]),float(x),int(va[6]),va[4],va[2])
        listaLacteos.append(a)
item=''
lisab=[]
lisac=[]
lisaL=[]
while item!='fin':
    item=input('Ingrese el id del producto: ')
    if item=='fin':
        break
    else: 
        for i in range(len(listaBebidas)):
            if int(item) == listaBebidas[i].get_id():
                if listaBebidas[i].get_unid_existencia() <=0:
                    print('No hay')
                    break
                listaBebidas[i].set_unid_existencia(listaBebidas[i].get_unid_existencia()-1)
                lisab.append(listaBebidas[i].get_precio_base())

        for i in range(len(listaLacteos)):
            if int(item) == listaLacteos[i].get_id():
                lisaL.append(listaLacteos[i].get_precio_base())
                if listaLacteos[i].get_unid_existencia() <=0:
                    print('No hay')
                    break
                listaLacteos[i].set_unid_existencia(listaLacteos[i].get_unid_existencia()-1)
                lisab.append(listaLacteos[i].get_precio_base())

        for i in range(len(listaCondimentos)):
            if int(item) == listaCondimentos[i].get_id():
                if listaCondimentos[i].get_unid_existencia() <=0:
                    print('No hay')
                    break
                listaCondimentos[i].set_unid_existencia(listaCondimentos[i].get_unid_existencia()-1)
                lisab.append(listaCondimentos[i].get_precio_base())   
print(f'Los lacteos que compro son: {len(lisaL)} y tiene un costo {sum(lisaL)} USD')
print(f'Los Condimentos que compro son: {len(lisac)} y tiene un costo {sum(lisac)} USD')
print(f'Los Bebidas que compro son: {len(lisab)} y tiene un costo {sum(lisab)} USD')
print(f'El costo total de la compra es : {sum(lisab)+sum(lisac)+sum(lisaL)} USD')