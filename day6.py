#1.
class Student:
    student_name = 'Ketan'
    marks = 92

print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")
setattr(Student, 'student_name', 'Raghu')
setattr(Student, 'marks', 93)
print(f"Student Name: {getattr(Student, 'student_name')}")
print(f"Marks: {getattr(Student, 'marks')}")

#2.

class Student:
    student_id = '10'
    student_name = 'ketan kotian'
    def display():
        print(f'Student id: {Student.student_id}\nStudent Name: {Student.student_name}')
print("Original attributes and their values of the Student class:")
Student.display()