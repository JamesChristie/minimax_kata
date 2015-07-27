class Player:
  def __init__(self, name, position):
    self.name      = name
    self.position  = position
    self.alive     = True
    self.direction = None

  def is_alive(self):
    return bool(self.alive)

  def is_dead(self):
    return not self.is_alive()
