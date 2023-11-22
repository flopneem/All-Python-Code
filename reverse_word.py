##https://youtu.be/t1cxB55BlnQ 


def rev_each_word_in(Sentence):

    return ' '.join(word[::-1] for word in Sentence.split(" "))


Sentence = "to be or not to be that is the question"
print(rev_each_word_in(Sentence))
