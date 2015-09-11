from minimax_kata.arena import DIRECTIONS

from minimax_kata.potential_game_presenter import get_potential_games

ALIVE_SCORE = 10
CRASH_SCORE = 0
DEATH_SCORE = -10

class MinimaxSolver:
  def __init__(self, game):
    self.game = game
    self.potential_games = get_potential_games(self.game)

  def get_best_moves(self):
    return [
      presenter.direction for presenter
      in self.potential_games
      if self.__get_score(presenter) == self.get_max_score()
    ]

  def get_max_score(self):
    return max(
      self.__get_score(presenter) for presenter
      in self.potential_games
    )

  def __get_score(self, presenter):
    if presenter.is_alive():
      return ALIVE_SCORE
    elif presenter.is_crash():
      return CRASH_SCORE
    else:
      return DEATH_SCORE
