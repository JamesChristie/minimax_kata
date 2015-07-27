import unittest

from minimax_kata.arena import Arena

class TestArena(unittest.TestCase):
  def setUp(self):
    self.arena = Arena(2, 3)

    self.expected_space = {
      (1, 1): None, (1, 2): None,
      (2, 1): None, (2, 2): None,
      (3, 1): None, (3, 2): None
    }

  def test_width(self):
    self.assertEqual(self.arena.width, 2)

  def test_length(self):
    self.assertEqual(self.arena.length, 3)

  def test_space(self):
    self.assertEqual(self.arena.space, self.expected_space)

  def test_get_upper_left_position(self):
    self.assertEqual(
      self.arena.get_upper_left_position(), (1, 1)
    )

  def test_get_upper_right_position(self):
    self.assertEqual(
      self.arena.get_upper_right_position(), (2, 1)
    )

  def test_get_lower_left_position(self):
    self.assertEqual(
      self.arena.get_lower_left_position(), (1, 3)
    )

  def test_get_lower_right_position(self):
    self.assertEqual(
      self.arena.get_lower_right_position(), (2, 3)
    )
