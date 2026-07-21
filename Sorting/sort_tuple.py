student=[
    ("Amit",50),
    ("Rohit",40),
    ("Aryan",80),
    ("Kishan",60),
    ("Roshan", 70)
]

student.sort(key=lambda student : student[1])

print(student)