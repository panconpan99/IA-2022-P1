from copy import deepcopy
from frog import Frog
from arbol import arbol


BOARD = [2, 2, 2, 0, 1, 1, 1]

def heuristic(board):
    """
        Returns a score based in how many values are in the right spot.
    """
    
    score = 0
    for i, j in zip(board, BOARD):
        if i == j:
            score += 1

    return score

def print_salto(move):
    if move == "L" :print("salto hacia la izuierda!")
    elif move == 'LL': print("salto doble hacia la izquierda")
    elif move == 'R': print("salto hacia la derecha")
    elif move =='RR': print("salto doble hacia la derecha")

def search_solution(arbol, eval_heuristic=False):
    """
        Deep-first search python implementation search python implementation with
        Best-first enhancement.

        Parameters
        ----------
        tree: Tree
            Instance with a inicial root node containing the initial state of the game.
        
        eval_heuristic: bool
            If use heuristic.
        
        Returns
        -------
        list[list[int]]
            Board of the Frog game instance.
            
    """

    moves = ['L', 'LL', 'R', 'RR']

    count = 0
    history = [arbol]
    #state list avoid duplicated values.
    estado = [arbol.data]
    while history:
        count += 1
        aux_tree = history.pop(0)

        if aux_tree.data.is_solve():
            print("historial:", count)
            return aux_tree.chain_to_root()
        #Additional code for auto-expansion of the tree.
        for move in moves:
            new_game = deepcopy(aux_tree.data)
            new_state = new_game.move_to(move)
            if new_state and not new_game in estado:
                estado.append(new_game)
                arbol.add_leaf(new_game, target=aux_tree.data)
        #===============================================

        if eval_heuristic:
            aux_tree.leafs.sort(key=lambda x: heuristic(x.data.get_board()), reverse=True)

        history = aux_tree.leafs + history
    return []

