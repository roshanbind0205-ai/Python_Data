from functools import cmp_to_key

students=[
    {"name":"Ankit","marks":90},
    {"name":"Ranjay","marks":70},
    {"name":"pathakl","marks":95},
    {"name":"Ranjay","marks":80}
]
def compare_students(a,b):
    return b["marks"] - a["marks"]
students.sort(key=cmp_to_key(compare_students))
for student in students:
    print(student)