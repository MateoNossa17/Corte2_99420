import math as m
def rad(x):
    r=x*m.pi/180
    return r
def calc():
    x=float(input('Ingrese el valor que quiera calcular: '))
    b=input('Ingrese la funcion que desea realizar:\n1.Seno\n2.Coseno\n3.Tangente\n4.Exponencial\n5.Logaritmo natural\n')
    if b=='seno' or b=='Seno':  
        s=m.sin(rad(x))
        print(f'El Seno de {x} es: {s}')
    elif b=='Coseno' or b=='coseno':    
        c=m.cos(rad(x))
        print(f'El coseno de {x} es: {c}')
    elif b=='Tangente' or b=='tangente':
        t=m.tan(rad(x))
        print(f'La tangente de {x} es: {t}')
    elif b=='exponencial' or b=='Exponencial':
        e=m.exp(x)
        print(f'La exponecial de {x} es: {e}')
    elif b=="Logaritmo natural" or b=='logoritmo natural':
        l=m.log(x)
        print(f'El logaritmo natural de {x} es: {l}')
    else:
        print('Datos fuera de los estipulados, verifique la entrada.')

if __name__=="__main__":
    calc()
