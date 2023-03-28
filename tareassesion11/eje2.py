def pro(n,p):
    if n==0:
        return 0
    else:
        num=n*p+pro(n-1,p)
        return num
n=int(input('Ingrese el valor de n para la progresión: '))
p=int(input('Ingrese el valor de p para la progresión: '))
print(f'El resultado de la progresión con {n} y {p} es : {pro(n,p)}')
