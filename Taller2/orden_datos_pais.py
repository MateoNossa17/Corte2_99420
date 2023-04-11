import mayorempre
import minimoempre
import empleaprome 
import csv
def pais(x):
    nombre_empresas_del_pais=[]
    sito_web_de_la_empreza=[]
    descricion_de_la_empresa=[]
    año_fundacio_de_la_empresa=[]
    industria_de_la_empresa=[]
    numero_de_empleados_de_la_empresa=[]
    with open('organization_data.csv', newline='') as datos:
        r=csv.DictReader(datos)
        for row in r:
            if row['Country'] ==x:
                nombre_empresas_del_pais.append(row['Name'])
                sito_web_de_la_empreza.append(row['Website'])
                descricion_de_la_empresa.append(row['Description'])
                año_fundacio_de_la_empresa.append(int(row['Founded']))
                industria_de_la_empresa.append(row['Industry'])
                numero_de_empleados_de_la_empresa.append(int(row['Number of employees']))
    datos.close
    print(f'País: {x}\n')
    mayorempre.empre_maxi(nombre_empresas_del_pais,sito_web_de_la_empreza,descricion_de_la_empresa,año_fundacio_de_la_empresa,industria_de_la_empresa,numero_de_empleados_de_la_empresa)
    minimoempre.empre_min(nombre_empresas_del_pais,sito_web_de_la_empreza,descricion_de_la_empresa,año_fundacio_de_la_empresa,industria_de_la_empresa,numero_de_empleados_de_la_empresa)
    empleaprome.promedio(numero_de_empleados_de_la_empresa)



     

