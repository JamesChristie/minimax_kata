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
  return OPPOSING_DIRECTIONS[direction]

def translated_position(position, direction):
  return tuple(map(
    lambda x, y: x + y, position, DIRECTION_DIFFERENTIALS[direction]
  ))

class Arena:
  def __init__(self, width=4, length=4):
    self.width  = width
    self.length = length
    self.space  = get_new_space(
      self.width, self.length
    )

  def get_upper_left_position(self):
    return (1, 1)

  def get_upper_right_position(self):
    return (self.width, 1)

  def get_lower_left_position(self):
    return (1, self.length)

  def get_lower_right_position(self):
    return (self.width, self.length)