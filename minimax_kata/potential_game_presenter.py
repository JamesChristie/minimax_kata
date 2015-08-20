from minimax_kata.move             import Move
from minimax_kata.game_advancement import GameAdvancement
from minimax_kata.executioner      import Executioner

class PotentialGamePresenter:
  def __init__(self, given_game, direction):
    self.potential_game = given_game.get_copy()
    self.direction      = direction
    self.subject        = self.potential_game.current_player

    move = Move(self.subject, self.direction)
    GameAdvancement(self.potential_game, move).do()

  def is_wall(self):
    return self.potential_game.player_is_out_of_bounds(self.subject)

  def is_trail(self):
    owner = self.potential_game.get_owner(self.subject.position)

    return owner is not None

  def is_crash(self):
    return Executioner(self.potential_game).collision_has_ocurred()
