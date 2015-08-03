from minimax_kata.executioner import Executioner

from minimax_kata.interface import WALL_SPACE_CHAR
from minimax_kata.interface import EMPTY_SPACE_CHAR
from minimax_kata.interface import PLAYER_ONE_TRAIL_CHAR
from minimax_kata.interface import PLAYER_TWO_TRAIL_CHAR
from minimax_kata.interface import PLAYER_ONE_CHARS
from minimax_kata.interface import PLAYER_TWO_CHARS
from minimax_kata.interface import CRASH_CHAR

class CharPolicy:
  def __init__(self, game, length, width):
    self.game     = game
    self.length   = length
    self.width    = width
    self.position = (self.width, self.length)
    self.player1  = self.game.player1
    self.player2  = self.game.player2

  def get_char(self):
    if self.__is_collision():
      return CRASH_CHAR
    elif self.__is_player1():
      return PLAYER_ONE_CHARS[self.player1.direction]
    elif self.__is_player2():
      return PLAYER_TWO_CHARS[self.player2.direction]
    elif self.__is_player1_trail():
      return PLAYER_ONE_TRAIL_CHAR
    elif self.__is_player2_trail():
      return PLAYER_TWO_TRAIL_CHAR
    else:
      return EMPTY_SPACE_CHAR

  # Private

  def __is_collision(self):
    executioner = Executioner(self.game)

    return (
      executioner.collision_has_ocurred()
        and executioner.get_collision_position() == (self.width, self.length)
    )

  def __is_player1(self):
    return self.player1.position == self.position

  def __is_player2(self):
    return self.player2.position == self.position

  def __is_player1_trail(self):
    return self.game.get_owner(self.position) is self.player1

  def __is_player2_trail(self):
    return self.game.get_owner(self.position) is self.player2
