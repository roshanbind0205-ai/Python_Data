# from functools import cmp_to_key

# students = [
#     {"name": "Roshan", "marks": 70},
#     {"name": "Prince", "marks": 74},
#     {"name": "Amit", "marks": 67},
#     {"name": "Kishan", "marks": 75}
# ]

# def compare_students(a, b):
#     return a["marks"] - b["marks"]

# students.sort(key=cmp_to_key(compare_students))

# for student in students:
#     print(student)
    
    
from functools import cmp_to_key
students=[
    {"name":"Roshan","marks":70},
    {"name":"Amit","marks":75},
    {"name":"kishan","marks":80},
    {"name":"karan","marks":90}
] 
def compare_students(a,b):
    return a["marks"] -b["marks"]
students.sort(key=cmp_to_key(compare_students))
for student in students:
    print(student)   