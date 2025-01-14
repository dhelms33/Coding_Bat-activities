def end_other(a,b):
    a_lower = a.lower()
    b_lower = b.lower()
    
    return a_lower.contains(b_lower) or b_lower.contains(a_lower)