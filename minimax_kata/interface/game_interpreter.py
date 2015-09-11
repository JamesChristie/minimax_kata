from minimax_kata.game import Game

from minimax_kata.interface                  import WALL_SPACE_CHAR
from minimax_kata.interface.char_interpreter import CharInterpreter

class GameInterpreter:
  def __init__(self, game_string):
    self.game_string = game_string
    self.char_space  = self.__split_game_string()
    self.game        = Game()

  def do(self):
    self.__create_game_space()
    self.__mutate_game()
    return self.game

  # Private

  def __split_game_string(self):
    char_space     = []

    for row in self.__clean_game_string().split('\n'):
      char_space.append([])
      for char in list(row):
        char_space[-1].append(char)

    return char_space

  def __clean_game_string(self):
    return self.game_string         \
      .replace(WALL_SPACE_CHAR, '') \
      .replace(' ', '')             \
      .strip()

  def __create_game_space(self):
    new_space = {}

    for length in range(1, len(self.char_space) + 1):
      for width in range(1, len(self.char_space[length - 1]) + 1):
        new_space[(width, length)] = None

    self.game.arena.space = new_space

  def __get_max_width(self):
    return max(
      len(row) for row
      in self.char_space
    )

  def __mutate_game(self):
    for length, row in enumerate(self.char_space):
      for width, char in enumerate(row):
        CharInterpreter(self.game, length+1, width+1, char).do()
