def dice(n):
    rolls = []
    for _ in range(n):
        rolls.append(random.randint(1, 6))
    return sum(rolls)

print(sum(rolls))
