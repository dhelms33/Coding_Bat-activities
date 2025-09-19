# my attempt
def centered_average(arr):
  length = len(arr)
  max = 0 
  minimum = 0
  average = []
  total = 0
  i = 0
  if length < 3:
    return 0
  for average in range(len(arr)-1):
    if average[i] > average[i+1]:
      max = average[i]
      total +=1
    elif average[i] < average[i+1]:
      min = average[i]
      total+=1
    else:
      average.append(average[i])
      total+=1
    sum_average = sum(average)
    return sum_average // total

#revision
def centered_average_v2(values: List[int], drop_all_extremes: bool = False)-> int:
    """ Compute the centered average of a list of integers. 
    By default, removes exactly one smallest value and one largest value. If 'drop_all_extremes=True, removes all instances of the min and max"""
    if len(values < 3):
        raise ValueError("Input list must contain at least 3 numbers.")
    
    minimum = min(values)
    maximum = max(values)
    
    if drop_all_extremes:
        trimmed = [v for v in values if v != minimum and v != maximum]
    else:
        sorted_values = sorted(values)
        trimmed = sorted_vales[1:-1] #drops exactly one min and one max
    if not trimmed:
        raise ValueError("No values remain after removing extremes.")
    return sum(trimmed) // len(trimmed)
        
    