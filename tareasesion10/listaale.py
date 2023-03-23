import random as r
import funm
import funpr
def listr():     
    listar=[]
    for i in range(10):
        n=r.randint(1,50)
        listar.append(n)
    print(f'La lista aleatoria es: \n{listar}')
    funm.mayor(listar)
    funpr.primos(listar)
if __name__=='__name__':
    list()