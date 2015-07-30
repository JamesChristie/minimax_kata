from minimax_kata.move import valid_directions_for

class GamePresenter:
  def __init__(self, game):
    self.game = game

  def get_current_arena_state(self):
    pass

  def get_current_player(self):
    return self.game.current_player

  def get_available_directions(self):
    direction = self.get_current_player().direction
    return valid_directions_for(direction)

  def get_next_player(self):
    return self.game.get_next_player()

  def get_player_one_postion(self):
    return self.game.player1.position

  def get_player_two_postion(self):
    return self.game.player2.position

  def get_copy(self):
    return GameCopier(self.game).generate()

  def get_text_visualization(self):
    return GameTextView(self.game).generate()
