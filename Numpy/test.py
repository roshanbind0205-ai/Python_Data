import numpy as np

print("=" * 60)
print("BASIC NUMERICAL THINKING NOTEBOOK")
print("=" * 60)

# 1. Indexing

numbers = [10, 20, 30, 40, 50]

print("\n1. INDEXING")
print("Numbers:", numbers)
print("First value:", numbers[0])
print("Second value:", numbers[1])
print("Last value:", numbers[-1])
print("Last value:", numbers[-1])

# 2. Slicing

print("\n2. SLICING")
print("First three values:", numbers[:3])
print("Values from index 1 to 3:", numbers[1:4])
print("Every second value:", numbers[::2])
print("Reverse list:", numbers[::-1])

# 3. Dictionary

student = {
    "name": "Aarav",
    "math": 80,
    "science": 85,
    "english": 90
}

print("\n3. DICTIONARY")
print("Student dictionary:", student)
print("Name:", student["name"])
print("Math marks:", student["math"])

# 4. NumPy Array

marks = np.array([80, 85, 90, 70, 75, 65])

print("\n4. NUMPY ARRAY")
print("Marks array:", marks)
print("Marks multiplied by 2:", marks * 2)
print("Marks plus 5:", marks + 5)

# 4B. Creating NumPy arrays automatically

print("\n4B. CREATING ARRAYS AUTOMATICALLY")

zeros_array = np.zeros(5)
ones_array = np.ones(5)
full_array = np.full((2, 3), 7)
range_array = np.arange(1, 11)
even_array = np.arange(2, 21, 2)
line_array = np.linspace(0, 1, 5)
random_decimal_array = np.random.rand(5)
random_marks = np.random.randint(40, 101, size=10)

print("Zeros array:", zeros_array)
print("Ones array:", ones_array)
print("Full array:")
print(full_array)
print("Range array:", range_array)
print("Even numbers:", even_array)
print("Linspace array:", line_array)
print("Random decimal array:", random_decimal_array)
print("Random marks:", random_marks)

print("Mean of random marks:", np.mean(random_marks))
print("Median of random marks:", np.median(random_marks))
print("Minimum random mark:", np.min(random_marks))
print("Maximum random mark:", np.max(random_marks))
print("Range of random marks:", np.max(random_marks) - np.min(random_marks))

# 5. Basic Statistics

print("\n5. BASIC STATISTICS")
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Minimum:", np.min(marks))
print("Maximum:", np.max(marks))
print("Range:", np.max(marks) - np.min(marks))

# 6. Two-dimensional Array

class_marks = np.array([
    [80, 85, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68]
])

print("\n6. TWO-DIMENSIONAL ARRAY")
print("Class marks:")
print(class_marks)
print("Shape:", class_marks.shape)

# 7. Axis

print("\n7. AXIS THINKING")

subject_names = np.array(["Math", "Science", "English"])

subject_mean = np.mean(class_marks, axis=0)
student_mean = np.mean(class_marks, axis=1)

print("Subject names:", subject_names)
print("Subject-wise mean:", subject_mean)
print("Student-wise mean:", student_mean)

print("Subject-wise min:", np.min(class_marks, axis=0))
print("Subject-wise max:", np.max(class_marks, axis=0))
print("Subject-wise range:", np.max(class_marks, axis=0) - np.min(class_marks, axis=0))

# 8. Dictionary + NumPy together

report = {
    "subjects": subject_names,
    "subject_mean": subject_mean,
    "student_mean": student_mean,
    "overall_mean": np.mean(class_marks),
    "overall_median": np.median(class_marks),
    "overall_min": np.min(class_marks),
    "overall_max": np.max(class_marks),
    "overall_range": np.max(class_marks) - np.min(class_marks)
}

print("\n8. FINAL REPORT DICTIONARY")

for key, value in report.items():
    print(key, ":", value)

print("\n" + "=" * 60)
print("NOTEBOOK COMPLETE")
print("=" * 60)

