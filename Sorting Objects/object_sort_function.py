from functools import cmp_to_key

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __repr__(self):
        return f"{self.name}:{self.marks}"
students = [
    Student("Amit",70),
    Student("Ravi",90),
    Student("Zoya",85),
    Student("Meena",60)
    
]  
def compare_students(a,b):
    return b.marks - a.marks  
students.sort(key=cmp_to_key(compare_students))
print(students)    