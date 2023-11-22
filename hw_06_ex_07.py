def to_secs(h,m,s):
    hours_to_sec = 60**2 * h
    mins_to_sec = 60 * m
    secondstotal = hours_to_sec + mins_to_sec + s
    return secondstotal

print(to_secs(2,30,10),to_secs(2,0,0),to_secs(0,2,0),to_secs(0,0,42),to_secs(0,-10,10))
