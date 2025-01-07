import math

class Student:
    def __init__(self, *args):
        if len(args) < 5:
            self.first_Name= "Unknown"
            self.last_Name = "Unknown"
            self.gender = "Unknown"
            self.year = "Unknown"
            self.gpa = 0
            
        else:
            self.first_Name= args[0]
            self.last_Name = args[1]
            self.gender = args[2]
            self.year = args[3]
            self.gpa = args[4]
            
    def show_student(self):
        print(f"First name: {self.first_Name}")
        print(f"Last name: {self.last_Name}")
        print(f"Gender: {self.gender}")
        print(f"Year: {self.year}")
        print(f"Grade point average: {self.gpa}")
        
    def student_study_time(self, study_time):
        self.gpa += math.log(study_time)
        
        if self.gpa > 4.0:
            self.gpa = 4.0
            
student_GPA = [
    Student("Alice", "Smith", "Female", "Sophomore", 0.1),
    Student("Bob", "Johnson", "Male", "First-year student", 1),
    Student("Richard", "Smith", "Male", "Sophomore", 1.4),  
    Student("Charlie", "Brown", "Male", "Senior", 2.3),
    Student("Diana", "Prince", "Female", "Junior", 2)
]

for i, student in enumerate(student_GPA):
    print(f"Student {i + 1} data:")
    print(f"First name: {student.first_Name}")
    print(f"Last name: {student.last_Name}")
    print(f"Gender: {student.gender}")
    print(f"Year: {student.year}")
    print(f"Grade point average: {student.gpa}\n")

study_times = [30, 60, 90, 120, 180]
for time, student in zip(study_times, student_GPA):
    student.student_study_time(time)

for i, student in enumerate(student_GPA):
    print(f"Student {i + 1} data:")
    print(f"First name: {student.first_Name}")
    print(f"Last name: {student.last_Name}")
    print(f"Gender: {student.gender}")
    print(f"Year: {student.year}")
    print(f"Grade point average: {student.gpa}\n")