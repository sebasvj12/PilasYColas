class Pila:
    def __init__(self):
        self.__datos = []

    def meter(self,valor):
        self.__datos.append(valor)

    def sacar(self):
        p_ult = len(self.__datos) - 1
        print(self.__datos[p_ult])
        if (p_ult > 0):
            del self.__datos[p_ult]

    def numElem(self):
        return len(self.__datos)

    # Invierte los elementos de pila
    def invertir(self):
        pass

    # Elimina todos los datos de la pila
    def vaciar(self):
        pass

    # Retorna los datos de la pila en una lista
    def listaPila(self):
        pass

    def __str__(self):
        return str(self.__datos)

    def buscar(self,categoria,dat):
        if self.numElem()== None:
            return False
        elif categoria== 'nombre':
             for i in range(self.numElem()):
                 if self.__datos[i].nombre == dat:
                     print(self.__datos[i].nombre, self.__datos[i].fecha, self.__datos[i].director )
                 


# PRINCIPAL
class Pelicula:
    def __init__(self,nombre,fecha,director):
        self.nombre = nombre
        self.fecha = fecha
        self.director = director
     
p = Pila()
q= Pila()
pel = Pelicula('pel','1980','Pablo')
pel2= Pelicula('1999','infantil','coco') 

p.meter(pel)
p.meter(pel2)

p.buscar('nombre','pel')




