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
from game_agent import AlphaBetaPlayer
from sample_players import improved_score, open_move_score, center_score, null_score


class AlphaBetaIsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = AlphaBetaPlayer(search_depth=2, score_fn=null_score, timeout=10.)
        self.player2 = AlphaBetaPlayer(search_depth=2, score_fn=null_score, timeout=10.)
        self.game = Board(self.player1, self.player2)

    def test_board_state(self):
        print(
        """
AssertionError: Failed to cut off search -- expanded too many nodes. (i.e., your agent did not prune at this node, but a correct alpha beta search did prune at this node when following the same expansion order that your agent followed.)
Alpha: 4.0
Beta: 3.0
Game tree evaluation order:
[(2, 1), (3, 0)]
[(5, 6)]

Nodes are shown with each layer sorted in the order the nodes were expanded
during search.  All nodes in each successive layer are children of the
furthest-right node in the parent layer above it.

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 2
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   |   | - | - |   |   |   |   |
3  |   |   | - | - | - | - | - |   |   |
4  |   |   | 1 | - | - | - | - |   |   |
5  |   |   | - |   | - | - |   |   |   |
6  |   |   | - | - |   | - | - |   |   |
7  |   |   |   |   |   | 2 |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 22]
        """
        )
        self.game.set_board_state([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 52, 22])
        print(self.game.to_string())
        self.game.play(rounds=1)
        # for debugging:
        # self.game.play(time_limit=9999000, rounds=1)
        print(self.game.to_string())
        # which heuristic?  & possibility to set alpha, beta directly! :(
        # self.assertIn(self.game.get_player_location(self.player1), [(2, 1), (3, 0)], "Failed to cut off search -- expanded too many nodes.")

    def test_board_state_2(self):
        print(
        """
AssertionError: Failed to cut off search -- expanded too many nodes. (i.e., your agent did not prune at this node, but a correct alpha beta search did prune at this node when following the same expansion order that your agent followed.)
Alpha: 3.0
Beta: 2.0
Game tree evaluation order:
[(0, 2), (0, 4)]
[(4, 5)]

Nodes are shown with each layer sorted in the order the nodes were expanded
during search.  All nodes in each successive layer are children of the
furthest-right node in the parent layer above it.

Test Case Details:
------------------
Heuristic: open_move_score
Depth limit: 2
Initial Board State:
     0   1   2   3   4   5   6   7   8
0  |   |   |   |   |   |   |   |   |   |
1  |   |   |   |   |   |   |   |   |   |
2  |   |   | - | 1 |   | - |   |   |   |
3  |   |   |   |   |   |   |   |   |   |
4  |   |   | - | - | - |   | - |   |   |
5  |   |   | - |   | - | - |   |   |   |
6  |   |   |   | - | 2 |   |   |   |   |
7  |   |   |   |   |   |   |   |   |   |
8  |   |   |   |   |   |   |   |   |   |

game._board_state:
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 29]
        """
        )
        self.game.set_board_state([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 29])
        print(self.game.to_string())
        self.game.play(rounds=1)
        # for debugging:
        # self.game.play(time_limit=9999000, rounds=1)
        print(self.game.to_string())
        # which heuristic? & possibility to set alpha, beta directly! :(
        # self.assertIn(self.game.get_player_location(self.player1), [(0, 2), (0, 4)], "Failed to cut off search -- expanded too many nodes.")

if __name__ == '__main__':
    unittest.main()
