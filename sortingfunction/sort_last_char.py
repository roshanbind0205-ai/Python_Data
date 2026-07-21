from functools import cmp_to_key
def compare_last_char(a, b):
    if a[-1] < b[-1]:
        return -1
    elif a[-1] > b[-1]:
        return 1
    else:
        return 0
words=["banana","apple","mango","grapes"]
words.sort(key=cmp_to_key(compare_last_char))
print(words)    
    
    