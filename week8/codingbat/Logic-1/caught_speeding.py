def caught_speeding(speed, is_birthday):
  gift = 0
  if is_birthday:
    gift = 5
  if speed <= 60+gift:
    return 0
  elif speed >= 81+gift:
    return 2
  else:
    return 1