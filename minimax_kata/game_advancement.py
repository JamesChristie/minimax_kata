from minimax_kata                import arena
from minimax_kata.executioner    import Executioner
from minimax_kata.game_presenter import GamePresenter

class GameAdvancement:
  def __init__(self, game, move):
    self.game              = game
    self.move              = move
    self.original_position = self.get_current_player().position

  def get_current_player(self):
    return self.move.player

  def opposing_player(self):
    return next(
      player for player
      in [self.game.player1, self.game.player2]
      if player != self.get_current_player()
    )

  def do(self):
    if self.move.is_valid():
      self.__move_player()
      self.__claim_arena_space()

    self.__perform_executions()
    self.game.update_current_player()

    return GamePresenter(self.game)

  # Private

  def __move_player(self):
    self.get_current_player().position  = self.move.new_position()
    self.get_current_player().direction = self.move.direction

  def __claim_arena_space(self):
    self.game.claim_space_for(
      self.get_current_player(), self.original_position
    )

  def __perform_executions(self):
    Executioner(self.game).do()
