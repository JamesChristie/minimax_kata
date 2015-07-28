import unittest

from minimax_kata.game        import Game
from minimax_kata.game_copier import GameCopier

class TestGameCopier(unittest.TestCase):
  def setUp(self):
    self.game       = Game()
    self.copy       = GameCopier(self.game).generate()
    self.arena      = self.game.arena
    self.arena_copy = self.copy.arena

  def test_arena_identity(self):
    self.assertFalse(
      self.game.arena is self.copy.arena
    )

  def test_arena_width(self):
    self.assertEqual(
      self.arena_copy.width,  self.arena.width
    )

  def test_arena_length(self):
    self.assertEqual(
      self.arena_copy.length, self.arena.length
    )

  def test_arena_space(self):
    self.assertEqual(
      self.arena_copy.space,  self.arena.space
    )

  def test_player_one(self):
    self.assertTrue(
      self.game.player1 is self.copy.player1
    )

  def test_player_two(self):
    self.assertTrue(
      self.game.player2 is self.copy.player2
    )
