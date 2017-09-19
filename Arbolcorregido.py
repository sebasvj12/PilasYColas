import sys
import nodo
import pila

class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der
        
class Pila:
     def __init__(self):
         self.items = []

     def estaVacia(self):
         return self.items == []

     def incluir(self, item):
         self.items.append(item)

     def extraer(self):
         return self.items.pop()

     def inspeccionar(self):
         return self.items[len(self.items)-1]

     def tamano(self):
         return len(self.items)
      
class val:
      def __init__(self, nombre, valor):
        self.nombre=nombre
        self.valor=valor
        

def evaluar(arbol):
    try:
      if(arbol.valor == '+'):
         return (evaluar(arbol.izq) + evaluar(arbol.der))
      if(arbol.valor == '-'):
         return (evaluar(arbol.izq) - evaluar(arbol.der))
      if(arbol.valor == '*'):
         return (evaluar(arbol.izq) * evaluar(arbol.der))
      if(arbol.valor == '/'):
         return (evaluar(arbol.izq) / evaluar(arbol.der))   
      return int(arbol.valor)
    except AttributeError:
      return int(arbol)


opcion = '0'
lista = []
while (opcion!='2'):
    opcion = raw_input("\n 1. Ingresar posfijo  \n 2. Cerrar \n")
    if (opcion == '1'):                    
        pil=Pila()
        cadena= raw_input("Ingrese posfijo: ")
        notacion=cadena.split(" ")

        for i in range(len(notacion)-1):
            if notacion[i+1] == '=':
                valor = evaluar(pil.extraer())
                print(notacion[i] + ' = ' + str(valor))
                valor = val(notacion[i],valor)
                lista.append(valor)
            else:
                if(notacion[i]!='+' and notacion[i]!='-' and notacion[i]!='*' and notacion[i]!='/'):
                    if (notacion[i].isalpha()):
                         for j in range (len(lista)):
                              if (lista[j].nombre==notacion[i]):
                                   pil.incluir(lista[j].valor)                  
                    else:  
                         pil.incluir(notacion[i])
                else:
                    num1=pil.extraer()
                    num2=pil.extraer()
                    nodo=Nodo(notacion[i],num2,num1)
                    pil.incluir(nodo)        
    else:
        if (opcion == '2'):
          sys.exit()  
        else:
            print ("Opcion No Valida")
