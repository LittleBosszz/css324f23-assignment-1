def initial_state():
    return (8 0, 0)

# end when a and b = 4
def is_goal(s):
    return s[0]==4 and s[1]==4 

def successors(s):
    a, b, c = s

    # pour to a (8)
    total = 8 - a
    if b>0 and total>0:
      if b>total:
        yield ((8, b-total, c), total)
      else :
        yield ((a+b, 0, c), b)
    if c > 0 and total>0:
      if c>total:
        yield ((8, b, c-total), total)
      else :
        yield ((a+c, b, 0), c)
    
    # pour to b (5)
    total = 5 - b
    if a>0 and total>0:
      if a>total:
        yield ((a-total, 5, c), total)
      else:
        yield ((0, b+a, c), a)
    if c>0 and total>0:
      if c>total:
        yield ((a, 5, c-total), total)
      else:
        yield ((a, b+c, 0), c)

     # pour to c (3)
    total = 3 - c
    if a>0 and total>0:
     if a>total:
      yield ((a-total, b, 3), total)
     else:
      yield ((0, b, c+a), a)
    if b>0 and total>0:
     if b>total:
      yield ((a, b-total, 3), total)
     else:
      yield ((a, 0, c+b), b)

