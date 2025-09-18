#wip
def sum67(arr):
  sum_arr = 0
  if len(arr) == 0:
    return 0
  ignore_section = False
  for num in range(len(arr)-1):
    sum_arr+=arr[num]
  return sum_arr