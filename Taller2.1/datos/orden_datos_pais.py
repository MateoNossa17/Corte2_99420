from procesos import mayorempre
from procesos import minimoempre
from procesos import empleaprome 
def pais(x):
    nombre_empresas_del_pais=[]
    sito_web_de_la_empreza=[]
    descricion_de_la_empresa=[]
    año_fundacio_de_la_empresa=[]
    industria_de_la_empresa=[]
    numero_de_empleados_de_la_empresa=[]

    datos=open('./datos/organization_data.csv','r')
    ren=datos.readlines()
    datos.seek(0)
    for i in range(len(ren)):
        empresa = datos.readline().replace('\n','').split(',')
        if empresa[4]==x:
            nombre_empresas_del_pais.append(empresa[2])
            sito_web_de_la_empreza.append(empresa[3])
            descricion_de_la_empresa.append(empresa[5])
            año_fundacio_de_la_empresa.append(int(empresa[6]))
            industria_de_la_empresa.append(empresa[7])
            numero_de_empleados_de_la_empresa.append(int(empresa[8]))
    datos.close
    print(f'País: {x}\n')
    mayorempre.empre_maxi(nombre_empresas_del_pais,sito_web_de_la_empreza,descricion_de_la_empresa,año_fundacio_de_la_empresa,industria_de_la_empresa,numero_de_empleados_de_la_empresa)
    minimoempre.empre_min(nombre_empresas_del_pais,sito_web_de_la_empreza,descricion_de_la_empresa,año_fundacio_de_la_empresa,industria_de_la_empresa,numero_de_empleados_de_la_empresa)
    empleaprome.promedio(numero_de_empleados_de_la_empresa)
    print(f'==================================================================================\n')
if __name__=='__main__':
    print(pais('Argentina'))



     

