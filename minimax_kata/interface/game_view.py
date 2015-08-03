from minimax_kata.interface             import WALL_SPACE_CHAR
from minimax_kata.interface.char_policy import CharPolicy

class GameView:
  def __init__(self, game):
    self.game    = game
    self.arena   = self.game.arena
    self.player1 = self.game.player1
    self.player2 = self.game.player2

    # Pad vertically and horizontally for bounding
    # wall chars
    self.vizualization = []

    for length in range(self.arena.get_width() + 2):
      self.vizualization.append([])
      for width in range(self.arena.get_length() + 2):
        self.vizualization[-1].append(WALL_SPACE_CHAR)

  def render(self):
    self.__update_vizualization()
    return self.__vizualization_to_string()

  # Private

  def __update_vizualization(self):
    for length in range(1, self.arena.get_length() + 1):
      for width in range(1, self.arena.get_width() + 1):
        self.__mutate_space(length, width)

  def __vizualization_to_string(self):
    inner_join = [''.join(char_list) for char_list in self.vizualization]
    return '\n'.join(inner_join)

  def __mutate_space(self, length, width):
    new_char = CharPolicy(self.game, length, width).get_char()
    self.vizualization[length][width] = new_char
