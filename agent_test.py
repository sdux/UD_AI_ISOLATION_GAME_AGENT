"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest
import isolation
import game_agent

from importlib import reload
print('this prints')

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""
    print('IsolationTest main class - this prints')

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        print("this doesn't print")

if __name__ == '__main__':
    unittest.main() 
    
    game.apply_move((2, 3))
    game.apply_move((0, 5))
    print(game.to_string())
    print("this doesn't print either :(")
    # get a list of the legal moves available to the active player
    print(game.get_legal_moves())