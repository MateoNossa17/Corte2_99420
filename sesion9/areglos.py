#cadena de texto
""" cadena='Hola Mundo!'
print(cadena[3])
print(len(cadena))#da el tamaño de la letra se caracteres CUENTA DESDE 1 """
#ARREGLOS DE DATOS [] inicia en 1
#unidimencion: SOLO VECTORES UN FILA MUCHAS COLUMNA
#se oude hacerder con el ciclos for
#tipo de datos
#Es fijo
#bidimencional: matrices
#Primero fila=horizontal columno=vertical
#Listas: distintos tipos de datos, {} inicia desde cero 0, se pueden modificar
""" cadena='Hola Mundo!'
print(cadena[3])
print(len(cadena))
texto=''
#Accediendo con un for
for i in cadena:
    texto+=str(f'{i},')
    print(texto)
#Accediendo con un while
contador=0
texto2=''
while contador<len(cadena):
    texto2+=str(f'{cadena[contador]},')
    contador+=1
print(texto2) """
n=input('Ingrese un número: ')
dimencion=len(n)
i5=0
if 2<dimencion<8:
    for i in n:
        if i=='5':
            print('Salto')
            i5+=1
        else:
            print(i)
    print(f'Los números iguales a 5 es: {i5}')
    print(f'Los números distintos a 5 es: {dimencion-i5}')
    print(f'Total de digitos : {dimencion}')
else:
    print('error, fuera de rango')