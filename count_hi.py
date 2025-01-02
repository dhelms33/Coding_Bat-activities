def count_hi(str):
  if len(str) < 2:
    return 0
  count = 0
  for i in range(len(str)-1):
    if str[i:i+2] == "hi":
      count+=1
  return count