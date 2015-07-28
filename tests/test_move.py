import unittest

from minimax_kata.move   import Move
from minimax_kata.move   import valid_directions_for
from minimax_kata.game   import Game
from minimax_kata.player import Player
from minimax_kata.arena  import DIRECTIONS

class TestValidDirectionHelper(unittest.TestCase):
  def setUp(self):
    self.direction        = DIRECTIONS.north
    self.valid_directions = valid_directions_for(self.direction)

  def test_west_is_in_list(self):
    self.assertTrue(
      DIRECTIONS.west in self.valid_directions
    )

  def test_north_is_in_list(self):
    self.assertTrue(
      DIRECTIONS.north in self.valid_directions
    )

  def test_east_is_in_list(self):
    self.assertTrue(
      DIRECTIONS.east in self.valid_directions
    )

  def test_south_not_in_list(self):
    self.assertTrue(
      DIRECTIONS.south not in self.valid_directions
    )

class TestMoveForwardToAnEmptySpace(unittest.TestCase):
  def setUp(self):
    self.player    = Player("Wat", (2, 2))
    self.direction = DIRECTIONS.south

    self.player.direction = DIRECTIONS.south

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertTrue(self.move.is_valid())

class TestMoveRightToAnEmptySpace(unittest.TestCase):
  def setUp(self):
    self.player    = Player("Wat", (2, 2))
    self.direction = DIRECTIONS.west

    self.player.direction = DIRECTIONS.south

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertTrue(self.move.is_valid())

class TestMoveLeftToAnEmptySpace(unittest.TestCase):
  def setUp(self):
    self.player    = Player("Wat", (2, 2))
    self.direction = DIRECTIONS.east

    self.player.direction = DIRECTIONS.south

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertTrue(self.move.is_valid())

class TestMoveBackward(unittest.TestCase):
  def setUp(self):
    self.player    = Player("Wat", (2, 2))
    self.direction = DIRECTIONS.north

    self.player.direction = DIRECTIONS.south

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertFalse(self.move.is_valid())

# NOTE (JamesChristie) Sanity checks, a player should be
# entirely capable of deciding to crash
class TestMoveForwardToAClaimedSpace(unittest.TestCase):
  def setUp(self):
    self.game      = Game()
    self.player    = Player("Wat", (2, 2))
    self.direction = DIRECTIONS.south

    self.player.direction = DIRECTIONS.south

    self.game.player1             = self.player
    self.game.arena.space[(2, 3)] = self.player

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertTrue(self.move.is_valid())

class TestMoveLeftToAWall(unittest.TestCase):
  def setUp(self):
    self.player    = Player("Wat", (3, 2))
    self.direction = DIRECTIONS.east

    self.player.direction = DIRECTIONS.south

    self.move = Move(self.player, self.direction)

  def test_is_valid(self):
    self.assertTrue(self.move.is_valid())
