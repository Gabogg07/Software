'''
Created on Jan 23, 2017

@author: gabriel
'''
import datetime
from calendar import monthrange

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
Restos=1
Anoe=2017
Mese=12
Diae=31

######################################################################################

def horasPorDia(I,F,C):
    global Restos
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
    Restos=Restos+resto
    
    print("resto= ",resto)
    
    if(resto!=0):
        horas+=1
        print("son horas no exactas, el resto es: ",resto)
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
            print("CAMBIO DE anio")
        else:
            inicio=datetime.datetime(I.date().year,I.date().month+1,1,0,0,0,0)
            print("NO CAMBIO DE anio")
    #inicio=datetime.datetime(I.year(),I.month(),I.days(),0,0,0,0)
    print(inicio ,"ESTO ES EL INCIO TEMP")
    return hours,inicio

######################################################################3

def calcularPrecio(Tarifa,tiempoDeServicio):
    global terminado,Restos
    InicioDeServicio=tiempoDeServicio[0]
    FinDeServicio=tiempoDeServicio[1]
    inic=InicioDeServicio

    totalh=[0,0]
    
    while not terminado:
        acum=[0,0]
        if(inic.date()==FinDeServicio.date()):
            #ES EL MISMO DIA
                acum,inic=horasPorDia(inic, FinDeServicio, Tarifa)
                terminado=True
                
        else:
                temp=datetime.datetime(inic.date().year,inic.date().month,inic.date().day,23,59,59,999)
                acum,inic=horasPorDia(inic, temp, Tarifa)
                print(inic, "INICIO LUEGO DE LA PRIMERA CORRIDA")
                
        totalh[0]+=acum[0]
        totalh[1]+=acum[1]
        print(totalh)
        print("-------------CORRIDA----------------")
    #print(Restos)
    #print(totalh)
    if(Restos>=3599):
        if(FinDeServicio.weekday()<5):
            totalh[0]=totalh[0]-1
        else:
            totalh[1]=totalh[1]-1
    #print(totalh)
    monto=totalh[0]*Tarifa[0]+ totalh[1]*Tarifa[1]
    return monto


######################################################################

#WEEKDAY 5 Y 6 SON SABADO Y DOMINGO
InicioDeServicio=datetime.datetime(Anoe,Mese,Diae,1,10,0,0)
FinDeServicio=datetime.datetime(Anoe+1,Mese-11,Diae-30,1,10,0,0)

TarifaSem=[2,5]
vSem=TarifaSem[0]+(TarifaSem[1]/100)
TarifaFin=[5,0]
vFin=TarifaFin[0]+(TarifaFin[1]/100)

tiempoDeServicio=[InicioDeServicio,FinDeServicio]

print(vSem,"  ",vFin)
        
Tarifa=[vSem,vFin]
print((FinDeServicio-InicioDeServicio).seconds)
print((FinDeServicio-InicioDeServicio).days)

if((FinDeServicio-InicioDeServicio).seconds<900 and (FinDeServicio-InicioDeServicio).days==0):
    print("El tiempo de servicio debe ser al menos 15 minutos")
elif((FinDeServicio-InicioDeServicio).days>7):
    print("El tiempo de servicio no puede ser mayor que 7 dias")
else:
    pago=calcularPrecio(Tarifa, tiempoDeServicio)
    bolivares,centimos=divmod(pago, 1)
    print("Se deben: ",bolivares," bolivares con: ",centimos, "centimos")
#tiempoDeTrabajo=[InicioDeServicio,FinDeServicio]
#print(InicioDeServicio, "   " ,FinDeServicio)
#print((FinDeServicio - InicioDeServicio))
'''
inic=InicioDeServicio
fin=FinDeServicio

totalh=[0,0]
print(InicioDeServicio.date()==FinDeServicio.date())

while not terminado:
    acum=[0,0]
    if(inic.date()==FinDeServicio.date()):
        #ES EL MISMO DIA
            acum,inic=horasPorDia(inic, FinDeServicio, Tarifa)
            terminado=True
            
    else:
            temp=datetime.datetime(inic.date().year,inic.date().month,inic.date().day,23,59,59,999)
            acum,inic=horasPorDia(inic, temp, Tarifa)
            print(inic, "INICIO LUEGO DE LA PRIMERA CORRIDA")
    totalh[0]+=acum[0]
    totalh[1]+=acum[1]
    print(totalh)
    print("-------------CORRIDA----------------")
    
if(Restos>=3599):
    if(FinDeServicio.weekday()<5):
        totalh[0]=totalh[0]-1
    else:
        totalh[1]=totalh[1]-1

print(totalh)
print(totalh[0]+totalh[1])
'''

