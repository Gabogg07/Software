from FirstModule import *
import unittest
import math 

class Test(unittest.TestCase):
	def testPrecioMinimo(self):
		InicioDeServicio=datetime.datetime(2017,1,23,8,0,0,0)
		FinDeServicio=datetime.datetime(2017,1,23,8,15,0,0)
		TarifaSem=[1,0]
		vSem=TarifaSem[0]+(TarifaSem[1]/100)
		TarifaFin=[0,0]
		vFin=TarifaFin[0]+(TarifaFin[1]/100)
		tiempoDeServicio=[InicioDeServicio,FinDeServicio]       
		Tarifa=[vSem,vFin]
		pago = calcularPrecio(Tarifa, tiempoDeServicio)
		bolivares = pago//1
		self.assertEquals(1,bolivares)


	def testPrecioMaximo(self):
		InicioDeServicio=datetime.datetime(2017,1,23,8,0,0,0)
		FinDeServicio=datetime.datetime(2017,1,23+7,8,0,0,0)
		TarifaSem=[1,0]
		vSem=TarifaSem[0]+(TarifaSem[1]/100)
		TarifaFin=[0,0]
		vFin=TarifaFin[0]+(TarifaFin[1]/100)
		tiempoDeServicio=[InicioDeServicio,FinDeServicio]       
		Tarifa=[vSem,vFin]
		pago = calcularPrecio(Tarifa, tiempoDeServicio)
		bolivares,centimos=divmod(pago, 1)
		self.assertEquals(167,bolivares)
		self.assertEquals(0,centimos)


	#Casos bordes
	def testPrecioMinimoBorde(self):
		InicioDeServicio=datetime.datetime(2017,1,23,8,0,0,0)
		FinDeServicio=datetime.datetime(2017,1,23,8,15,0,1)
		TarifaSem=[1,0]
		vSem=TarifaSem[0]+(TarifaSem[1]/100)
		TarifaFin=[0,0]
		vFin=TarifaFin[0]+(TarifaFin[1]/100)
		tiempoDeServicio=[InicioDeServicio,FinDeServicio]       
		Tarifa=[vSem,vFin]
		pago = calcularPrecio(Tarifa, tiempoDeServicio)
		bolivares = pago//1
		self.assertEquals(1,bolivares)


	def testPrecioMaximoBorde(self):
		InicioDeServicio=datetime.datetime(2017,1,23,8,0,0,0)
		FinDeServicio=datetime.datetime(2017,1,23+7,8,0,15,1)
		TarifaSem=[1,0]
		vSem=TarifaSem[0]+(TarifaSem[1]/100)
		TarifaFin=[0,0]
		vFin=TarifaFin[0]+(TarifaFin[1]/100)
		tiempoDeServicio=[InicioDeServicio,FinDeServicio]       
		Tarifa=[vSem,vFin]
		pago = calcularPrecio(Tarifa, tiempoDeServicio)
		bolivares,centimos=divmod(pago, 1)
		self.assertEquals(167,bolivares)
		self.assertEquals(0,centimos)




if __name__ == '__main__':
	unittest.main()
