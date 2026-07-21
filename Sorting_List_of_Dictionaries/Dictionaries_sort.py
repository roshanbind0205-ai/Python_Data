students=[
    {"name":"Amit","marks":80},
    {"name":"Ravi","marks":90},
    {"name":"Zoya","marks":85},
    {"name":"Meena","marks":60}
]
# students.sort(key=lambda student: student["marks"])
# for student in students:
#     print(student)

students.sort(key=lambda student: student["name"])
for student in students:
    print(student)    

students.sort(key=lambda student: student["name"],reverse=True)
for student in students:
    print(student)