from enum import Enum

from minimax_kata.arena_tools import get_new_space

DIRECTIONS = Enum(
  'DIRECTIONS',
  'north east south west'
)

OPPOSING_DIRECTIONS = {
  DIRECTIONS.north: DIRECTIONS.south,
  DIRECTIONS.east:  DIRECTIONS.west,
  DIRECTIONS.south: DIRECTIONS.north,
  DIRECTIONS.west:  DIRECTIONS.east
}

DIRECTION_DIFFERENTIALS = {
  DIRECTIONS.north: (0, -1),
  DIRECTIONS.east:  (1, 0),
  DIRECTIONS.south: (0, 1),
  DIRECTIONS.west:  (-1, 0)
}

def opposing_direction_for(direction):
  return OPPOSING_DIRECTIONS.get(direction, None)

def translated_position(position, direction):
  return tuple(map(
    lambda x, y: x + y, position, DIRECTION_DIFFERENTIALS[direction]
  ))

class Arena:
  def __init__(self, width=4, length=4):
    self.space = get_new_space(width, length)

  def get_width(self):
    return max(self.__width_values())

  def get_length(self):
    return max(self.__length_values())

  def get_upper_left_position(self):
    return (1, 1)

  def get_upper_right_position(self):
    return (self.get_width(), 1)

  def get_lower_left_position(self):
    return (1, self.get_length())

  def get_lower_right_position(self):
    return (self.get_width(), self.get_length())

  def get_owner(self, position):
    return self.space.get(position, None)

  def player_is_in_bounds(self, player):
    return player.position in self.space.keys()

  def player_is_out_of_bounds(self, player):
    return not self.player_is_in_bounds(player)

  def claim_space_for(self, player, position, force=False):
    if self.__claimable_for(player, position) or force:
      self.space[position] = player

  # Private

  def __width_values(self):
    return set([
      x for x, y
      in self.space.keys()
    ])

  def __length_values(self):
    return set([
      y for x, y
      in self.space.keys()
    ])

  def __claimable_for(self, player, position):
    return (
      not self.get_owner(position)
        and self.player_is_in_bounds(player)
    )
