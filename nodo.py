class nodo:
    def __init__(self, dato, nivel=0):
        self.dato = dato
        self.padre = None
        self.hijos = []
        self.nivel = nivel

    def agregar_hijo(self, dato, espacio=None):
        #insercion de elemento y cambio de lugar
        if espacio:
            if espacio == self.dato:
                hijo = nodo(dato, nivel=self.nivel + 1)
                hijo.padre = self
                self.hijos.append(hijo)
            else:
                for hijo in self.hijos:
                    hijo.agregar_hijo(dato, espacio=espacio)
        else:
            hijo = nodo(dato, nivel=self.nivel + 1)
            hijo.padre = self
            self.hijos.append(hijo)

    def cadena_padres(self):
        #Devuelve una lista de elementos del padre actual al hijo
        cadena = [self.dato]
        aux_nodo = self.padre
        while aux_nodo: 
            cadena.append(aux_nodo.dato)
            aux_nodo = aux_nodo.padre
        return cadena

    def mostrar_nodo(self):
        #mostrar lista de nodos
        print(str(self.dato))
        if self.hijos:
            for hijo in self.hijos:
                hijo.mostrar_nodo()