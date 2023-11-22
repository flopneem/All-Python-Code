def count_letters(ltr, string):
    """Count the number of times a letter ltr appears in a string."""
    count = 0
    for char in string:
        if char == ltr:
            count += 1
    return count
