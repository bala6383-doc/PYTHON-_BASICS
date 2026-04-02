marks = { "Ram": 80, "Sita": 90, "John": 75 }
name = input("Enter student name: ")
if name in marks:
    print("Marks:", marks[name])
else:
    print("Student not found")
