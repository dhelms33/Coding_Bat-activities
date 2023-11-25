def last2(str):
  count = 0
  last2 = str[len(str)-2:]
  if len(str) < 2:
    return 0
  for i in range(len(str)-2):
    if last2 == str[i:i+2]:
      count+=1
  return count