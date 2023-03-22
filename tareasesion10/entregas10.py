import listaale
import eje1
opc=int(input('Que ejercicio desea ejecutar(ingrese el número): '))
if opc==1:
    eje1.horario()
elif opc==2:
    listaale.listr()
else:
    print('Ingrese un 1 o 2 para ejecutar el ejercicio uno o dos respectivamente')
