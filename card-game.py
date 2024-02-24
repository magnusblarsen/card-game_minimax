#!/usr/bin/python3

from enum import Enum


# function MINIMAX-SEARCH(state) returns an action
# 	value, move ← MAX-VALUE(state)
# return move

# function MAX-VALUE(state) returns (utility,move)
# 	if IS-TERMINAL(state) then
# 		return UTILITY(state,MAX), null
# 	v ← -∞
# 	for each a in ACTIONS(state) do
# 		v2,a2 ← MIN-VALUE(RESULT(state,a))
# 		if v2 > v then
# 			v,move ← v2,a
# 	return v,move

# function MIN-VALUE(state) returns (utility,move)
# 	if IS-TERMINAL(state) then
# 		return UTILITY(state,MAX), null
# 	v ← +∞
# 	for each a in ACTIONS(state) do
# 		v2,a2 ← MAX-VALUE(RESULT(state,a))
# 		if v2 < v then
# 			v,move ← v2,a
# 	return v,move

# TODO: implement alpha-beta pruning 
# TODO: persist state for each move

# Always ordered. 
# State[0] is first row and so on, and number indicates number of cards in that row.
Player = Enum('Player', ['MAX', 'MIN'])

def print_state(state):
    to_print = ""
    for i, no_of_cards in enumerate(state):
        for j in range(1, no_of_cards + 1):
            to_print += "O "
        to_print += "\n"
    print(to_print)

def play_game():
    state = [1, 2, 3, 4, 5]
    turn = Player.MAX
    print_state(state)
    while not is_terminal(state):
        move = minimax_search(state)
        state = result(state, move[0], move[1])
        print_state(state)
        turn = Player.MAX if turn == Player.MIN else Player.MIN

    who_won = "Max" if utility(turn) == 1 else "Min"
    print("Game Over... {0} won!".format(who_won))

def minimax_search(state) -> tuple:
    value, move = max_value(state)
    print("Value: {0}, Move: {1}".format(value, move))
    return move


def is_terminal(state: list) -> bool:
    state = [x for x in state if x > 0]
    state.sort()

    if not state:
        return True

def utility(player: Player) -> int:
    if player == Player.MAX:
        return 1
    else: 
        return -1

def result(state, row, take_amount):
    new_state = state.copy()
    new_state[row] -= take_amount
    if new_state[row] < 0:
        # invalid
        exit(1)
    return new_state

# move : (int, int) (index, no_of_cards)
def max_value(state) -> tuple[int, tuple]:
    if is_terminal(state):
        return utility(Player.MAX), None
    v = float('-inf')
    
    for row, no_of_cards in enumerate(state):
        for i in range(1, no_of_cards + 1):
            (v2, _) = min_value(result(state, row, i))
            if v2 > v:
                v = v2
                move = (row, i)
    return v, move

def min_value(state) -> tuple[int, tuple]:
    if is_terminal(state):
        return utility(Player.MIN), None
    v = float('inf')

    for row, no_of_cards in enumerate(state):
        for i in range(1, no_of_cards + 1):
            v2, _ = max_value(result(state, row, i))
            if v2 < v:
                v = v2
                move = (row, i)
    return v, move

play_game()