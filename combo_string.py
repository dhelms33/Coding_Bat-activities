def combo_string(a,b):
  short_string = ""
  long_string = ""
  if (len(a) > len(b)):
    short_string = b
    long_string = a
  else:
    short_string = a
    long_string = b
  return short_string + long_string + short_string