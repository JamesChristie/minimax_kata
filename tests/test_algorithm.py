import unittest

import minimax_kata

class TestShouldTieInTwoByThree(unittest.TestCase):
  def setUp(self):
    self.game = minimax_kata.get_new_game()
