student=[
    ("Deepak", 30),
    ("Arpit", 90),
    ("Prince",80),
    ("Kishan",70),
    ("piyush",40)
]

student.sort(key=lambda student : student[1], reverse=True)
print(student)