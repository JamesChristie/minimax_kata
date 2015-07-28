import unittest

from unittest.mock import MagicMock

from minimax_kata.game_advancement import GameAdvancement
from minimax_kata.game             import Game
from minimax_kata.move             import Move
from minimax_kata.arena            import DIRECTIONS
from minimax_kata.arena            import translated_position

class TestAdvancingInvalidMove(unittest.TestCase):
  def setUp(self):
    self.game            = Game()
    self.space           = self.game.arena.space
    self.player          = self.game.player1
    self.player.position = (1, 1)
    self.move            = Move(self.player, DIRECTIONS.south)
    self.new_position    = translated_position(
      self.player.position, DIRECTIONS.south
    )

    # Assume the move reports invalid
    self.move.is_valid = MagicMock(return_value=False)

    self.advancement = GameAdvancement(self.game, self.move)

  def test_player_position(self):
    self.assertEqual(
      self.player.position, (1, 1)
    )

  def test_player_direction(self):
    self.assertEqual(
      self.player.direction, DIRECTIONS.south
    )

  def test_player_vital_status(self):
    self.assertTrue(self.player.is_alive())

  def test_arena_space_ownership(self):
    self.assertIsNone(
      self.space[self.new_position]
    )
