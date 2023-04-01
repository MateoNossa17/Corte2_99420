import valor
def eje():
    dic={}
    f=open('Alimentos.txt','rt')
    ali=f.readlines()
    f.seek(0)
    for i in range(len(ali)):
        va=f.readline().rstrip('\n').split(',')
        dic[va[1]]=float(va[2])
    valor.b(dic)
if __name__=='__main__':
    eje()
    

