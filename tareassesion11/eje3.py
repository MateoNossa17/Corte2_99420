def fac(x):
    if x<=0:
        return 1
    else:   
        f=x*fac(x-1)
        return f
x=int(input('Ingrese el número para saber cual es el factorial: '))
print(f'El factorial de {x} es: {fac(x)}')
