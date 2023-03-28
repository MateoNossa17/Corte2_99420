import random as r
matriz=[]
for i in range(5):
    matriz.append([])
    for j in range(10):
        x=r.randint(0,50)
        matriz[i].append(x)
print(matriz)
listam=[]
listame=[]
pos=[]
posm=[]
for i in matriz:
    h=max(i)
    u=min(i)
    pm=i.index(u)
    p=i.index(h)
    listam.append(h)
    pos.append(p)
    listame.append(u)
    posm.append(pm)
b=max(listam)
h=listam.index(b)
e=min(listame)
k=listame.index(e)
print(f'El número mayor es {b} es cual esta en [{h}][{pos[h]}]')
print(f'El número menor es {e} es cual esta en [{k}][{posm[k]}]')




