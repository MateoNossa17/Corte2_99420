# Crealcion de listas Bidimensional
#  Dos dimenciones (Ranglones x columnas)
#     i=Rengloes y j=Columnas
""" import random as r

def matris(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=r.randint(1,10)
            matriz[i].append(num)
    return matriz
def es(ma,n):
    for i in ma:
        for j in range(len(i)):
            i[j]=n*i[j]
    print(ma)


def app():
    i=int(input('Ingrese el número de filas: '))
    j=int(input('Ingrese el número de columnas: '))
    matriz=matris(i,j)
    print(matriz)
    n= int(input('Ingrese un número para escalar la matriz: '))
    es(matriz,n)
if __name__=='__main__':
    app() """
# Función recursiva es capas de llamarse a si misma:

""" def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)
    else:
        print(f'Finalizo {x}')
if __name__=='__main__':
    imprimir(5) """
def impar(x):
    if x<=0:
        return 0
    else:
        num=(2*x-1) + impar(x+1)
        return num
def app():
    n=int(input('Cuantos numeros desea generar'))
    for i in range(n):
        valor=impar(i)
        print(valor, end=' ')
if __name__=='__main__':
    app()
