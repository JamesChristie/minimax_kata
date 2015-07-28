import unittest

from minimax_kata.executioner import Executioner
from minimax_kata.game        import Game

class TestGameWithNoDeaths(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.position = (1, 1)
    self.game.player2.position = (1, 2)

    Executioner(self.game).do()

  def test_player1_vital_status(self):
    self.assertTrue(self.game.player1.is_alive())

  def test_player2_vital_status(self):
    self.assertTrue(self.game.player2.is_alive())

class TestGameWithPlayerInWall(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.position = (0, 1)
    self.game.player2.position = (1, 2)

    Executioner(self.game).do()

  def test_player1_vital_status(self):
    self.assertTrue(self.game.player1.is_dead())

  def test_player2_vital_status(self):
    self.assertTrue(self.game.player2.is_alive())

class TestGameWithPlayerInClaimedSpace(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.position = (1, 1)
    self.game.player2.position = (1, 2)

    self.game.arena.space[(1, 2)] = self.game.player1

    Executioner(self.game).do()

  def test_player1_vital_status(self):
    self.assertTrue(self.game.player1.is_alive())

  def test_player2_vital_status(self):
    self.assertTrue(self.game.player2.is_dead())

class TestGameWithPlayersInSameSpace(unittest.TestCase):
  def setUp(self):
    self.game = Game()
    self.game.player1.position = (1, 1)
    self.game.player2.position = (1, 1)

    Executioner(self.game).do()

  def test_player1_vital_status(self):
    self.assertTrue(self.game.player1.is_dead())

  def test_player2_vital_status(self):
    self.assertTrue(self.game.player2.is_dead())
