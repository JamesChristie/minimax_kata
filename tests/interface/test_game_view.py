import unittest
import textwrap

import minimax_kata

from minimax_kata.interface.game_view import GameView

from minimax_kata.arena     import DIRECTIONS
from minimax_kata.interface import WALL_SPACE_CHAR
from minimax_kata.interface import EMPTY_SPACE_CHAR
from minimax_kata.interface import PLAYER_ONE_TRAIL_CHAR
from minimax_kata.interface import PLAYER_TWO_TRAIL_CHAR
from minimax_kata.interface import PLAYER_ONE_CHARS
from minimax_kata.interface import PLAYER_TWO_CHARS
from minimax_kata.interface import CRASH_CHAR

class TestGameViewWithoutCrash(unittest.TestCase):
  def setUp(self):
    self.game    = minimax_kata.get_new_game()
    self.player1 = self.game.player1
    self.player2 = self.game.player2

    self.new_space = {
      (1, 1): self.player1, (2, 1): None, (3, 1): None,
      (1, 2): None,         (2, 2): None, (3, 2): None,
      (1, 3): None,         (2, 3): None, (3, 3): self.player2
    }

    self.player1.position  = (1, 2)
    self.player1.direction = DIRECTIONS.south
    self.player2.position  = (3, 2)
    self.player2.direction = DIRECTIONS.north

    minimax_kata.set_arena_state(
      self.game, self.new_space,
      self.player1.position, self.player2.position
    )

    self.expected_view  = """\
      ██████████
      ██① ☐ ☐ ██
      ██↓ ☐ ▲ ██
      ██☐ ☐ ② ██
      ██████████"""

  def test_render(self):
    self.assertEqual(
      GameView(self.game).render(),
      self.expected_view.replace("      ", "")
    )

class TestGameViewWithCrash(unittest.TestCase):
  def setUp(self):
    self.game    = minimax_kata.get_new_game()
    self.player1 = self.game.player1
    self.player2 = self.game.player2

    self.new_space = {
      (1, 1): self.player1, (2, 1): None, (3, 1): None,
      (1, 2): self.player1, (2, 2): None, (3, 2): self.player2,
      (1, 3): None,         (2, 3): None, (3, 3): self.player2
    }

    self.player1.position  = (2, 2)
    self.player1.direction = DIRECTIONS.east
    self.player2.position  = (2, 2)
    self.player2.direction = DIRECTIONS.west

    minimax_kata.set_arena_state(
      self.game, self.new_space,
      self.player1.position, self.player2.position
    )

    self.expected_view  = """\
      ██████████
      ██① ☐ ☐ ██
      ██① 🔥 ② ██
      ██☐ ☐ ② ██
      ██████████"""

  def test_render(self):
    self.assertEqual(
      GameView(self.game).render(),
      self.expected_view.replace("      ", "")
    )
