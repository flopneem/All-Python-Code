def reverse(string):
    reversestring = ''
    for i in range(1,len(string)+1):
        reversestring += string[-i]
    return reversestring

print(reverse("happy"),reverse("Python"))
