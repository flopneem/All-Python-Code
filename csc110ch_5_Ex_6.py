def grade(mark):
    mark_scheme = [(75, "First"),(70, "Upper Second"),(60, "Second"),(50, "Third"), (45, "F1 Supp"), (40, "FS")]
     
    for threshold in mark_scheme:
        if mark >= threshold[0]:
            return threshold[1]
        
largelist = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in largelist:
    print(x, grade(x))
