import orden_datos
import orden_datos_pais
def main():
    p=''
    while p!=0:
        p=int(input('Indice del país de busqueda (escriba "0" para terminar la busqueda): '))
        if 1<=p<=243:
            c=orden_datos.orden(p)
            orden_datos_pais.pais(c)
        elif p==0:
            break
        else:
            print('Ingrese datos validos. (1 a 243)')
if __name__=='__main__':
    main()
