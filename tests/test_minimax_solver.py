import unittest

import minimax_kata

from minimax_kata.minimax_solver import MinimaxSolver

class TestShouldTieInTwoByThree(unittest.TestCase):
  def setUp(self):
    self.game    = minimax_kata.get_new_game()
    self.player1 = self.game.player1
    self.player2 = self.game.player2

    self.new_space = {
      (1, 1): self.player1, (1, 2): None,
      (1, 2): None,         (2, 2): None,
      (1, 3): None,         (2, 3): self.player2
    }

    self.player1_position = (1, 2)
    self.player2_position = (2, 2)

    minimax_kata.set_arena_state(
      self.game, self.new_space,
      self.player1_position, self.player2_position
    )

    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
      set(self.minimax_solver.get_best_moves()),
      set([(2, 2)])
    )
