# NOTE (JamesChristie) This suite ended up being useful
# as a set of integration specs, since this is the primary
# driver of the most important logic for the game

import unittest

from unittest.mock import MagicMock

from minimax_kata.game_advancement import GameAdvancement
from minimax_kata.game             import Game
from minimax_kata.move             import Move
from minimax_kata.arena            import DIRECTIONS
from minimax_kata.arena            import translated_position

class TestAdvancingInvalidMove(unittest.TestCase):
  def setUp(self):
    self.game                = Game()
    self.space               = self.game.arena.space
    self.player              = self.game.player1
    self.player2             = self.game.player2
    self.game.current_player = self.player
    self.player.position     = (1, 1)
    self.move                = Move(self.player, DIRECTIONS.south)
    self.new_position        = translated_position(
      self.player.position, DIRECTIONS.south
    )

    # Assume the move reports as invalid
    self.move.is_valid = MagicMock(return_value=False)

    GameAdvancement(self.game, self.move).do()

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

  def test_player2_vital_status(self):
    self.assertTrue(self.player2.is_alive())

  def test_arena_space_ownership(self):
    self.assertIsNone(
      self.space.get((1, 1), None)
    )

  def test_game_is_over(self):
    self.assertFalse(self.game.is_over())

  def test_game_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_game_is_won(self):
    self.assertFalse(self.game.is_won())

  def test_game_get_winner(self):
    self.assertIsNone(self.game.get_winner())

  def test_current_player(self):
    self.assertTrue(
      self.game.current_player is self.player
    )

  def test_last_player(self):
    self.assertIsNone(self.game.last_player)

class TestAdvancingValidMoveToEmptySpace(unittest.TestCase):
  def setUp(self):
    self.game                = Game()
    self.space               = self.game.arena.space
    self.player              = self.game.player1
    self.player2             = self.game.player2
    self.game.current_player = self.player
    self.player.position     = (1, 1)
    self.move                = Move(self.player, DIRECTIONS.south)
    self.new_position        = translated_position(
      self.player.position, DIRECTIONS.south
    )

    self.space[self.new_position] = None

    GameAdvancement(self.game, self.move).do()

  def test_player_position(self):
    self.assertEqual(
      self.player.position, (1, 2)
    )

  def test_player_direction(self):
    self.assertEqual(
      self.player.direction, DIRECTIONS.south
    )

  def test_player_vital_status(self):
    self.assertTrue(self.player.is_alive())

  def test_player2_vital_status(self):
    self.assertTrue(self.player2.is_alive())

  def test_arena_space_ownership(self):
    self.assertEqual(
      self.space.get((1, 1), None), self.player
    )

  def test_game_is_over(self):
    self.assertFalse(self.game.is_over())

  def test_game_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_game_is_won(self):
    self.assertFalse(self.game.is_won())

  def test_game_get_winner(self):
    self.assertIsNone(self.game.get_winner())

  def test_current_player(self):
    self.assertTrue(
      self.game.current_player is self.player2
    )

  def test_last_player(self):
    self.assertTrue(
      self.game.last_player is self.player
    )

class TestAdvancingValidMoveToClaimedSpace(unittest.TestCase):
  def setUp(self):
    self.game            = Game()
    self.space           = self.game.arena.space
    self.player          = self.game.player1
    self.player2         = self.game.player2
    self.player.position = (1, 1)
    self.move            = Move(self.player, DIRECTIONS.south)
    self.new_position    = translated_position(
      self.player.position, DIRECTIONS.south
    )

    self.space[self.new_position] = self.player2

    GameAdvancement(self.game, self.move).do()

  def test_player_position(self):
    self.assertEqual(
      self.player.position, (1, 2)
    )

  def test_player_direction(self):
    self.assertEqual(
      self.player.direction, DIRECTIONS.south
    )

  def test_player_vital_status(self):
    self.assertTrue(self.player.is_dead())

  def test_player2_vital_status(self):
    self.assertTrue(self.player2.is_alive())

  def test_arena_space_ownership(self):
    self.assertEqual(
      self.space.get((1, 2), None), self.player2
    )

  def test_game_is_over(self):
    self.assertTrue(self.game.is_over())

  def test_game_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_game_is_won(self):
    self.assertTrue(self.game.is_won())

  def test_game_get_winner(self):
    self.assertEqual(
      self.game.get_winner(), self.player2
    )

class TestAdvancingValidMoveToWall(unittest.TestCase):
  def setUp(self):
    self.game            = Game()
    self.space           = self.game.arena.space
    self.player          = self.game.player1
    self.player2         = self.game.player2
    self.player.position = (1, 1)
    self.move            = Move(self.player, DIRECTIONS.west)
    self.new_position    = translated_position(
      self.player.position, DIRECTIONS.west
    )

    GameAdvancement(self.game, self.move).do()

  def test_player_position(self):
    self.assertEqual(
      self.player.position, (0, 1)
    )

  def test_player_direction(self):
    self.assertEqual(
      self.player.direction, DIRECTIONS.west
    )

  def test_player_vital_status(self):
    self.assertTrue(self.player.is_dead())

  def test_player2_vital_status(self):
    self.assertTrue(self.player2.is_alive())

  def test_arena_space_ownership(self):
    self.assertIsNone(
      self.space.get((1, 1), None)
    )

  def test_game_is_over(self):
    self.assertTrue(self.game.is_over())

  def test_game_is_tie(self):
    self.assertFalse(self.game.is_tie())

  def test_game_is_won(self):
    self.assertTrue(self.game.is_won())

  def test_game_get_winner(self):
    self.assertEqual(
      self.game.get_winner(), self.player2
    )

class TestAdvancingValidMoveToOtherPlayer(unittest.TestCase):
  def setUp(self):
    self.game             = Game()
    self.space            = self.game.arena.space
    self.player           = self.game.player1
    self.player2          = self.game.player2
    self.player.position  = (1, 1)
    self.player2.position = (1, 2)
    self.move             = Move(self.player, DIRECTIONS.south)
    self.new_position     = translated_position(
      self.player.position, DIRECTIONS.west
    )

    GameAdvancement(self.game, self.move).do()

  def test_player_position(self):
    self.assertEqual(
      self.player.position, (1, 2)
    )

  def test_player_direction(self):
    self.assertEqual(
      self.player.direction, DIRECTIONS.south
    )

  def test_player_vital_status(self):
    self.assertTrue(self.player.is_dead())

  def test_player2_vital_status(self):
    self.assertTrue(self.player2.is_dead())

  def test_arena_space_ownership(self):
    self.assertEqual(
      self.space.get((1, 1)), self.player
    )

  def test_game_is_over(self):
    self.assertTrue(self.game.is_over())

  def test_game_is_tie(self):
    self.assertTrue(self.game.is_tie())

  def test_game_is_won(self):
    self.assertFalse(self.game.is_won())

  def test_game_get_winner(self):
    self.assertIsNone(self.game.get_winner())
