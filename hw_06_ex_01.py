def turn_clockwise(d):
    if d == "N":
        return "E"
    elif d == "E":
        return "S"
    elif d == "S":
        return "W"
    elif d == "W":
        return "N"
    else:
        return

print(turn_clockwise("N"))
print(turn_clockwise("E"))
print(turn_clockwise("S"))
print(turn_clockwise("W"))
print(turn_clockwise("egg"))
