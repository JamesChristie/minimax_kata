from minimax_kata.game             import Game
from minimax_kata.game_advancement import GameAdvancement
from minimax_kata.game_presenter   import GamePresenter
from minimax_kata.move             import Move
from minimax_kata.arena            import DIRECTIONS

def move_north():
  return DIRECTIONS.north

def move_east():
  return DIRECTIONS.east

def move_south():
  return DIRECTIONS.south

def move_west():
  return DIRECTIONS.west

def get_new_game():
  return GamePresenter(Game())

def make_move(game_presenter, direction):
  player      = game_presenter.get_current_player
  move        = Move(player, direction)
  advancement = GameAdvancement(game_presenter.game, move)

  return advancement.do()

def set_arena_state(game_presenter, new_space, player1_position, player2_position):
  new_game = Game()

  new_game.player1.position = player1_position
  new_game.player2.position = player2_position
  new_game.arena.space      = new_space

  return GamePresenter(new_game)
