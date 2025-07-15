def lucky_sum(a,b,c):
  sum_13 = a+b+c
  if a == 13:
    sum_13 = 0
  elif b == 13:
    sum_13 = a
  elif c == 13:
    sum_13 = a+b
  return sum_13