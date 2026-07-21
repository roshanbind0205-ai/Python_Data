from functools import cmp_to_key
def compare(a, b):
    if a < b:
       return -1
    elif a> b:
       return 1
    else:
       return 0
numbers=[10,4,90,20,30]
answer = sorted(numbers,key=cmp_to_key(compare))
print(answer)