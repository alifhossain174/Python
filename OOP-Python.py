class Student :
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades)/len(self.grades)


student = Student("MD Fahim Hossain", [50,100])
print(f"{student.name}'s average grade is {student.average()}")

student2 = Student("Alif Hossain", [80,100])
print(f"{student2.name}'s average grade is {student2.average()}")