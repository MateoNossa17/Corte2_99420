import cal 
import ejercicio1
def main():
    e=int(input("Ingrese el ejercicio que desa ver: "))
    if e==1:
        ejercicio1.eje1()
    elif e==2:
        cal.calc()
    else:
        print('Ingrese 1 o 2 para ver el ejercicio uno y dos respectivamente')
if __name__=='__main__':
    main()
