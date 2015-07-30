class Space:
  def __init__(self, **kwargs):
    self.player_one = False
    self.player_two = False

  def is_empty(self):
    return True

  def is_owned(self):
    return False

  def owned_by_player_one(self):
    return False

  def owned_by_player_two(self):
    return False

  def is_player_one(self):
    return False

  def is_player_two(self):
    return False

  def __eq__(self, other):
    return (
      isinstance(other, self.__class__)
        and self.__dict__ == other.__dict__
    )

  def __ne__(self, other):
    return not self.__eq__(other)

class Trail(Space):
  def __init__(self, player_one=False, player_two=False):
    self.player_one = player_one
    self.player_two = player_two

  def is_owned(self):
    return True

  def owned_by_player_one(self):
    return bool(self.player_one)

  def owned_by_player_two(self):
    return bool(self.player_two)

class Player(Space):
  def __init__(self, player_one=False, player_two=False):
    self.player_one = player_one
    self.player_two = player_two

  def is_player_one(self):
    return bool(self.player_one)

  def is_player_two(self):
    return bool(self.player_two)
