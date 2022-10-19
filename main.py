from busqueda import *

BOARD = [2, 2, 2, 0, 1, 1, 1]
BOARD_INICIAL=[1, 1, 1, 0, 2, 2, 2]
# Create game instance
game = Frog(BOARD_INICIAL)

print("Estado inicial:")
print(game)
print('===============================================')

# Empieza el estado del arbol por profundidad
init_state = deepcopy(game)
game_tree = arbol(init_state)
print("Algoritmo por Profundidad")
solution = search_solution(game_tree, eval_heuristic=False)
solution.reverse()

# Final tree
print("iteraciones:")
game_tree.print_tree()

print('===============================================')
print('Solucion:')
for move in solution:
    print(move)


init_state = deepcopy(game)
game_tree = arbol(init_state)
print("Algoritmo por Better first")
solution = search_solution(game_tree, eval_heuristic=True)
solution.reverse()

# Final tree
print("iteraciones:")
game_tree.print_tree()

print('===============================================')
print('Solucion:')
for move in solution:
    print(move)


