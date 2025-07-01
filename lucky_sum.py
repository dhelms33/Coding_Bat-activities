def lucky_sum(a,b,c):
  if (a == 13): #independent ifs check each one can also be done with one if and two specific elif statements
    return 0
  if (b == 13):
    return a
  if (c == 13):
    return a + b
  return a+b+c