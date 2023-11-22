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

def day_name(d):
    if d == 0:
        return "Sunday"
    elif d == 1:
        return "Monday"
    elif d == 2:
        return "Tuesday"
    elif d == 3:
        return "Wednesday"
    elif d == 4:
        return "Thursday"
    elif d == 5:
        return "Friday"
    elif d == 6:
        return "Saturday"
    else:
        return

def returnday(d,n):
    change = day_num(d) + n % 7
    if change > 6:
        return day_name(change - 7)
    else:
        return day_name(change)

print(returnday("Monday",4),returnday("Tuesday",0),returnday("Tuesday",14),returnday("Sunday",100),
returnday("Saturday",1))
