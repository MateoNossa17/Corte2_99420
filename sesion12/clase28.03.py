# Tipos de archivos:
#Archivos de texto: texto .txt / XML .xml / de intercambio de inoformacion .jmson
#archivos binarios: PDF .pdf / imagea / video

#Manejo de archivos:
# f=open(<NOmbre del archivo>,'rt')
# rstrip(<caracteres finales>)
# 'r'= Read
# 'a'= append /crea el archivo si no existe escribe al final del archivo
# 'w'= write (abre el archivo para escribir)
# 'x' = crea un archivo
# rstrip //elimina lo que le da el prametro
# split // crea una lista cuando encuentra una 
# 
import buscar
def main():
    dicc={}
    f=open('matrizAsignacion.txt','rt')
    #matriz = f.read()# Lee todo el  archivo
    matriz=f.readlines() #Lee la primera linea
    f.seek(0)
    print(len(matriz))
    #matriz=f.readlines() #cada linea en una listqa

    for i in range(len(matriz)):
        valor=f.readline().rstrip('\n').split(',')
        for j in range(len(valor)):
            pos= str(f'{i}{j}')
            dicc[pos]=valor[j]
    print(dicc)
    f.close()
    buscar.b(dicc)
    #print(f'La posición 4,3 es {dicc["43"]}')
    

if __name__=='__main__':
    main()
