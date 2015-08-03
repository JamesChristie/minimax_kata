import unittest

import minimax_kata

from minimax_kata.minimax_solver import MinimaxSolver
from minimax_kata.arena          import DIRECTIONS

class TestThatTieIsChosenInOneByTwo(unittest.TestCase):
  def setUp(self):
    self.game    = minimax_kata.get_new_game()
    self.player1 = self.game.player1
    self.player2 = self.game.player2

    self.new_space = {
      (1, 1): None,
      (1, 2): None
    }

    self.player1.position  = (1, 1)
    self.player1.directoin = DIRECTIONS.south
    self.player2.position  = (1, 2)
    self.player2.directoin = DIRECTIONS.north

    minimax_kata.set_arena_state(
      self.game, self.new_space,
      self.player1.position, self.player2.position
    )

    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
      set(self.minimax_solver.get_best_moves()),
      set([DIRECTIONS.south])
    )
