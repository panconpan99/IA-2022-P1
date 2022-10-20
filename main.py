from busqueda import *

ARREGLO_FINAL = [2, 2, 2, 0, 1, 1, 1]
ARREGLO_INICIAL=[1, 1, 1, 0, 2, 2, 2]
# Creacion del juego
juego = Rana(ARREGLO_INICIAL)

print("Estado inicial:")
print(juego)
print('===============================================')

# Empieza el estado del nodo por profundidad
init_state = deepcopy(juego)
juego_rana = nodo(init_state)
print("Algoritmo por Profundidad")
solucion = buscar_solucion(juego_rana, eval_heuristica=False)
solucion.reverse()

# Final nodo no imformada
print("iteraciones:")
juego_rana.mostrar_nodo()

print('===============================================')
print('historial:')
for mover in solucion:
    print(mover)

init_state = deepcopy(juego)
juego_rana = nodo(init_state)
print("Algoritmo por Better first")
solucion = buscar_solucion(juego_rana, eval_heuristica=True)
solucion.reverse()

# Final nodo informada
print("iteraciones:")
juego_rana.mostrar_nodo()

print('===============================================')
print('Solucion:')
for mover in solucion:
    print(mover)
