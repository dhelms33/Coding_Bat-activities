def round10(num):
  """ """
  diff_until_10 = (num // 10 + 1) *10
  # get last number out of num using % 10, this will always be last digit
  if num % 10 > 5:
    num = num + diff_until_10
  elif num % 10 < 5:
    num = num - diff_until_10
  return num
  
def round_sum(a,b,c):
  round_a = round10(a)
  round_b = round10(b)
  round_c = round10(c)
  return round_a + round_b + round_c