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
students.sort(key=lambda student: student.marks)
for student in students:
    print(student)       