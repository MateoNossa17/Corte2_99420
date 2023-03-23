import random as r
def eje1():
    n=0
    while n<10:
        x=r.randint(110,120)
        if x==110 or x==115 or x==119:
            continue
        elif x%2==0:
            print(x)
            n+=1
            while n<=10:
                d=r.randint(110,120)
                if d==110 or d==115 or d==119:
                    pass 
                elif d%2==1:
                    print(d)
                    n+=1
                    break
if __name__=="__name__":
    eje1()




