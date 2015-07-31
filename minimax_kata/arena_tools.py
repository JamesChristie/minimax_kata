import itertools

def get_new_space(width, length):
    return dict(
      (tuple, None) for tuple in
      tuple_list(width, length)
    )

def tuple_list(width, length):
  return list(
    itertools.product(
      list_for_span(width), list_for_span(length)
    )
  )

def list_for_span(length):
  return [
    position for position in
    range(1, length + 1)
  ]
