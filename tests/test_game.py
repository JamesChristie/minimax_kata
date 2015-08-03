import unittest

from minimax_kata.game import Game
from minimax_kata.game import DIRECTIONS

class TestOngoingGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def test_is_over(self):
    self.assertFalse(self.game.is_over())

  def test_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_is_won(self):
    self.assertFalse(self.game.is_won())

  def test_get_winner(self):
    self.assertIsNone(self.game.get_winner())

  def test_get_available_directions(self):
    expected_directions = [
      DIRECTIONS.west,
      DIRECTIONS.south,
      DIRECTIONS.east
    ]

    self.assertEqual(
      set(self.game.get_available_directions()),
      set(expected_directions)
    )

class TestWonGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.alive = False

  def test_is_over(self):
    self.assertTrue(self.game.is_over())

  def test_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_is_won(self):
    self.assertTrue(self.game.is_won())

  def test_get_winner(self):
    self.assertEqual(
      self.game.get_winner(), self.game.player2
    )

class TestTiedGame(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.alive = False
    self.game.player2.alive = False

  def test_is_over(self):
    self.assertTrue(self.game.is_over())

  def test_is_tie(self):
    self.assertTrue(self.game.is_tie())

  def test_is_won(self):
    self.assertFalse(self.game.is_won())

  def test_get_winner(self):
    self.assertIsNone(self.game.get_winner())
