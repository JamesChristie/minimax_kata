from minimax_kata.interface import PLAYER_ONE_TRAIL_CHAR
from minimax_kata.interface import PLAYER_TWO_TRAIL_CHAR
from minimax_kata.interface import PLAYER_ONE_CHARS
from minimax_kata.interface import PLAYER_TWO_CHARS

class CharInterpreter:
  def __init__(self, game, length, width, char):
    self.game   = game
    self.length = length
    self.width  = width
    self.char   = '{} '.format(char.strip()) # re-pad

  def do(self):
    if self.__is_player1():
      self.game.player1.position  = self.get_position()
      self.game.player1.direction = self.get_direction(PLAYER_ONE_CHARS)
    elif self.__is_player2():
      self.game.player2.position = self.get_position()
      self.game.player2.direction = self.get_direction(PLAYER_TWO_CHARS)
    elif self.__is_player1_trail():
      self.game.claim_space_for(self.game.player1, self.get_position(), force=True)
    elif self.__is_player2_trail():
      self.game.claim_space_for(self.game.player2, self.get_position(), force=True)

  def get_position(self):
    return (self.width, self.length)

  def get_direction(self, directions):
    char_directions = self.__inverted_directions(directions)
    return char_directions.get(self.char, None)

  # Private

  def __is_player1(self):
    return self.char in PLAYER_ONE_CHARS.values()

  def __is_player2(self):
    return self.char in PLAYER_TWO_CHARS.values()

  def __is_player1_trail(self):
    return self.char == PLAYER_ONE_TRAIL_CHAR

  def __is_player2_trail(self):
    return self.char == PLAYER_TWO_TRAIL_CHAR

  def __inverted_directions(self, directions):
    return dict(
      (value, key) for key, value
      in directions.items()
    )
