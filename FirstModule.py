'''
Created on Jan 23, 2017

@author: gabriel
'''
import datetime
from calendar import monthrange
from builtins import print
'''
print("Introduzca Ano,mes,dia,hora,min,seg y milisegundos de entrada")
Anoe=input()
Mese=input()
Diae=input()
Horae=input()
Mine=input()
Sege=input()
Milse=input()


print("Introduzca Ano,mes,dia,hora,min,seg y milisegundos de salida")
Anos=input()
Mess=input()
Dias=input()
Horas=input()
Mins=input()
Segs=input()
Milss=input()
'''
global terminado,Restos
terminado=False
Restos=0
Anoe=2017
Mese=1
Diae=30
######################################################################################

def horasPorDia(I,F,C):
    print("------------------------------------------------")
    print(I, "  HASTA ", F)
    print("------------------------------------------------")
    hours=[0,0]
    if(I.weekday()<5 ):
        print("Es un dia de semana ")
    else:
        print("Es fin de semana")
    delta=F-I
    print("DELTA", delta)
    horas=delta.seconds//3600
    resto=delta.seconds%3600
    
    print("resto= ",resto)
    
    if(resto!=0):
        horas+=1
        print("son horas no exactas, el resto es: ",Restos)
    else:
        print("Son horas exactas")
    
    print(horas," Numero de horas")

    if(I.weekday()<5):
        hours[0]=horas
    else:
        hours[1]=horas
    
    #CHEQUEO SI EL DIA SIGUIENTE A TRABAJAR ESTA EN OTRO MES O EN ESE MISMO.
    if(I.date().day+1 in range(1,monthrange(I.date().year, I.date().month)[1]+1)):
        print("NO CAMBIO DE MES")
        inicio=datetime.datetime(I.date().year,I.date().month,I.date().day+1,0,0,0,0)
    else:
        print("CAMBIO DE MES")
        if(I.date().month==12):
            inicio=datetime.datetime(I.date().year+1,1,1,0,0,0,0)
        else:
            inicio=datetime.datetime(I.date().year,I.date().month+1,1,0,0,0,0)
    #inicio=datetime.datetime(I.year(),I.month(),I.days(),0,0,0,0)
    print(inicio ,"ESTO ES EL INCIO TEMP")
    return hours,inicio

######################################################################3


#WEEKDAY 5 Y 6 SON SABADO Y DOMINGO
InicioDeServicio=datetime.datetime(Anoe,Mese,Diae,1,10,0,0)
FinDeServicio=datetime.datetime(Anoe,Mese,Diae+1,1,10,0,0)
Tarifa=[1,2]
print(InicioDeServicio, "   " ,FinDeServicio)
print((FinDeServicio - InicioDeServicio))

inic=InicioDeServicio
fin=FinDeServicio

print(InicioDeServicio.date()==FinDeServicio.date())

while not terminado:
    if(inic.date()==FinDeServicio.date()):
        #ES EL MISMO DIA
            Costo,inic=horasPorDia(inic, FinDeServicio, Tarifa)
            terminado=True
            
    else:
            temp=datetime.datetime(inic.date().year,inic.date().month,inic.date().day,23,59,59,999)
            Costo,inic=horasPorDia(inic, temp, Tarifa)
            print(inic, "INICIO LUEGO DE LA PRIMERA CORRIDA")
    print("-------------CORRIDA----------------")


#print(add(1,2))

