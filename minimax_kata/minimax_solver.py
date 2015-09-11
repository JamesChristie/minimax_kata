from minimax_kata.arena import DIRECTIONS

class MinimaxSolver:
  def __init__(self, game):
    self.game = game

  def get_best_moves(self):
    available = self.game.get_available_directions()

    if DIRECTIONS.north not in available:
      return [DIRECTIONS.south]
    elif DIRECTIONS.east not in available:
      return [DIRECTIONS.west]
    elif DIRECTIONS.south not in available:
      return [DIRECTIONS.north]
    else:
      return [DIRECTIONS.east]
