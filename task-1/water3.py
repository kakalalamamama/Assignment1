def initial_state():
    return (8, 0, 0)  # Start with 8 liters in the 8-liter bottle, and 0 liters in the others

def is_goal(s):
    return s[0] == 4 and s[1] == 4  # The goal is to have 4 liters in the 8-liter and 5-liter bottles

def successors(s):
    x, y, z = s
    # Possible actions:
    actions = []
    p= 'pour'

    # Pour water from the 8-liter bottle to the 5-liter bottle
    if x > 0 and y < 5:
        p = min(x, 5 - y)
        yield(((x - p, y + p, z), p))

    # Pour water from the 8-liter bottle to the 3-liter bottle
    if x > 0 and z < 3:
        p = min(x, 3 - z)
        yield(((x - p, y, z + p), p))

    # Pour water from the 5-liter bottle to the 8-liter bottle
    if y > 0 and x < 8:
        p = min(y, 8 - x)
        yield(((x + p, y - p, z), p))

    # Pour water from the 5-liter bottle to the 3-liter bottle
    if y > 0 and z < 3:
        p = min(y, 3 - z)
        yield(((x, y - p, z + p), p))

    # Pour water from the 3-liter bottle to the 8-liter bottle
    if z > 0 and x < 8:
        p = min(z, 8 - x)
        yield(((x + p, y, z - p), p))

    # Pour water from the 3-liter bottle to the 5-liter bottle
    if z > 0 and y < 5:
        p = min(z, 5 - y)
        yield(((x, y + p, z - p), p))

    return actions