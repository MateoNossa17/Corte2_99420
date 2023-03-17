#TUPLAS
""" 
def main(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)#El resto de los elementos
    print(kwargs)#Genera los parametros definidos crea un diccionario 
if __name__=="__main__":
    main(1,2,3,4,5,j=20,m=10) """

#Libreria numeros aleatorios 
import random as rand #Importa numeros aleatorios 
for i in range(5):
    numero=rand.randint(10,20)
    real=round(rand.uniform(10,20),4)#round redondea al el numero final/ el uniform numeors flotantes
    letras=rand.choice('Mateo')#Imprime letras aleatorias del ingresado
    print(numero, end=' ')
    print(real, end=' ')
    print(letras, end='\n')