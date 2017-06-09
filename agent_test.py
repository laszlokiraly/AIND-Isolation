#!/Users/laszlo/anaconda2/envs/aind/bin/python
"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

# either deactivate reload, so that the test can be executed without error with atom script
# or add magic line #!/Users/laszlo/anaconda2/envs/aind/bin/python to top of file
from importlib import reload

# import isolation
from isolation import Board
import game_agent
from game_agent import MinimaxPlayer, custom_score
from sample_players import improved_score


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = MinimaxPlayer(search_depth=1, score_fn=improved_score, timeout=10.)
        self.player2 = MinimaxPlayer(search_depth=1, score_fn=improved_score, timeout=10.)
        self.game = Board(self.player1, self.player2)

    def test_game_setup(self):
        """
        smoke check game setup
        """
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        winner, history, outcome = self.game.play()
        gwinner = "1" if winner == self.player1 else "2"
        print("\nWinner: {}\nOutcome: {}".format(gwinner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))
        print(self.game._board_state)

    def test_successive_moves(self):
        """
        checks player 1 and 2 move one after the other
        """
        self.assertEqual(self.player1, self.game.active_player)
        self.game.apply_move((2, 3))
        self.assertEqual(self.player2, self.game.active_player)
        self.game.apply_move((0, 5))
        self.assertEqual(self.player1, self.game.active_player)

    def test_different_players(self):
        """
        check that players are different
        """
        self.assertNotEqual(self.player1, self.player2)

    def test_board_state(self):
        self.game.set_board_state([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 65])
        print(
        """
AssertionError: False is not true : Your MinimaxAgent.minimax function returned a move that was not one of the optimal moves for the given heurisitc.
Available choices:
[(0, 6), (1, 5)]
Your Selection:
(0, 8)

Test Case Details:
------------------
Heuristic: improved_score
Depth limit: 1
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   | - | - | - |   | 1 |   |
3  |   | - | - | - | - | - | - |   |   |
4  |   |   | - | - |   |   | - |   |   |
5  |   |   | - | - |   | - | - |   |   |
6  |   |   | - | - | - | - |   |   |   |
7  |   |   |   |   | 2 |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 43, 65]        """
        )
        print(self.game.to_string())
        self.game.play(time_limit=9999000, rounds=1)
        print(self.game.to_string())
        self.assertIn(self.game.get_player_location(self.player1), [(0, 6), (1, 5)], "Your MinimaxAgent.minimax function returned a move that was not one of the optimal moves for the given heurisitc.")

if __name__ == '__main__':
    unittest.main()
