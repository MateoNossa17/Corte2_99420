def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
def primos(l):
    np=[]
    for i in l:
        x=i
        if es_primo(x)==True:
                np.append(x)        
    print(f'Los números primos de la lista son: \n{np}')
if __name__=='__main__':
    listp=[1,4,7,91,23]
    primos(listp)