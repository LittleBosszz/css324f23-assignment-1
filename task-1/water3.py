def initial_state():
    return (0, 0, 0)

def is_goal(s):
    return s[0]==4 and s[1]==4 

def successors(s):
    a, b, c = s
    # pour from one to another

    # pour to a
    t = 8 - a
    if b>0 and t>0:
      if b>t:
        yield ((8, b-t, c), t)
      else :
        yield ((a+b, 0, c), b)
    if c > 0 and t>0:
      if c>t:
        yield ((8, b, c-t), t)
      else :
        yield ((a+c, b, 0), c)
    
    # pour to b
    t = 5 - b
    if a>0 and t>0:
      if a>t:
        yield ((a-t, 5, z), t)
      else:
        yield ((0, b+a, c), a)
    if c>0 and t>0:
      if c>t:
        yield ((a, 5, c-t), t)
      else:
        yield ((a, b+c, 0), c)

     # pour to c
    t = 3 - c
    if a>0 and t>0:
     if a>t:
      yield ((a-t, b, 3), t)
     else:
      yield ((0, b, c+a), a)
    if b>0 and t>0:
     if b>t:
      yield ((a, b-t, 3), t)
     else:
      yield ((a, 0, c+b), b)
return []
