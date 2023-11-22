weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 
            4: "Thursday", 5: "Friday", 6: "Saturday"}

x = int(input("What number day did you leave on? \n"))
print("That's a {}.".format(weekdays[x]))
y = int(input("How many sleeps? \n"))

z = (x + y) % 7
print("You will return on a {}.".format(weekdays[z]))
