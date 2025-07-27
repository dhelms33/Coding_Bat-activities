def fix_teen(n):
  if n == 15 or n==16:
    return n
  elif (n >= 13 and n < 15):
    return 0
  elif (n > 16 and n < 19):
    return 0
  else:
    return n
def no_teen_sum(n,a,b,c):
  int_test = [a,b,c]
  if int_test >= 13 or int_test <= 19:
    return 0
  return a+b+c