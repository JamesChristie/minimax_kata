from minimax_kata.arena  import DIRECTIONS
from minimax_kata.arena  import Arena
from minimax_kata.player import Player

class Game:
  def __init__(self, player_one_name="1", player_two_name="2"):
    self.arena   = Arena()
    self.player1 = Player(
      player_one_name,
      self.arena.get_upper_left_position()
    )
    self.player2 = Player(
      player_two_name,
      self.arena.get_lower_right_position()
    )

    self.player1.direction = DIRECTIONS.south
    self.player2.direction = DIRECTIONS.north

  def is_over(self):
    return (
      self.player1.is_dead() or self.player2.is_dead()
    )

  def is_tie(self):
    return (
      self.player1.is_dead() and self.player2.is_dead()
    )

  def is_won(self):
    return (
      not self.is_tie() and self.is_over()
    )

  def get_winner(self):
    if self.is_won():
      return next(
        player for player
        in [self.player1, self.player2]
        if player.is_alive()
      )
