class nodoPila(object):
    """son los elementos de la pila, tienen un valor y un puntero al siguiente nodo"""
    valor, next = None, None


class Pila(object):
    """ Clase Pila"""
    def __init__(self, num):
        self.cima = None  # de base no hay nada
        self.tamanio = 0
        self.num = num

    def push(self, v):
        nodo = nodoPila()
        nodo.valor = v  # valor del nodo
        nodo.next = self.cima  # el nuevo elemento apunta a la cima anterior
        self.cima = nodo  # y se convierte en la nueva cima
        self.tamanio += 1  # y se aumenta en uno su tamaño
    
    def pop(self):
        '''funcion pop, elimina el nodo en la cima y devuelve su valor'''
        v = self.cima.valor  # guardamos el valor del nodo
        self.cima = self.cima.next  # la cima pasa a ser el siguiente elemento
        self.tamanio -= 1  # se reduce el tamaño
        return v  # devolvemos el valor del nodo

    def imprimir(self):
        '''Muestra el contenido de la pila (sin modificarla()'''
        pila_aux = Pila(0)  # pila auxiliar donde vamos a ir metiendo los nodos cuando los desapilemos de la original
        lista_pila = []

        # hasta que la pila esté vacía, vamos a desapilar sus elementos para ir contbilizandolos
        while not (self.cima is None):
            v = self.pop()  # guardamos el valor del nodo que desapilamos
            #print(v)  # lo imprimimos
            lista_pila.append(v)
            pila_aux.push(v)  # y lo apilamos en la auxiliar

        # y ahora los devolvemos a la pila original
        while not (pila_aux.cima is None):
            v = pila_aux.pop()
            self.push(v)
        
        return lista_pila

