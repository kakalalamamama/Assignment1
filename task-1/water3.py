def initial_state():
    return (8, 0, 0)  # Start with 8 liters 

def is_goal(s):
    return s[0] == 4 and s[1] == 4  # The goal is (4,4,0)

def successors(s):
    x, y, z = s
    # Possible actions:
    path = []
    p= 'pour'

    # Pour water  8-liter bottle to 5-liter bottle
    if x > 0 and y < 5:
        p = min(x, 5 - y)
        yield(((x - p, y + p, z), p))

    # Pour water  8-liter bottle to 3-liter bottle
    if x > 0 and z < 3:
        p = min(x, 3 - z)
        yield(((x - p, y, z + p), p))

    # Pour water  5-liter bottle to 8-liter bottle
    if y > 0 and x < 8:
        p = min(y, 8 - x)
        yield(((x + p, y - p, z), p))

    # Pour water  5-liter bottle to 3-liter bottle
    if y > 0 and z < 3:
        p = min(y, 3 - z)
        yield(((x, y - p, z + p), p))

    # Pour water  3-liter bottle to 8-liter bottle
    if z > 0 and x < 8:
        p = min(z, 8 - x)
        yield(((x + p, y, z - p), p))

    # Pour water 3-liter bottle to 5-liter bottle
    if z > 0 and y < 5:
        p = min(z, 5 - y)
        yield(((x, y + p, z - p), p))

    return path