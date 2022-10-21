Reglas = {
    'L': -1,
    'LL': -2,
    'R': 1,
    'RR': 2
}

class Rana:
    def __init__(self, arreglo,mov):
        self.arreglo = arreglo
        self.aux = self.arreglo.index(0)
        self.move=mov

    def get_arreglo(self):
        return self.arreglo

    def get_aux(self):
        return self.aux

    def intercambio(self, mover):  
        p = self.aux
        m = self.aux + mover

        self.aux = m
        self.arreglo[p], self.arreglo[m] = self.arreglo[m], self.arreglo[p]
        self.move=mover
    def mover_a(self, mover):
        if mover in Reglas.keys():
            if mover.startswith('L'):
                regla = 1
            else:
                regla = 2
            if 0 <= self.aux + Reglas[mover] < 7:
                if self.arreglo[self.aux + Reglas[mover]] == regla:
                    self.intercambio(Reglas[mover])
                    return True
        return False

    def es_solucion(self):
        #Devuelve True si es solucion
        return self.arreglo == [2, 2, 2, 0, 1, 1, 1]

    def __str__(self):
        if self.move is not None:
            return f'{self.arreglo}, {self.move}'
        else:
            return f'{self.arreglo}'