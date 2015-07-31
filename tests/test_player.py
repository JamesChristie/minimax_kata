import unittest

from minimax_kata.player import Player
from minimax_kata.arena  import DIRECTIONS

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

class TestCopiedPlayer(unittest.TestCase):
  def setUp(self):
    self.player           = Player("Ada", (1, 1))
    self.player.direction = DIRECTIONS.north
    self.copy             = self.player.get_copy()

  def test_change_name(self):
    self.player.name = "Someone Else"
    self.assertEqual(self.copy.name, "Ada")

  def test_change_position(self):
    self.player.position = (2, 2)
    self.assertEqual(self.copy.position, (1, 1))

  def test_change_direction(self):
    self.player.direction = DIRECTIONS.south
    self.assertEqual(self.copy.direction, DIRECTIONS.north)
