##Youtue:http://youtu.be/pxX4Zc9U7bM?hd=1
def reverse(string):
    reversestring = ''
    for i in range(1,len(string)+1):
        reversestring += string[-i]
    return reversestring

def remove_punc(word):  
    punc = word.replace('.','')
    return punc

def rev_each_word_in(sentence):
    rev_sentence = ''
    splitter = sentence.split()
    for i in splitter:
        if i.count('.') > 0:
            word = remove_punc(i)
            rev_sentence += reverse(word)
            rev_sentence += ". "
        else:
            rev_sentence += reverse(i)
            rev_sentence += " "
    return rev_sentence

print(rev_each_word_in("to be or not to be that is the question."))
print(rev_each_word_in("to be or not to be that is the question"))
        
    
