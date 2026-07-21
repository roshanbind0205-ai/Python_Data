# from functools import cmp_to_key
# def compare_words(a,b):
#     if len(a) != len(b):
#         return len(a) - len(b)
    
#     if a< b:
#         return -1
#     elif a > b:
#         return 1
#     else:
#         return 0
# words=["dig","ants","apple","elephant","tiger","egal"]
# words.sort(key=cmp_to_key(compare_words))
# print(words)

from functools import cmp_to_key
def compare_word(a,b):
    if len(a)-len(b):
        return len(a)-len(b)
    if a<b:
        return -1
    elif a>b:
        return 1
    else:
        return 0
words=["Roshan","Rohit","Amit","kishan","pankaja"]
words.sort(key=cmp_to_key(compare_word))
print(words)    