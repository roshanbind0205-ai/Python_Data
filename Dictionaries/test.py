student = {
    "name": "Aarav",
    "math": 86,
    "science": 91
}

print(student["math"])

student["english"] = 78
student["math"] = 90
student["science"]

print(student.get("history", "Not found"))

# for key, value in student.items():
#     print(key, "=", value)