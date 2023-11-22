def day_num(name):
    if name == "Sunday":
        return 0
    elif name == "Monday":
        return 1
    elif name == "Tuesday":
        return 2
    elif name == "Wednesday":
        return 3
    elif name == "Thursday":
        return 4
    elif name == "Friday":
        return 5
    elif name == "Saturday":
        return 6
    else:
        return

print(day_num("Sunday"),day_num("Whatisaday"))
