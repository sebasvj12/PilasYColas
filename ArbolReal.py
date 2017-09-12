from Nodo import *
from Cola import *
class Arbol:
	def __init__(self, Lista):
		self.Lista=Lista

	def llenar(self, Lista,Arbol):
		if Lista.numElem()>0:
			if Arbol==None:
				Arbol=Nodo(None)								
				self.llenar(Lista, Arbol)
			else:				
				if self.Tipo(Lista.primero()) ==1: #valor entero					
					Arbol.valor=Lista.primero()					
					Lista.sacar()						
				elif self.Tipo(Lista.primero()) ==0:					
					Arbol.valor=Lista.primero()
					Lista.sacar()				
					Arbol.Izquierdo=Nodo(None)
					self.llenar(Lista, Arbol.Izquierdo)
					Arbol.Derecho=Nodo(None)
					self.llenar(Lista, Arbol.Derecho)	
		return Arbol

	
	
	def Tipo(self,valor):# 0 operaciones 1 numero entero 2 paila
		if valor=='+':
			numero=0
		elif valor=='-':
			numero=0
		elif valor=='/':
			numero=0
		elif valor=='*':
			numero=0
		else:
			numero=2
			try:
				num= int(valor)
				numero=1
			except Exception as e:
				print "Este valor no es numerico "
		return numero


	def evaluar(self,arbol):
		if arbol.valor=='+':
			return self.evaluar(arbol.Izquierdo)+ self.evaluar(arbol.Derecho)
		elif arbol.valor=='-':
			return self.evaluar(arbol.Izquierdo)- self.evaluar(arbol.Derecho)
		elif arbol.valor=='/':
			return self.evaluar(arbol.Izquierdo)/ self.evaluar(arbol.Derecho)
		elif arbol.valor=='*':
			return self.evaluar(arbol.Izquierdo)* self.evaluar(arbol.Derecho)
		else: return arbol.valor


pr=Cola();
#pr.meter("-")
#pr.meter(7)
#pr.meter("/")
#pr.meter(4)
#pr.meter(2)
#pr.meter(3)
pr.meter("+")
pr.meter("/")
pr.meter(4)
pr.meter(2)
pr.meter("*")
pr.meter(3)
pr.meter(5)
p=Arbol(pr)
pino=p.llenar(pr,None)

print p.evaluar(pino)
