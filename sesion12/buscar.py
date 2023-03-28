def b(dicc):
    n=('')
    while n!='salir':
        n=input('Ingrese ')
        if n=='salir':
            break
        elif n not in dicc:
            print('error, fuerda de rango')
        else:
            print(dicc[n])