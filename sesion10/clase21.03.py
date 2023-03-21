# Listas metodos:
# append() inserta un elemento el  final de la lista 
# insert() insertar un elemento en un indice aspecifico 
# clear() Borra todos los elemtos de la lista 
# remove() elimina el primer elemento que sea igual a el numero dado.
# index() indica la ubicaion del dato el primero
""" 
listM=[]

listM.append(7)# agrega el dato a el final de la lista
listM.append(1)
listM.append('Hola')
listM.insert(0,1)# Indice y variable; indice donde va ubicado/ variable dato
# listM.clear()# Limpia la lista
listM.remove(7)
print(listM) """
milista=[3,5,7,5]
opc=''
while opc!='salir' :
    opc=input('Que quiere hacer: ')
    if opc=='agragar':
        dato=int(input('Cual dato quiere agregar: '))
        milista.append(dato)
        print(milista)
    elif opc=='borrar':
        dato=int(input('Cual dato quiere borrar: '))
        milista.remove(dato)
        print(milista)
    elif opc=='Buscar':
        dato=int(input('Cual dato quiere buscar: '))
        pos=milista.index(dato)
        print(f'el indice es {pos}')
    elif opc=='insertar':
        dato=int(input('Cual dato quiere insertar: '))
        idx=int(input('Ingrese un indice: '))
        milista.insert(idx,dato)
        print(milista)
    elif opc=='limpiar':
        milista.clear()
        print(milista)
    elif opc=='pop':
        ind=int(input('Ingrese el indice: '))
        x=milista.pop(ind)
        print(x)
    elif opc=='tamaño':
        print(len(milista))
    elif opc=='comparar':
        print(f'El valor maximo es: {max(milista)} \n El minimo es: {min(milista)}')
    elif opc=='contar':
        c=int(input('Que dato desea sabar la cantidad: '))
        print(milista.count(c))
    elif opc=='suma':
        print(f'La suma de la lista es {sum(milista)}')
    elif opc=='Existe':
        k=int(input('Que datos dasea saber si hay en la lista: '))
        print(k in milista)
    elif opc=='extender':
        n=[1,2,3,4]
        milista.extend(n)
        print(milista)
    elif opc=='ascender':
        milista.sort()
        print(milista)
    elif opc=='desender':
        milista.reverse()
        print(milista)
