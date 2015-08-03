import unittest

from minimax_kata.interface.game_interpreter import GameInterpreter
from minimax_kata.arena                      import DIRECTIONS

class TestGameInterpreter(unittest.TestCase):
  def setUp(self):
    self.game_string = """\
      ██████████
      ██① ☐ ☐ ██
      ██↓ ☐ ▲ ██
      ██☐ ☐ ② ██
      ██████████"""

    self.game_string = self.game_string.replace("      ", "")
    self.interpreted_game = GameInterpreter(self.game_string).do()

  def test_width(self):
    self.assertEqual(
      self.interpreted_game.arena.get_width(), 3
    )

  def test_length(self):
    self.assertEqual(
      self.interpreted_game.arena.get_length(), 3
    )

  def test_player1_position(self):
    self.assertEqual(
      self.interpreted_game.player1.position, (1, 2)
    )

  def test_player1_direction(self):
    self.assertEqual(
      self.interpreted_game.player1.direction, DIRECTIONS.south
    )

  def test_player2_position(self):
    self.assertEqual(
      self.interpreted_game.player2.position, (3, 2)
    )

  def test_player2_direction(self):
    self.assertEqual(
      self.interpreted_game.player2.direction, DIRECTIONS.north
    )

  def test_player1_trail(self):
    self.assertTrue(
      self.interpreted_game.get_owner((1, 1))
        is self.interpreted_game.player1
    )

  def test_player2_trail(self):
    self.assertTrue(
      self.interpreted_game.get_owner((3, 3))
        is self.interpreted_game.player2
    )

class TestOwnershipRegression(unittest.TestCase):
  def setUp(self):
    self.game_string = """\
      ████████
      ██↓ ② ██
      ██☐ ▼ ██
      ████████"""

    self.game_string = self.game_string.replace("      ", "")
    self.interpreted_game = GameInterpreter(self.game_string).do()

  def test_player2_trail(self):
    self.assertTrue(
      self.interpreted_game.get_owner((2, 1))
        is self.interpreted_game.player2
    )
