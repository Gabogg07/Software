'''
Created on Jan 23, 2017

@author: Fabiana Acosta 10-10005
         Gabriel Gutierrez 13-10625
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

######################################################################################
#FUNCION horasPorDia
# funcion encargada de calcular para un dia, cuantas horas de servicio son. Toma en cuenta si es dia de semana.
#ENTRADA:
#    - I : objeto datetime.datetime , contiene la hora inicial desde la cual se van a calcular las horas
#    - F : objeto datetime.datetime , contiene la hora hasta la cual se van a calcular el numero de horas
#
#SALIDA:
#    - hours: tupla que contiene el numero de horas de servicio, en su primera posicion las de dia de semana
#             y en la segunda las de fines de semana.
#    - inicio: objeto datetime.datetime , contiene la fecha de inicio del dia siguiente a evaluar
#######################################################################################
def horasPorDia(I,F):
    global Restos
    hours=[0,0]
    delta=F-I

    horas=delta.seconds//3600
    resto=delta.seconds%3600
    Restos=Restos+resto
    
    
    if(resto!=0):
        #Como hubo segundos de sobra en la hora, se agrega la hora extra
        horas+=1

    if(I.weekday()<5):
        hours[0]=horas
    else:
        hours[1]=horas
    
    #CHEQUEO SI EL DIA SIGUIENTE A TRABAJAR ESTA EN OTRO MES O EN ESE MISMO.
    if(I.date().day+1 in range(1,monthrange(I.date().year, I.date().month)[1]+1)):
        #No hubo cambio de mes
        inicio=datetime.datetime(I.date().year,I.date().month,I.date().day+1,0,0,0,0)
    else:
        #Hubo cambio de mes
        if(I.date().month==12):
            #Hubo cambio de anio
            inicio=datetime.datetime(I.date().year+1,1,1,0,0,0,0)
        else:
            #No hubo cambio de anio
            inicio=datetime.datetime(I.date().year,I.date().month+1,1,0,0,0,0)
    return hours,inicio

####################################################################################

####################################################################################
# Funcion calcularPrecio
#    funcion que dada una tarifa y unas horas de servicio, calcula el monto a pagar
# ENTRADA:
#    - tupla Tarifa, tupla que tiene en la primera posicion la tarifa para dia de semana, y en la segunda
#                    para los fines de semana
#    - tupla tiempoDeServicio, tupla de datetime.datetime que contiene las fechas y horas de entrada y salida para
#                              calcular el servicio.
# SALIDA:
#    - decimal monto, variable que contiene el monto a pagar por las horas de servicio
####################################################################################
def calcularPrecio(Tarifa,tiempoDeServicio):
    global terminado,Restos
    InicioDeServicio=tiempoDeServicio[0]
    FinDeServicio=tiempoDeServicio[1]
    inic=InicioDeServicio

    totalh=[0,0]
    
    while not terminado:
        acum=[0,0]
        if(inic.date()==FinDeServicio.date()):
                acum,inic=horasPorDia(inic, FinDeServicio)
                terminado=True
                
        else:
                temp=datetime.datetime(inic.date().year,inic.date().month,inic.date().day,23,59,59,999)
                acum,inic=horasPorDia(inic, temp)
                
        totalh[0]+=acum[0]
        totalh[1]+=acum[1]
    if(Restos>=3599):
        if(FinDeServicio.weekday()<5):
            totalh[0]=totalh[0]-1
        else:
            totalh[1]=totalh[1]-1
    monto=totalh[0]*Tarifa[0]+ totalh[1]*Tarifa[1]
    return monto


######################################################################

#DECLARACION DE VARIABLES CABLEADAS
Anoe=2017
Mese=5
Diae=17
InicioDeServicio=datetime.datetime(Anoe,Mese,Diae,8,0,0,0)
FinDeServicio=datetime.datetime(Anoe,Mese,Diae+6,21,0,0,0)

# TarifaSem y TarifaFin son dos tuplas, en su primera posicion tiene los bolivares y en la segunda los centimos
TarifaSem=[2,5]
vSem=TarifaSem[0]+(TarifaSem[1]/100)
TarifaFin=[5,0]
vFin=TarifaFin[0]+(TarifaFin[1]/100)

#Cuerpo del codigo
tiempoDeServicio=[InicioDeServicio,FinDeServicio]       
Tarifa=[vSem,vFin]
print((FinDeServicio-InicioDeServicio))

if((FinDeServicio-InicioDeServicio).seconds<900 and (FinDeServicio-InicioDeServicio).days==0):
    print("El tiempo de servicio debe ser al menos 15 minutos")
elif((FinDeServicio-InicioDeServicio).days>7):
    print("El tiempo de servicio no puede ser mayor que 7 dias")
else:
    pago=calcularPrecio(Tarifa, tiempoDeServicio)
    bolivares,centimos=divmod(pago, 1)
    print("Se deben: ",bolivares," bolivares con: ",centimos*100, "centimos")