from minimax_kata.arena import Arena

class GameCopier:
  def __init__(self, game):
    self.game      = game
    self.game_copy = None

  def generate(self):
    if self.game_copy is None:
      self.game_copy = type(self.game)()
      self.__mutate_members()

    return self.game_copy

  # Private

  def __mutate_members(self):
    self.game_copy.arena   = self.__get_arena_copy()
    self.game_copy.player1 = self.game.player1.get_copy()
    self.game_copy.player2 = self.game.player2.get_copy()

    self.__assign_current_player()
    if self.game.last_player is not None:
      self.__assign_last_player()

  # Private

  def __get_arena_copy(self):
    original = self.game.arena

    arena_copy = Arena(
      width=original.get_width(),
      length=original.get_length()
    )

    arena_copy.space = original.space.copy()

    return arena_copy

  def __assign_current_player(self):
    if self.game.player1 is self.game.current_player:
      self.game_copy.current_player = self.game_copy.player1
    else:
      self.game_copy.current_player = self.game_copy.player2

  def __assign_last_player(self):
    if self.game.last_player is self.game.player1:
      self.game_copy.last_player = self.game_copy.player1
    else:
      self.game_copy.last_player = self.game_copy.player2
