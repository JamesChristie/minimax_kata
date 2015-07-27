import unittest

from minimax_kata.player import Player

class TestBasicPlayer(unittest.TestCase):
  def setUp(self):
    self.player = Player("Ada", (1, 1))

  def test_name(self):
    self.assertEqual(self.player.name, "Ada")

  def test_position(self):
    self.assertEqual(self.player.position, (1, 1))

  def test_direction(self):
    self.assertIsNone(self.player.direction)

  def test_is_alive(self):
    self.assertTrue(self.player.is_alive())

  def test_is_dead(self):
    self.assertFalse(self.player.is_dead())
