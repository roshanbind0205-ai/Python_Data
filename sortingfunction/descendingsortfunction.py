from functools import cmp_to_key
def compare(a, b):
    return b-a
numbers=[20,40,54,13,43]
numbers.sort(key=cmp_to_key(compare))
print(numbers)
