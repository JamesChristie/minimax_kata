from minimax_kata.arena import DIRECTIONS

# NOTE (JamesChristie) All strings in this file currently
# include a space of padding after the character to avoid
# bunching when they exceed the allowed width in a mono-
# spaced font (the wall is a double wall character)

WALL_SPACE_CHAR  = '██'
EMPTY_SPACE_CHAR = '☐ '

PLAYER_ONE_TRAIL_CHAR = '① '
PLAYER_TWO_TRAIL_CHAR = '② '

PLAYER_ONE_CHARS = {
  DIRECTIONS.north: '↑ ',
  DIRECTIONS.east:  '→ ',
  DIRECTIONS.south: '↓ ',
  DIRECTIONS.west:  '← '
}

PLAYER_TWO_CHARS = {
  DIRECTIONS.north: '▲ ',
  DIRECTIONS.east:  '▶ ',
  DIRECTIONS.south: '▼ ',
  DIRECTIONS.west:  '◀ '
}

CRASH_CHAR = '🔥 '
