import unittest

from minimax_kata.game        import Game
from minimax_kata.game_copier import GameCopier

class TestGameCopier(unittest.TestCase):
  def setUp(self):
    self.game                = Game()
    self.game.current_player = self.game.player1
    self.game.last_player    = self.game.player2

    self.copy       = GameCopier(self.game).generate()
    self.arena      = self.game.arena
    self.arena_copy = self.copy.arena

  def test_arena_identity(self):
    self.assertFalse(
      self.game.arena is self.copy.arena
    )

  def test_arena_width(self):
    self.assertEqual(
      self.arena_copy.get_width(),  self.arena.get_width()
    )

  def test_arena_length(self):
    self.assertEqual(
      self.arena_copy.get_length(), self.arena.get_length()
    )

  def test_arena_space(self):
    self.assertEqual(
      self.arena_copy.space,  self.arena.space
    )

  def test_player_one(self):
    self.assertEqual(
      self.game.player1, self.copy.player1
    )

  def test_player_one_identity(self):
    self.assertTrue(
      self.game.player1 is not self.copy.player1
    )

  def test_player_two(self):
    self.assertEqual(
      self.game.player2, self.copy.player2
    )

  def test_player_two_identity(self):
    self.assertTrue(
      self.game.player2 is not self.copy.player2
    )

  def test_current_player(self):
    self.assertEqual(
      self.game.current_player, self.copy.current_player
    )

  def test_current_player_identity(self):
    self.assertTrue(
      self.game.current_player is not self.copy.current_player
    )

  def test_next_player(self):
    self.assertEqual(
      self.game.get_next_player(), self.copy.get_next_player()
    )

  def test_next_player_identity(self):
    self.assertTrue(
      self.game.get_next_player() is not self.copy.get_next_player()
    )

  def test_last_player(self):
    self.assertEqual(
      self.game.last_player, self.copy.last_player
    )

  def test_last_player_identity(self):
    self.assertTrue(
      self.game.last_player is not self.copy.last_player
    )
