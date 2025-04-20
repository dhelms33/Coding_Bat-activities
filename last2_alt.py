def last2(str):
  if len(str) < 2:
    return 0
  count = 0
  last_two = ""
  for i in range(len(str)-2):
    first_two = str[i:i+2]
    last_two = str[len(str)-2:]
    if first_two == last_two:
      count +=1
  return count