def print_multiplication_table(n):
    """Print a multiplication table n by n.
    Formatting gets all screwed if n >= 32. But why would anyone
    want a multiplication table that large?
    """
    # make first line
    line = "    "
    for i in range(1, n + 1):
        line = line + "{:4}".format(i)
    print(line)
    # make dividing line
    line = "   :"
    for i in range(n):
        line = line + "----"
    print(line)
    # make the main body line by line
    for i in range(1, n+1):
        line = "{0:3}:".format(i)
        for j in range(1, n + 1):
            line = line + "{:4}".format(i*j)
        print(line)
