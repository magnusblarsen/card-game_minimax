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


# Always ordered. 
# State[0] is first row and so on, and number indicates number of cards in that row.
Player = Enum('Player', ['MAX', 'MIN'])

# function MINIMAX-SEARCH(state) returns an action
# 	value, move ← MAX-VALUE(state)
# return move

def minimax_search() -> tuple:
    state = [1, 2, 3, 4]
    value, move = max_value(state)
    print("Value: {0}, Move: {1}".format(value, move))
    return move


def is_terminal(state: list) -> bool:
    if state[0] == 0:
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

minimax_search()