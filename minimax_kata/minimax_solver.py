from minimax_kata.arena import DIRECTIONS

from minimax_kata.potential_game_presenter import get_potential_games

class MinimaxSolver:
  def __init__(self, game):
    self.game = game
    self.potential_games = get_potential_games(self.game)

  def get_best_moves(self):
    return [
      presenter.direction for presenter
      in self.potential_games
      if not presenter.is_wall()
    ]
