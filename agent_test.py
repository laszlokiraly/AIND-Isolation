#!/Users/laszlo/anaconda2/envs/aind/bin/python
"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
from isolation import Board
import game_agent
from game_agent import MinimaxPlayer, IsolationPlayer

# either deactivate reload, so that the test can be executed without error with atom script
# or add magic line #!/Users/laszlo/anaconda2/envs/aind/bin/python to top of file
from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = MinimaxPlayer(IsolationPlayer())
        self.player2 = MinimaxPlayer(IsolationPlayer())
        self.game = Board(self.player1, self.player2)

    def test_correctPlayersToMove(self):
        self.assertEqual(self.player1, self.game.active_player)
        self.game.apply_move((2, 3))
        self.assertEqual(self.player2, self.game.active_player)
        self.game.apply_move((0, 5))
        self.assertEqual(self.player1, self.game.active_player)

    def test_Game(self):
        # print(self.game.to_string())
        winner, history, outcome = self.game.play()
        self.assertEqual("forfeit", outcome)

    def test_differentPlayers(self):
        self.assertNotEqual(self.player1, self.player2)

if __name__ == '__main__':
    unittest.main()
