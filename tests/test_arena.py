import unittest

from minimax_kata.arena  import DIRECTIONS
from minimax_kata.arena  import translated_position
from minimax_kata.arena  import Arena
from minimax_kata.player import Player

class TestNorthTranslation(unittest.TestCase):
  def setUp(self):
    self.position  = (2, 2)
    self.direction = DIRECTIONS.north

  def test_translated_position(self):
    self.assertEqual(
      translated_position(self.position, self.direction), (2, 1)
    )

class TestEastTranslation(unittest.TestCase):
  def setUp(self):
    self.position  = (2, 2)
    self.direction = DIRECTIONS.east

  def test_translated_position(self):
    self.assertEqual(
      translated_position(self.position, self.direction), (3, 2)
    )

class TestSouthTranslation(unittest.TestCase):
  def setUp(self):
    self.position  = (2, 2)
    self.direction = DIRECTIONS.south

  def test_translated_position(self):
    self.assertEqual(
      translated_position(self.position, self.direction), (2, 3)
    )

class TestWestTranslation(unittest.TestCase):
  def setUp(self):
    self.position  = (2, 2)
    self.direction = DIRECTIONS.west

  def test_translated_position(self):
    self.assertEqual(
      translated_position(self.position, self.direction), (1, 2)
    )

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

  def test_player_is_in_bounds_for_in_bounds_player(self):
    player = Player("Test", (1, 1))

    self.assertTrue(
      self.arena.player_is_in_bounds(player)
    )

  def test_player_is_in_bounds_for_out_of_bounds_player(self):
    player = Player("Test", (0, 17))

    self.assertFalse(
      self.arena.player_is_in_bounds(player)
    )

  def test_claim_space_for_unclaimed_space(self):
    player = Player("Test", (1, 1))

    self.arena.claim_space_for(player, (1, 2))

    self.assertEqual(
      self.arena.space.get((1, 2)), player
    )

  def test_claim_space_for_out_of_bounds_space(self):
    player = Player("Test", (1, 1))

    self.arena.claim_space_for(player, (0, 0))

    self.assertIsNone(
      self.arena.space.get(player.position, None)
    )

  def test_claim_space_for_claimed_space(self):
    player  = Player("Test", (1, 1))
    player2 = Player("Already Here", (1, 2))

    self.arena.space[(3, 3)] = player2

    self.arena.claim_space_for(player, (3, 3))

    self.assertEqual(
      self.arena.space.get((3, 3)), player2
    )
