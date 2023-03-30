class Persona():
    def __init__(self):
        self.nombre:str|None=None
        self.altura:float=0.0
        self.masa:float=0.0
    def p_imc(self):
        imc=(self.masa)/(self.altura/100)**2
        if imc <=18.5:
            return str ('Por debajo')
        elif 18.5<imc<24.9:
            return str ('saludable')
        elif 25<imc<29.9:
            return str ('sobrepeso')
        elif 30<imc<34.9:
            return str ('obesidad I')
        elif 35<imc<39.9:
            return str ('obesidad II')
        else:
            return str ('obesidad III')
def main():
    estudiante_1=Persona()
    estudiante_1.nombre='Pedro Caceres'
    estudiante_1.altura=188
    estudiante_1.masa=97
    estudiante_2=Persona()
    estudiante_2.nombre='Maria Perez'
    estudiante_2.altura=160
    estudiante_2.masa=47
    estudiante_3=Persona()
    estudiante_3.nombre='Julian Dominguez'
    estudiante_3.altura=158
    estudiante_3.masa=58
    estudiante_4=Persona()
    estudiante_4.nombre='Jessica'
    estudiante_4.altura=170
    estudiante_4.masa=73

    print(f'Estuciantes {estudiante_1.nombre} resultado: {estudiante_1.p_imc()}')
    print(f'Estuciantes {estudiante_2.nombre} resultado: {estudiante_2.p_imc()}')
    print(f'Estuciantes {estudiante_3.nombre} resultado: {estudiante_3.p_imc()}')
    print(f'Estuciantes {estudiante_4.nombre} resultado: {estudiante_4.p_imc()}')
if __name__=='__main__':
    main()
    

        
        
