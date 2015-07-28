from minimax_kata import arena

def valid_directions_for(subject_direction):
  return [
    direction for direction
    in list(arena.DIRECTIONS)
    if direction is not arena.opposing_direction_for(subject_direction)
  ]

class Move:
  def __init__(self, player, direction):
    self.player    = player
    self.direction = direction

  def is_valid(self):
    return self.is_not_backwards()

  def is_not_backwards(self):
    return self.direction is not self.__backwards()

  def new_position(self):
    return arena.translated_position(
      self.player.position, self.direction
    )
  
  # Private
  
  def __backwards(self):
    return arena.opposing_direction_for(self.player.direction)
