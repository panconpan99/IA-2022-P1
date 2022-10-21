from copy import deepcopy
from Rana import Rana
from nodo import nodo

ARREGLO_FINAL = [2, 2, 2, 0, 1, 1, 1]

def heuristica(arreglo):
    punto = 0
    for i, j in zip(arreglo, ARREGLO_FINAL):
        if i == j:
            punto += 1
    return punto

def mostrar_salto(mover):
    if mover == "L" :print("izquierda")
    elif mover == 'LL': print("2x izquierda")
    elif mover == 'R': print("derecha")
    elif mover =='RR': print("2x derecha")

def buscar_solucion(nodo, eval_heuristica=False):
    movimiento = ['L', 'LL', 'R', 'RR']

    contador = 0
    historial = [nodo]
    #lista de estado y valores duplicados
    estado = [nodo.dato]
    while historial:
        contador += 1
        aux_nodo = historial.pop(0)

        if aux_nodo.dato.es_solucion():
            print("iteraciones:", contador)
            return aux_nodo.cadena_padres()
        #expansion de los nodos
        for mover in movimiento:
            nuevo_juego = deepcopy(aux_nodo.dato)
            nuevo_estado = nuevo_juego.mover_a(mover)
            if nuevo_estado and not nuevo_juego in estado:
                estado.append(nuevo_juego)
                nodo.agregar_hijo(nuevo_juego, espacio=aux_nodo.dato)
        if eval_heuristica:
            aux_nodo.hijos.sort(key=lambda x: heuristica(x.dato.get_arreglo()), reverse=True)

        historial = aux_nodo.hijos + historial
    return []