def horario():
    materia=['Cálculo intregral','Física Mecánica','Programación','Constitución y democracia','Circuitos DC','Cultura ecológica','Taller de física mecánica']
    day_class=['Martes y Jueves','Martes y Jueves','Martes y Jueves','Miércoles','Miécoles y Viernes','Viernes','Viernes']
    hour_class=['7:00 a 9:00','9:00 a 11:00','13:00 a 15:00','7:00 a 9:00','11:00 a 13:00','9:00 a 11:00','15:00 a 17:00']
    classroom=['407 DB','405 DB','303 GO','405 DB','306 DB','306 PS','204 PS']
    name_teacher=['Acuña Gomez Edwin Julian','Pineda Rey Hernan','Torres Barrera David Nicolás','Sanchez Parra Yurberney','Bohórquez Ávila Roberto','Sanchez Parra Yurberney','Dora Mora Paula Andrea']
    c=input('Ingrese la clase que desea saber su horario: ')
    pos=materia.index(c)
    print(f'{c} tiene los días: {day_class[pos]}\nA las: {hour_class[pos]}\nEn el salón: {classroom[pos]}\nCon el docente: {name_teacher[pos]}')
if __name__=='__main__':
    horario()