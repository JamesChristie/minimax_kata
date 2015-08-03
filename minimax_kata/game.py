from minimax_kata.move           import valid_directions_for
from minimax_kata.arena          import DIRECTIONS
from minimax_kata.arena          import Arena
from minimax_kata.player         import Player
from minimax_kata.game_copier    import GameCopier
from minimax_kata.game_text_view import GameTextView

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

    self.move_count     = 0
    self.last_player    = None
    self.current_player = self.player1

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

  def get_owner(self, position):
    return self.arena.get_owner(position)

  def player_is_in_bounds(self, player):
    return self.arena.player_is_in_bounds(player)

  def player_is_out_of_bounds(self, player):
    return self.arena.player_is_out_of_bounds(player)

  def claim_space_for(self, player, position):
    self.arena.claim_space_for(player, position)

  def get_next_player(self):
    if not self.is_won():
      return next(
        player for player
        in [self.player1, self.player2]
        if player is not self.current_player
      )

  def get_available_directions(self):
    direction = self.current_player.direction
    return valid_directions_for(direction)

  def get_copy(self):
    return GameCopier(self).generate()

  def render_current_arena_state(self):
    return GameTextView(self).generate()
