def reverse(string):
    reversestring = ''
    for i in range(1,len(string)+1):
        reversestring += string[-i]
    return reversestring

def mirror(string):
    return string + reverse(string)

def is_palindrome(string):
    if reverse(string) == string:
        return True
    else:
        return False

print(is_palindrome("world"),is_palindrome("eye"),is_palindrome("racecar"),is_palindrome("tacocat"))
