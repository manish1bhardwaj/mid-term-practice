class Students:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age 
        self.grade = grade
    def Student_details(self):
        print(f"Name:{self.name}    Age:{self.age}  Grade:{self.grade}")
    def calculate_grades(self,percentage):
        if 95<=percentage<100:
            return 'O'
        elif 90<=percentage<95:
            return 'A+'
        elif 80<=percentage<90:
            return 'A'
        elif 70<=percentage<80:
            return 'B+'
        elif 60<=percentage<70:
            return 'B'
        elif 50<=percentage<60:
            return 'C+'
        else:
            return 'C' 


#maincode
student1 = Students("Manish Bhardwaj",18,"A+")
student2 = Students("Alok Bhadauria",18,"A+")
student3 = Students("Priyanshu Sharma",18,"A")
student4 = Students("Divraj",18,"O")
student5 = Students("Ayaan",18,"O+")
student1.Student_details()
student2.Student_details()
student3.Student_details()
student4.Student_details()
student5.Student_details()

#calculating grades

Percentage1 = 94
Percentage2 = 96
Percentage3 = 95
Percentage4 = 80
Percentage5 = 90

grade1 =student1.calculate_grades(Percentage1)
grade2 =student2.calculate_grades(Percentage2)
grade3 =student3.calculate_grades(Percentage3)
grade4 =student4.calculate_grades(Percentage4)
grade5 =student5.calculate_grades(Percentage5)

print(f"Grade of {student1.name}:{grade1}")
print(f"Grade of {student2.name}:{grade2}")
print(f"Grade of {student3.name}:{grade3}")
print(f"Grade of {student4.name}:{grade4}")
print(f"Grade of {student5.name}:{grade5}")

