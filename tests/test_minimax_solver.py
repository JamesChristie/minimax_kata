import unittest

import minimax_kata

from minimax_kata.minimax_solver import MinimaxSolver
from minimax_kata.arena          import DIRECTIONS

from minimax_kata.interface.game_interpreter import GameInterpreter

class TestThatTieIsChosenInOneByTwo(unittest.TestCase):
  def setUp(self):
    self.game_string  = """\
      ██████
      ██↓ ██
      ██▲ ██
      ██████"""

    self.game = GameInterpreter(self.game_string.replace("      ", "")).do()
    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
      set(self.minimax_solver.get_best_moves()),
      set([DIRECTIONS.south])
    )

class TestThatTieIsChosenInMirroredOneByTwo(unittest.TestCase):
  def setUp(self):
    self.game_string  = """\
      ██████
      ██▼ ██
      ██↑ ██
      ██████"""

    self.game = GameInterpreter(self.game_string.replace("      ", "")).do()
    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
        set(self.minimax_solver.get_best_moves()),
        set([DIRECTIONS.north])
    )

class TestThatTieIsChosenInTwoByOne(unittest.TestCase):
  def setUp(self):
    self.game_string  = """\
      ████████
      ██→ ◀ ██
      ████████"""

    self.game = GameInterpreter(self.game_string.replace("      ", "")).do()
    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
      set(self.minimax_solver.get_best_moves()),
      set([DIRECTIONS.east])
    )

class TestThatTieIsChosenInMirroredTwoByOne(unittest.TestCase):
  def setUp(self):
    self.game_string  = """\
      ████████
      ██▶ ← ██
      ████████"""

    self.game = GameInterpreter(self.game_string.replace("      ", "")).do()
    self.minimax_solver = MinimaxSolver(self.game)

  def test_best_moves(self):
    self.assertEqual(
      set(self.minimax_solver.get_best_moves()),
      set([DIRECTIONS.west])
    )
