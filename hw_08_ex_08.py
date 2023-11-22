def reverse(string):
    reversestring = ''
    for i in range(1,len(string)+1):
        reversestring += string[-i]
    return reversestring

def mirror(string):
    return string + reverse(string)

print(mirror("good"),mirror("Python"),mirror("a"),mirror(""))
