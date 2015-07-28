from minimax_kata import arena

class Move:
  def __init__(self, player, direction):
    self.player    = player
    self.direction = direction

  def is_valid(self):
    return self.is_not_backwards()

  def is_not_backwards(self):
    return self.direction is not self.__backwards()
  
  # Private
  
  def __backwards(self):
    return arena.opposing_direction_for(self.player.direction)
