#!/usr/bin/python3

from enum import Enum
import math

Player = Enum('Player', ['MAX', 'MIN'])

def print_state(state):
    to_print = ""
    for _, no_of_cards in enumerate(state):
        for _ in range(1, no_of_cards + 1):
            to_print += "O "
        to_print += "\n"
    print(to_print)

def play_game():
    
    state = [1, 2, 3, 4]
    turn = Player.MAX
    print_state(state)
    while not is_terminal(state):
        move = minimax_search(state)
        state = result(state, move[0], move[1])
        print_state(state)
        turn = Player.MAX if turn == Player.MIN else Player.MIN

    who_won = "Max" if utility(turn) == 1 else "Min"
    print("Game Over... {0} won!".format(who_won))

# State[0] is first row and so on, and number indicates number of cards in that row.
def minimax_search(state) -> tuple:
    value, move = max_value(state, -math.inf, math.inf)
    print("Value: {0}, Move: {1}".format(value, move))
    return move


def is_terminal(state: list) -> bool:
    state = [x for x in state if x > 0]
    state.sort()

    return True if not state else False

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

def max_value(state, alpha, beta) -> tuple[int|float, tuple]:
    if is_terminal(state):
        return utility(Player.MAX), ()

    v = -math.inf

    move = ()

    for row, no_of_cards in enumerate(state):
        for i in range(1, no_of_cards + 1):
            (v2, _) = min_value(result(state, row, i), alpha, beta)
            if v2 > v:
                v = v2
                move = (row, i)
                alpha = max(alpha, v)
            if v >= beta:
                return v, move
    return v, move

def min_value(state, alpha, beta) -> tuple[int|float, tuple]:
    if is_terminal(state):
        return utility(Player.MIN), ()
    v = math.inf
    move = ()

    for row, no_of_cards in enumerate(state):
        for i in range(1, no_of_cards + 1):
            v2, _ = max_value(result(state, row, i), alpha, beta)
            if v2 < v:
                v = v2
                move = (row, i)
                beta = max(beta, v)
            if v <= alpha:
                return v, move
    return v, move

play_game()
