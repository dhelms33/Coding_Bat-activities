def round10(num):
  
  """ rounds an integer to the nearest multiple of 10
  if number is greater than or equal to 5, round up. Otherwise round down."""
  last_digit = num % 10
# diff_until_10 = (num // 10 + 1) *10
  # get last number out of num using % 10, this will always be last digit
  if last_digit % 10 >= 5:
    return num + (10-last_digit)
  else:
    return num - last_digit

  # elif num % 10 < 5:
  #   num = num - diff_until_10
  # return num
  
def round_sum(a,b,c):
  """Returns the sum of three integers after the round."""
  round_a = round10(a)
  round_b = round10(b)
  round_c = round10(c)
  return round_a + round_b + round_c