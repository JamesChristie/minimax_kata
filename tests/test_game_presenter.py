import unittest

from minimax_kata.game_presenter   import GamePresenter
from minimax_kata.space_presenters import Space
from minimax_kata.space_presenters import Trail
from minimax_kata.space_presenters import Player
from minimax_kata.game             import Game
from minimax_kata.arena            import DIRECTIONS

class TestGamePresenter(unittest.TestCase):
  def setUp(self):
    self.game      = Game()
    self.presenter = GamePresenter(self.game)
    self.space     = self.game.arena.space

    self.space[(1, 1)] = self.game.player1
    self.space[(4, 4)] = self.game.player2

    self.game.player1.position = (1, 2)
    self.game.player2.position = (4, 3)

    self.game.player1.direction = DIRECTIONS.north

    self.game.current_player = self.game.player1

  def test_get_current_arena_state(self):
    pass

  def test_get_available_directions(self):
    expected_directions = [
      DIRECTIONS.west,
      DIRECTIONS.north,
      DIRECTIONS.east
    ]

    self.assertEqual(
      set(self.presenter.get_available_directions()),
      set(expected_directions)
    )

  def test_get_current_player(self):
    self.assertEqual(
      self.presenter.get_current_player(), self.game.player1
    )

  def test_get_next_player(self):
    self.assertEqual(
      self.presenter.get_next_player(), self.game.player2
    )

  def test_get_current_player_position(self):
    self.assertEqual(
      self.presenter.get_current_player_position(), (1, 2)
    )
