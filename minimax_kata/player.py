class Player:
  def __init__(self, name, position):
    self.name      = name
    self.position  = position
    self.alive     = True
    self.direction = None

  def __eq__(self, other):
    return self.name == other.name

  def __ne__(self, other):
    return not self.__eq__(other)

  def is_alive(self):
    return bool(self.alive)

  def is_dead(self):
    return not self.is_alive()

  def kill(self):
    self.alive = False

  def resurrect(self):
    self.alive = True

  def get_copy(self):
    new_player           = Player(self.name, self.position)
    new_player.direction = self.direction

    return new_player
