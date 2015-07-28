class GameAdvancement:
  def __init__(self, game, move):
    self.game               = game
    self.move               = move
    self.original_position  = self.get_position()
    self.original_direction = self.get_direction()

  def get_position(self):
    return self.move.player.position

  def get_direction(self):
    return self.move.player.direction

  def perform(self):
    pass
    # advance only if move is valid
    # mutate player
    #   update position
    #   update direction
    #   claim arena space
    # detect death
    #   player position is out of bounds
    #   player position is claimed
    #   kill() player if appropriate

  def undo(self):
    pass
