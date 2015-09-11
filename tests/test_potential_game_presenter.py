import unittest

from minimax_kata.potential_game_presenter import PotentialGamePresenter
from minimax_kata.arena                    import DIRECTIONS

from minimax_kata.interface.game_interpreter import GameInterpreter

class TestPotentialGamePresenter(unittest.TestCase):
  def setUp(self):
    self.game_string  = """\
      ██████
      ██↓ ██
      ██☐ ██
      ██▲ ██
      ██████"""

    self.game = GameInterpreter(self.game_string.replace("      ", "")).do()
    self.presenter = PotentialGamePresenter(self.game, DIRECTIONS.south)

  def test_get_current_player(self):
    self.assertEqual(
      self.presenter.get_current_player(),
      self.game.player2
    )

  def test_is_alive(self):
    self.assertTrue(self.presenter.is_alive())

  def test_is_wall(self):
    self.assertFalse(self.presenter.is_wall())

  def test_is_trail(self):
    self.assertFalse(self.presenter.is_trail())

  def test_is_crash(self):
    self.assertFalse(self.presenter.is_crash())
