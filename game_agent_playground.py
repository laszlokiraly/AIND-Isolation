"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random
import math
from isolation.isolation import Board

class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game: Board, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.

    results
    =======
    2 forecasts:
    ------------
     Match #   Opponent     AB_Custom
                            Won | Lost
        1       Random      10  |   0
        2       MM_Open      7  |   3
        3      MM_Center     8  |   2
        4     MM_Improved   10  |   0
        5       AB_Open      4  |   6
        6      AB_Center     4  |   6
        7     AB_Improved    4  |   6
    --------------------------------------------------------------------------
               Win Rate:      67.1%

    1 forecast:
    -----------
     Match #   Opponent     AB_Custom
                            Won | Lost
        1       Random      10  |   0
        2       MM_Open      6  |   4
        3      MM_Center     9  |   1
        4     MM_Improved    8  |   2
        5       AB_Open      4  |   6
        6      AB_Center     7  |   3
        7     AB_Improved    5  |   5
    --------------------------------------------------------------------------
               Win Rate:      70.0%

    2 forecasts but only in potential endgame (last 15 rounds):
    -----------------------------------------------------------
    first try:
     Match #   Opponent     AB_Custom
                            Won | Lost
        1       Random       9  |   1
        2       MM_Open      6  |   4
        3      MM_Center     9  |   1
        4     MM_Improved    6  |   4
        5       AB_Open      5  |   5
        6      AB_Center     3  |   7
        7     AB_Improved    5  |   5
    --------------------------------------------------------------------------
               Win Rate:      61.4%
    second try:
     Match #   Opponent     AB_Custom
                            Won | Lost
        1       Random      10  |   0
        2       MM_Open      9  |   1
        3      MM_Center     8  |   2
        4     MM_Improved    7  |   3
        5       AB_Open      6  |   4
        6      AB_Center     6  |   4
        7     AB_Improved    4  |   6
    --------------------------------------------------------------------------
               Win Rate:      71.4%

    VS AB_Improved:
    ===============
    2 forecasts but before potential endgame (except 15 rounds):
    ----------------------------------------------------------
     Match #   Opponent     AB_Custom
                            Won | Lost
        1     AB_Improved   22  |  18
    --------------------------------------------------------------------------
               Win Rate:      55.0%

    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    opponent = game.get_opponent(player)

    own_moves = []
    opp_moves = []

    if len(game.get_blank_spaces()) <= 25:
        # 2 forecasts
        for move_player in game.get_legal_moves(player):
            moves_opponent = game.forecast_move(move_player).get_legal_moves(opponent)
            for move_opponent in moves_opponent:
                ply = game.forecast_move(move_opponent)
                own_moves += ply.get_legal_moves(player)
                opp_moves += ply.get_legal_moves(opponent)
    else:
        own_moves = game.get_legal_moves(player)
        opp_moves = game.get_legal_moves(opponent)


    return float(len(own_moves) - len(opp_moves))


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    opponent = game.get_opponent(player)

    own_moves = []
    opp_moves = []

    # 1 forecast
    for move_player in game.get_legal_moves(player):
        ply = game.forecast_move(move_player)
        own_moves += ply.get_legal_moves(player)
        opp_moves += ply.get_legal_moves(opponent)

    return float(len(own_moves) - len(opp_moves))


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.

    Result
    ------
     Match #   Opponent    AB_Custom_3
                            Won | Lost
        1       Random      50  |   0
        2       MM_Open     40  |  10
        3      MM_Center    44  |   6
        4     MM_Improved   40  |  10
        5       AB_Open     25  |  25
        6      AB_Center    34  |  16
        7     AB_Improved   26  |  24
    --------------------------------------------------------------------------
               Win Rate:      74.0%

    Blanks mean:  18.302857142857142
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    opponent = game.get_opponent(player)
    multiplier = 1

    if others_toe(game, player, opponent):
        multiplier = 2

    own_moves = len(game.get_legal_moves(player)) * multiplier
    opp_moves = len(game.get_legal_moves(opponent))

    return float(own_moves - opp_moves)

def others_toe(game, player, other_player):
    # find a position, which steps on the toe of the opponent
    r, c = game.get_player_location(player)
    directions = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
    player_moves = [(r + dr, c + dc) for dr, dc in directions]

    return game.get_player_location(other_player) in player_moves

def custom_score_4(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    opponent = game.get_opponent(player)

    progress = game.move_count / len(game.get_blank_spaces())

    if progress < 0.25:
        # stay at center, and away from corners
        w, h = game.width / 2., game.height / 2.
        y, x = game.get_player_location(player)
        return float(-(h - y)**2 - (w - x)**2)
    elif progress < 0.5:
        own_moves = len(game.get_legal_moves(player))
        opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
        return float(own_moves - opp_moves)
    else:
        opponent = game.get_opponent(player)

        own_moves = []
        opp_moves = []

        # 2 forecasts
        for move_player in game.get_legal_moves(player):
            moves_opponent = game.forecast_move(move_player).get_legal_moves(opponent)
            for move_opponent in moves_opponent:
                ply = game.forecast_move(move_opponent)
                own_moves += ply.get_legal_moves(player)
                opp_moves += ply.get_legal_moves(opponent)


        return float(len(own_moves) - len(opp_moves))


def custom_score_5(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    opponent = game.get_opponent(player)
    multiplier = 1

    # find a blocking position
    if game.get_player_location() in game.get_legal_moves(opponent):
        multiplier = 10
    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(opponent))
    return float(own_moves - opp_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        Algorithm
        ---------
        function MINIMAX-DECISION(state) returns an action
            return arg max a E ACTIONS(s) MIN-VALUE(RESULT(state, a))
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        max_value = -math.inf
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if (len(legal_moves) == 1):
            return legal_moves[0]
        if legal_moves:
            best_move = legal_moves[0]

        for move in game.get_legal_moves():
            max_value_before = max_value
            max_value = max(max_value,
                            self.min_value(game.forecast_move(move),
                                           depth - 1))
            if max_value > max_value_before:
                best_move = move
        return best_move

    def max_value(self, board: Board, depth):
        """
        function MAX-VALUE(state) returns a utility value
        if TERMINAL-TEST(state) then return UTILITY(state)
        v <- -infinity
        for each a in ACTIONS(state) do
            v <- MAX(v, MIN-VALUE(RESULT(state, a)))
        return v
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        maxi = self
        utility = board.utility(maxi)
        if utility != 0:
            return utility
        if depth <= 0:
            return self.score(board, maxi)
        max_value = -math.inf
        for move in board.get_legal_moves():
            max_value = max(max_value,
                            self.min_value(board.forecast_move(move),
                                           depth - 1))
        return max_value

    def min_value(self, board: Board, depth):
        """
        function MIN-VALUE(state) returns a utility value
        if TERMINAL-TEST(state) then return UTILITY(state)
        v <- infinity
        for each a in ACTIONS(state) do
            v <- MIN(v, MAX-VALUE(RESULT(state, a)))
        return v
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        mini = self
        utility = board.utility(mini)
        if utility != 0:
            return utility
        if depth <= 0:
            return self.score(board, mini)
        min_value = math.inf
        for move in board.get_legal_moves():
            min_value = min(min_value,
                            self.max_value(board.forecast_move(move),
                                           depth - 1))
        return min_value

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.

        Algorithm
        ---------
        function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution, or failure
            for depth = 0 to infinity do
                result <- DEPTH-LIMITED-SEARCH(problem,depth)
                if result != cutoff then return result
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            depth = 0
            while True:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move = self.alphabeta(game, depth)
                depth += 1

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        Algorithm
        ---------
        function ALPHA-BETA-SEARCH(state) returns an action
            v <- MAX-VALUE(state, -infinity, +infinity)
            return the action in ACTIONS(state) with value v
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        max_value = -math.inf
        best_move = (-1, -1)
        legal_moves = game.get_legal_moves()
        if (len(legal_moves) == 1):
            return legal_moves[0]
        if legal_moves:
            best_move = legal_moves[0]

        for move in game.get_legal_moves():
            max_value_before = max_value
            max_value = max(max_value,
                            self.min_value(game.forecast_move(move),
                                           depth - 1, alpha, beta))
            if max_value >= beta:
                return move
            alpha = max(alpha, max_value)
            if max_value > max_value_before:
                best_move = move
        return best_move

    def max_value(self, board: Board, depth, alpha, beta):
        """
        function MAX-VALUE(state, alpha, beta) returns a utility value
            if TERMINAL-TEST(state) the return UTILITY(state)
                v <- -infinity
            for each a in ACTIONS(state) do
                v <- MAX(v, MIN-VALUE(RESULT(state, a), alpha, beta))
                if v >= beta then return v
                alpha <- MAX(alpha, v)
            return v
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        maxi = self
        utility = board.utility(maxi)
        if utility != 0:
            return utility
        if depth <= 0:
            return self.score(board, maxi)
        max_value = -math.inf
        for move in board.get_legal_moves():
            max_value = max(max_value,
                            self.min_value(board.forecast_move(move),
                                           depth - 1, alpha, beta))
            if max_value >= beta:
                return max_value
            alpha = max(alpha, max_value)
        return max_value

    def min_value(self, board: Board, depth, alpha, beta):
        """
        function MIN-VALUE(state, alpha, beta) returns a utility value
            if TERMINAL-TEST(state) the return UTILITY(state)
                v <- +infinity
            for each a in ACTIONS(state) do
                v <- MIN(v, MAX-VALUE(RESULT(state, a), alpha, beta))
                if v <= alpha then return v
                beta <- MIN(beta, v)
            return v
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        mini = self
        utility = board.utility(mini)
        if utility != 0:
            return utility
        if depth <= 0:
            return self.score(board, mini)
        min_value = math.inf
        for move in board.get_legal_moves():
            min_value = min(min_value,
                            self.max_value(board.forecast_move(move),
                                           depth - 1, alpha, beta))
            if min_value <= alpha:
                return min_value
            beta = min(beta, min_value)
        return min_value

"""
 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3  AB_Custom_4  AB_Custom_5
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      49  |   1    48  |   2    48  |   2    47  |   3    50  |   0    47  |   3
    2       MM_Open     38  |  12    33  |  17    38  |  12    32  |  18    38  |  12    35  |  15
    3      MM_Center    45  |   5    41  |   9    45  |   5    43  |   7    42  |   8    44  |   6
    4     MM_Improved   31  |  19    32  |  18    36  |  14    32  |  18    36  |  14    33  |  17
    5       AB_Open     27  |  23    20  |  30    26  |  24    20  |  30    20  |  30    16  |  34
    6      AB_Center    30  |  20    23  |  27    23  |  27    28  |  22    26  |  24    24  |  26
    7     AB_Improved   26  |  24    20  |  30    21  |  29    20  |  30    25  |  25    21  |  29
--------------------------------------------------------------------------
           Win Rate:      70.3%        62.0%        67.7%        63.4%        67.7%        62.9%

Blanks mean:  18.467142857142857
"""
