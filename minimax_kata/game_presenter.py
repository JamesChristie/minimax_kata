from minimax_kata.move           import valid_directions_for
from minimax_kata.game_copier    import GameCopier
from minimax_kata.game_text_view import GameTextView

class GamePresenter:
  def __init__(self, game):
    self.game    = game
    self.player1 = self.game.player1
    self.player2 = self.game.player2

  def get_current_arena_state(self):
    pass

  def get_current_player(self):
    return self.game.current_player

  def get_available_directions(self):
    direction = self.get_current_player().direction
    return valid_directions_for(direction)

  def get_next_player(self):
    return self.game.get_next_player()

  def get_current_player_position(self):
    return self.get_current_player().position

  def get_copy(self):
    return GameCopier(self.game).generate()

  def get_text_visualization(self):
    return GameTextView(self.game).generate()
