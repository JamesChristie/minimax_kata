import unittest

from minimax_kata.move   import Move
from minimax_kata.game   import Game
from minimax_kata.player import Player
from minimax_kata.arena  import DIRECTIONS

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
