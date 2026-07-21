from functools import cmp_to_key
def compare_by_length(a,b):
    return len(a) - len(b)
word=["banana","apple","cat","tiger"]
word.sort(key=cmp_to_key(compare_by_length))
print(word)