from enum import Enum

from minimax_kata.arena_tools import get_new_space

DIRECTONS = Enum(
  'DIRECTIONS',
  'North East South West'
)

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
