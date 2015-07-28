from minimax_kata.game  import Game
from minimax_kata.arena import Arena

class GameCopier:
  def __init__(self, game):
    self.game = game

  # NOTE (JamesChristie) This is awkward and inefficient,
  # as a new games with Arena and Player members are
  # created, then promptly discarded and replaced
  def generate(self):
    game_copy = Game()
    self.__mutate_members(game_copy)
    return game_copy

  # Private

  def __mutate_members(self, game_copy):
    game_copy.arena   = self.__get_arena_copy()
    game_copy.player1 = self.game.player1
    game_copy.player2 = self.game.player2

  def __get_arena_copy(self):
    original = self.game.arena

    arena_copy = Arena(original.width, original.length)
    arena_copy.space = original.space.copy()

    return arena_copy
