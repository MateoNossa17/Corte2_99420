def mayor(l):
    new_list=l.copy()
    new_list.sort()
    print(f'El numero mayor es de la lista es: {new_list[-1]}')
if __name__=="__main__":
    list_p=[1,2,6,99]
    mayor(list_p)