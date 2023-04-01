
def b(dicc):
    n=''
    while n!='salir':
        n=input('Ingrese el alimento que quiera saber el valor base y su iva (escriba "salir" para termina): ')
        if n=='salir':
            break
        else: 
            v=float(input('Ingrese el valor neto del producto del mercado actual: '))
            iv=dicc[n]*v
            print(f'\nEl valor base del producto "{n}" es: {v-iv}\nEl valor del IVA es: {iv}')