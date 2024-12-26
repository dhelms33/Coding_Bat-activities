def alarm_clock(day, vacation):
  result = ""
  if 1 <= day <= 5 and not vacation:
    result += "7:00"
  elif (day == 0 or day == 6) and not vacation:
    result += "10:00"
  else:
    if (1 <= day <= 5) and vacation:
      result += "10:00"
    else:
      result += "off"
  return result