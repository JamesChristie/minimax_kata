import unittest

from minimax_kata import arena_tools

class TestGetNewSpace(unittest.TestCase):
  def setUp(self):
    self.space = arena_tools.get_new_space(3, 3)

    self.expected_space = {
        (1, 1): None, (1, 2): None, (1, 3): None,
        (2, 1): None, (2, 2): None, (2, 3): None,
        (3, 1): None, (3, 2): None, (3, 3): None
    }

  def test_space(self):
    self.assertEqual(self.space, self.expected_space)
