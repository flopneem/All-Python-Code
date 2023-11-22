def is_factor(f,n):
    '''the factors do not include 1 or the number itself'''
    if n % f == 0 and f != n and f != 1:
        return True
    else:
        return False

print(is_factor(3,12))
print(not(is_factor(5,12)))
print(is_factor(7,14))
print(not(is_factor(7,15)))
print(is_factor(1,15))
print(is_factor(15,15))
print(not(is_factor(25,15)))

