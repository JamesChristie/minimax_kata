from minimax_kata.game             import Game
from minimax_kata.game_advancement import GameAdvancement
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
  return Game()

def make_move(game, direction):
  player      = game.get_current_player
  move        = Move(player, direction)
  advancement = GameAdvancement(game.game, move)

  return advancement.do()

def set_arena_state(game, new_space, player1_position, player2_position):
  game.player1.position = player1_position
  game.player2.position = player2_position
  game.arena.space      = new_space
