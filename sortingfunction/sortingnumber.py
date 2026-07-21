from functools import cmp_to_key

def compare(a,b):
    return a - b
numbers = [40,10,20,40,30]
numbers.sort(key=cmp_to_key(compare))
print(numbers)