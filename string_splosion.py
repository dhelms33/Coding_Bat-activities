def string_splosion(str):
    if len(str) == 0:
        return("Please have a length greater than zero for this activity to work.")
    string_splode = ""
    for i in range(len(str)):
        string_splode += str[:i+1]
    return string_splode