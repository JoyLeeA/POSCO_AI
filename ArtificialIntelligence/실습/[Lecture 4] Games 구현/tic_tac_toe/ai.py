import game
import random

_FILL_IN_ = None

#==========================================================
# MinimaxAgent class
#==========================================================

class MinimaxAgent:
    def V(self, state, verbose=0):
        if verbose >= 1:
            print('call V({})'.format(state))

        # If IsEnd(s)
        if game.is_end(state):
            return game.utility(state)

        # Get possible actions
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        # If player == agent (maximizing player)
        if game.get_player_from_state(state) == game.MAX_PLAYER:
            value = -game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state

        # If player == opponent (minimzing player)
        else:
            value = game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state

        return value

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        optimal = max if game.get_player_from_state(state) == game.MAX_PLAYER else min
        return optimal(actions, key=lambda x: self.V(game.get_next_state(state, x)))

#==========================================================
# Alpha-beta Pruning class
#==========================================================

class PruningMinimaxAgent:
    def V(self, state, alpha=-game.INT_INF, beta=game.INT_INF, verbose=0):
        if verbose >= 1:
            print('call V({})'.format(state))

        # If IsEnd(s)
        if game.is_end(state):
            return game.utility(state)

        # Get possible actions
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        # If player == agent (maximizing player)
        if game.get_player_from_state(state) == game.MAX_PLAYER:
            value = -game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state
                alpha = _FILL_IN_
                if _FILL_IN_: break

        # If player == opponent (minimzing player)
        else:
            value = game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state
                beta = _FILL_IN_
                if _FILL_IN_: break

        return value

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        alpha = -game.INT_INF
        beta = game.INT_INF

        if game.get_player_from_state(state) == game.MAX_PLAYER:
            values = []
            for action in actions:
                value = self.V(game.get_next_state(state, action), alpha, beta)
                values.append(value)
                alpha = max(alpha, value)
            return max(zip(actions, values), key=lambda x: x[1])[0]
        else:
            values = []
            for action in actions:
                value = self.V(game.get_next_state(state, action), alpha, beta)
                values.append(value)
                beta = min(beta, value)
            return min(zip(actions, values), key=lambda x: x[1])[0]

#==========================================================
# DepthLimitedMinimaxAgent class
#==========================================================

heuristic_array = [
    [  0, -10, -100, -1000],
    [  10,  0,    0,     0],
    [ 100,  0,    0,     0],
    [1000,  0,    0,     0]
]

def eval(state):
    result = 0
    for cond in game.WIN_CONDITIONS:
        maxs = mins = 0
        for loc in cond:
            if state[loc] == game.MAX_PLAYER:
                maxs += 1
            elif state[loc] == game.MIN_PLAYER:
                mins += 1
        result += heuristic_array[maxs][mins]

    return result

class DepthLimitedMinimaxAgent:
    def __init__(self, max_depth=2):
        self.max_depth = max_depth

    def V(self, state, depth, verbose=0):
        if verbose >= 1:
            print('call V({})'.format(state))

        # If IsEnd(s)
        if game.is_end(state):
            return game.utility(state)

        # If depth = 0
        if depth == 0:
            #print game.get_board_str(state), eval(state)
            return eval(state)

        # Get possible actions
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        # If player == agent (maximizing player)
        if game.get_player_from_state(state) == game.MAX_PLAYER:
            value = -game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state

        # If player == opponent (minimzing player)
        else:
            value = game.INT_INF
            for action in actions:
                value = _FILL_IN_  # HINT: use self.V (with verbose=verbose) and game.get_next_state

        return value

    def policy(self, state):
        actions = game.get_possible_actions(state)
        assert len(actions) > 0

        optimal = max if game.get_player_from_state(state) == game.MAX_PLAYER else min
        return optimal(actions, key=lambda x: self.V(game.get_next_state(state, x), self.max_depth))
