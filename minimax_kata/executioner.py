class Executioner:
  def __init__(self, game):
    self.game = game

  def do(self):
    for player in self.get_players():
      player.kill() if self.player_should_die(player) else None

  def get_players(self):
    return [self.game.player1, self.game.player2]

  def get_positions(self):
    return [
      player.position for player
      in self.get_players()
    ]

  def player_should_die(self, player):
    return (
      self.game.player_is_out_of_bounds(player) or
      self.game.get_owner(player.position) is not None or
      self.collision_has_ocurred()
    )

  def collision_has_ocurred(self):
    return len(set(self.get_positions())) == 1

  def get_collision_position(self):
    if self.collision_has_ocurred():
      return self.game.player1.position
